from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from . models import User


class CustomUserCreateForms(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        error_class = 'error'
        
class  CustomUserChangeForms(UserChangeForm):
    class Meta:
        model = "User"
        fields = ['username', 'first_name', 'last_name', 'email']
        error_class = 'error'
        