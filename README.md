# Data and feature extractor for taxi cabs dataset 

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

To start the application, please run the following command from the project root directory: 

```console
PYTHONPATH=/Users/{your username}/{your projects directory}/taxi_cabs python api/api.py
```
