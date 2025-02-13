from django.db import models


# Instagram DB
class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(upload_to='users/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=50, null=True)


class UserFollower(models.Model):
    follower = models.ForeignKey( # Abdulloh
        User, 
        on_delete=models.CASCADE, 
        related_name="user_follower"
    )
    following = models.ForeignKey( # Jasur
        User, 
        on_delete=models.CASCADE,
        related_name="user_following"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Post(models.Model):
    poster = models.ImageField(upload_to="posters/", null=True)
    caption = models.TextField(null=True)
    tagged_users = models.ManyToManyField(User)
    location = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')


class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.FileField(upload_to='contents/')
    order = models.IntegerField(default=1)
    

    class Meta:
        ordering = ('order',)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # comment_set
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    gif = models.CharField(max_length=500, null=True)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='comments_reply')
    created_at = models.DateTimeField(auto_now_add=True)
    top_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='comments_top')


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts_like")
    created_at = models.DateTimeField(auto_now_add=True)




# 1) bitta postga bosilgan likelar soni
# 2) Jasurning barcha postlariga yozilgan comentariyalar soni
# 3) Jasurning yozgan barcha komentariyalar soni
# 4) Jasurning eng ko'p va eng kam laykka ega posti
# 5) jasurning postlariga yozilgan eng ohirgi comment 
# 6) Eng Ko'p followerga ega bo'lgan foydalanuvchining postlar soni
# 7) Eng ko'p layk bosilgan postdagi komentariyalar soni 