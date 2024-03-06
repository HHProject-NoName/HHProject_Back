from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id:int
    email: str

class SaveLogin(BaseModel):
    id:int
    check_mail : str
    email: str
    token: Optional[str]  = None
    delete_yn:Optional[str] = None
    start_dt:str 
    end_dt:Optional[str] = None
    last_dt:str 