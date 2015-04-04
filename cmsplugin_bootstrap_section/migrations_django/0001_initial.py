# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('css_classes', models.CharField(help_text='Add extra classes to bootstrap section. (Separate classes with space)', max_length=255, null=True, verbose_name='CSS Classes', blank=True)),
                ('container', models.BooleanField(default=True, help_text='Define bootstrap container inside section, if true.', verbose_name='Container')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
