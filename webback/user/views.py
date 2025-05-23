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
from django.db.models import Q
import re

# 글 작성
@login_required
def write_post(request):#request.method => 요청방식(get/post)
    if request.method == 'POST': 
        title = request.POST.get('title') #request.POST=>POST방식으로 전달된 값들만 모아둔 딕셔너리리, get.()=>파이썬 딕셔너리에서 값을 꺼내는 함수
        content = request.POST.get('content')
        post = Post.objects.create(#post라는 모델에 새 글 저장장
            title=title,#왼쪽 title,content,author이 POST모델의 필드드
            content=content,#오른쪽은 사용자가 입력
            author=request.user #request는 사용자의 요청 정보를 담는 객체, 누가 요청했는지, 어떤방식 get.post인지 어떤 데이터 담겼는지 정보포함
        )
        for img in request.FILES.getlist('images'):
            PostImage.objects.create(post=post, image=img)
        return redirect('post_list')
    return render(request, 'user/write.html')

# 글 목록

def post_list(request):
    query = request.GET.get('q', '').strip()
    search_type = request.GET.get('search_type', 'all')  # 기본값 'all'
    posts = Post.objects.all()

    if query:
        keywords = re.split(r'[\s,]+', query)

        q = Q()
        for word in keywords:
            if search_type == 'title':
                q |= Q(title__icontains=word)
            elif search_type == 'content':
                q |= Q(content__icontains=word)
            else:  # 'all' 또는 아무 것도 선택하지 않았을 때
                q |= Q(title__icontains=word) | Q(content__icontains=word)

        posts = posts.filter(q)

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
    
    images = post.images.all() #
    return render(request, 'user/edit.html', {'post': post, 'images': images})

# user/views.py
from .forms import CustomUserCreationForm

#댓글
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    images = post.images.all()
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

    return render(request, 'user/detail.html', {'post': post, 'images': images, 'comments': comments, 'form': form})
#좋아요
@login_required #로그인 한 사용자만 이 함수에 접근, 비로그인 상태에서는 로그인 페이지로 감감
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id) #post_id에 해당하는 post객체를 DB에서 찾고 없으면 404에러 발생생

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('post_detail', post_id=post.id)
