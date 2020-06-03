from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'input-email', 'id': 'email', 'placeholder': 'Email'}),
        required=True
    )