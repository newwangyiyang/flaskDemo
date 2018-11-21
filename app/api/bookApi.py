from app.libs.httpJson import HTTP
from flask import current_app

class Api:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        res = HTTP.get(url)
        return res

    @classmethod
    def search_by_key(cls, q, page=1):
        url = cls.key_url.format(q, current_app.config['PER_PAGE'], cls.page_to_count(page))
        res = HTTP.get(url)
        return res

    @staticmethod
    def page_to_count(page):
        return (page - 1) * current_app.config['PER_PAGE']
