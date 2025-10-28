from django.test import TestCase


class PollsTestCase(TestCase):
    """Basic test case for polls app."""

    def test_basic(self):
        """Basic test to ensure test framework is working."""
        self.assertEqual(1 + 1, 2)

    def test_string_operations(self):
        """Test basic string operations."""
        self.assertEqual("hello".upper(), "HELLO")
        self.assertEqual("WORLD".lower(), "world")
