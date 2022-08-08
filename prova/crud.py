from typing import Optional

from django.contrib.auth.models import User
from django.db.models import QuerySet
from prova.models import BlogPost


def get_blog_posts(user: User) -> QuerySet:
    return BlogPost.objects.filter(user=user)


def create_blog_post(title: str, text: str, user: User, color: str) -> BlogPost:
    return  BlogPost.objects.create(title=title, text=text, user=user, color=color)




def delete_blog_post(post_id: int) -> int:
    """
    :param post_id:
    :return: Status code -> 200 = ok, 500 = error
    """
    # ugly except but meh, don't know what .delete() throws
    try:
        BlogPost.objects.filter(id=post_id).delete()
        return 200
    except:
        return 500



def updated_blog_post(post_id: int, **kwargs) -> Optional[BlogPost]:
    BlogPost.objects.filter(id=post_id).update(**kwargs)

#ALL IS TO BE TESTED