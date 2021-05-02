from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Order, Customer

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class LoginForm(forms.Form):

    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class UserForm(ModelForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        # Validate username
        if User.objects.filter(username=username).exists():
            msg = "The username '{}' exists.".format(username)
            self.add_error('username', msg)
            raise forms.ValidationError(msg)

        # Validate password
        if password1 != password2:
            msg = "The passwords don't match."
            self.add_error('password1', msg)
            raise forms.ValidationError(msg)
    
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class CustomerForm(ModelForm):

    cellphone_no = forms.CharField(required=True, max_length=10)

    def clean(self):
        cellphone_no = self.cleaned_data.get('cellphone_no')

        for digit in cellphone_no:
            if not ( '0' <= digit <= '9'):
                msg = "The cellphone number is invalid."
                self.add_error('cellphone_no', msg)
                raise forms.ValidationError(msg)

        return self.cleaned_data
        
    class Meta:
        model = Customer
        fields = ('cellphone_no',)
