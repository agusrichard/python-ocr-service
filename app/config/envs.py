import os, sys
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, '.env.dev'))
sys.path.append(BASE_DIR)

class Envs:
    SECRET_KEY = os.getenv('SECRET_KEY')
    HOST = os.getenv('HOST')
    PORT = int(os.getenv('PORT'))
    ENVIRONMENT = os.getenv('ENVIRONMENT')