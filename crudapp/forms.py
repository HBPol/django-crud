from Django import forms
from cProfile import label

class MyTestModelForm(forms.Form):
    my_char = forms.CharField(label='My char field', max_length=50)