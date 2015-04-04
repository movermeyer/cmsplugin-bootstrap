# coding: utf-8
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cmsplugin_bootstrap_grid.forms import ColumnPluginForm
from cmsplugin_bootstrap_grid.models import Row, Column
from django.utils.translation import ugettext_lazy as _


class BootstrapRowPlugin(CMSPluginBase):
    model = Row
    name = _('Row')
    module = _('Bootstrap')
    render_template = 'cmsplugin_bootstrap_grid/row.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'row': instance, 'placeholder': placeholder})
        return context


class BootstrapColumnPlugin(CMSPluginBase):
    model = Column
    name = _('Column')
    module = _('Bootstrap')
    render_template = 'cmsplugin_bootstrap_grid/column.html'
    allow_children = True
    form = ColumnPluginForm

    def render(self, context, instance, placeholder):
        context.update({'column': instance, 'placeholder': placeholder})
        return context


# register plugins
plugin_pool.register_plugin(BootstrapRowPlugin)
plugin_pool.register_plugin(BootstrapColumnPlugin)
