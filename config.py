class Config :
    HOST = ''
    DATABASE = 'recipe'
    DB_USER = 'recipe_db_user'
    DB_PASSWORD = '1234'

    SALT = '12312312'

    JWT_SECRET_KEY = 'hello~!by@'
    JWT_ACCESS_TOKEN_EXPIRES = False # 토큰의 만료 시간
    PROPAGATE_EXCEPTIONS = True # 명시적으로 예외를 전파하는 것에 대한 활성화