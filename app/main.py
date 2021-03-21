import uvicorn
from fastapi import FastAPI

from app.config.envs import Envs
from app.routers.recognizer import recognizer_router


app = FastAPI(title='Python OCR Service')

# Register routers
app.include_router(recognizer_router)


@app.get('/')
def root():
    """
    Hi, Welcome to the Python OCR service
    """
    return 'Welcome to the Python OCR Service'


def run():
    """
    Running the app from manage.py file
    """
    uvicorn.run('app.main:app', host=Envs.HOST, port=Envs.PORT, reload=True if Envs.ENVIRONMENT == 'development' else False)