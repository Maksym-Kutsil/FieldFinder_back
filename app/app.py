from __future__ import annotations
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os


class ResponseOK(BaseModel):
    ok: bool = True
    data: list


class ResponseError(BaseModel):
    ok: bool = False
    error_code: int
    description: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=ResponseOK | ResponseError)
def get_sport():
    load_dotenv()
    sport = psycopg2.connect(os.getenv('DATABASE_URL'))
    mycursor = sport.cursor()
    mycursor.execute(f"SELECT * FROM sportstable")
    myresult = mycursor.fetchall()
    return {"ok": True, "data": myresult}




