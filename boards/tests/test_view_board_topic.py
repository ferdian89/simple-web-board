from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.urls import resolve
from django.test import TestCase

from ..forms import NewTopicForm
from ..views import home, board_topics, new_topic
from ..models import Board, Topic, Post


class BoardTopicTests(TestCase):
	def setUp(self):
		Board.objects.create(name='Django', description='Django board.')

	def test_board_topics_view_success_status_code(self):
		url = reverse('board_topics', kwargs={'pk': 1})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_board_topics_view_not_found_status_code(self):
		url = reverse('board_topics', kwargs={'pk': 99})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 404)

	def test_board_topic_url_resolves_board_topic_view(self):
		view = resolve('/boards/1/')
		self.assertEquals(view.func, board_topics)