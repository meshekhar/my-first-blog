from django import forms
from django_comments.forms import CommentForm
from django_comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode
from django.conf import settings
import datetime

class UserCommentForm(CommentForm):

    """
        A comment form which matches the default djanago.
        contrib.comments one, but with 3 removed fields
    """
    def get_comment_create_data(self):
        # Use the data of the superclass, and remove extra fields
        return dict(
            content_type = ContentType.objects.get_for_model(self.target_object),
            object_pk    = force_unicode(self.target_object._get_pk_val()),
            comment      = self.cleaned_data["comment"],
            submit_date  = datetime.datetime.now(),
            site_id      = settings.SITE_ID,
            is_public    = True,
            is_removed   = False,
        )

UserCommentForm.base_fields.pop('name')
UserCommentForm.base_fields.pop('email')
UserCommentForm.base_fields.pop('url')
