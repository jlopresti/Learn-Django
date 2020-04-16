from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class AdminUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username','is_secretary', 'is_inspector', 'is_student')


class AdminUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username','is_secretary', 'is_inspector', 'is_student')

class SecretaryUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'is_inspector', 'is_student')


class SecretaryUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'is_inspector', 'is_student')

