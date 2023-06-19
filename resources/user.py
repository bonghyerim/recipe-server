from flask_restful import Resource
from flask import request
import mysql.connector
from mysql.connector import Error

from mysql_connection import get_connection

from email_validator import validate_email, EmailNotValidError

from utills import hash_password # 에러났을 때 처리해주는 거

class UserRegisterResource (Resource):
    def post(self) : 

        # {
        #     "username": "홍길동",
        #     "email": "abc@naver.com",
        #     "password": "1234"
        # }

        # 1. 클라이언트가 보낸 데이터를 받아준다.

        data = request.get_json()

        # 2. 이메일 주소 형식이 올바른지 확인한다.

        try :
            validate_email( data['email'])
        except EmailNotValidError as e :
            print (e)
            return {'result':'fail','error':str(e)}, 400
        
        # 3. 비밀번호 길이 유효한지 체크한다.
        # 만약, 비번이 4자리 이상 12자리 이하라고 한다면,
        
        if len( data['password'] ) < 4 or len( data ['password']) >12:
            return {'result':'fail', 'error' : '비번 길이 에러'},400
        
    
        # 4. 비밀번호를 암호화 한다.
        hashed_password = hash_password(data['password'])
        
        print('비번 암호화',str(hashed_password))

        # 5. DB에 이미 회원 정보가 있는지 확인한다.

        try :
            connection = get_connection()
            query = '''select * 
                    from user
                    where email = %s;'''
            record = ( data['email'],)
 
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, record)

            result_list = cursor.fetchall()

            print(result_list)
            
            if len(result_list) == 1 :
                return {'result': 'fail', 'error' : '이미 회원가입 한 사람'}, 400
            
            # 회원이 아니므로, 회원가입 코드를 작성한다.
            # DB에 저장한다.

            query = '''insert into user(username, email, password)
                        values (%s, %s, %s);'''
            
            record = (data['username'],
                      data['email'],
                      hashed_password)
            cursor = connection.cursor()
            cursor.execute(query, record)

            connection.commit()

            cursor.close()
            connection.close()

        except Error as e:
            print(e)
            return{'result': 'fail', 'error' : str(e)}, 500

        return {'result':'success'}

        

    