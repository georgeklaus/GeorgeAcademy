from django.test import TestCase
from .models import Course  # Replace with the actual Course model import

class CourseTest(TestCase):
    def test_course_creation(self):
        # Example test case
        course = Course.objects.create(name='Test Course')  # Adjust parameters as needed
        self.assertEqual(course.name, 'Test Course')
