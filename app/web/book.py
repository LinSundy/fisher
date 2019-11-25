from flask import jsonify, request
from werkzeug.datastructures import ImmutableMultiDict

from app.forms.book import SearchBook

from app.web import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search/<q>/<page>')
def search_book(q, page):
    d = {
        "q": q,
        "page": page
    }
    d1 = ImmutableMultiDict(d)
    form = SearchBook(d1)
    q = form.q.data
    page = form.page.data
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    elif isbn_or_key == 'key':
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)


@web.route('/')
def home():
    return 'book home'
