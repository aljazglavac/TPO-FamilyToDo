from django import forms
from .enums import Importance

''' error messages dict '''
err_msg = {
    'required': 'This field is required',
    'invalid': 'Invalid field',
    'max_value': 'Please enter numeric password that is four digits long.',
    'min_value': 'Please enter numeric password that is four digits long.',
}

''' Family registration form '''
class FamilyRegistrationForm(forms.Form):
    ''' Family name and passwords '''
    family_name = forms.CharField(label="Family name", max_length=30, strip=True)
    family_password = forms.CharField(label="Full password", max_length=30, widget=forms.PasswordInput)
    family_easy_password = forms.IntegerField(label="Easy password", min_value=0000, max_value=9999, widget=forms.PasswordInput, error_messages=err_msg)
    
    ''' Family parents '''
    father_name = forms.CharField(label="Father name", max_length=30, strip=True)
    mother_name = forms.CharField(label="Mother name", max_length=30, strip=True)

''' Family login form '''
class FamilyLoginForm(forms.Form):
    family_name = forms.CharField(label="Family name", max_length=30, strip=True)
    family_parent = forms.CharField(label="Parent name", max_length=30, strip=True)
    family_password = forms.CharField(label="Family password", max_length=30, widget=forms.PasswordInput)

''' Child login form '''
class ChildLoginForm(forms.Form):
    family_name = forms.CharField(label="Family name", max_length=30, strip=True)
    family_easy_password = forms.IntegerField(label="Family password", min_value=0000, max_value=9999, widget=forms.PasswordInput, error_messages=err_msg)

''' Task adding form '''
class TaskAddForm(forms.Form):
    task_name = forms.CharField(label="Task name", max_length=30, strip=True)
    task_importance = forms.ChoiceField(label="Task importance", choices=[(tag, tag.value) for tag in Importance]) 
    task_reward = forms.CharField(label="Task reward", max_length=30, strip=True)
    task_due = forms.IntegerField(label="Taks due days", min_value=0, error_messages=err_msg)
    ''' child choice will be added from views and passed to the html from and than back 
    if i find better solution will add it later '''

