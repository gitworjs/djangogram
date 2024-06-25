from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

class TestPosts(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username = 'django' , email = 'django@gmail.com' , password = 'admin'
        )

    def test_get_posts_page(self):
        url = reverse('posts:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/index.html')

    def test_creating_posts(self):
        login = self.client.login(username="django", password ="admin")
        self.assertTure(login)
        
        url = reverse('posts:post_create')
        image = SimpleUploadedFile("test.jpg", b"whatevercontents")
        response = self.client.post(
            url,
            {"image": image, "caption": 'test'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/base.html")

    def test_post_posts_create_not_login(self):
        url = reverse('posts:post_create')
        image = SimpleUploadedFile("test.jpg", b"whatevercontents")
        response = self.client.post(
            url,
            {"image": image, "caption": 'test test'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/main.html")