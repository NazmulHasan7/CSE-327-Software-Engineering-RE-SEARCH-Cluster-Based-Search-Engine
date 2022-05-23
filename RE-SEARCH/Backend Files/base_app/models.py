from django.conf.urls import url
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from spider.spider.spiders.crawler import begin_crawl

'''
Cluster
One user can have multiple clusters
So an one-to-many relationship has been created
'''
class Cluster(models.Model):
    # Once the user deletes his account, clusters related to his account will be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='clusters')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, default='Creating a Search Cluster for advanced search')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        # Default ordering is set to date_created
        ordering = ['date_created']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Cluster, self).save(*args, **kwargs)

'''
Each Cluster can have multiple urls
So an one-to-many-relationship has been created 
'''
output_preference = (
        ('html', 'Textual Data'),
        ('pdf', 'PDF File'),
        ('txt', 'TXT File'),
        ('doc', 'DOC File'),
        ('docx', 'Docx File'),
    )

class Url(models.Model):
    # Once a Cluster is deleted, all the urls related to that cluster will be deleted
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE, null=True, blank=True, related_name='urls')
    cluster_url = models.URLField(max_length=200)
    depth = models.PositiveIntegerField()
    output_type = models.CharField(max_length=20, choices=output_preference)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    is_crawled= models.BooleanField(default=False)

    class Meta:
        # Default ordering is set to date_created
        ordering = ['date_added']

    def __str__(self):
        return self.cluster_url
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.cluster)
        super(Url, self).save(*args, **kwargs)
       