from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from parent.models import Parent
from user.models import User
from user.rest.serializers.user import UserSerializer


class UserParentDeleteViewTest(APITestCase):
    def setUp(self):
        # Create a User and Parent instance for testing
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
        )
        self.parent = Parent.objects.create(
            user=self.user,
            street="Test Street",
            city="Test City",
            state="Test State",
            zip_code="12345",
        )

    def test_delete_user_and_parent(self):
        # Ensure that the endpoint deletes the user and associated parent
        url = f"/parent/delete/{self.parent.uid}"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the user and parent have been deleted
        self.assertFalse(User.objects.filter(uid=self.user.uid).exists())
        self.assertFalse(Parent.objects.filter(id=self.parent.id).exists())
