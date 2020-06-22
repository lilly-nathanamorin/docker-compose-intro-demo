from django.db import models


class Poll(models.Model):
    """Represents a set of polls and attributes associated with them."""
    name = models.CharField(max_length=64, blank=False,
                            help_text="The short name for a poll.")
    description = models.TextField(
        null=False,
        help_text="A longer description of the poll to give more detail than "
                  "just the name."
    )
    question = models.CharField(max_length=250, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
