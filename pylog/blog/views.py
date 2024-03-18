from django.shortcuts import render
from blog.models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id) # id값이 URL에서 받은 post_id값인 Post 객체
    print(post)                         # 가져온 객체를 print 함수로 확인

    context = {
        # post_id 대신 Post 객체를 전달
        "post":post,
    }
    return render(request, 'post_detail.html', context)

def post_add(request):
    return render(request, 'post_add.html')