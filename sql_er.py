import re
import codecs
import argparse
from sqlextractor.SqlExtractor import TextSqlExtractor, MysqlGeneralLogSqlExtractor, MybatisInlineSqlExtractor
from sqlparser.ERExtractor import get_er_from_sql
from representation import create_er_html

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', help='`text`, `mybatis_inline` or `general_log`', required=True)
    parser.add_argument('-i', '--input', help='file for mode `text` and `general_log`, directory for `mybatis_inline`', required=True)
    parser.add_argument('-o', '--output', help='output file path', required=True)
    args = parser.parse_args()

    relations = []
    if args.mode == 'text':
        for sql in TextSqlExtractor(args.input).get_sqls():
            if re.search('\sjoin\s', sql.sql, re.IGNORECASE):
                relations.extend(get_er_from_sql(sql.default_db, sql.sql))
    elif args.mode == 'mybatis_inline':
        for sql in MybatisInlineSqlExtractor(args.input).get_sqls():
            if re.search('\sjoin\s', sql.sql, re.IGNORECASE):
                relations.extend(get_er_from_sql(sql.default_db, sql.sql))
    elif args.mode == 'general_log':
        for sql in MysqlGeneralLogSqlExtractor(args.input).get_sqls():
            if re.search('\sjoin\s', sql.sql, re.IGNORECASE):
                relations.extend(get_er_from_sql(sql.default_db, sql.sql))
    with codecs.open(args.output, 'w', 'utf-8') as f:
        f.write(create_er_html(relations))
