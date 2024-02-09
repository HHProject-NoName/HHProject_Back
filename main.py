from typing import Union
from fastapi import Depends,FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
import crud, model, schema

import mysql.connector
from db import session


# FastAPI() 인스턴스 생성
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/", response_model=list[schema.User])
def get_all_user(db:session=Depends(get_db)):
    dataall =  crud.get_all_user(db)
    if dataall is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dataall

@app.post("/users/")
def create_users(check_mail:str, email:str, token:str, delete_yn:bool, start_dt:str,end_dt:str, last_dt:str ):
    return read_root()