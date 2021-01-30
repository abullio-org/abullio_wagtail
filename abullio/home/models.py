from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from blog.models import BlogPage


class HomePage(Page):
    brand_img = models.CharField(max_length=250,default='no_upload.png')
    sub_title = models.CharField(max_length=250, default="Sub Title")
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('brand_img'),
        FieldPanel('sub_title'),
        FieldPanel('body', classname="full"),
    ]
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        sectionpages = HomePageSection.objects.live().order_by('sec_order')
        latestblog = BlogPage.objects.live().order_by('-first_published_at')[:3]
        context['sectionpages'] = sectionpages
        context['latestblog'] = latestblog
        return context

class HomePageSection(Page):
    bg_image = models.CharField(max_length=250)
    bg_HEX = models.CharField(max_length=10)
    intro = models.CharField(max_length=250)
    snap = RichTextField(blank=True)
    body = RichTextField(blank=True)
    sec_order = models.IntegerField()
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('sec_order'),
            FieldPanel('bg_image'),
            FieldPanel('bg_HEX'),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('snap'),
        FieldPanel('body'),
    ]