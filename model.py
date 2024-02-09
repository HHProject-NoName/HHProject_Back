from sqlalchemy import Boolean, Column, Integer, String 
from db import Base
from db import ENGINE
from sqlalchemy.orm import relationship

class UserTable(Base):
    __tablename__ = 'HH_Login_login'
    id=Column(Integer, primary_key=True, autoincrement=True)
    check_mail = Column(String(5), nullable=False)
    email = Column(String(50), unique=True)
    token = Column(String(50))
    delete_yn = Column(Boolean, default=False)
    start_dt = Column(String(8))
    end_dt = Column(String(8))
    last_dt = Column(String(8))
    
