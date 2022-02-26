from lib.db import setup as db_setup
from lib.data_extractors.mobility_to_taxi_rides_extractor import MobilityToTaxiRidesExtractor
from lib.feature_extractors.taxi_rides_features_extractor import TaxiRidesFeaturesExtractor

def startup(data_extractor_overwrite = False, feature_extractor_overwrite = False):
    db_setup.execute()

    mobility_to_taxi_rides_extractor  = MobilityToTaxiRidesExtractor(overwrite=data_extractor_overwrite)
    mobility_to_taxi_rides_extractor.extract()

    taxi_rides_features_extractor = TaxiRidesFeaturesExtractor(overwrite=feature_extractor_overwrite)
    taxi_rides_features_extractor.extract()