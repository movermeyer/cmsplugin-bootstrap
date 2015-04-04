# coding: utf-8
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext as _
from cmsplugin_bootstrap.utils import join_classes as join, split_classes as split, AttributeDict
from filer.fields.image import FilerImageField as ImageField

YES_NO_OPTIONS = {True: _('Yes'), False: _('No')}


class Carousel(CMSPlugin):

    effect = models.CharField(
        _('Effect'), max_length=20,
        help_text=_("Transiction items effect."),
        choices=(("", "slide"), ("carousel-fade", "fade")),
        default="", blank=True)

    interval = models.IntegerField(
        help_text=_(
            "The amount of time in milliseconds to delay cycling items. "
            "If zero carousel will not automatically cycle."),
        default=5000)

    css_classes = models.CharField(
        _('CSS Classes'), max_length=255, null=True, blank=True,
        help_text=_("Add extra classes to bootstrap carousel. (Separate classes with space)"))

    show_controls = models.BooleanField(
        _('Show controls'),
        help_text=_("Display carousel controls, if true."),
        default=True)

    show_indicator = models.BooleanField(
        _('Show indicator'),
        help_text=_("Display slide indicator, if true."),
        default=True)

    def _get_attrs_dict(self):
        return AttributeDict({
            "id": self.id_for_html_prop,
            "data-interval": self.interval,
            "data-ride": "carousel",
            "class": join(['carousel', 'slide', self.effect], *split(self.css_classes))
        })
    attrs = property(_get_attrs_dict)

    def _get_id_for_html_prop(self):
        return "id_carousel-%d" % self.id
    id_for_html_prop = property(_get_id_for_html_prop)

    def __unicode__(self):
        return _('Interval: %dms, Show Controls: %s, Show Indicator: %s' % (
            self.interval,
            YES_NO_OPTIONS[self.show_controls],
            YES_NO_OPTIONS[self.show_indicator]
        ))


class CarouselItem(CMSPlugin):

    image = ImageField(
        blank=True, null=True,
        help_text=_("Image to carousel item."))

    def _get_id_for_html_prop(self):
        return "id_carousel_item-%d" % self.instance.id
    id_for_html_prop = property(_get_id_for_html_prop)

    def __unicode__(self):
        return "%02d" % (self.position + 1)