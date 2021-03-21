from fastapi import APIRouter

from app.recognizer.recognizer import initialize_model

recognizer_router = APIRouter(prefix='/recognizer', tags=['recognizer'])

model = initialize_model()


@recognizer_router.get('/')
def index():
    return {'message': str(model.summary())}