from django import forms

from userform.models import UserForm


class UserFormForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = ['name', 'date_of_birth', 'email', 'phone_number']
        widgets = {
            'date_of_birth' : forms.DateInput(attrs={'type':'date'})
        }
