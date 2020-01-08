from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """Set up the environment for testing"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@chaupv.com",
            password="admin1234"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@chaupv.com",
            password="user1234",
            name="Test user full name"
        )

    def test_users_listed(self):
        """Test the users are listed on user page"""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)

    def test_user_change_page(self):
        """Test that the user eidt page is workings"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_user_add_page(self):
        """Test that the user add page works"""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
