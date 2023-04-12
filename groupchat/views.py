from django.shortcuts import render, redirect
from django.views.generic import ListView
from groupchat.forms import GroupChatMessageForm, GroupChatForm
from groupchat.models import GroupChatMessage, GroupChat
from django.contrib.auth.models import User


class GroupChatView(ListView):
    template_name = 'layouts/index.html'
    model = GroupChatMessage
    

    def get_context_data(self, **kwargs):
        context = {
            'current_user': kwargs['current_user'],
            'user_list': kwargs['user_list'],
            'group_list': kwargs['group_list'],
            'groupforms': kwargs['groupforms'],
            'group_chat_history': kwargs['group_chat_history'],
            'creategroupforms': kwargs['creategroupforms'],
            'group': kwargs['group'],
        }

        return context
    

    def get(self, request, id):
        
        msgform = GroupChatMessageForm()
        group = GroupChat.objects.get(id=id)
        current_user = None if request.user.is_anonymous else request.user
        creategroupforms = GroupChatForm(user=current_user)
        group_chat_history = self.model.objects.filter(group=group)
        user_list = User.objects.all()
        group_list = GroupChat.objects.filter(participants=current_user)
        
        
        return render(request, self.template_name, context=self.get_context_data(
            groupforms=msgform,
            creategroupforms=creategroupforms,
            user_list=user_list,
            group_list=group_list,
            current_user=current_user,
            group_chat_history=group_chat_history.order_by('date', 'time'),
            group=group
        ))


    def post(self, request, id):
        
        form = GroupChatMessageForm(data=request.POST)
        create_group_forms = GroupChatForm(data=request.POST)
        group = GroupChat.objects.get(id=id)
        current_user = None if request.user.is_anonymous else request.user
        group_chat_history = self.model.objects.filter(group=group)
        user_list = User.objects.all()
        group_list = GroupChat.objects.filter(participants=current_user)


        if form.is_valid():
            self.model.objects.create(
                group=group,
                sender=request.user,
                text=form.cleaned_data.get('text'),
                photo=form.cleaned_data.get('photo')
            )
            return redirect(f'/group/{id}/')
        
        elif create_group_forms.is_valid():
            users = [user.id for user in create_group_forms.cleaned_data.get('participants')]
            users.append(current_user)
            grp = GroupChat.objects.create(groupname=create_group_forms.cleaned_data.get('groupname'))
            grp.participants.set(users)
            grp.save()
            return redirect(f'/group/{id}/')

        else:
            return render(request, self.template_name, context=self.get_context_data(
                groupforms=GroupChatMessageForm,
                creategroupforms=GroupChatForm,
                user_list=user_list,
                group_list=group_list,
                current_user=current_user,
                group_chat_history=group_chat_history.order_by('date', 'time'),
                group=group
            ))


def leave_group_view(request, id):
    current_group = GroupChat.objects.get(id=id)
    current_user = request.user
    current_group.participants.remove(current_user)
    return redirect('/')