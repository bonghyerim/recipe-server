from flask import Flask
from flask_restful import Api
from resource.recipe import RecipeListResource, RecipeResource

app = Flask(__name__)

api = Api(app)

api.add_resource(RecipeListResource , '/recipes')
api.add_resource(RecipeResource,'/recipes/<int:recipe_id')

if __name__ = '__main__':
    app.run()