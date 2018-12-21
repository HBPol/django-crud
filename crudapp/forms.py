from django import forms

class MyTestModelForm_01(forms.Form):
    my_char = forms.CharField(label='My char field', max_length=50)
    my_date = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget)
    my_datetime = forms.DateTimeField(label='Date and time')
    my_integer = forms.IntegerField(label='Integer')
    my_boolean = forms.BooleanField(label='A boolean field')
    my_email = forms.EmailField(label='E-mail', max_length=254)
    my_text = forms.CharField(label='Text', max_length=500, widget=forms.Textarea)
    my_time = forms.TimeField(label='Time')
    
# Creating forms from models
from django.forms import ModelForm
from crudapp.models import MyTestModel
    # The form class
class MyTestModelForm_02(ModelForm):
    class Meta:
        model = MyTestModel
        fields = ['my_char', 'my_date', 'my_email', 'my_datetime', 'my_boolean', 'my_integer', 'my_text', 'my_time']