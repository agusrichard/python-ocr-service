import cv2
import numpy as np
from keras.preprocessing.image import array_to_img
from fastapi import APIRouter, File, UploadFile

from app.recognizer.recognizer import get_word, get_letters


recognizer_router = APIRouter(prefix='/recognizer', tags=['recognizer'])


@recognizer_router.get('/')
def index():
    return {'message': 'You are in the index section of recognizer routers'}

@recognizer_router.post('/recognizing')
def recognizing(file: bytes = File(...)):
    decoded = cv2.imdecode(np.frombuffer(file, np.uint8), -1)
    letters, marked_image = get_letters(decoded)
    word = get_word(letters)
    return {'message': word}