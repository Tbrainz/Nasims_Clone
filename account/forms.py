from django import forms

class Registrationform(forms.Form):
    first_name = forms.CharField()
    middle_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.IntegerField()
    DoB = forms.DateField()
    gender = forms.CharField(widget=forms.Select(
        choices=(
        ('MALE', 'MALE'), ('FEMAIL', 'FEMALE')
        )
    ))