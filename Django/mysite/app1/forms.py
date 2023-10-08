from django import forms
from app1.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('contact_name', 'contact_mailaddress','contact_subject','contact_message')
        labels = {
            'contact_name':'名前',
            'contact_mailaddress':'メールアドレス',
            'contact_subject':'インスタグラムのユーザー名',
            'contact_message':'貸出可能な備品（あればでいい）',

        }
        