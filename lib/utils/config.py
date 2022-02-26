import os

def is_development_env():
    return os.environ['ENVIRONMENT'] == 'development'