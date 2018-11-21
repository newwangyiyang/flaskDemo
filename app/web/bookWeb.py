"""
    book的视图函数(controller层)
"""
from flask import jsonify, request
from app.api.bookApi import Api
from app.libs.helpers import is_isbn_or_key
from . import web
from app.form.bookForm import SearchForm

# 注册蓝图


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            res = Api.search_by_isbn(q)
        if isbn_or_key == 'key':
            res = Api.search_by_key(q, page)
        return jsonify(res)
    else:
        return jsonify(form.errors)
