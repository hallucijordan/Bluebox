
from django.db import models
from django.contrib.auth.models import AbstractUser


class Articles(models.Model):
    """
    攻略详情
    """
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80, verbose_name='文章标题')
    content = models.TextField(blank=True, null=True)
    level_id = models.ForeignKey(to="Levels", to_field="level_id",on_delete=models.CASCADE)
    user = models.ForeignKey("Users",on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    up_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class ArticleUp(models.Model):
    """
    点赞情况
    """
    nid = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("Users", null=True,on_delete=models.CASCADE)
    article_id = models.ForeignKey("Articles", null=True,on_delete=models.CASCADE)

    class Meta:
        unique_together = [
            ('article_id', 'user_id'),
        ]


class Comments(models.Model):
    """
    评论表
    """
    nid = models.AutoField(primary_key=True)
    article_id = models.ForeignKey("Articles",on_delete=models.CASCADE)
    user_id = models.ForeignKey("Users",on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Games(models.Model):
    """
    游戏主页
    """
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=20)
    screen_1 = models.CharField(max_length=50, blank=True, null=True)
    screen_2 = models.CharField(max_length=50, blank=True, null=True)
    screen_3 = models.CharField(max_length=50, blank=True, null=True)
    screen_4 = models.CharField(max_length=50, blank=True, null=True)
    screen_5 = models.CharField(max_length=50, blank=True, null=True)
    min_demand = models.CharField(max_length=20)
    min_operator = models.CharField(max_length=20)
    min_cpu = models.CharField(max_length=20)
    min_istorage = models.CharField(max_length=20)
    min_gpu = models.CharField(max_length=20)
    min_directx = models.CharField(db_column='min_directX', max_length=20)  # Field name made lowercase.
    rec_demand = models.CharField(max_length=20)
    rec_operator = models.CharField(max_length=20)
    rec_cpu = models.CharField(max_length=20)
    rec_istorage = models.CharField(max_length=20)
    rec_gpu = models.CharField(max_length=20)
    rec_directx = models.CharField(db_column='rec_directX', max_length=20)  # Field name made lowercase.
    min_storage = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    abstract = models.CharField(max_length=255, blank=True, null=True)
    publish_time = models.PositiveIntegerField()
    producer = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.game_name


class Levels(models.Model):
    """
    关卡信息
    """
    level_id = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(to="Games", to_field="game_id",on_delete=models.CASCADE)
    level_name = models.CharField(max_length=20)
    screen_1 = models.CharField(max_length=50, blank=True, null=True)
    screen_2 = models.CharField(max_length=50, blank=True, null=True)
    screen_3 = models.CharField(max_length=50, blank=True, null=True)
    screen_4 = models.CharField(max_length=50, blank=True, null=True)
    screen_5 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.level_name


class Users(models.Model):
    """
    用户信息
    """
    user_id = models.AutoField(primary_key=True)
    avatar = models.FileField(upload_to='avatars/', default="/avatars/default_avatar.png")
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.username()



