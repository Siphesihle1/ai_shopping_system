
from django.test import TestCase
from django.contrib.auth.models import User
from ecommerce.models import Customer, Product, Order, OrderItem, ShippingAddress, CustomerActivity, PurchaseHistory
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
    
    def test_username(self):
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

        self.product1 = Product.objects.create(price=20.0, 
            name='product1', digital=True, image='image_path1', 
            description='TBD')

        self.product2 = Product.objects.create(price=10.0,
            name='product2',digital=False, image='image_path2',
            description='TBD')
        
    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        self.assertTrue(isinstance(self.product1, Product))
        self.assertTrue(isinstance(self.product2, Product))
        
    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        products = Product.objects.all()
        self.assertEqual(products.count(), 2)

    def test_product_name(self):    
        self.assertEqual(str(self.product1), 'product1')
        self.assertEqual(str(self.product2), 'product2')
        
        
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

        self.order1 = Order.objects.create(customer=self.user.customer, transaction_id='00001A', complete=True)
        self.order2 = Order.objects.create(customer=self.user.customer, transaction_id='00001B', complete=False)
        
    def test_get_cart_items(self):
        self.assertEqual(self.order1.get_cart_items, 0)
        self.assertEqual(self.order2.get_cart_items, 0)

    def test_get_cart_total(self):
        self.assertEqual(self.order1.get_cart_total, 0.0)
        self.assertEqual(self.order2.get_cart_total, 0.0)

    def test_shipping(self):
        self.assertEqual(self.order1.shipping, False)
        self.assertEqual(self.order2.shipping, False)

    def test_id(self):
        self.assertEqual(str(self.order1.id), str(self.order1))
        self.assertEqual(str(self.order2.id), str(self.order2))
    
    def test_order_model_entry(self):
        """
        Test order model data insertion/types/field attributes
        """
        self.assertTrue(isinstance(self.order1, Order))
        self.assertTrue(isinstance(self.order2, Order))

class TestOrderItemModel(TestCase):
    def setUp(self):
        # Sign up
        password = 'django12345'
        self.user = User.objects.create_user('django', 'django@test.com', password)
        self.user.customer.cellphone_no = '0793942414'
        self.user.save()

        # Login
        self.c = Client()
        self.c.login(username=self.user.username, password=password)

        # Order Creation
        self.order = Order.objects.create(customer=self.user.customer, transaction_id='00001A', complete=True)
        
        # Products
        self.product1 = Product.objects.create(price=20.0, 
            name='product1', digital=True, image='image_path1', 
            description='TBD')

        self.product2 = Product.objects.create(price=10.0,
            name='product2', digital=False, image='image_path2',
            description='TBD')

        # Order items
        self.order_item1 = OrderItem.objects.create(product=self.product1, order=self.order,
            quantity=1)
        self.order_item2 = OrderItem.objects.create(product=self.product2, order=self.order,
            quantity=1)
        
    def test_get_total(self):
        self.assertEqual(self.order_item1.get_total, 20.0)
        self.assertEqual(self.order_item2.get_total, 10.0)
    
    def test_orderitem_model_entry(self):
        self.assertTrue(isinstance(self.order_item1, OrderItem))
        self.assertTrue(isinstance(self.order_item2, OrderItem))

class TestShippingAddressModel(TestCase):
    def setUp(self):
        # Sign up
        password = 'django12345'
        self.user = User.objects.create_user('django', 'django@test.com', password)
        self.user.customer.cellphone_no = '0793942414'
        self.user.save()

        # Login
        self.c = Client()
        self.c.login(username=self.user.username, password=password)

        # Order Creation
        self.order = Order.objects.create(customer=self.user.customer, transaction_id='00001A', complete=True)
        
        # Shipping Address
        self.shipping_adddress = ShippingAddress.objects.create(customer=self.user.customer,
            order=self.order, address='', city='', state='', zipcode='')
        
    def test_address(self):
        self.assertEqual(str(self.shipping_adddress), '')
    
    def test_shipping_address_entry(self):
        self.assertTrue(isinstance(self.shipping_adddress, ShippingAddress))

class TestCustomerActivityModel(TestCase):
    def setUp(self):
        # Sign up
        password = 'django12345'
        self.user = User.objects.create_user('django', 'django@test.com', password)
        self.user.customer.cellphone_no = '0793942414'
        self.user.save()

        # Login
        self.c = Client()
        self.c.login(username=self.user.username, password=password)

        # Product creation
        self.product = Product.objects.create(price=20.0, 
            name='product', digital=True, image='image_path', 
            description='TBD')

        # Customer Activity
        self.customer_activity = CustomerActivity.objects.create(customer=self.user.customer,
            product=self.product, action=CustomerActivity.VIEW)
        
        
    def test_product_name(self):
        self.assertEqual(str(self.customer_activity), 'product')
    

    def test_customer_activity_entry(self):
        self.assertTrue(isinstance(self.customer_activity, CustomerActivity))

class TestPurchaseHistoryModel(TestCase):
    def setUp(self):
        # Sign up
        password = 'django12345'
        self.user = User.objects.create_user('django', 'django@test.com', password)
        self.user.customer.cellphone_no = '0793942414'
        self.user.save()

        # Login
        self.c = Client()
        self.c.login(username=self.user.username, password=password)

        # Order Creation
        self.order = Order.objects.create(customer=self.user.customer, transaction_id='00001A', complete=True)
        
        # Shipping Address
        self.shipping_adddress = ShippingAddress.objects.create(customer=self.user.customer,
            order=self.order, address='', city='', state='', zipcode='')
        
        # Purchase history
        self.purchase_history = PurchaseHistory.objects.create(username=self.user.customer,
            order=self.order, state=self.shipping_adddress)

    def test_purchase_history_entry(self):
        self.assertTrue(isinstance(self.purchase_history, PurchaseHistory))
