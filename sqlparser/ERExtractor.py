from antlr4 import *
from sqlparser.antlr.MySQLParser import MySQLParser
from sqlparser.antlr.MySQLLexer import MySQLLexer
from sqlparser.antlr.MySQLParserVisitor import MySQLParserVisitor, TableInfo


class FieldPath(object):
    """Class for field path

    """

    def __init__(self, db, tb, fd):
        """Constructor.

        Args:
           db (str): Database's name.
           tb (str): Table's name.
           fd (str): Field's name.

        """
        self.db = db
        self.tb = tb
        self.fd = fd

    def __str__(self):
        return self.db + '.' + self.tb + '.' + self.fd

    def __repr__(self):
        return self.db + '.' + self.tb + '.' + self.fd

    def __hash__(self):
        return hash((self.db, self.tb, self.fd))

    def __eq__(self, other):
        return (self.db, self.tb, self.fd) == (other.db, other.tb, other.fd)


def get_er_from_sql(default_db_name, sql):
    """This function gets entity relationship from one sql line.

    Args:
       default_db_name (unicode):  The default database name.
       sql (unicode):   The sql line to be parse.

    Returns:
       A list of pairs of :class:`FieldPath`. For example:
       [(FieldPath(u'database0', 'table0', 'field0'), FieldPath(u'database0', 'table1', 'field1'))]

    A way might be used is

    >>> print get_er_from_sql(default_db_name = u'', sql = u'select a.id, b.name from db.ac a join db.bc b on a.id=b.id or a.id=b.iid where a.cnt > 10')
    [(('db', 'ac', 'id'), ('db', 'bc', 'id')), (('db', 'ac', 'id'), ('db', 'bc', 'iid'))]

    """

    def form_field_path(default_db_name, path):
        sub_names = path.split('.')
        # check and form (db_name, tb_name, field_name)
        if len(sub_names) < 2:
            return
        elif len(sub_names) == 2:
            if default_db_name == '':
                return
            sub_names.insert(0, default_db_name)
        return FieldPath(*sub_names)

    sql = sql if isinstance(sql, unicode) else sql.decode('utf-8')
    input = InputStream(sql.lower())
    lexer = MySQLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MySQLParser(stream)
    tree = parser.stat()
    v = MySQLParserVisitor()
    v.visit(tree)
    ers = []
    for condition in TableInfo.on_conditions:
        tokens = [_.strip() for _ in condition.split('=')]
        er = []
        for token in tokens:
            sub_names = token.split('.')
            tb_name = '.'.join(sub_names[:-1])
            field_path = None
            if tb_name in TableInfo.table_name_to_alias:
                field_path = form_field_path(default_db_name, token)
            elif tb_name in TableInfo.table_alias_to_name:
                field_path = form_field_path(default_db_name, TableInfo.table_alias_to_name[tb_name] + '.' + sub_names[-1])
            if field_path:
                er.append(field_path)
        if len(er) == 2:
            ers.append(tuple(er))
    # clear
    TableInfo.reset()
    return ers
