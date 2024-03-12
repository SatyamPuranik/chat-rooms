from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat, Room
from asgiref.sync import sync_to_async


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected...')
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(self.room_name, self.channel_name)

        # Get old chats from database
        chat = await sync_to_async(Chat.objects.get)(room = await sync_to_async(Room.objects.get)(room_name = self.room_name))

        await self.accept()

        # Show old chats 
        await self.send(text_data=chat.chat)


    async def disconnect(self, code):
        print('disconnected....', code)
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        print('Server sending messages...')

        # if user is authenticated save chat in database
        if self.scope['user'].is_authenticated:
            print('User is authenticated')

            prev_chat =  await sync_to_async(Chat.objects.get)(room = await sync_to_async(Room.objects.get)(room_name = self.room_name))
            new_chat =  prev_chat.chat + '\n' + text_data
            prev_chat.chat = new_chat
            await sync_to_async(prev_chat.save)()
            # Saved 

            # Broadcasts
            await self.channel_layer.group_send(
                self.room_name,
                {
                    "type": "chat.message",
                    "message": text_data,
                }
            )
        else:
            print('User is not authenticated')

    async def chat_message(self, event):
        # Send a message down to the client
        print('Sending actual message...',event)
        await self.send(event["message"])
        # print(self.channel_name)