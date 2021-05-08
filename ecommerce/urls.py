from django.urls import path
from . import views
from . import apps

#app_name="ecommerce"
urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
 	path('cart/', views.cart, name="cart"),
 	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"), 
	#path('deletefromcart/', views.deletefromcart, name="deletefromcart"),


]
