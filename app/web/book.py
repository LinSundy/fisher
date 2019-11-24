from flask import jsonify, Blueprint

from helper import is_isbn_or_key
from yushu_book import YuShuBook

book = Blueprint('book', __name__)


@book.route('/book/search/<p>/<page>')
def index(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    elif isbn_or_key == 'key':
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
