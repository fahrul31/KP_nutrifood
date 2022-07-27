from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Message dari file todo/models.py
from .models import Message


# membuat class MessageForm untuk membuat Message
class MessageForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Message
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('name', 'nim', 'messages')
        # mengatur teks label untuk setiap field
        labels = {
            'name': _('Nama'),
            'nim': _('NIM'),
            'messages': _('messages')
        }
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'name': {
                'required': _("Nama harus diisi."),
            },
            'nim': {
                'required': _("NIM harus diisi."),
            },
        }