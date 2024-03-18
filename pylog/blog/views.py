from django.shortcuts import render, redirect
from blog.models import Post, Comment
# Create your views here.

def post_list(request):
    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id) # id값이 URL에서 받은 post_id값인 Post 객체
    if request.method == 'POST':
        comment_content = request.POST["comment"]
        Comment.objects.create(
            post=post,
            content=comment_content,
        )
    context = {
        # post_id 대신 Post 객체를 전달
        "post":post,
    }
    return render(request, 'post_detail.html', context)

def post_add(request):
    if request.method == 'POST': # method가 POST일 때

        title = request.POST['title']
        content = request.POST['content']
        thumbnail = request.FILES['thumbnail']

        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail,
        )

        return redirect(f'/posts/{post.id}/')

    return render(request, 'post_add.html')
