from django.db import models
from django.contrib.auth.models import User


class Coder(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    

class Room(models.Model):
    room_name = models.CharField(max_length=255, null = False, blank = False,unique = True)
    owner = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.room_name
    
class Chat(models.Model):
    room = models.OneToOneField(Room, on_delete = models.CASCADE)
    chat = models.CharField(max_length = 255,blank = True)
    
    def __str__(self) -> str:
        return 'chat_' + self.room.room_name
