from django.shortcuts import render
from .models import *
from django.db.models import Count
from django.http import HttpResponse


# 1) bitta postga bosilgan likelar soni
# 2) Jasurning barcha postlariga yozilgan comentariyalar soni
# 3) Jasurning yozgan barcha komentariyalar soni
# 4) Jasurning eng ko'p va eng kam laykka ega posti
# 5) jasurning postlariga yozilgan eng ohirgi comment 
# 6) Eng Ko'p followerga ega bo'lgan foydalanuvchining postlar soni
# 7) Eng ko'p layk bosilgan postdagi komentariyalar soni 

# function agrument sifatida har doim request qabul qiladi request >>> response
def orm(request):

    # CRUD >>> Read 
    jasur, _ = User.objects.get_or_create(
        username='jasur01',
        defaults={
            "email":'jasur@gmail.com',
            "password":'1',
            "full_name":'Jasur'    
            }
    )   

    post, _ = Post.objects.get_or_create(caption='test', owner=jasur)
    post_likes = post.post_likes.count()  # bitta postga bosilgan likelar soni

    # CRUD >>> Cread
    

    jasur_post = Post.objects.create(
        caption='Bu juda zo\'r experience boldi',
        location='Toshkent, Uzbekistan',
        owner=jasur
    )

    Comment.objects.create(
        post=jasur_post,
        commentator=jasur,
        text='😎 ha bilaman'
    )    

    # jasurning barcha postlaridagi comentariyalar soni 
    # komment_soni = Comment.objects.filter(post__owner=jasur).count()

    komment_soni = jasur.posts.aggregate(total_comments=Count("comment"))['total_comments'] or 0 #{'total_comments': None}


    # Jasurning yozgan barcha komentariyalar soni
    # jasur_comments = Comment.objects.filter(commentator=jasur).count()

    # jasur_comments = jasur.comment_set.count()

    jasur_post_like_max = jasur.posts.annotate(likes_count = Count('post_likes')).order_by('-likes_count').first()


    # jasurning postlariga yozilgan eng ohirgi comment 
    jasur_last_post_comment = Comment.objects.filter(post__owner=jasur).last()


    # Eng Ko'p followerga ega bo'lgan foydalanuvchining postlar soni
    eng_kop_followerga_ega_shaxs = User.objects.annotate(follower_count = Count('user_following')).order_by('-follower_count').first()
    eng_kop_followerga_ega_shaxs_postlar_soni = eng_kop_followerga_ega_shaxs.posts.count()


    #  Eng ko'p layk bosilgan postdagi komentariyalar soni 
    eng_kop_layk_post = Post.objects.annotate(likes_count=Count('post_likes')).order_by('-likes_count').first()
    eng_kop_layk_post_comments = eng_kop_layk_post.comment_set.count()

    return HttpResponse(f"{komment_soni}, {jasur_post_like_max}, {jasur_last_post_comment}, {eng_kop_followerga_ega_shaxs_postlar_soni}, {eng_kop_layk_post_comments}")
