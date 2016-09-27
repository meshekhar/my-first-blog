def get_model():
    from django_comments.models import Comment
    return Comment


def get_form():
    from og_comments_app.forms import UserCommentForm
    return UserCommentForm
