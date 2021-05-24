
from django.test import TestCase
from store.models import Customer, Product, Order, OrderItem, ShippingAddress

class TestCustomersModel(TestCase):

    def setUp(self):
        self.data1 = Customer.objects.create(user='django',cellphone_no='0793942414',latitude='django10.10', longitude='django11.11')

    def test_customer_model_entry(self):
        """
        Test Customer model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Customer))
        self.assertEqual(str(data), 'django')
        
class TestProductsModel(TestCase):

    def setUp(self):
    
        Customer.objects.create(user='django',cellphone_no='0793942414',latitude='django10.10', longitude='django11.11')
        self.data1 = Product.objects.create(price='20.00', name='django', digital=True, image='django', description='a django product')
        self.data2 = Product.products.create(price='10.00',name='django1',digital=False, image='django1', description='a django1 project')
        
    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django')
        
    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        data = Product.products.all()
        self.assertEqual(data.count(), 2)
        
        
class TestOrderModel(TestCase):

    def setUp(self):
        customer = Customer.objects.create(user='django',cellphone_no='0793942414',latitude='django10.10', longitude='django11.11')
        self.data1 = Order.objects.create(customer, transaction_id='00001A', date_ordered='2020-01-01', complete=True)
        self.data2 = Order.orders.create(customer, transaction_id='00001B', date_ordered='2020-02-01', complete=False)
    #def test_shipping(self):
        
       # data = self.data1
       # self.assertEqual(data.digital, 2)
        
    def test_get_cart_total(self):
        
        orderitems=self.orderitem_set.all()
        self.assertEqual(orderitems.count(), 2)
        
    def test_order_model_entry(self):
        """
        Test order model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data,Order))
        self.assertEqual(str(data), 'django')
        
class TestOrderItem(TestCase):
    def setUp(self):
        self.prod1 = Product.products.create(price='10.00',name='django1',digital=False, image='django1', description='a django1 project')
        self.data1 = Order.objects.create(customer, transaction_id='00001A', date_ordered='2020-01-01', complete=True)
        self.data2 = Order.orders.create(customer, transaction_id='00001B', date_ordered='2020-02-01', complete=False)
        self.orderitem1 = OrderItem.objects.create(prod1,data1,quantity='1',date_added='2021-02-02')
        
    def test_get_total(self):
        orderitems = self.orderitem1
        self.assertEqual(orderitems.get_total(), orderitems.product.price*orderitems.quantity)
    

