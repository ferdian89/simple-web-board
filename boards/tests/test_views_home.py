from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.urls import resolve
from django.test import TestCase

from ..forms import NewTopicForm
from ..views import home, board_topics, new_topic
from ..models import Board, Topic, Post

# Create your tests here.
class HomeTests(TestCase):
	def setUp(self):
		self.board = Board.objects.create(name='Django', description='Django board.')
		User.objects.create_user(username='john', email='john@doe.com', password='123')  # <- included this line here
		url = reverse('home')
		self.response = self.client.get(url)

	def test_home_view_status_code(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_home_url_resolves_home_view(self):
		view = resolve('/')
		self.assertEquals(view.func, home)

	def test_home_view_contains_link_to_topics_page(self):
		board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
		self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

	def test_board_topics_view_contains_link_back_to_homepage(self):
		board_topics_url = reverse('board_topics', kwargs={'pk': 1})
		response = self.client.get(board_topics_url)
		homepage_url = reverse('home')
		self.assertContains(response, 'href="{0}"'.format(homepage_url))




