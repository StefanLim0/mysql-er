# Generated from MySQLParser.g4 by ANTLR 4.5.3
from antlr4 import *

class TableInfo:
    table_name_to_alias = {}
    table_alias_to_name = {}
    on_conditions = []

    @staticmethod
    def reset():
        TableInfo.table_name_to_alias = {}
        TableInfo.table_alias_to_name = {}
        TableInfo.on_conditions = []

def get_table_alias_to_name():
    return

# This class defines a complete generic visitor for a parse tree produced by MySQLParser.

class MySQLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MySQLParser#stat.
    def visitStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#schema_name.
    def visitSchema_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#select_clause.
    def visitSelect_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#table_name.
    def visitTable_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#table_alias.
    def visitTable_alias(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#column_name.
    def visitColumn_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#column_name_alias.
    def visitColumn_name_alias(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#index_name.
    def visitIndex_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#column_list.
    def visitColumn_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#column_list_clause.
    def visitColumn_list_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#from_clause.
    def visitFrom_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#select_key.
    def visitSelect_key(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#where_clause.
    def visitWhere_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#element.
    def visitElement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#right_element.
    def visitRight_element(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#left_element.
    def visitLeft_element(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#target_element.
    def visitTarget_element(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#relational_op.
    def visitRelational_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#expr_op.
    def visitExpr_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#between_op.
    def visitBetween_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#is_or_is_not.
    def visitIs_or_is_not(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#simple_expression.
    def visitSimple_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#table_references.
    def visitTable_references(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#table_reference.
    def visitTable_reference(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#table_factor1.
    def visitTable_factor1(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#table_factor2.
    def visitTable_factor2(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#table_factor3.
    def visitTable_factor3(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#table_factor4.
    def visitTable_factor4(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableAtomBasic.
    def visitTableAtomBasic(self, ctx):
        table_name, table_alias = '', ''
        if ctx.table_name():
            table_name = ctx.table_name().getText()
        if ctx.table_alias():
            table_alias = ctx.table_alias().getText()
        if table_name:
            TableInfo.table_name_to_alias[table_name] = table_alias
        if table_alias:
            TableInfo.table_alias_to_name[table_alias] = table_name
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableAtomSubquery.
    def visitTableAtomSubquery(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableAtomParen.
    def visitTableAtomParen(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#tableAtomComplex.
    def visitTableAtomComplex(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#join_clause.
    def visitJoin_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#joinOn.
    def visitJoinOn(self, ctx):
        if ctx.expression():
            for sub0 in ctx.expression():
                for sub1 in sub0.children:
                    TableInfo.on_conditions.append(sub1.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#joinColumns.
    def visitJoinColumns(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#index_hint_list.
    def visitIndex_hint_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#index_options.
    def visitIndex_options(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#index_hint.
    def visitIndex_hint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#index_list.
    def visitIndex_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partition_clause.
    def visitPartition_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partition_names.
    def visitPartition_names(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#partition_name.
    def visitPartition_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#subquery_alias.
    def visitSubquery_alias(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#subquery.
    def visitSubquery(self, ctx):
        return self.visitChildren(ctx)


