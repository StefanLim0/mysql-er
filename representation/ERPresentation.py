from itertools import groupby
from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('./representation/templates/'))


def create_structure_ers_from_relations(relations):
    """This function gets structured entity relationship.

    Args:
       relations (list):  List of (:class:`FieldPath` :class:`FieldPath`)

    Returns:
       Structured ER dict. For example:
       {'database_name': {'table_name': {'field_name': ['foreign_database_table_field']}}

    A way might be used is

    >>> print create_structure_ers_from_relations([(FieldPath('db', 'ac', 'id'), FieldPath('db', 'bc', 'id'))])
    {'db': {'ac': {'id': ['db.bc.id']}, {'bc': {'id': ['db.ac.id']}}}}

    """
    relations.extend([_[::-1] for _ in relations]) # add reverse
    relations = sorted(list(set([tuple(_) for _ in relations])), key=lambda _: _[0].db) # remove duplicate
    dbs = {}
    for db_key, tb_grp in groupby(relations, key=lambda _: _[0].db): # group by db name
        if db_key == '':
            continue
        tbs = {}
        for tb_key, fd_grp in groupby(sorted(list(tb_grp), key=lambda _: _[0].tb), key=lambda _: _[0].tb):
            fds = {}
            for fd_key, foreign_grp in groupby(sorted(list(fd_grp), key=lambda _: _[0].fd), key=lambda _: _[0].fd):
                fds[fd_key] = sorted([str(_[1]) for _ in list(foreign_grp)])
            tbs[tb_key] = fds
        dbs[db_key] = tbs
    return dbs


def create_er_html(relations):
    """This function create entity-relationship html.

    Args:
       relations (list):  List of (:class:`FieldPath` :class:`FieldPath`)

    Returns:
       Html str.

    A way might be used is

    >>> print create_structure_ers_from_relations([(FieldPath('db', 'ac', 'id'), FieldPath('db', 'bc', 'id'))])

    """
    dbs = create_structure_ers_from_relations(relations)
    template = ENV.get_template('er_template.html')
    return template.render(dbs=dbs)