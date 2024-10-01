from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import BlogPost, Comment

User = get_user_model()

class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = BlogPost.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user
        )

    def test_blog_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(self.post.author, self.user)

    def test_blog_post_comment(self):
        comment = Comment.objects.create(
            post=self.post,
            content="This is a test comment.",
            author=self.user
        )
        self.assertEqual(comment.content, "This is a test comment.")
        self.assertEqual(comment.post, self.post)

    def test_blog_post_author(self):
        self.assertEqual(self.post.author.username, 'testuser')
