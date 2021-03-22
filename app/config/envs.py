import os, sys
from dotenv import load_dotenv

# Setup base directory and load environment variables
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, 'prod.env'))
sys.path.append(BASE_DIR)


class Envs:
    """
    This class includes all environment variables used in this application
    """
    SECRET_KEY = os.getenv('SECRET_KEY')
    HOST = os.getenv('HOST')
    PORT = int(os.getenv('PORT'))
    ENVIRONMENT = os.getenv('ENVIRONMENT')
    DATABASE_URL = os.getenv('DATABASE_URL')