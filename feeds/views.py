from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Roadmap, Career, Solution


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'feeds/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'feeds/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 37


class UserPostListView(ListView):
    model = Post
    template_name = 'feeds/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 37

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class SolutionCreateView(LoginRequiredMixin, CreateView):
    model = Solution
    template = 'feeds/solution_form.html'
    fields = ['solution']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_pk'])
        return super().form_valid(form)


def givesolution(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'feeds/givesolution.html', context)


def roadmap(request):
    context = {
        'posts': Roadmap.objects.all()
    }
    return render(request, 'feeds/roadmap.html', context)


def careers(request):
    context = {
        'posts': Career.objects.all()
    }
    return render(request, 'feeds/careers.html', context)


def privacy(request):
    return render(request, 'feeds/privacy.html', {'title': 'Privacy'})


def terms(request):
    return render(request, 'feeds/terms.html', {'title': 'Terms'})


def faq(request):
    return render(request, 'feeds/faq.html', {'title': 'faq'})


def about(request):
    return render(request, 'feeds/about.html', {'title': 'About'})
