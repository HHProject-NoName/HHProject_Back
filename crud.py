from sqlalchemy.orm import Session 
import model, schema
from typing import Optional


###########################################################################################
# 검색
###########################################################################################

#임시 전체 검색
def get_all_user(db:Session):
    return db.query(model.UserTable)

# 메일 검색
def get_mail_search(db:Session, email:str):
    return db.query(model.UserTable).filter(model.UserTable.email == email)

###########################################################################################
# 로그인 저장, 삭제
###########################################################################################

#로그인 저장
def save_login(db:Session, itemdict:schema.SaveLogin):
    input_data = model.UserTable(**itemdict.dict())
    print("??:", input_data)
    db.add(input_data)
    
    db.commit()
    # db.refresh()
    return "성공?"


