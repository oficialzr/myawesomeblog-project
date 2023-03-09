from django.db import models

import datetime

class Event(models.Model):
	event_image = models.ImageField(upload_to='event_images/')
	event_text = models.CharField(max_length=200)

	def __str__(self):
		return self.event_text
