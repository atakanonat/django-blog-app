from django import forms


class RegisterForm(forms.Form):

    first_name = forms.CharField(max_length=50, label="Your Name")
    username = forms.CharField(max_length=50, label="Username")
    email = forms.EmailField(max_length=50, label="Your Email")
    password = forms.CharField(
        max_length=20, label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Repeat your password")

    # Implement a clean() method on your Form when you must add custom validation for fields that are interdependent.
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        email = self.cleaned_data.get("email")
        first_name = self.cleaned_data.get("first_name")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords doesn't match.")

        values = {
            "username": username,
            "password": password,
            "first_name": first_name,
            "email": email,
        }

        return values


class LoginForm(forms.Form):

    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(
        max_length=20, label="Password", widget=forms.PasswordInput)