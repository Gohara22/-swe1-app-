from django.test import TestCase


class PollsTestCase(TestCase):
    """Basic test case for polls app."""

    def test_basic(self):
        """Basic test to ensure test framework is working."""
        self.assertEqual(1 + 1, 2)
