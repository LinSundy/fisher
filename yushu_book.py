from axios import Axios
from flask import current_app


class YuShuBook:
    isbn_url = 'HTTP://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'HTTP://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    @classmethod
    def search_by_isbn(cls, keywords):
        url = cls.isbn_url.format(keywords)
        r = Axios.get(url)
        return r

    @classmethod
    def search_by_keyword(cls, keywords, page):
        url = cls.keyword_url.format(keywords, cls.calc_page(page), current_app.config['PER_PAGE'])
        r = Axios.get(url)
        return r

    @classmethod
    def calc_page(cls, page):
        return (page - 1) * current_app.config['PER_PAGE']
