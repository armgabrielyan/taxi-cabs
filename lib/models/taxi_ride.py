from sqlalchemy import Column, Integer, Float, DateTime

from lib.models.base import Base


class TaxiRide(Base):
    __tablename__ = 'taxi_rides'

    id = Column(Integer, primary_key=True)
    taxi_id = Column(Integer)
    ride_id = Column(Integer)
    start_latitude = Column(Float)
    start_longitude = Column(Float)
    end_latitude = Column(Float)
    end_longitude = Column(Float)
    number_of_waypoints = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    distance = Column(Float)
