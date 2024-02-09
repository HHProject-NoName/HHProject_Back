from sqlalchemy.orm import Session 
import model, schema

def get_user(db:Session, email:str):
    return db.query(model.UserTable).filter(model.UserTable.email == email)

def get_all_user(db:Session):
    return db.query(model.UserTable)