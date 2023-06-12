from fastapi import FastAPI
from datetime import datetime
import pandas as pd

app = FastAPI()


@app.get('/')
def index():

    return 'hola'
