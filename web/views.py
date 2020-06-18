from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Message
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#留言列表
class MessageList(ListView):
    model = Message

class MessageDetail(DetailView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    fields = ['user','subject','content']
    success_url = reverse_lazy('msglist')

class MessageDelete(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')   