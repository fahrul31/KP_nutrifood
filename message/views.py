import imp
from django.shortcuts import redirect,render
from matplotlib.style import context

import message
from .models import Message

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic

# import class MessageForm dari file message/forms.py
from .forms import MessageForm
# Create your views here.
def index(request):
    message = Message.objects.all()
    context = {
        'messages' : message,
    }

    return render(request, 'message/index.html', context)
    
# Membuat View untuk halaman detail Message
def detail_view(request, id):
    # Mengambil data Message berdasarkan Message ID
    try:
        message = Message.objects.get(pk=id)
        context = {
            'message' : message,
        }
    except Message.DoesNotExist:
        # Jika data Message tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Message tidak ditemukan.")
    # parsing data Message ke template message/detail.html dan merendernya
    return render(request, 'message/detail.html', context)

# Membuat View untuk halaman form tambah Message
def create_view(request):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        # membuat objek dari class MessageForm
        form = MessageForm(request.POST)
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Message baru dengan data yang disubmit
            new_message = MessageForm(request.POST)
            # Simpan data ke dalam table Messages
            new_message.save()
            # mengeset pesan sukses dan redirect ke halaman daftar Message
            return redirect('message:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class MessageForm
        form = MessageForm()
    # merender template form dengan memparsing data form
    return render(request, 'message/create.html', {'form': form})

# Membuat View untuk halaman form ubah Message
def update_view(request, id):
    try:
        # mengambil data Message yang akan diubah berdasarkan Message id
        message = Message.objects.get(pk=id)
    except Message.DoesNotExist:
        # Jika data Message tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Message tidak ditemukan.")
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            # Simpan perubahan data ke dalam table Messages
            form.save()
            # mengeset pesan sukses dan redirect ke halaman daftar Message
            return redirect('message:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class MessageForm
        form = MessageForm(instance=message)
    # merender template form dengan memparsing data form
    return render(request, 'message/create.html', {'form': form})

# Membuat View untuk menghapus data Message
def delete_view(request,id):
    try:
        # mengambil data Message yang akan dihapus berdasarkan Message id
        message = Message.objects.get(pk=id)
        # menghapus data dari table Messages
        message.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar Message
        return redirect('message:index')
    except Message.DoesNotExist:
        # Jika data Message tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Message tidak ditemukan.")