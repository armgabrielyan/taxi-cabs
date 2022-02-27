import os
import pandas as pd
from joblib import dump, load
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from ml.data_loaders.taxi_ride_data_loader import LatLongDataLoader


class BaseRegressor:
    NUMERIC_VARIABLES = [
      'start_latitude',
      'start_longitude',
      'duration',
      'distance'
    ]

    CATEGORICAL_VARIABLES = ['start_weekday', 'number_of_waypoints']

    def __init__(self, model_name, dependent_variable):
        if model_name == 'linear_regression':
            self.regressor = LinearRegression()
        elif model_name == 'gradient_boosting':
            self.regressor = GradientBoostingRegressor()
        elif model_name == 'random_forest':
            self.regressor = RandomForestRegressor()

        self.model_name = model_name
        self.dependent_variable = dependent_variable

        self.__load_data()

    def train(self):
        numeric_transformer = MinMaxScaler()

        pre_processing = ColumnTransformer(transformers=[
            ('numeric', numeric_transformer, self.NUMERIC_VARIABLES),
        ], remainder='passthrough')

        self.regressor_pipeline = Pipeline(steps=[
            ('pre_processing', pre_processing),
            ('model', self.regressor)
        ])

        self.regressor_pipeline.fit(self.X_train, self.y_train)

        return self.regressor_pipeline

    def test(self):
        on_train = self.__evaluate_metrics(X=self.X_train, y=self.y_train)
        on_test = self.__evaluate_metrics(X=self.X_test, y=self.y_test)

        return {'on_train': on_train, 'on_test': on_test}

    def predict(self, X):
        return self.regressor_pipeline.predict(X)

    def save_model(self):
        path = self.__get_model_path()

        dump(self.regressor_pipeline, path)

    def load_model(self):
        path = self.__get_model_path()

        self.regressor_pipeline = load(path)

        return self.regressor_pipeline

    def __load_data(self):
        lat_long_loader = LatLongDataLoader(
            dependent_variable=self.dependent_variable
        )
        self.X_train, self.X_test, self.y_train, self.y_test = lat_long_loader.load()

    def __evaluate_metrics(self, X, y):
        y_pred = self.regressor_pipeline.predict(X)

        r2 = self.regressor_pipeline.score(X, y)
        rmse = mean_squared_error(y, y_pred, squared=False)
        mae = mean_absolute_error(y, y_pred)

        return {
            'r2': r2,
            'rmse': rmse,
            'mae': mae,
        }

    def __get_model_path(self):
        return os.path.join(
            os.environ['OUTPUT_PATH'],
            self.dependent_variable,
            f'{self.model_name}.joblib'
        )
