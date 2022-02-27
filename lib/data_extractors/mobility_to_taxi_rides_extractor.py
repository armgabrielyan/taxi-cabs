import os
import glob
from datetime import datetime
import pandas as pd
from tqdm import tqdm
from geopy import distance as geo_distance
from lib.models.taxi_ride import TaxiRide
from lib.utils.rides import get_rides_indices
from lib.db.connection import session


class MobilityToTaxiRidesExtractor:
    def __init__(self, overwrite=False):
        self.table_name = 'taxi_rides_features'
        self.data_path = os.environ['DATA_PATH']
        self.overwrite = overwrite

    def extract(self):
        taxi_ride = session.query(TaxiRide).first()

        if self.overwrite or not taxi_ride:
            session.execute(f'TRUNCATE TABLE {TaxiRide.__tablename__};')
            session.commit()
            session.close()

            self.__transform()
            self.__save()

    def __transform(self):
        taxi_data_file_paths = glob.glob(os.path.join(self.data_path, '*.txt'))

        total_taxi_rides = []

        for taxi_id, file_path in tqdm(enumerate(taxi_data_file_paths, start=1)):
            taxi_data = self.__read_data_file(file_path)
            taxi_rides = self.__transform_single_taxi_data(
                data=taxi_data,
                taxi_id=taxi_id
            )

            total_taxi_rides.extend(taxi_rides)

        self.total_taxi_rides = total_taxi_rides

    def __transform_single_taxi_data(self, data, taxi_id):
        rides_indices = get_rides_indices(data.occupancy)

        taxi_rides = []

        for ride_id, (start, end) in enumerate(rides_indices, start=1):
            start_row = data.iloc[start]
            end_row = data.iloc[end - 1]

            start_time = datetime.fromtimestamp(start_row['time'])
            end_time = datetime.fromtimestamp(end_row['time'])

            distance = geo_distance.distance(
                (start_row['latitude'], start_row['longitude']),
                (end_row['latitude'], end_row['longitude']),
            ).km

            taxi_ride = TaxiRide(
                taxi_id=taxi_id,
                ride_id=ride_id,
                start_latitude=start_row['latitude'],
                start_longitude=start_row['longitude'],
                end_latitude=end_row['latitude'],
                end_longitude=end_row['longitude'],
                number_of_waypoints=end - start,
                start_time=start_time,
                end_time=end_time,
                distance=distance,
            )

            taxi_rides.append(taxi_ride)

        return taxi_rides

    def __read_data_file(self, file_path):
        data = pd.read_csv(
            file_path,
            sep=' ',
            header=None
        )
        data.columns = ['latitude', 'longitude', 'occupancy', 'time']

        return data

    def __save(self):
        session.add_all(self.total_taxi_rides)
        session.commit()
        session.close()
