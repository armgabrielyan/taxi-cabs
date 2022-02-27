from ml.train_test.regressors.lat_regressor import LatRegressor
from ml.train_test.regressors.long_regressor import LongRegressor


class LatLongPredictor:
  def __init__(self, lat_model_name, long_model_name):
    self.lat_regressor = LatRegressor(model_name=lat_model_name)
    self.long_regressor = LongRegressor(model_name=long_model_name)
    
    self.lat_regressor.load_model()
    self.long_regressor.load_model()

  def predict(self, X):
    lat = self.lat_regressor.predict(X)
    long = self.long_regressor.predict(X)

    return zip(lat, long)

    