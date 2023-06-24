from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import PostForm
from datetime import datetime
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Response
from django.conf import settings
from django.contrib.sites.models import Site
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .forms import ResponseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class PostList(ListView):
    model = Post
    ordering = 'text'
    template_name = 'post.html'
    context_object_name = 'post'
    paginate_by = 10


class PostCreate(CreateView):
    permission_required = ('new.add_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)



class PostDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response_form'] = ResponseForm()
        return context

    def post(self, request, *args, **kwargs):
        response_form = ResponseForm(request.POST)
        if response_form.is_valid():
            post_id = kwargs.get('pk')
            post = get_object_or_404(Post, pk=post_id)
            user = request.user

            response = response_form.save(commit=False)
            response.post = post
            response.author = user
            response.save()

            # Отправка письма на почту автору объявления
            subject = 'Новый отклик на ваше объявление'
            message = f'Пользователь {user.username} оставил отклик на ваше объявление "{post.tittle}".'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = post.author.email

            send_mail(subject, message, from_email, [to_email], fail_silently=False)

            return redirect('post_detail', pk=post.pk)
        else:
            return self.get(request, *args, **kwargs)





class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('new.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('new.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


@login_required
def accept_response(request, response_id):
    response = get_object_or_404(Response, pk=response_id)
    post = response.post

    if request.user == post.author:
        response.accepted = True
        response.save()

        # Отправка письма на почту пользователю, чей отклик был принят
        subject = 'Ваш отклик принят'
        message = f'Ваш отклик на объявление "{post.tittle}" был принят автором.'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = response.author.email

        send_mail(subject, message, from_email, [to_email], fail_silently=False)

    return redirect('author_page')


@login_required
def reject_response(request, response_id):
    response = get_object_or_404(Response, pk=response_id)
    post = response.post

    if request.user == post.author:
        response.accepted = False
        response.save()

        # Отправка письма на почту пользователю, чей отклик был отклонен
        subject = 'Ваш отклик отклонен'
        message = f'Ваш отклик на объявление "{post.tittle}" был отклонен автором.'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = response.author.email

        send_mail(subject, message, from_email, [to_email], fail_silently=False)

    return redirect('author_page')



class AuthorPage(LoginRequiredMixin, TemplateView):
    template_name = 'author_page.html'
    context_object_name = 'news_list'


    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user).prefetch_related('responses').order_by('-dataCreation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        posts = Post.objects.filter(author=user)
        responses = Response.objects.filter(post__author=user).select_related('post')
        accepted_responses = responses.filter(accepted=True)
        pending_responses = responses.filter(accepted=False)

        context['author'] = user
        context['posts'] = posts
        context['accepted_responses'] = accepted_responses
        context['pending_responses'] = pending_responses
        return context

    def post(self, request, *args, **kwargs):
        response_id = request.POST.get('response_id')
        response = get_object_or_404(Response, pk=response_id)
        post = response.post

        if request.user == post.author:
            if 'accept' in request.POST:
                response.accepted = True
                response.save()
            elif 'reject' in request.POST:
                response.delete()

        return redirect('author_page')


