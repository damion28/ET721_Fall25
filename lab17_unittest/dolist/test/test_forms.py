from django.test import TestCase
from dolist.forms import Todolisform

class TodolistFormTest(TestCase):
    def test_todo_list_form_valid_data(self):
        # test if new data is properly collected from the form
        form = Todolisform(data = {'text' : 'Buy groceries'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['text'], 'Buy groceries')

    def test_todo_list_form_empty_data(self):
        form = Todolisform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], ['This field is required.'])