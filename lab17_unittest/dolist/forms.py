from django import forms

class Todolisform(forms.Form):
    text = forms.CharField(max_length=45, widget=forms.TextInput(
        attrs={
            'class': 'text-todo',
            'placeholder': 'Enter to do...',
            'aria-label': 'Todo',
            'aria-describedby': 'add-btn'
        }
    ))