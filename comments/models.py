from django.db import models
from core import models as core_models


class Comment(core_models.TimeStampedModel):
    """ Comment Model Definition """

    comment = models.TextField()
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment} - {self.feed}"
