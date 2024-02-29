from fastapi import FastAPI, HTTPException 
import aiosmtplib
import main
import asyncio
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os


app = FastAPI()

###########################################################################################
# 메일 인증
###########################################################################################



email_host = os.getenv('MAIL_SERVER')
email_port = os.getenv('MAIL_PORT') #SSL/TLS 암호화사용시 465, TLS암호화사용시 587, 암호화 X 25
email_username = os.getenv('MAIL_USERNAME')
email_password = os.getenv('MAIL_PASSWORD') #?? 띄워쓰기해야하나?
MAIL_USE_TSL = os.getenv('MAIL_USE_TSL')
MAIL_USE_SSL = os.getenv('MAIL_USE_SSL')   

#메일 설정 초기화
mail_config = {
    "MAIL_USERNAME": email_username,
    "MAIL_PASSWORD": email_password,
    "MAIL_SERVER" : email_host,
    "MAIL_PORT" : email_port
}

#사용자에게 인증 코드 전송
async def send_verification_email(email, body):
    message = MIMEMultipart()
    message["From"] = email_username
    message["To"] = email
    message["Subject"] = "Hi! check your code."
    message.attach(MIMEText(body, "plain"))
    print(message)
    try:
        with smtplib.SMTP(mail_config["MAIL_SERVER"],  mail_config["MAIL_PORT"]) as server:
            server.starttls()
            server.login(email_username, email_password)
            server.sendmail(message["From"], message["To"], message.as_string())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"fastemail fail={str(e)}")
    
    
import random
import string
#무작위 6자리 인증코드 생성
def generate_random_code():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))