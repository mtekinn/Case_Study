from django.contrib.sitemaps import Sitemap, GenericSitemap
from django.urls import reverse
from myApp.models import Notes



class NotesSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Notes.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
    


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ['home', 'about', 'contact', 'login', 'register']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'notes': NotesSitemap,
    'static': StaticViewSitemap,
}

