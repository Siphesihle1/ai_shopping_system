
from django.test import TestCase
from django.contrib.auth.models import User
from ecommerce.models import Customer, Product, Order, OrderItem, ShippingAddress
from django.test.client import Client

class TestCustomerModel(TestCase):

    def setUp(self):
        
        # Sign up
        password = 'django12345'
        self.user = User.objects.create_user('django', 'django@test.com', password)
        self.user.customer.cellphone_no = '0793942414'
        self.user.save()

        # Login
        self.c = Client()
        self.c.login(username=self.user.username, password=password)
        
    def test_customer_model_entry(self):
        """
        Test Customer model data insertion/types/field attributes
        """
        
        self.assertTrue(isinstance(self.user.customer, Customer))
        self.assertEqual(str(self.user.customer), 'django')
        
class TestProductModel(TestCase):

    def setUp(self):
        # Sign up
        password = 'django12345'
        self.user = User.objects.create_user('django', 'django@test.com', password)
        self.user.customer.cellphone_no = '0793942414'
        self.user.save()

        # Login
        self.c = Client()
        self.c.login(username=self.user.username, password=password)

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
        self.assertEqual(products.count(), 2)
        
        
class TestOrderModel(TestCase):

    def setUp(self):
        # Sign up
        password = 'django12345'
        self.user = User.objects.create_user('django', 'django@test.com', password)
        self.user.customer.cellphone_no = '0793942414'
        self.user.save()

        # Login
        self.c = Client()
        self.c.login(username=self.user.username, password=password)

        self.order1 = Order.objects.create(self.user.customer, transaction_id='00001A', complete=True)
        self.order2 = Order.orders.create(self.usercustomer, transaction_id='00001B', complete=False)
        
    def test_get_cart_items(self):
        self.assertEqual(orderitems.get_cart_items, 0)

    def test_get_cart_total(self):
        self.assertEqual(orderitems.get_cart_total, 0.0)

    def test_order_model_entry(self):
        """
        Test order model data insertion/types/field attributes
        """
        self.assertTrue(isinstance(self.order1, Order))
        self.assertTrue(isinstance(self.order2, Order))
        
