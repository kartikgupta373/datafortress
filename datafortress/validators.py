from django.core.exceptions import ValidationError
import re

def validate_password_special_characters(value):
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError("The password must contain at least one special character.")

def validate_password_has_uppercase(value):
    if not any(char.isupper() for char in value):
        raise ValidationError("The password must contain at least one uppercase letter.")
    
def validate_password_mixed_case(value):
    if not any(char.islower() for char in value) or not any(char.isupper() for char in value):
        raise ValidationError("The password must contain both uppercase and lowercase characters.")
