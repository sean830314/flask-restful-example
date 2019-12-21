from db import db
import datetime
class ArticleModel(db.Model):
    __tablename__ = 'article'

    aid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    author = db.Column(db.String(40))
    content = db.Column(db.String(40))
    ip = db.Column(db.String(40))
    submission_date = db.Column(db.Date, default=datetime.datetime.now())

    def __init__(self, aid, title, author, content, ip, submission_date):
        self.aid = aid
        self.title = title
        self.author = author
        self.content = content
        self.ip = ip
        self.submission_date = submission_date

    def json(self):
        return {'aid': self.aid, 'title': self.title, 'author': self.author, 'content': self.content, 'ip': self.ip, 'submission_date': self.submission_date.strftime("%Y-%m-%d") }

    @classmethod
    def find_by_aid(cls,aid):
        return cls.query.filter_by(aid=aid).first()

    def save_to_db(self): #upserting
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()