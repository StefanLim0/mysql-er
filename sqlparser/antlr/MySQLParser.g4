
parser grammar MySQLParser;

options
   { tokenVocab = MySQLLexer; }

stat
   : select_clause+
   ;

schema_name
   : ID
   ;

select_clause
   : SELECT column_list_clause ( FROM table_references )? ( where_clause )?
   ;

table_name
   : (schema_name DOT )? ID
   ;

table_alias
   : ID
   ;

column_name
   : ( ( schema_name DOT )? ID DOT )? ID ( ( AS )? column_name_alias )? | ( table_alias DOT )? ID | USER_VAR ( ( AS )? column_name_alias )?
   ;

column_name_alias
   : ID
   ;

index_name
   : ID
   ;

column_list
   : LPAREN column_name ( COMMA column_name )* RPAREN
   ;

column_list_clause
   : column_name ( COMMA column_name )*
   ;

from_clause
   : FROM table_name ( COMMA table_name )*
   ;

select_key
   : SELECT
   ;

where_clause
   : WHERE expression
   ;

expression
   : simple_expression ( expr_op simple_expression )*
   ;

element
   : USER_VAR | ID | ( '|' ID '|' ) | INT | column_name
   ;

right_element
   : element
   ;

left_element
   : element
   ;

target_element
   : element
   ;

relational_op
   : EQ | LTH | GTH | NOT_EQ | LET | GET
   ;

expr_op
   : AND | XOR | OR | NOT
   ;

between_op
   : BETWEEN
   ;

is_or_is_not
   : IS | IS NOT
   ;

simple_expression
   : left_element relational_op right_element | target_element between_op left_element AND right_element | target_element is_or_is_not NULL
   ;

table_references
   : table_reference ( ( COMMA table_reference ) | join_clause )*
   ;

table_reference
   : table_factor1 | table_atom
   ;

table_factor1
   : table_factor2 ( ( INNER | CROSS )? JOIN table_atom ( join_condition )? )?
   ;

table_factor2
   : table_factor3 ( STRAIGHT_JOIN table_atom ( ON expression )? )?
   ;

table_factor3
   : table_factor4 ( ( LEFT | RIGHT ) ( OUTER )? JOIN table_factor4 join_condition )?
   ;

table_factor4
   : table_atom ( NATURAL ( ( LEFT | RIGHT ) ( OUTER )? )? JOIN table_atom )?
   ;

table_atom
   : ( table_name ( partition_clause )? ( ( AS )? table_alias )? ( index_hint_list )? ) # tableAtomBasic
   | ( subquery subquery_alias ) # tableAtomSubquery
   | ( LPAREN table_references RPAREN ) # tableAtomParen
   | ( OJ table_reference LEFT OUTER JOIN table_reference ON expression ) # tableAtomComplex
   ;

join_clause
   : ( ( INNER | CROSS )? JOIN table_atom ( join_condition )? ) | ( STRAIGHT_JOIN table_atom ( ON expression )? ) | ( ( LEFT | RIGHT ) ( OUTER )? JOIN table_factor4 join_condition ) | ( NATURAL ( ( LEFT | RIGHT ) ( OUTER )? )? JOIN table_atom )
   ;

join_condition
   : ( ON expression ( expr_op expression )* ) # joinOn
   | ( USING column_list ) # joinColumns
   ;

index_hint_list
   : index_hint ( COMMA index_hint )*
   ;

index_options
   : ( INDEX | KEY ) ( FOR ( ( JOIN ) | ( ORDER BY ) | ( GROUP BY ) ) )?
   ;

index_hint
   : USE index_options LPAREN ( index_list )? RPAREN | IGNORE index_options LPAREN index_list RPAREN
   ;

index_list
   : index_name ( COMMA index_name )*
   ;

partition_clause
   : PARTITION LPAREN partition_names RPAREN
   ;

partition_names
   : partition_name ( COMMA partition_name )*
   ;

partition_name
   : ID
   ;

subquery_alias
   : ID
   ;

subquery
   : LPAREN select_clause RPAREN
   ;
