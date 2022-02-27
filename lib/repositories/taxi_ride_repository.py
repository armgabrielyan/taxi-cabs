from sqlalchemy import and_
from lib.db.connection import session


class TaxiRideRepository:
    def get_by_taxi_id_and_ride_id(self, taxi_id, ride_id):
        from lib.views.taxi_rides_features import TaxiRidesFeatures

        taxi_ride_query = session.query(TaxiRidesFeatures). \
            filter(
                and_(
                    TaxiRidesFeatures.taxi_id == taxi_id,
                    TaxiRidesFeatures.ride_id == ride_id
                )
            ). \
            first()

        if taxi_ride_query is None:
            return None
        
        taxi_ride = {
            'id': taxi_ride_query.id,
            'taxi_id': taxi_ride_query.taxi_id,
            'ride_id': taxi_ride_query.ride_id,
            'duration': taxi_ride_query.duration,
            'start_weekday': taxi_ride_query.start_weekday,
            'distance': taxi_ride_query.distance,
        }

        return taxi_ride
