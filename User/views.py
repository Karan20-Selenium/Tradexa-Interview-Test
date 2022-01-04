from django.shortcuts import render, HttpResponseRedirect
from .forms import PostRegistration
from .models import User,Post
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class PostAddShowView(TemplateView):
  template_name = 'addPost.html'
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    fm = PostRegistration()
    posts = Post.objects.all()
    context = {'posts':posts, 'form':fm}
    return context
  
  def post(self, request):
    fm = PostRegistration(request.POST)
    if fm.is_valid():
      usr = fm.cleaned_data['user']
      txt = fm.cleaned_data['text']
      cat = fm.cleaned_data['created_at']
      uat = fm.cleaned_data['updated_at']

      reg = Post(user=usr, text=txt, created_at=cat, updated_at=uat)
      reg.save()
    return HttpResponseRedirect('/')



# This Class will Update/Edit
@method_decorator(login_required, name='dispatch')
class PostUpdateView(View):
  def get(self, request, id):
    pi = Post.objects.get(pk=id)
    fm = PostRegistration(instance=pi)
    return render(request, 'updatepost.html', {'form':fm})
  
  def post(self, request, id):
    pi = Post.objects.get(pk=id)
    fm = PostRegistration(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
    return HttpResponseRedirect('/')

# This Class will Delete
@method_decorator(login_required, name='dispatch')
class PostDeleteView(RedirectView):
  url = '/'
  def get_redirect_url(self, *args, **kwargs):
    del_id = kwargs['id']
    Post.objects.get(pk=del_id).delete()
    return super().get_redirect_url(*args, **kwargs)
