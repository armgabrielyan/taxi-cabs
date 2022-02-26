from lib.models.base import Base
from lib.models.taxi_ride import TaxiRide
from lib.db.connection import engine

def execute():
  TaxiRide.__table__

  Base.metadata.create_all(engine)
