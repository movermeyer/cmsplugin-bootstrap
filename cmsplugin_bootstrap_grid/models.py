# coding: utf-8
from cms.models import CMSPlugin
from cmsplugin_bootstrap_grid.utils import HtmlAttributeDict
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

CONFIG = {'COLUMNS': 12}
CONFIG.update(getattr(settings, 'CMSPLUGIN_GRID_CONFIG', {}))

SIZE_XS_CHOICES = [('%s' % i, 'col-xs-%s' % i) for i in range(1, CONFIG['COLUMNS'] + 1)]
SIZE_SM_CHOICES = [('%s' % i, 'col-sm-%s' % i) for i in range(1, CONFIG['COLUMNS'] + 1)]
SIZE_MD_CHOICES = [('%s' % i, 'col-md-%s' % i) for i in range(1, CONFIG['COLUMNS'] + 1)]
SIZE_LG_CHOICES = [('%s' % i, 'col-lg-%s' % i) for i in range(1, CONFIG['COLUMNS'] + 1)]

SIZE_XS_OFFSET_CHOICES = [('%s' % i, 'col-xs-offset-%s' % i) for i in range(0, CONFIG['COLUMNS'] + 1)]
SIZE_SM_OFFSET_CHOICES = [('%s' % i, 'col-sm-offset-%s' % i) for i in range(0, CONFIG['COLUMNS'] + 1)]
SIZE_MD_OFFSET_CHOICES = [('%s' % i, 'col-md-offset-%s' % i) for i in range(0, CONFIG['COLUMNS'] + 1)]
SIZE_LG_OFFSET_CHOICES = [('%s' % i, 'col-lg-offset-%s' % i) for i in range(0, CONFIG['COLUMNS'] + 1)]


class Row(CMSPlugin):
    css_classes = models.CharField(
        _('css classes'), max_length=200, blank=True,
        help_text=_("Add extra classes to bootstrap row. (Separate classes with space)"))

    def _get_attrs(self):
        if not hasattr(self, '_cached_attrs'):
            self._cached_attrs = HtmlAttributeDict({"class": "row"})
            self._cached_attrs.add_class(self.css_classes)
        return self._cached_attrs
    attrs = property(_get_attrs)

    def __unicode__(self):
        return ''


class Column(CMSPlugin):
    size_xs = models.CharField(
        _('Size xs'), choices=SIZE_XS_CHOICES,
        default=None, max_length=50, null=True, blank=True,
        help_text=_("Extra small devices Phones (<768px)"))

    size_sm = models.CharField(
        _('Size sm'), choices=SIZE_SM_CHOICES,
        default=None, max_length=50, null=True, blank=True,
        help_text=_("Small devices Tablets (≥768px)"))

    size_md = models.CharField(
        _('Size md'), choices=SIZE_MD_CHOICES,
        default=None, max_length=50, null=True, blank=True,
        help_text=_("Medium devices Desktops (≥992px)"))

    size_lg = models.CharField(
        _('Size lg'), choices=SIZE_LG_CHOICES,
        default=None, max_length=50, null=True, blank=True,
        help_text=_("Large devices Desktops (≥1200px)"))

    size_offset_xs = models.CharField(
        _('Offset xs'), choices=SIZE_XS_OFFSET_CHOICES,
        default=None, max_length=50, null=True, blank=True,
        help_text=_("Extra small devices Phones (<768px)"))

    size_offset_sm = models.CharField(
        _('Offset sm'), choices=SIZE_SM_OFFSET_CHOICES,
        default=None, max_length=50, null=True, blank=True,
        help_text=_("Small devices Tablets (≥768px)"))

    size_offset_md = models.CharField(
        _('Offset md'), choices=SIZE_MD_OFFSET_CHOICES,
        default=None, max_length=50, null=True, blank=True,
        help_text=_("Medium devices Desktops (≥992px)"))

    size_offset_lg = models.CharField(
        _('Offset lg'), choices=SIZE_LG_OFFSET_CHOICES,
        default=None, max_length=50, null=True, blank=True,
        help_text=_("Large devices Desktops (≥1200px)"))

    css_classes = models.CharField(
        _('css classes'), max_length=200, blank=True,
        help_text=_("Add extra classes to bootstrap column. (Separate classes with space)"))

    def _get_attrs(self):
        if not hasattr(self, '_cached_attrs'):
            self._cached_attrs = HtmlAttributeDict()
            self._cached_attrs.add_class(self.css_classes)
            self._cached_attrs.add_class(self.get_size_xs_display())
            self._cached_attrs.add_class(self.get_size_sm_display())
            self._cached_attrs.add_class(self.get_size_md_display())
            self._cached_attrs.add_class(self.get_size_lg_display())
            self._cached_attrs.add_class(self.get_size_offset_xs_display())
            self._cached_attrs.add_class(self.get_size_offset_sm_display())
            self._cached_attrs.add_class(self.get_size_offset_md_display())
            self._cached_attrs.add_class(self.get_size_offset_lg_display())
        return self._cached_attrs
    attrs = property(_get_attrs)

    def __unicode__(self):
        return self.attrs['class']