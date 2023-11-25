from django.test import TestCase
from rest_framework.test import APITestCase
from parent.models import Parent
from parent.rest.serilizers.parent_update import ParentUpdateSerializer


class ParentUpdateSerializerTest(TestCase):
    def setUp(self):
        # Create a Parent instance for testing
        self.parent = Parent.objects.create(
            street="Test Street",
            city="Test City",
            state="Test State",
            zip_code="12345",
        )

    def test_update_parent_serializer(self):
        # Create a serialized representation of the Parent instance
        serialized_data = ParentUpdateSerializer(instance=self.parent).data
        print("#####################################################", serialized_data)

        # Modify some data in the serialized representation
        modified_data = {
            "street": "Updated Street",
            "city": "Updated City",
            "state": "Updated State",
        }

        serialized_data.update(modified_data)

        # Create a serializer instance with the modified data
        serializer = ParentUpdateSerializer(instance=self.parent, data=serialized_data)

        # Validate the serializer
        self.assertTrue(serializer.is_valid())

        # Update the instance using the serializer
        serializer.save()

        # Refresh the instance from the database
        updated_parent = Parent.objects.get(id=self.parent.id)

        # Check that the instance has been updated
        self.assertEqual(updated_parent.street, "Updated Street")
        self.assertEqual(updated_parent.city, "Updated City")
        self.assertEqual(updated_parent.state, "Updated State")
