from typing import Union
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

import mysql.connector
from db import session
from model import UserTable

# FastAPI() 인스턴스 생성
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/")
def read_root():
    dataall =  session.query(UserTable).all()
    return dataall

@app.post("/users/")
def create_users(check_mail:str, email:str, token:str, delete_yn:bool, start_dt:str,end_dt:str, last_dt:str ):
    return read_root()