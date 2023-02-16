from django import forms
from django.core.exceptions import ValidationError
from .models import Member

DATE_INPUT_FORMATS = ('%Y-%m-%d', '%d/%m/%Y')

def only_digits(value): 
  if value.isdigit()==False:
      raise ValidationError('The field must only contain numbers.')

class DateInput(forms.DateInput):
    input_type = 'date'

class MemberForm(forms.ModelForm):
  class Meta:
    model = Member
    fields = "__all__"
  ddd_phone = forms.CharField(validators=[only_digits], label="DDD")
  phone = forms.CharField(validators=[only_digits], label="Phone Number")
  joined_date = forms.DateField(label="Member since", input_formats=DATE_INPUT_FORMATS)