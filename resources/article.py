# import sqlite3
from flask_restful import Resource, reqparse
from models.article import ArticleModel
import datetime
"""
article_list = [{
    "aid": 1,
    "title": "title1",
    "author": "kroos.chen",
    "date": "2019-12-20 11:29:00",
    "content": "test content",
    "ip": "127.0.0.1",
}, {
    "aid": 2,
    "title": "title2",
    "author": "jimmy.chen",
    "date": "2019-12-20 10:29:00",
    "content": "test content2",
    "ip": "8.8.8.8",
}, {
    "aid": 3,
    "title": "title3",
    "author": "tome.chen",
    "date": "2019-12-20 08:29:00",
    "content": "test content3",
    "ip": "7.7.7.7",
}]
"""


class ArticleList(Resource):

    def get(self):
        return {'articles': [article.json() for article in ArticleModel.query.all()]}
        #return {'message': article_list}, 201


class Article(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help='This field title is required.', location='form')
    parser.add_argument('author', type=str, required=True, help='This field author is required.', location='form')
    #parser.add_argument('date', type=str, required=True, help='This field date is required.', location='form')
    parser.add_argument('content', type=str, required=True, help='This field content is required.', location='form')
    parser.add_argument('ip', type=str, required=True, help='This field ip is required.', location='form')

    def get(self, aid):
        article = ArticleModel.find_by_aid(aid)
        if article:
            return article.json()
        return {'message': 'Article not found.'}, 404
        """
        for article in article_list:
            if article['aid'] == aid:
                return {'message': article}, 201
        return {'message': 'the aid:{} is empty data'.format(aid)}, 201
        """
    def post(self, aid):
        if ArticleModel.find_by_aid(aid):
            return {'message': "An article with aid '{}' alread exists.".format(aid)}, 400

        data = Article.parser.parse_args()

        article = ArticleModel(aid, data['title'], data['author'], data['content'], data['ip'], datetime.datetime.now())
        try:
            article.save_to_db()
        except:
            return {'message': 'An error occurred when inserting the article.'}, 500
        return article.json(), 201
        """
        for article in article_list:
            if article['aid'] == aid:
                return {'message': 'the aid:{} is alread exists'.format(aid)}, 201
        data = Article.parser.parse_args()
        article_list.append({
            "aid": aid,
            "title": data['title'],
            "author": data['author'],
            "date": data['date'],
            "content": data['content'],
            "ip": data['ip'],
        })
        return {'message': 'Article created successfully.'}, 201
        """

    def put(self, aid):
        data = Article.parser.parse_args()
        article = ArticleModel.find_by_aid(aid)

        if article is None:
            article = ArticleModel(aid, data['title'], data['author'], data['content'], data['ip'], datetime.datetime.now())
        else:
            article.aid = aid
            article.title = data['title']
            article.author = data['author']
            article.content = data['content']
            article.ip = data['ip']
            article.submission_date = datetime.datetime.now()

        article.save_to_db()

        return article.json()
        """
        for article in article_list:
            if article['aid'] == aid:
                article["title"] = data['title']
                article["author"] = data['author']
                article["date"] = data['date']
                article["content"] = data['content']
                article["ip"] = data['ip']
                return {'message': 'Article created successfully. {}'.format(article)}, 201
        return {'message':  'the aid:{} is empty data'.format(aid)}, 401
        """
    def delete(self, aid):
        article = ArticleModel.find_by_aid(aid)
        if article:
            article.delete_from_db()
        return {'message' : 'article deleted'}
        """
        for index, article in enumerate(article_list):
            if article['aid'] == aid:
                article_list.pop(index)
                return {'message': 'Article delete successfully.'}, 201
        return {'message': 'the aid:{} is empty data'.format(aid)}, 201
        """