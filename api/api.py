import os
import flask
from flask import jsonify
from lib.utils.startup import startup
from lib.utils.config import is_development_env
from lib.repositories.taxi_ride_repository import TaxiRideRepository


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


app.run()
