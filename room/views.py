from django.shortcuts import render
from .models import Room, Message

# Create your views here.
def rooms(request):
    rooms=Room.objects.all()
    return render(request, 'room/rooms.html',{'rooms':rooms})

def room(request, slug):
    room=Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room':room, 'messages':messages})