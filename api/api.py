import os
import pandas as pd
import flask
from flask import jsonify, request
from lib.utils.startup import startup
from lib.utils.config import is_development_env
from lib.repositories.taxi_ride_repository import TaxiRideRepository
from ml.predictors.lat_long_predictor import LatLongPredictor


app = flask.Flask(__name__)
app.config['DEBUG'] = is_development_env()

with app.app_context():
    startup()


@app.route('/taxi_rides/taxi_id/<int:taxi_id>/ride_id/<int:ride_id>', methods=['GET'])
def get_taxi_ride(taxi_id, ride_id):
    taxi_ride_repo = TaxiRideRepository()
    taxi_ride = taxi_ride_repo.get_by_taxi_id_and_ride_id(
        taxi_id=taxi_id,
        ride_id=ride_id
    )

    if taxi_ride is None:
        return jsonify({ 'message': f'Taxi ride with taxi_id {taxi_id} and ride_id {ride_id} is not found. Please provide other taxi_id and ride_id.' })

    taxi_ride['duration'] = taxi_ride['duration'].total_seconds()

    return jsonify(taxi_ride)
    
@app.route('/predict_lat_long', methods=['GET'])
def predict_lat_long():
    start_latitude = request.args.get('start_latitude')
    start_longitude = request.args.get('start_longitude')
    duration = request.args.get('duration')
    distance = request.args.get('distance')
    start_weekday = request.args.get('start_weekday')
    number_of_waypoints = request.args.get('number_of_waypoints')

    X = pd.DataFrame({
        'start_latitude': [start_latitude],
        'start_longitude': [start_longitude],
        'duration': [duration],
        'distance': [distance],
        'start_weekday': [start_weekday],
        'number_of_waypoints': [number_of_waypoints]
    })

    predictor = LatLongPredictor(
        lat_model_name=os.environ['LAT_MODEL_NAME'],
        long_model_name=os.environ['LONG_MODEL_NAME']
    )
    lat_long = predictor.predict(X)
    lat_long = list(lat_long)
    
    return jsonify(lat_long)

if __name__ == '__main__':
    app.run()
