from flask import Flask
from flask_restful import Api
from resources.user import UserRegister
from resources.article import Article, ArticleList
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@127.0.0.1:3306/flask_demo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

api = Api(app)
api.add_resource(UserRegister, '/register')
api.add_resource(Article, '/article/<string:aid>')
api.add_resource(ArticleList, '/articles')
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5001, debug=True)