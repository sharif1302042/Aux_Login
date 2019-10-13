# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
import asyncio
from channels.consumer import AsyncConsumer


class Consumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'handle_otp',
                'message': message,
                'sharif': 'sharif'
            }
        )

    # Receive message from room group
    def handle_otp(self, event):
        message = event['message']
        print("Your OTP is :", event['message'])
        print("Your_name is:", event['sharif'])

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))


class OTPConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected ", event)

    async def websocket_receive(self, event):
        print("connected ", event)


