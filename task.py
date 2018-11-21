from .order import Order
from .service import Service

def celery_task(order_id):
    service = Service(order_id)
