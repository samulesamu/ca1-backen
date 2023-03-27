from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from subjects.models import Subject, Notes
from io import BytesIO
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.subject = Subject.objects.create(subject_name="Test subject")

    def test_subject_creation(self):
        self.assertEqual(self.subject.__str__(), self.subject.subject_name)

    def test_add_subject_view(self):
        self.client.login(username='admin', password='password')
        url = reverse('add_subject')
        response = self.client.post(url, {'subject_name': 'New Subject'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Subject.objects.count(), 2)

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')
        self.subject = Subject.objects.create(subject_name="Test subject")
        self.file = SimpleUploadedFile("test_file.txt", b"file_content", content_type="text/plain")
        self.note = Notes.objects.create(name="Test note", subject=self.subject, file=self.file, user=self.user)

    def test_note_creation(self):
        self.assertEqual(self.note.__str__(), self.note.name)

    def test_upload_file_view(self):
        file = BytesIO(b"test file content") # create a file-like object
        file.name = 'test_file.txt'
        uploaded_file = SimpleUploadedFile("test_file.txt", file.getvalue())

        response = self.client.post('/upload_file', {'file': uploaded_file})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Notes.objects.count(), 1)

    def test_notes_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


    def test_delete_file_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('delete_file', args=[self.note.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Notes.objects.count(), 0)
    def test_sign_up_view(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_login_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_password_reset_view(self):
        url = reverse('password_reset')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_password_reset_done_view(self):
        url = reverse('password_reset_done')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_password_reset_complete_view(self):
        url = reverse('password_reset_complete')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)