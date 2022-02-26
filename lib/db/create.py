from lib.db.connection import engine
from sqlalchemy_utils import database_exists, create_database

def execute():
  if not database_exists(engine.url):
      create_database(engine.url)
