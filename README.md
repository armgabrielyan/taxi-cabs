# Data and feature extractor for taxi cabs dataset

The API is available over [here](https://taxi-cabs.herokuapp.com)

## Installation and prerequisites

1. Change to your working directory and clone the repository: ``.
2. Change to the project directory: `cd taxi_cabs`.
3. Create a new Python3 virtual environment for the project: `python3 -m venv taxi_cabs`.
4. Activate the virtual environment: `source taxi_cabs/bin/activate`.
5. Install project dependencies: `pip install -r requirements.txt`.
6. Copy `.env.example` file to `.env` file by `cp .env.example .env` and replace environment variables with the appropriate ones based on your environment setup.
7. Download the dataset and move it to the `data` directory under the project directory.

## Usage

The project includes two programs: CLI and API.

#### CLI

CLI application can be used to extract data and features from the provided taxi cabs dataset and seed them into program's database.

This can be run from the project root directory by the following command:

```console
PYTHONPATH=/Users/{your username}/{your projects directory}/taxi_cabs python cli/cli.py
```

where `/Users/{your username}/{your projects directory}/taxi_cabs` is the path for the project on your enviroment.

Please, run the command above with `--help` argument to get further details about it.

#### API

API application provides a functionality to get features about taxi rides. Currently, it includes the following endpoints:

- `GET /taxi_rides/taxi_id/<int:taxi_id>/ride_id/<int:ride_id>` - It can be used to fetch features about a certain taxi ride by providing `taxi_id` and `ride_id` parameters.
- `GET /predict_lat_long` - It can be used to fetch a ride's destination.

To start the application on your environment, please run the following command from the project root directory: 

```console
PYTHONPATH=/Users/{your username}/{your projects directory}/taxi_cabs python api/api.py
```

To use the live application deployed on Heroku, please navigate to [this website](https://taxi-cabs.herokuapp.com). For example, [this url](https://taxi-cabs.herokuapp.com/taxi_rides/taxi_id/1/ride_id/47) returns a successful API response while [this one](https://taxi-cabs.herokuapp.com/taxi_rides/taxi_id/2/ride_id/16) returns a not found response.

#### ML

We have also tried to build a predictor, which allows us to predict ride's destination. We have tried to predict the latitude and longitude separately with two different models.

Three models have been built for each coordinate, namely Linear Regression, Gradient Boosting and Random Forest. The results can be shown as follows:

**Linear Regression**


```
Latitude

{
    "on_test": {
        "mae": 0.022177760242011513,
        "r2": 0.3215514319070768,
        "rmse": 0.038243256621417934
    },
    "on_train": {
        "mae": 0.021851837912469894,
        "r2": 0.3472821588936241,
        "rmse": 0.03849552367550934
    }
}

Longitude

{
    "on_test": {
        "mae": 0.018810541331086086,
        "r2": 0.17046991169450387,
        "rmse": 0.029918019583945056
    },
    "on_train": {
        "mae": 0.018815432358114382,
        "r2": 0.17713706716262478,
        "rmse": 0.030239693064768872
    }
}
```

**Gradient Boosting**

```
{
    "on_test": {
        "mae": 0.013097763034182423,
        "r2": 0.7283122397448294,
        "rmse": 0.024200895668414057
    },
    "on_train": {
        "mae": 0.012837392222191532,
        "r2": 0.7748788590433009,
        "rmse": 0.022607660914583477
    }
}

{
    "on_test": {
        "mae": 0.014223745856292592,
        "r2": 0.479751939104783,
        "rmse": 0.023693106447759005
    },
    "on_train": {
        "mae": 0.013746269979230785,
        "r2": 0.5681265921098293,
        "rmse": 0.021907451602438226
    }
}
```

**Random Forest**

```
{
    "on_test": {
        "mae": 0.01051564599573859,
        "r2": 0.7733511489677847,
        "rmse": 0.02210411663485326
    },
    "on_train": {
        "mae": 0.004042313360907428,
        "r2": 0.9622286908252679,
        "rmse": 0.009260373619455786
    }
}

{
    "on_test": {
        "mae": 0.01206068725216195,
        "r2": 0.5689290568707346,
        "rmse": 0.021567069874296577
    },
    "on_train": {
        "mae": 0.004575521554021362,
        "r2": 0.9386946539390918,
        "rmse": 0.008253968426195434
    }
}
```

Random Forest shows good results on test dataset but it also shows some over-fitting.

To replicate the results (approximately) on your environment, you can use the following command:

```console
PYTHONPATH=/Users/{your username}/{your projects directory}/taxi_cabs python ml/train_test/train_test.py
```

This predictor is deployed on the Heroku application and an example can be seen by navigating to the following [url](https://taxi-cabs.herokuapp.com/predict_lat_long?start_latitude=37.8&start_longitude=-122.56&duration=1247&distance=14.67&start_weekday=5&number_of_waypoints=27). Due to storage limitations, Gradient Boosting predictors are deployed on the live environment.

However, this is not so interesting problem and we are more interested in the starting location of the next taxi ride.
