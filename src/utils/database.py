"""
    database.py
    ~~~~~~~~~~~
    Provides an abstraction over the database interaction, by providing
    a class using a Singleton pattern to perform database operations
    abstracted as functions.
"""

import enum

import sqlalchemy
from sqlalchemy import sql

__INSTANCE__ = None

class ProjectDatabase:
    """ Minimal abstraction over the project database """

    def __init__(self, database_engine):
        self.engine          = database_engine
        self.meta            = sqlalchemy.MetaData(database_engine)

        self.user            = sqlalchemy.Table('user', self.meta, autoload=True)

    def execute(self, *queries):
        """ Executes the given set of queries, or a set of query sets.
            This method operates in two modes:
            - If given a set of query parameter tuples passed as positional arguments,
                the queries are executed as a single transaction.
            - If given a set of query sets, with each query set being a collection of
                query tuples, each query set is executed as a single transaction.
            Query tuples consist of a parameterized SQL query object and the set of parameters
            to bind with the query during execution as a dictionary.

        Returns:
            list[sqlalchemy.LegacyCursorResult]: Results of the queries for a single transaction.
            list[list[sqlalchemy.LegacyCursorResult]]: Results of the queries for multiple transactions.
        """
        if len(queries) == 0: return

        with self.engine.begin() as connection:
            if isinstance(queries[0], (list, tuple)) and \
                isinstance(queries[0][0], (list, tuple)):
                result = []
                for atomic_queries in queries:
                    with connection.begin() as transaction:
                        result.append([
                            connection.execute(*query)
                            for query in atomic_queries
                        ])
                return result
            else:
                with connection.begin():
                    if isinstance(queries[0], (list, tuple)):
                        return [
                            connection.execute(*query)
                            for query in queries
                        ]
                    else:
                        return [
                            connection.execute(query)
                            for query in queries
                        ]

def get_instance(database_engine):
    """ Returns the current instance of the ProjectDatabase abstraction. """
    # pylint: disable=global-statement
    global __INSTANCE__
    if not __INSTANCE__:
        __INSTANCE__ = ProjectDatabase(database_engine)
    return __INSTANCE__