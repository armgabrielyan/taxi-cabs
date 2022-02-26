from lib.db import create, migrate


def execute():
    create.execute()
    migrate.execute()
