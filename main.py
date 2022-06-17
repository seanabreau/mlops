from datetime import datetime

import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI, Query, Request

load_dotenv()

app = FastAPI()
db_file = "data.csv"


@app.get("/v1/getmodel/{model}")
async def get_model(request: Request, model: str):
    """
    Get model data from the database
