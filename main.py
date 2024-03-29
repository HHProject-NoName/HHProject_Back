from typing import Union
from fastapi import Depends,FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
import crud, model, schema, fastemail
import asyncio

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
###########################################################################################
# 검색
###########################################################################################
 
#예시) 현재 접속하자마자 전체 DB정보 가져오는 상태
@app.get("/", response_model=list[schema.User])
def get_all_user(db:session=Depends(get_db)):
    dataall =  crud.get_all_user(db)
    if dataall is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dataall

#메일 검색
@app.post("/email_search/")
def create_users(email:str, db:session=Depends(get_db)):
    dataone = crud.get_mail_search(db, email)
    return dataone

###########################################################################################
# 인증
###########################################################################################
from flask import Flask, request, jsonify

#임시저장소
verification_codes = {}
#사용자에게 인증 코드 전송
@app.post('/submit_email/')
async def submit_email(email:str):
    # data = request.get_json()
    # print("=======? request" + data)
    # email = data.get('email')
    print(email)
    if email:
        code = fastemail.generate_random_code()
        message = f"아래의 인증번호를 입력하세요. \n{code}"
        verification_codes[email] = code
        await asyncio.gather(fastemail.send_verification_email(email, message))
        # return HTTPException(status_code=200, detail='sent successfully')
        return {"email_send": "success"}
    else:
        return HTTPException(status_code=400, detail='empty email')
    
#사용자 제출된 인증 코드 확인
@app.post('/submit_code/')
def submit_code(email:str, code:str):
    # data = request.get_json();
    # email = data.get('email')
    # code = data.get('code')
    
    if email and code:
        stored_code = verification_codes.get(email)
        
        if stored_code == code :
            return {"return" : "True"}
        else:
            return {"return" : "False"}
    else:
        return HTTPException(status_code=400, detail='email or code is empty')
    

###########################################################################################
# 로그인 저장, 삭제
###########################################################################################

# @app.post('/login_save', response_model=list[schema.SaveLogin])
@app.post('/login_save')   
# def login_save(check_mail:str,
#                email:str, 
#                start_dt:str, 
#                last_dt:str, 
#                token: Union[str, None] = None,
#                delete_yn: Union[str, None] = None,
#                end_dt:Union[str, None] = None, 
#                db:session=Depends(get_db)):
    # input_dict = input_Data.dict()
    # check_mail = input_dict.check_mail
    # email = input_dict.email
def login_save(input_data:schema.SaveLogin, db:session=Depends(get_db)):
    if input_data.check_mail and input_data.email:
        result = crud.save_login(db, input_data)
        return {"result": result}
    else:
        return HTTPException(status_code=400, detail='email or check_mail is empty')

def login_del(input_date:schema.User, db:session=Depends(get_db)):
    if input_date.email:
        result = crud.del_login(db, db,input_date)
        return {"reulst" : result}
    else:
        return HTTPException(status_code=400, detail='email is empty')

if __name__ == '__main__':
    import uvicorn
    import os
    uvicorn.run(app, host=os.getenv('HOST'), port=os.get_env('PORT'), debug=True)
    
    
