# coding: utf-8
from cmsplugin_bootstrap_grid.models import Column
from django import forms
from django.utils.translation import ugettext as _


class ColumnPluginForm(forms.ModelForm):
    class Meta:
        model = Column
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')

    def clean(self):
        cleaned_data = super(ColumnPluginForm, self).clean()
        sizes = [cleaned_data.get('size_xs'), cleaned_data.get('size_sm'),
                 cleaned_data.get('size_md'), cleaned_data.get('size_lg')]

        if not any(sizes):
            raise forms.ValidationError(_("Choose at least one size before saving!"))

        return cleaned_data