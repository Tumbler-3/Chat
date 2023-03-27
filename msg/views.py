from django.shortcuts import render, redirect
from django.views.generic import ListView
from msg.forms import CreateMessage
from msg.models import Message
from django.contrib.auth.models import User
from itertools import chain


def main_view(request):
    return render(request, 'layouts/index.html', context={
        'current_user': None if request.user.is_anonymous else request.user,
        'user_list': User.objects.all(),
    })


class ChatView(ListView):
    template_name = 'chats/chat.html'
    model = Message

    def get_context_data(self, request, **kwargs):
        context = {
        }

        return context

    def get(self, request, id, *args, **kwargs):
        second_user = User.objects.get(id=id)
        current_user = None if request.user.is_anonymous else request.user
        second = self.model.objects.filter(receiver=second_user, sender=current_user)
        current = self.model.objects.filter(receiver=current_user, sender=second_user)
        chat_history = second | current
        
        
        return render(request, self.template_name, context={
            'form': CreateMessage,
            'user_list': User.objects.all(),
            'current_user': current_user,
            'second_user': second_user,
            'chat_history': chat_history.order_by('date'),
        })

    def post(self, request, id, **kwargs):
        current_user = None if request.user.is_anonymous else request.user
        second_user = User.objects.get(id=id)
        form = CreateMessage(data=request.POST)
        second = self.model.objects.filter(receiver=second_user, sender=current_user)
        current = self.model.objects.filter(receiver=current_user, sender=second_user)
        chat_history = second | current
        
        if form.is_valid():
            Message.objects.create(
                receiver = second_user,
                sender = request.user,
                text = form.cleaned_data.get('text'),
                photo = form.cleaned_data.get('photo')
            )
            return redirect(f'/user/{id}/')
        
        else:
            return render(request, self.template_name, context={
            'form': CreateMessage,
            'user_list': User.objects.all(),
            'current_user': current_user,
            'second_user': second_user,
            'chat_history': chat_history.order_by('date'),
        })

        