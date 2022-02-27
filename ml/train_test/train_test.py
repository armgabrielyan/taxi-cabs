import json
from ml.train_test.regressors.lat_regressor import LatRegressor
from ml.train_test.regressors.long_regressor import LongRegressor

if __name__ == '__main__':
    for (coordinate, Regressor) in [('latitude', LatRegressor), ('longitude', LongRegressor)]:
        print(f'***** Start training models for {coordinate} regression *****')

        for model_name in ['linear_regression', 'gradient_boosting', 'random_forest']:
            print(f'Start training {model_name} model...')

            regressor = Regressor(model_name=model_name)
            regressor.train()
            regressor.save_model()

            test_results = regressor.test()
            test_results = json.dumps(test_results, sort_keys=True, indent=4)

            print(f'Test results: {test_results}')
            print(f'End training {model_name} model.')

        print(f'***** End training models for {coordinate} regression *****')
