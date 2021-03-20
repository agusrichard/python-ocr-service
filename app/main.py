import uvicorn
from fastapi import FastAPI

from app.config.envs import Envs

app = FastAPI(title='Python OCR Service')

@app.get('/')
def root():
    return 'Welcome to the Python OCR Service'


def run():
    """
    Running the app from manage.py file
    """
    uvicorn.run('app.main:app', host=Envs.HOST, port=Envs.PORT, reload=True if Envs.ENVIRONMENT == 'development' else False)