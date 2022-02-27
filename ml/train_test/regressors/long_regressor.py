from ml.train_test.regressors.base_regressor import BaseRegressor


class LongRegressor(BaseRegressor):
    def __init__(self, model_name):
        super().__init__(
            model_name=model_name,
            dependent_variable='end_longitude'
        )
