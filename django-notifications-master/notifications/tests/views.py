''' Django notifications views for tests '''
# -*- coding: utf-8 -*-
import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from notifications.signals import notify



@login_required
def live_tester(request):
    notify.send(sender=request.user, recipient=request.user, verb='you loaded the page')

    return render(request, 'test_live.html', {
        'unread_count': request.user.notifications.unread().count(),
        'notifications': request.user.notifications.all()
    })


def send_email(request):

    notify.send(sender=request.user, recipient=request.user,
                verb='You have sent an email')




     
    
