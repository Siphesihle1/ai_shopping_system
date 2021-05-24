
from django.test import TestCase
from django.contrib.auth.models import User
from ecommerce.models import Customer, Product, Order, OrderItem, ShippingAddress
from django.test.client import Client

class TestCustomerModel(TestCase):

    def setUp(self):
        password = 'django12345'
        self.user = User.objects.create_user('django', 'django@test.com', password)
        self.c = Client()
        self.c.login(username=self.user.username, password=password)
        self.customer = Customer.objects.create(user=self.user,cellphone_no='0793942414')

    def test_customer_model_entry(self):
        """
        Test Customer model data insertion/types/field attributes
        """
        
        self.assertTrue(isinstance(self.customer, Customer))
        self.assertEqual(str(self.customer), 'django')
        
class TestProductModel(TestCase):

    def setUp(self):
        password = 'django12345'
        self.user = User.objects.create_user('django', 'django@test.com', password)
        self.c = Client()
        self.c.login(username=self.user.username, password=password)
        self.customer = Customer.objects.create(user=self.user,cellphone_no='0793942414')

        self.product1 = Product.objects.create(price='20.00', 
            name='product1', digital=True, image='image_path1', 
            description='TBD')

        self.product2 = Product.products.create(price='10.00',
            name='product2',digital=False, image='image_path2',
            description='TBD')
        
    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        
        self.assertTrue(isinstance(product1, Product))
        self.assertTrue(isinstance(product2, Product))
        self.assertEqual(str(product1), 'product1')
        self.assertEqual(str(product2), 'product2')
        
    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        products = Product.products.all()
        self.assertEqual(len(products), 2)
        
        
class TestOrderModel(TestCase):

    def setUp(self):
        password = 'django12345'
        self.user = User.objects.create_user('django', 'django@test.com', password)
        self.c = Client()
        self.c.login(username=self.user.username, password=password)
        self.customer = Customer.objects.create(user=self.user,cellphone_no='0793942414')

        self.order1 = Order.objects.create(customer, transaction_id='00001A', complete=True)
        self.order2 = Order.orders.create(customer, transaction_id='00001B', complete=False)
        
    def test_get_cart_total(self):
        orderitems=self.orderitem_set.all()
        self.assertEqual(len(orderitems), 0)
        
    def test_order_model_entry(self):
        """
        Test order model data insertion/types/field attributes
        """
        self.assertTrue(isinstance(self.order1,Order))
        self.assertTrue(isinstance(self.order2,Order))
        
