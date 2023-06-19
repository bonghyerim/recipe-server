<<<<<<< HEAD
import mysql.connector
from config import Config

def get_connection() :
    connection = mysql.connector.connect(
        host='database-1.c56mxvfytstp.ap-northeast-2.rds.amazonaws.com', # 호스트는 사용자의 호스트 입력
        database='recipe', # 예시에 쓸 DB recipe
        user='recipe_db_user', # 관리 권한을 가진 'recipe_user1234'로 접속
        password='1234' )
=======
# 데이터베이스 연결 전용 파일
import mysql.connector
from config import Config

def get_connection() : 
    connection = mysql.connector.connect(
        host = Config.HOST, 
        database = Config.DATABASE, 
        user = Config.DB_USER,
        password = Config.DB_PASSWORD
    )
>>>>>>> f0ec4aba87431c4d3a20425dd4309e8857bea939
    return connection