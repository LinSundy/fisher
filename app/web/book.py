from flask import jsonify, Blueprint

from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search/<p>/<page>')
def search_book(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    elif isbn_or_key == 'key':
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)


@web.route('/')
def home():
    return 'book home'
