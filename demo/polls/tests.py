"""Polls Application Tests."""

from django.db.utils import DataError, IntegrityError
from django.core.exceptions import ValidationError
from django.test import TestCase

from demo.polls.models import Poll


class TestPollModel(TestCase):
    """Test the Poll Model."""

    def test_object_can_be_created(self):
        """Test that we can create an object with the fields name and
        description populated."""
        test_poll = Poll.objects.create(
            name="test",
            description="test"
        )
        self.assertEqual(
            test_poll.name,
            "test",
            f"Expected name to be test but saw {test_poll.name}"
        )
        self.assertEqual(
            test_poll.description,
            "test",
            f"Expected description to be test but saw {test_poll.description}"
        )

    def test_name_char_limit(self):
        """Test that the name field enforces 64 character limit."""
        # first create one exactly at the limit to show it doesn't raise error
        Poll.objects.create(
            name="x"*64,
            description="test"
        )
        self.assertRaises(
            DataError,
            Poll.objects.create,
            name="x"*65,
            description="test"
        )

    def test_description_is_non_nullable(self):
        """Test that description field is non nullable."""
        self.assertRaises(
            IntegrityError,
            Poll.objects.create,
            name="test",
            description=None
        )

    def test_name_is_non_nullable(self):
        """Test that name field is not nullable."""
        self.assertRaises(
            IntegrityError,
            Poll.objects.create,
            name=None,
            description="test"
        )

    def test_question_field_exists(self):
        """Test question field can be populated."""
        poll = Polls.objects.create(
            name="test",
            description="test",
            question="What do you want to learn about Docker?"
        )
