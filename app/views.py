from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import UserForm, RoomForm
from .models import Coder, Room, Chat
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    userform = UserForm()

    if request.method == 'POST':
        userform = UserForm(request.POST)

        if userform.is_valid():
            coder = Coder()
            user = userform.save()
            user.set_password(user.password)
            coder.user = user
            coder.save()

            return redirect(reverse('app:login_coder'))
        
    return render(request,'app/signup.html',{'userform':userform})

def login_coder(request):
    if request.method == 'POST':
        user = authenticate(request, username = request.POST.get('username'), password= request.POST.get('password'))
        if user:
            login(request,user)
            return redirect(reverse('app:index'))
        
    return render(request,'app/login.html')


@login_required
def logout_coder(request):
    logout(request)
    return redirect(reverse('app:login_coder'))

@login_required
def index(request):
    rooms = Room.objects.all()
    roomform = RoomForm()

    if request.method == 'POST':
        roomform = RoomForm(request.POST)

        if roomform.is_valid():
            room = roomform.save(commit=False)
            # Save owner
            room.owner = request.user
            room.save()

            # Create chat for room
            chat = Chat(room = room)
            chat.save()

            rooms = Room.objects.all()

    return render(request,'app/index.html',{'username' : request.user, 'rooms':rooms, 'roomform' :roomform })


@login_required
def room(request, room_name):
    return render(request,'app/room.html',{'room_name':room_name})


