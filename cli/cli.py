import argparse
from lib.utils.startup import startup


parser = argparse.ArgumentParser(
  description='This program is to extract data and features from San Francisco taxi cabs dataset on mobility traces.'
)
parser.add_argument(
    '--data_extractor_overwrite',
    type=bool,
    default=False,
    help='Indicates if data extractor should overwrite already existing data or not.'
)
parser.add_argument(
    '--feature_extractor_overwrite',
    type=bool,
    default=False,
    help='Indicates if feature extractor should overwrite already existing data or not.'
)

args = parser.parse_args()

if __name__ == '__main__':
    startup(
      data_extractor_overwrite = args.data_extractor_overwrite,
      feature_extractor_overwrite = args.feature_extractor_overwrite
    )
