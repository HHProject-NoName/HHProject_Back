from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

user_name = "hj"
user_pwd="hh"
db_host="localhost"
db_name="HH_base"

DATABASE='mysql://%s:%s@%s/%s?charset=utf8'%(
    user_name,
    user_pwd,
    db_host,
    db_name,
)

ENGINE = create_engine(
    DATABASE,
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()