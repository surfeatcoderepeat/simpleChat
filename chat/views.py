from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username':username,
        'room': room,
        'room_details':room_details 
        })

def checkview(request):
    room = request.POST['roomName']
    username = request.POST['name']
    
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    room_id = request.POST['room_id']
    username = request.POST['username']
    message = request.POST['message']

    new_message = Message.objects.create(name=username, value=message, room=room_id)
    new_message.save()
    return HttpResponse('message sent succesfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({'messages':list(messages.values())[-8:]})    