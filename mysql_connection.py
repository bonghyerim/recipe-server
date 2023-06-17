import mysql.connector
from config import Config

def get_connection() :
    connection = mysql.connector.connect(
        host='database-1.c56mxvfytstp.ap-northeast-2.rds.amazonaws.com', # 호스트는 사용자의 호스트 입력
        database='recipe', # 예시에 쓸 DB recipe
        user='recipe_db_user', # 관리 권한을 가진 'recipe_user1234'로 접속
        password='1234' )
    return connection