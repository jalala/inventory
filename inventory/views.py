# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from inventory.models import Section, Room
from django.contrib import auth
def home(request):
    return render_to_response('home.html',
                          context_instance=RequestContext(request))

@login_required()
def sections(request):
    sections = Section.objects.all()
    context = {'sections':sections}
    return render_to_response('sections.html', context,
                          context_instance=RequestContext(request))


@login_required()
def section_rooms(request, section_id):
    if request.user is None:
        return HttpResponseRedirect('/inventory/login/')

    section = Section.objects.get(pk=section_id)
    context = {'section':section}
    return render_to_response('section_rooms.html', context,
                          context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
@login_required()
def room_items(request, room_id):
    if request.user is None:
        return HttpResponseRedirect('/inventory/login/')
    room = Room.objects.get(pk=room_id)
    context = {'room':room}
    return render_to_response('room_items.html', context,
                          context_instance=RequestContext(request))
