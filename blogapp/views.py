from django.shortcuts import render,render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http.response import HttpResponse
from blogapp.models import Post, Comment
from blogapp.forms import PostForm, CommentForm
from custom.decorators.blogapp import decorators




# Create your views here.
def index(request):
    context = {'posts': Post.objects.all(), 'commentForm': CommentForm()}
    template_name = 'blogapp/post_index.html'

    return render(request, template_name, context)


@user_passes_test(decorators.check_superuser, login_url='blogapp:post_index')
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            print(post)
            return redirect('blogapp:post_index')

    context = {'form': PostForm()}
    template_name = 'blogapp/post_create.html'
    return render(request, template_name, context)


@user_passes_test(decorators.check_superuser, login_url='blogapp:post_index')
def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=True)
            return redirect('blogapp:post_index')

    context = {'form': PostForm(instance=post)}
    template_name = 'blogapp/post_edit.html'

    return render(request, template_name, context)


@user_passes_test(decorators.check_superuser, login_url='blogapp:post_index')
def destroy(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('blogapp:post_index')



# adding the Comment View
def comment_store(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blogapp:post_index')

    return redirect('blogapp:post_index')



def comment_index(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {'post': post}
    template_name = 'blogapp/comment_index.html'
    return render(request, template_name, context)



def approved_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.approve()

    return redirect('blogapp:post_index')
    # return HttpResponse(f'comment page renders out with the id {comment_id}')
