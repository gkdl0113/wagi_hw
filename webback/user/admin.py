from django.contrib import admin
from .models import Post, PostImage, Comment  # ✅ Comment를 꼭 import 해줘야 함!

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Comment)  # ✅ 여기에 빨간 줄 생겼다면 위에서 import 안 했기 때문
