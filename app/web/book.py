from flask import jsonify, request
from werkzeug.datastructures import ImmutableMultiDict

from app.forms.book import SearchBook

from app.web import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search')
def search_book():
    d = {
        "q": request.args['q'],
        "page": request.args['page']
    }
    d1 = ImmutableMultiDict(d)
    form = SearchBook(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q, page)
        elif isbn_or_key == 'key':
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)


@web.route('/')
def home():
    return 'book home'
