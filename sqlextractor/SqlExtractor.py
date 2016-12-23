import re
import os
import codecs
from mysql.utilities.common.parser import GeneralQueryLog


class SQL(object):
    """Class for SQL

    """

    def __init__(self, default_db, sql):
        """Constructor.

        Args:
           default_db (str): Default database's name.
           sql (str): One sql text.

        """
        self.sql = sql
        self.default_db = default_db

    def __str__(self):
        return self.sql


class SqlExtractor(object):
    """Base class for sql extractor

    """

    def get_sqls(self):
        """This function extracts sqls.

        Returns:
           A list of :class:`SQL`. For example:
           [SQL('', u'select a.id, b.name from db.ac a join db.bc b on a.id=b.id or a.id=b.iid where a.cnt > 10')]

        """
        return []


class TextSqlExtractor(SqlExtractor):
    """Class for file sql extractor

    """

    def __init__(self, path):
        """Constructor.

        Args:
           path (str): File path.

        """
        self.path = path

    def get_sqls(self):
        """This function extracts sqls from the text file.

        Returns:
           A list of :class:`SQL`. For example:
           [SQL('', u'select a.id, b.name from db.ac a join db.bc b on a.id=b.id or a.id=b.iid where a.cnt > 10')]

        """
        with codecs.open(self.path, 'r', 'utf-8') as f:
            return filter(lambda _: _ != '', [SQL('', _.strip()) for _ in f.read().split(';')])


class MybatisInlineSqlExtractor(SqlExtractor):
    """Class for inline-mybatis sql extractor

    """

    def __init__(self, dir, encoding='utf-8'):
        """Constructor.

        Args:
           dir (str): directory path.

        Kwargs:
           encoding (str): file encoding type, e.g., *utf-8*

        """
        self.dir = dir
        self.encoding = encoding

    @staticmethod
    def remove_comment(content):
        content = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "",
                        content)  # remove all occurance streamed comments (/*COMMENT */) from string
        content = re.sub(re.compile("//.*?\n"), "",
                         content)  # remove all occurance singleline comments (//COMMENT\n ) from string
        return content

    @staticmethod
    def remove_params(content):
        return re.sub(r'#\{[\w\.]+\}', r'0', content)

    @staticmethod
    def find_right_paren_pos(content):
        quoting = False
        pre_slash = False
        for i, char in enumerate(content):
            if pre_slash:
                char = '\\' + char
                pre_slash = not pre_slash
            if char == '"':
                quoting = not quoting
            elif char == '\\':
                pre_slash = True
            elif char == ')' and not quoting:
                return i
        return -1

    @staticmethod
    def get_selects_from_text(content):
        sqls = []
        select_keyword = '@Select\s*\('
        for m in re.finditer(select_keyword, content):
            rparen_pos = MybatisInlineSqlExtractor.find_right_paren_pos(content[m.end():])
            if rparen_pos < 0:
                continue
            sqls.append(SQL('', eval(content[m.end():m.end() + rparen_pos].replace('\r', '').replace('\n', '')).strip()))
        return sqls

    def get_sqls(self):
        """This function extracts sqls from the java files with mybatis sqls.

        Returns:
           A list of :class:`SQL`. For example:
           [SQL('', u'select a.id, b.name from db.ac a join db.bc b on a.id=b.id or a.id=b.iid where a.cnt > 10')]

        """
        sqls = []
        for root, dirs, files in os.walk(self.dir):
            for file in files:
                if not file.endswith('.java'):
                    continue
                with codecs.open(os.path.join(root, file), 'r', encoding=self.encoding) as f:
                    sqls.extend(MybatisInlineSqlExtractor.get_selects_from_text(MybatisInlineSqlExtractor.remove_comment(f.read())))
        return sqls


class MysqlGeneralLogSqlExtractor(SqlExtractor):
    """Class for mysql-general-log sql extractor

    """

    def __init__(self, log_path):
        """Constructor.

        Args:
           log_path (str): mysql general log file path.

        """
        self.log_path = log_path

    def get_sqls(self):
        """This function extracts sqls from mysql general log file.


        Returns:
           A list of :class:`SQL`. For example:
           [SQL('', u'select a.id, b.name from db.ac a join db.bc b on a.id=b.id or a.id=b.iid where a.cnt > 10')]

        """
        general_log = open(self.log_path)
        log = GeneralQueryLog(general_log)
        session_db_map = {}
        sqls = []
        for entry in log:
            if entry['command'] == 'Connect':
                m = re.search('\s+on\s(?P<name>\w+)', entry['argument'])
                if m:
                    session_db_map[entry['session_id']] = m.groupdict()['name'].strip()
            elif entry['command'] == 'Init DB':
                session_db_map[entry['session_id']] = entry['argument'].strip()
            elif entry['command'] == 'Query':
                sql = entry['argument']
                if sql.strip()[:6].lower() == 'select':
                    yield SQL(session_db_map.get(entry['session_id'], ''), sql)

