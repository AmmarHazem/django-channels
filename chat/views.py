from django.shortcuts import render
from django.views.generic import View
from django.utils.safestring import mark_safe
import json


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chat/index.html')


class Room(View):
    def get(self, request, room_name):
        return render(request, 'chat/room.html', {'room_name_json' : mark_safe(json.dumps(room_name))})
