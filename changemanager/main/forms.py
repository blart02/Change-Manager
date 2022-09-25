
from django import forms
from .models import Service, Requestor, ChangeRequest, ChangeRequestUpdate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'business_unit', 'description',
                  'main_contact_number', 'parent_service']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ServiceForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(ServiceForm, self).clean()
        # checks to ensure the telephone number supplied has 11 characters
        if len(self.cleaned_data["main_contact_number"].replace(" ", "")) != 11:
            self._errors["main_contact_number"] = self.error_class(
                ["Please enter a valid UK phone number"])
        return self.cleaned_data


class RequestorForm(forms.ModelForm):
    class Meta:
        model = Requestor
        fields = ['first_name', 'last_name', 'is_approver',
                  'contact_number', 'service', 'line_manager']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RequestorForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(RequestorForm, self).clean()
        if len(self.cleaned_data["contact_number"].replace(" ", "")) > 11:
            self._errors["contact_number"] = self.error_class(
                ["Please enter a valid UK phone number"])
        return self.cleaned_data


class ChangeRequestForm(forms.ModelForm):
    class Meta:
        model = ChangeRequest
        fields = ['requestor', 'approver', 'priority', 'status',
                  'title', 'description', 'date_completed']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ChangeRequestForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(ChangeRequestForm, self).clean()

        # checks if the approver is authorised to approve requests
        if self.cleaned_data["approver"].is_approver == False:
            self._errors['approver'] = self.error_class(
                ["This requestor cannot approve requests"])

        return self.cleaned_data


class ChangeRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = ChangeRequestUpdate
        fields = ['text']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ChangeRequestUpdateForm, self).__init__(*args, **kwargs)


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
