from django.test import TestCase
from django.urls import reverse
from .models import MyModel

class HomeViewTest(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

class FormViewTest(TestCase):
    def test_form_view_get(self):
        response = self.client.get(reverse('form_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

    def test_form_view_post(self):
        response = self.client.post(reverse('form_view'), {
            'name': 'Test Name',
            'description': 'Test Description'
        })
        self.assertEqual(response.status_code, 302)  # Expect redirect
        self.assertRedirects(response, reverse('data_list'))
        
        # Check that the object was created
        self.assertEqual(MyModel.objects.count(), 1)
        self.assertEqual(MyModel.objects.first().name, 'Test Name')

class DataListViewTest(TestCase):
    def setUp(self):
        MyModel.objects.create(name='Item 1', description='Description 1')
        MyModel.objects.create(name='Item 2', description='Description 2')

    def test_data_list_view_status_code(self):
        response = self.client.get(reverse('data_list'))
        self.assertEqual(response.status_code, 200)

    def test_data_list_view_template(self):
        response = self.client.get(reverse('data_list'))
        self.assertTemplateUsed(response, 'data_list.html')

    def test_data_list_view_content(self):
        response = self.client.get(reverse('data_list'))
        self.assertContains(response, 'Item 1')
        self.assertContains(response, 'Item 2')

class DetailViewTest(TestCase):
    def setUp(self):
        self.item = MyModel.objects.create(name='Test Item', description='Test Description')

    def test_detail_view_status_code(self):
        response = self.client.get(reverse('detail_view', args=[self.item.pk]))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_template(self):
        response = self.client.get(reverse('detail_view', args=[self.item.pk]))
        self.assertTemplateUsed(response, 'detail.html')

    def test_detail_view_content(self):
        response = self.client.get(reverse('detail_view', args=[self.item.pk]))
        self.assertContains(response, 'Test Item')
        self.assertContains(response, 'Test Description')

