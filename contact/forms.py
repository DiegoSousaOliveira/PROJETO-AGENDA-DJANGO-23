from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
  first_name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'class-a class-b',
        'placeholder': 'Aqui veio do init',
      }
    ),
    label='Primeiro Nome',
    help_text='Texto de ajuda para seu usuário'
  )

  qualquer = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'class-a class-b',
        'placeholder': 'Aqui veio do init',
      }
    ),
    help_text='Texto de ajuda para seu usuário'
  )
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
  class Meta:
    model = Contact
    fields = (
      'first_name', 'last_name', 'phone',
      )
  
  def clean(self):
    #cleaned_data = self.cleaned_data

    self.add_error(
      'first_name',
      ValidationError(
        'Mensagem de erro',
        code='invalid'
      )
    )

    return super().clean()
