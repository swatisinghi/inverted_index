from django.db import models

class Documents(models.Model):
	text = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.text
