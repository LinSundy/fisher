from axios import Axios


class YuShuBook:
    isbn_url = 'HTTP://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'HTTP://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    @classmethod
    def search_by_isbn(cls, q):
        url = cls.isbn_url.format(q)
        r = Axios.get(url)
        return r

    @classmethod
    def search_by_keyword(cls, q, start=1, count=10):
        url = cls.keyword_url.format(q, start, count)
        r = Axios.get(url)
        return r
