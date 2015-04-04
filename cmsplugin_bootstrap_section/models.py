# coding: utf-8
from django.db import models
from django.utils.translation import ugettext as _

from cms.models.pluginmodel import CMSPlugin
from cmsplugin_bootstrap.utils import AttributeDict, join_classes as join, split_classes as split


YES_NO_OPTIONS = {True: _("Yes"), False: _("No")}


class Section(CMSPlugin):

    css_classes = models.CharField(
        _('CSS Classes'), max_length=255, null=True, blank=True,
        help_text=_("Add extra classes to bootstrap section. (Separate classes with space)"))

    container = models.BooleanField(
        _('Container'),
        help_text=_("Define bootstrap container inside section, if true."),
        default=True)

    def _get_attrs_dict(self):
        return AttributeDict({
            "id": self.id_for_html_prop,
            "class": join(['section'], *split(self.css_classes))
        })
    attrs = property(_get_attrs_dict)

    def _get_id_for_html_prop(self):
        return "id_section-%d" % self.id
    id_for_html_prop = property(_get_id_for_html_prop)

    def __unicode__(self):
        return _('Container: %s' % (YES_NO_OPTIONS[self.container]))

