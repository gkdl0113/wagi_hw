# user/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Post, PostImage
from django.shortcuts import get_object_or_404, redirect
from .forms import CommentForm

# 글 작성
@login_required
def write_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        for img in request.FILES.getlist('images'):
            PostImage.objects.create(post=post, image=img)
        return redirect('post_list')
    return render(request, 'user/write.html')

# 글 목록
def post_list(request):
    query = request.GET.get('q')  # ?q=검색어
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()
    return render(request, 'user/list.html', {'posts': posts})


# 글 수정

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return HttpResponseForbidden("수정 권한이 없습니다.")

    if request.method == 'POST':
        # 제목과 내용 수정
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()

        # ✅ 체크된 이미지 삭제
        delete_ids = request.POST.getlist('delete_images')  # name="delete_images"
        for img_id in delete_ids:
            image = PostImage.objects.filter(id=img_id, post=post).first()
            if image:
                image.delete()

        # ✅ 새 이미지 추가
        for img in request.FILES.getlist('images'):
            PostImage.objects.create(post=post, image=img)

        # ✅ post_detail 페이지로 이동
        return redirect('post_detail', post_id=post.id)

    return render(request, 'user/edit.html', {'post': post})

# user/views.py
from .forms import CustomUserCreationForm
#회원가입
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login') #로그인 페이지로 이동동
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/signup.html', {'form': form})
#로그인
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')  # 로그인 성공 시 이동할 페이지
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')

    return render(request, 'user/login.html')

#댓글
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)

    return render(request, 'user/detail.html', {'post': post, 'comments': comments, 'form': form})
#좋아요
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('post_detail', post_id=post.id)
#로그아웃
def logout_view(request):
    logout(request)
    return redirect('login')