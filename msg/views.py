from django.shortcuts import render, redirect
from django.views.generic import ListView
from msg.forms import CreateMessage
from msg.models import Message
from django.contrib.auth.models import User


def main_view(request):
    if not request.user.is_anonymous:
        return redirect(f'/user/{request.user.id}/')
    else:
        return redirect('/login/')


class ChatView(ListView):
    template_name = 'layouts/index.html'
    model = Message

    def get_context_data(self, **kwargs):
        context = {
            'current_user': kwargs['current_user'],
            'second_user': kwargs['second_user'],
            'user_list': kwargs['user_list'],
            'forms': kwargs['forms'],
            'chat_history': kwargs['chat_history'],
        }

        return context

    def get(self, request, id, *args, **kwargs):
        second_user = User.objects.get(id=id)
        current_user = None if request.user.is_anonymous else request.user
        second = self.model.objects.filter(
            receiver=second_user, sender=current_user)
        current = self.model.objects.filter(
            receiver=current_user, sender=second_user)
        chat_history = second | current

        if id == current_user.id:
            return render(request, self.template_name, context={
                'current_user': None if request.user.is_anonymous else request.user,
                'user_list': User.objects.all(),
            })

        elif id != current_user.id:

            return render(request, self.template_name, context=self.get_context_data(
                forms=CreateMessage,
                user_list=User.objects.all(),
                current_user=current_user,
                second_user=second_user,
                chat_history=chat_history.order_by('date', 'time')
            ))

    def post(self, request, id, **kwargs):
        current_user = None if request.user.is_anonymous else request.user
        second_user = User.objects.get(id=id)
        form = CreateMessage(data=request.POST)
        second = self.model.objects.filter(
            receiver=second_user, sender=current_user)
        current = self.model.objects.filter(
            receiver=current_user, sender=second_user)
        chat_history = second | current

        if form.is_valid():
            Message.objects.create(
                receiver=second_user,
                sender=request.user,
                text=form.cleaned_data.get('text'),
                photo=form.cleaned_data.get('photo')
            )
            return redirect(f'/user/{id}/')

        else:
            return render(request, self.template_name, context=self.get_context_data(
                forms=CreateMessage,
                user_list=User.objects.all(),
                current_user=current_user,
                second_user=second_user,
                chat_history=chat_history.order_by('date', 'time')
            ))
