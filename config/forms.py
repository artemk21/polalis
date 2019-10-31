from django import forms
from django.contrib.auth.models import User
from insights.models import UserProfile

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CustomLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'color: black;',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'color: black;',
        })
    )

# touched on 2025-05-27T15:28:51.111952Z
# touched on 2025-05-27T15:28:53.860787Z
# touched on 2025-05-27T15:28:59.284261Z
# touched on 2025-07-09T21:55:29.630391Z
# touched on 2025-07-09T21:55:36.406464Z
# touched on 2025-07-09T21:55:41.754846Z
# touched on 2025-07-09T21:56:05.105869Z
# touched on 2025-07-09T21:56:07.670441Z
# touched on 2025-07-09T21:56:10.104327Z
# touched on 2025-07-09T21:56:28.479833Z
# touched on 2025-07-09T21:56:47.021374Z
# touched on 2025-07-09T21:56:51.818413Z
# touched on 2025-07-09T21:57:14.842168Z