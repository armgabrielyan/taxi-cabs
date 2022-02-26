from lib.models.base import Base

from sqlalchemy import Column, Integer, Float, Interval

class TaxiRidesFeatures(Base):
    __tablename__ = 'taxi_rides_features'

    id = Column(Integer, primary_key=True)
    taxi_id = Column(Integer)
    ride_id = Column(Integer)
    duration = Column(Interval)
    start_weekday = Column(Integer)
    distance = Column(Float)
