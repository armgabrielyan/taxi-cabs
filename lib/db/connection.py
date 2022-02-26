from psycopg2.extensions import register_adapter, AsIs
import numpy as np
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.utils.config import is_development_env

load_dotenv()

db_adapter = os.environ['DATABASE_ADAPTER']
db_host = os.environ['DATABASE_HOST']
db_name = os.environ['DATABASE_NAME']
db_username = os.environ['DATABASE_USERNAME']
db_password = os.environ['DATABASE_PASSWORD']

engine = create_engine(
    f'{db_adapter}://{db_username}:{db_password}@{db_host}/{db_name}',
    echo=is_development_env()
)

Session = sessionmaker(bind=engine)
session = Session()


def addapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)


def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)


register_adapter(np.float64, addapt_numpy_float64)
register_adapter(np.int64, addapt_numpy_int64)
