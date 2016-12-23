**Mysql-er** is a project to extract entity relationships from SQLs since foreign keys are not encouraged in RDMS
due to performance degradation. Instead of creating ER diagram by trivial human work, this project tries to extract
entity relationships by SQLs from source codes and RDMS query logs.

## Feature Support

  - ERs from `JOIN` statements in `SELECT` query
  - SQLs from text file(`;` separated), java source codes with inline mybatis SQLs and mysql general log
  - ER representation in html format

## Quickstart

  ```shell
  $ cd mysql-er
  $ pip install -r requirements.txt
  $ python sql_er.py -m text -i examples/example.sql -o examples/example-text.html
  $ python sql_er.py -m general_log -i examples/example.log -o examples/example-general-log.html
  ```shell

  `example-text.html` and `example-general-log.html` will be created under `examples` folder.

## Structure

  - sqlextractor: components to extract SQLs from multipule sources
  - sqlparser: components to parse SQL and form entity relationships
  - representation: components to show ERs
  - examples: input/output files
  - doc: documentation created by sphinx

## Acknowledgement

  - [grammars-v4](https://github.com/antlr/grammars-v4)