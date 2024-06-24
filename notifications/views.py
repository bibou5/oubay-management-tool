from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Notification
from .forms import CreateNotificationForm
from django.contrib import messages
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .decorators import admin_required


# Create your views here.

@admin_required
def add_notification(request):
    if request.method == "POST":
        form = CreateNotificationForm(request.POST)
        if form.is_valid():
            notification = form.save()
            channel_layer = get_channel_layer()
            for user in form.cleaned_data['reciptients']:
                async_to_sync(channel_layer.group_send)(
                    f'notifications_{user.id}',
                    {
                        'type': 'send_notification',
                        'notification': {
                            'message': notification.message,
                        }
                    }
                )
            if 'save' in request.POST:
                messages.success(request, 'Notification created successfully!')
                return redirect('dashboard')
            elif 'save_and_add_another' in request.POST:
                messages.success(request, 'Notification created successfully! You can add another one.')
                return redirect(reverse('notifications:add_notification'))
    else:
        form = CreateNotificationForm()
    return render(request, 'notifications/add_notification.html', {'form': form})
