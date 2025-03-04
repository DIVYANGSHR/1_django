from django import forms

class MarvelForms (forms.Form):
    name = forms.CharField(label='first name ', required= False, initial='Spider')
    email = forms.EmailField(help_text='Enter your email', widget=forms.TextInput(attrs={'placeholder':'Enter your email'}))
    age = forms.IntegerField(max_value=5,disabled=True)
    password = forms.CharField(widget=forms.PasswordInput)
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control x'}))
    describe = forms.CharField(widget=forms.Textarea)