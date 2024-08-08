from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    ingredients = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    carbohydrates = forms.IntegerField(required=False)
    fats = forms.IntegerField(required=False)
    proteins = forms.IntegerField(required=False)
