# app.py

from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource

# API 서버를 구축하기 위한 기본 구조
app = Flask(__name__)

# restfulAPI 생성
api = Api(app)

# 경로와 리소스(api코드) 연결
api.add_resource(RecipeListResource, '/recipes')

if __name__ == '__main__' :
    app.run()