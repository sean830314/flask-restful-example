from models.article import ArticleModel
from faker import Factory
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@127.0.0.1:3306/flask_demo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


def gen_data():
    fake = Factory.create()
    db = SQLAlchemy(app)
    for num in range(0, 8):
        fullname = fake.name()
        address = fake.address()
        city = fake.city()
        mi_contacto = ArticleModel(0, city, fullname,  address, '127.0.0.{}'.format(num), datetime.datetime.now())
        try:
            db.session.add(mi_contacto)
            db.session.commit()
        except Exception as err:
            print("error:{}".format(err))


if __name__ == "__main__":
    gen_data()