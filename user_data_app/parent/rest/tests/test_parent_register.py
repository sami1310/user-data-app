from django.test import TestCase
from django.contrib.auth import get_user_model
from parent.rest.serilizers.parent_register import ParentRegisterSerializer


class ParentRegisterSerializerTest(TestCase):
    def test_create_parent(self):
        # Test data
        data = {
            "user": {
                "email": "test@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "gender": "Male",
            },
            "password": "testpassword",
            "street": "123 Main St",
            "city": "Cityville",
            "state": "Stateville",
            "zip_code": "12345",
        }

        # Creating a user using the serializer
        serializer = ParentRegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        parent = serializer.save()

        # Checking if the user and parent objects are created correctly
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(parent.user.email, data["user"]["email"])
        self.assertEqual(parent.street, data["street"])
        self.assertEqual(parent.city, data["city"])
        self.assertEqual(parent.state, data["state"])
        self.assertEqual(parent.zip_code, data["zip_code"])
        self.assertTrue(parent.is_parent)

        # Check if the user password is set correctly
        self.assertTrue(parent.user.check_password(data["password"]))
