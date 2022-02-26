import sqlalchemy
from sqlalchemy import select, func
from sqlalchemy_utils import create_view
from lib.models.base import Base
from lib.models.taxi_ride import TaxiRide
from lib.db.connection import session, engine


class TaxiRidesFeaturesExtractor:
    def __init__(self, overwrite = False):
        self.view_name = 'taxi_rides_features'
        self.overwrite = overwrite

    def extract(self):
        view_exists = sqlalchemy.inspect(engine).has_table(self.view_name)

        if self.overwrite or not view_exists:
            session.execute(f'DROP VIEW IF EXISTS {self.view_name};')
            session.commit()
            session.close()

            self.__create_features_view()
            self.__save()

    def __create_features_view(self):
        feature_selector = self.__select_features()

        create_view(
            self.view_name,
            feature_selector,
            Base.metadata
        )

    def __select_features(self):
        feature_selector = select([
            TaxiRide.id,
            TaxiRide.taxi_id,
            TaxiRide.ride_id,
            (TaxiRide.end_time - TaxiRide.start_time).label('duration'),
            func.extract('isodow', TaxiRide.start_time).label('start_weekday'),
            TaxiRide.distance,
        ])

        return feature_selector

    def __save(self):
        Base.metadata.create_all(engine)
