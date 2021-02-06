from django.db import models
from core import models as core_models


class Photo(core_models.TimeStampedModel):
    """Photo Models Definition

    Fields:
    - file : image file for the Feed(Image Field)
    - feed : connected to the feed by Foreignkey
    """

    file = models.ImageField()
    feed = models.ForeignKey("Feed", related_name="photo", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.feed} - {self.updated}"


class Feed(core_models.TimeStampedModel):
    """Feed Models Definition

    Fields:
    - description : description of the feed with tag(Text Field)
    - account : connected to the user account by Foreignkey

    Connected:
    - Photo
    """

    description = models.TextField(blank=True)
    account = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account} - {self.updated}"
