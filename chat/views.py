from django.shortcuts import render
from .models import Message

def chat_room(request):
    messages = Message.objects.all()
    return render(request, 'chat/chat_room.html', {'messages': messages})

