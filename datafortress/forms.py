from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from .validators import *
from .models import Video, Notification

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    role = forms.ChoiceField(choices=[('editor', 'Editor'), ('creator', 'Creator')])
    username = forms.CharField(
        label=_("Username"),
        validators=[ASCIIUsernameValidator()],
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        validators=[validate_password_has_uppercase, validate_password_special_characters, validate_password_mixed_case],
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
        
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        try:
            validate_password(password1, self.instance)
        except ValidationError as e:
            self.add_error('password1', e.messages[0]) 

        return password1
    
    def clean_password2(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        return password2
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            try:
                ASCIIUsernameValidator()(username)
            except ValidationError as e:
                raise forms.ValidationError(str(e))
        return username
    
    

class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file', 'is_public']
        
        
class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['recipient', 'message', 'phone']

    def __init__(self, editor, *args, **kwargs):
        super(NotificationForm, self).__init__(*args, **kwargs)
        # Limit the recipient choices to users in the "creator" group
        self.fields['recipient'].queryset = User.objects.filter(groups__name='creator')