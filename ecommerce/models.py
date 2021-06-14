from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

User._meta.get_field('username')._unique = True

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cellphone_no = models.CharField(max_length=10, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    
    @receiver(post_save, sender=User)
    def update_user_customer(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)
        instance.customer.save()
    
    def __str__(self):
        return self.user.username



class Product(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=255, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False)
    class Meta:
        db_table = "ecommerce_order"


    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping=False
        orderitems = self.orderitem_set.all()

        for i in orderitems:
            if i.product.digital == False:
                shipping=True
        return shipping

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address=models.CharField(max_length=200, null=False)
    city=models.CharField(max_length=200, null=False)
    state=models.CharField(max_length=200, null=False)
    zipcode=models.CharField(max_length=200, null=False)
    date_added=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.address

class CustomerActivity(models.Model):
    ADD = "A"
    VIEW = "V"
    WISH = "W"
    ACTIONS = [(ADD, "add"), (VIEW, "view"), (WISH, "wish"),]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Customer activities'

    action = models.CharField(
        max_length=1,
        choices=ACTIONS,
        default=ADD,
    )

    event_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    
class PurchaseHistory(models.Model):

    user = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True, null=True)
    order = models.CharField(max_length=10,null=True)
    date = models.DateTimeField(auto_now_add=True)
    state= models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=True)
    total = models.IntegerField(default=0,null=True,blank=True)
    product = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    
 

