from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from uuid import uuid4
from core.consumers import code_snippet_store


class HomeView(View):
    def get(self, request):
        if request.session.get('language'):
            del request.session['language']
        return render(request, 'index.html')
    
    def post(self, request):
        language = request.POST.get('language')
        if not language:
            language = 'javascript'
        request.session['language'] = language
        request.session.save()

        return HttpResponseRedirect('/editor/' + str(uuid4()))
    
class WorkspaceView(View):
    def get(self, request, room_uuid):

        language_map = {
            'javascript': 'javascript',
            'python': 'python',
            'c': 'text/x-csrc',
            'php': 'php',
            'c#': 'text/x-csharp',
            'c++': 'text/x-c++src',
        }

        if not code_snippet_store.get(room_uuid):
            language = request.session.get('language', 'javascript')
            code_snippet_store[room_uuid] = {'uuid': room_uuid, 'language': language, 'code': ''}

        language = code_snippet_store.get(room_uuid, {}).get('language', '')

        return render(request, 'editor.html' , {'room_uuid': room_uuid, 
                                                'language': language, 
                                                'mode': language_map[language],
                                                "saved_code": code_snippet_store.get(room_uuid, {}).get('content', '')})
    
    def post(self, request):
        return HttpResponseRedirect('/')