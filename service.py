from order import Order #Первый вариант

class Service(object):

    order_id = None

    def __init__(self, order_id, *args, **kwargs):
        super(Service, self).__init__(*args, **kwargs)
        self.order_id = order_id

    def call(self):
        # from order import Order #Второй враинт
        order = Order.objects.get(id=self.order_id)
