from .service import Service
from .task import task

class Order(object):
    pass


def post_save_me():
    task()
