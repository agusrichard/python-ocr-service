import os
from keras.models import load_model

from app.config.envs import BASE_DIR


def initialize_model():
    model = load_model(os.path.join(BASE_DIR, 'app', 'recognizer', 'model.h5'))
    print('Model Summary', model.summary())

    return model