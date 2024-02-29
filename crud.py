from sqlalchemy.orm import Session 
import model, schema


###########################################################################################
# 검색
###########################################################################################

#임시 전체 검색
def get_all_user(db:Session):
    return db.query(model.UserTable)

# 메일 검색
def get_mail_search(db:Session, email:str):
    return db.query(model.UserTable).filter(model.UserTable.email == email)




