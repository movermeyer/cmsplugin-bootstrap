# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_bootstrap_carousel.models import Carousel, CarouselItem
from django.utils.translation import ugettext as _


class BootstrapCarouselPlugin(CMSPluginBase):
    model = Carousel
    name = _('Carousel')
    module = _('Bootstrap')
    allow_children = True
    child_classes = ['BootstrapCarouselItemPlugin']
    render_template = 'cmsplugin_bootstrap_carousel/carousel.html'

    def render(self, context, instance, placeholder):
        context.update({'carousel': instance})
        return context


class BootstrapCarouselItemPlugin(CMSPluginBase):
    model = CarouselItem
    name = _('Item')
    module = _('Carousel')
    allow_children = True
    require_parent = True
    render_template = 'cmsplugin_bootstrap_carousel/item.html'

    def render(self, context, instance, placeholder):
        context.update({'item': instance})
        return context


plugin_pool.register_plugin(BootstrapCarouselPlugin)
plugin_pool.register_plugin(BootstrapCarouselItemPlugin)