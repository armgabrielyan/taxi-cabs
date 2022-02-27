import pandas as pd
from sklearn.model_selection import train_test_split
from lib.db.connection import session
from lib.models.taxi_ride import TaxiRide
from lib.views.taxi_rides_features import TaxiRidesFeatures


class LatLongDataLoader:
    FEATURE_VARIABLES = [
      'start_latitude',
      'start_longitude',
      'duration',
      'distance',
      'start_weekday',
      'number_of_waypoints',
    ]

    def __init__(self, dependent_variable, test_size=0.2):
        self.dependent_variable = dependent_variable
        self.test_size = test_size

    def load(self):
        taxi_rides_query = session.query(TaxiRide).all()
        taxi_ride_feature_query = session.query(TaxiRidesFeatures).all()

        taxi_rides = []

        for tr, tr_feature in zip(taxi_rides_query, taxi_ride_feature_query):
            taxi_ride = {
                'id': tr.id,
                'start_latitude': tr.start_latitude,
                'start_longitude': tr.start_longitude,
                'end_latitude': tr.end_latitude,
                'end_longitude': tr.end_longitude,
                'number_of_waypoints': tr.number_of_waypoints,
                'taxi_id': tr_feature.taxi_id,
                'ride_id': tr_feature.ride_id,
                'duration': tr_feature.duration.total_seconds(),
                'start_weekday': tr_feature.start_weekday,
                'distance': tr_feature.distance,
            }

            taxi_rides.append(taxi_ride)

        taxi_rides_df = pd.DataFrame(taxi_rides)

        X = taxi_rides_df[self.FEATURE_VARIABLES]
        y = taxi_rides_df[self.dependent_variable].values

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=42
        )

        return X_train, X_test, y_train, y_test
