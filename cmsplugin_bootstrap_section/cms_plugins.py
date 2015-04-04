# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_bootstrap_section.models import Section
from django.utils.translation import ugettext as _


class BootstrapSectionPlugin(CMSPluginBase):
    model = Section
    name = _('Section')
    module = _('Bootstrap')
    allow_children = True
    render_template = 'cmsplugin_bootstrap_section/section.html'

    def render(self, context, instance, placeholder):
        context.update({'section': instance})
        return context


plugin_pool.register_plugin(BootstrapSectionPlugin)