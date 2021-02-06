from django.db import models


class Following(models.Model):
    """Following Model Definition
    The list of following
    Fields:
    - user : connected to the user account by Foreignkey
    - following : List of accounts for whom  the user(logged in user) wants to receive feeds.(Many to many field)
    """

    user = models.ForeignKey("users.User", related_name="following", on_delete=models.CASCADE)
    following = models.ManyToManyField("users.User", blank=True, related_name="following_list")

    def __str__(self):
        return f"Following"


class Follower(models.Model):
    """Follower Model Definition
    The list of follower
    Fields:
    - user : connected to the user account by Foreignkey
    - following : List of accounts who want to receive the user(logged in user) feeds (Many to many field)
    """

    user = models.ForeignKey("users.User", related_name="follower", on_delete=models.CASCADE)
    follower = models.ManyToManyField("users.User", blank=True, related_name="follower_list")

    def __str__(self):
        return f"Follower"
