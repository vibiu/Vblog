from tornado import gen
from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Futrue


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


def asynchronous_fetch(url, callback):
    http_client = AsyncHTTPClient()

    def handle_response(response):
        callback(response.body)

    http_client.fetch(url, callback=handle_response)


def async_fetch_future(url):
    http_client = AsyncHTTPClient()
    my_future = Futrue()
    fetch_futrue = http_client.fetch(url)
    fetch_futrue.add_done_callback(
        lambda f: my_future.set_result(f.result())
    )
    return my_future


@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)


async def fetch_async_coroutine(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body
