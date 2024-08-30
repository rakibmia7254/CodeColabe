import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime
from asgiref.sync import sync_to_async

code_snippet_store = {}

class CodeEditorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'code_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({
            'type': 'connection_established'
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        code = text_data_json['code']
        language = text_data_json['language']
        await self.create_or_update_code(self.room_name, code, language)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'brodcast',
                'code': code
            }
        )

    async def brodcast(self, event):
        code = event['code']
        await self.send(text_data=json.dumps({
            'code': code,
            'types': 'update'
        }))

    # create or update code
    @sync_to_async
    def create_or_update_code(self, uuid, code, language):
        snippet = {
            'uuid': uuid,
            'content': code,
            'language': language,
            'timestamp': datetime.now().isoformat()
        }
        
        if uuid in code_snippet_store:
            code_snippet_store[uuid].update(snippet)
        else:
            code_snippet_store[uuid] = snippet

        # Maintain only the last 50 snippets
        if len(code_snippet_store) > 50:
            code_snippet_store.popitem(last=False)
            
        return code_snippet_store[uuid]
    
