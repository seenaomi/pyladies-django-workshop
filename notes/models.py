from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100, default='')
    content = models.TextField(default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_pinned = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    COLOR_CHOICES = (
        ('white', 'White'),
        ('red', 'Red'),
        ('orange', 'Orange'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('turquoise', 'Turquoise'),
        ('blue', 'Blue'),
        ('gray', 'Gray'),
    )

    color = models.CharField(max_length=9,
                             choices=COLOR_CHOICES,
                             default=COLOR_CHOICES[0][0])

    def __unicode__(self):
        return '{0}'.format(self.title)

class Tag(models.Model):
    keyword = models.CharField(max_length=50)

    def __unicode__(self):
        return '#{0}'.format(self.keyword)

class NoteCollection(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '{0}'.format(self.name)
