from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ecommerce.models import Customer, Product, OrderItem, ShippingAddress
from django.test.client import Client
from ecommerce import views

class TestLoginView(TestCase):

    def setUp(self):
        self.login_url = reverse('login')

    def test_request_store(self):
        response = self.client.get(self.login_rul)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce/login.html')

class TestLoginView(TestCase):

    def setUp(self):
        self.login_url = reverse('signup')

    def test_request_store(self):
        response = self.client.get(self.login_rul)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce/login.html')

class TestStoreView(TestCase):

    def setUp(self):
        self.client = Client()
        self.store_url = reverse('store')
        self.user = User.objects.create(username='django')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='django', password='12345')

    def test_request_store(self):
        response = self.client.get(self.store_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce/store.html')

class TestCartView(TestCase):

    def setUp(self):
        self.client = Client()
        self.cart_url = reverse('cart')
        self.user = User.objects.create(username='django')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='django', password='12345')

    def test_request_cart(self):
        response = self.client.get(self.cart_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce/cart.html')

class TestCheckoutView(TestCase):

    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse('checkout')
        self.user = User.objects.create(username='django')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='django', password='12345')

    def test_request_checkout(self):
        response = self.client.get(self.checkout_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce/checkout.html')

class TestCustomerActivityView(TestCase):

    def setUp(self):
        self.client = Client()
        self.past_activity_url = reverse('past_activity')
        self.user = User.objects.create(username='django')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='django', password='12345')

    def test_request_checkout(self):
        response = self.client.get(self.past_activity_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce/pastactivity.html')

class TestOrderHistoryView(TestCase):

    def setUp(self):
        self.client = Client()
        self.order_history_url = reverse('orderhistory')
        self.user = User.objects.create(username='django')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='django', password='12345')

    def test_request_checkout(self):
        response = self.client.get(self.order_history_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce/orderhistory.html')

class TestWishListView(TestCase):

    def setUp(self):
        self.client = Client()
        self.order_history_url = reverse('wish_items')
        self.user = User.objects.create(username='django')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='django', password='12345')

    def test_request_checkout(self):
        response = self.client.get(self.order_history_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecommerce/wishlist.html')

