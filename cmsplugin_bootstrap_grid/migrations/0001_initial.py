# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('size_xs', models.CharField(default=None, choices=[(b'1', b'col-xs-1'), (b'2', b'col-xs-2'), (b'3', b'col-xs-3'), (b'4', b'col-xs-4'), (b'5', b'col-xs-5'), (b'6', b'col-xs-6'), (b'7', b'col-xs-7'), (b'8', b'col-xs-8'), (b'9', b'col-xs-9'), (b'10', b'col-xs-10'), (b'11', b'col-xs-11'), (b'12', b'col-xs-12')], max_length=50, blank=True, null=True, verbose_name='size xs')),
                ('size_sm', models.CharField(default=None, choices=[(b'1', b'col-sm-1'), (b'2', b'col-sm-2'), (b'3', b'col-sm-3'), (b'4', b'col-sm-4'), (b'5', b'col-sm-5'), (b'6', b'col-sm-6'), (b'7', b'col-sm-7'), (b'8', b'col-sm-8'), (b'9', b'col-sm-9'), (b'10', b'col-sm-10'), (b'11', b'col-sm-11'), (b'12', b'col-sm-12')], max_length=50, blank=True, null=True, verbose_name='size sm')),
                ('size_md', models.CharField(default=None, choices=[(b'1', b'col-md-1'), (b'2', b'col-md-2'), (b'3', b'col-md-3'), (b'4', b'col-md-4'), (b'5', b'col-md-5'), (b'6', b'col-md-6'), (b'7', b'col-md-7'), (b'8', b'col-md-8'), (b'9', b'col-md-9'), (b'10', b'col-md-10'), (b'11', b'col-md-11'), (b'12', b'col-md-12')], max_length=50, blank=True, null=True, verbose_name='size md')),
                ('size_lg', models.CharField(default=None, choices=[(b'1', b'col-lg-1'), (b'2', b'col-lg-2'), (b'3', b'col-lg-3'), (b'4', b'col-lg-4'), (b'5', b'col-lg-5'), (b'6', b'col-lg-6'), (b'7', b'col-lg-7'), (b'8', b'col-lg-8'), (b'9', b'col-lg-9'), (b'10', b'col-lg-10'), (b'11', b'col-lg-11'), (b'12', b'col-lg-12')], max_length=50, blank=True, null=True, verbose_name='size lg')),
                ('size_offset_xs', models.CharField(default=None, choices=[(b'1', b'col-xs-1'), (b'2', b'col-xs-2'), (b'3', b'col-xs-3'), (b'4', b'col-xs-4'), (b'5', b'col-xs-5'), (b'6', b'col-xs-6'), (b'7', b'col-xs-7'), (b'8', b'col-xs-8'), (b'9', b'col-xs-9'), (b'10', b'col-xs-10'), (b'11', b'col-xs-11'), (b'12', b'col-xs-12')], max_length=50, blank=True, null=True, verbose_name='offset xs')),
                ('size_offset_sm', models.CharField(default=None, choices=[(b'1', b'col-sm-1'), (b'2', b'col-sm-2'), (b'3', b'col-sm-3'), (b'4', b'col-sm-4'), (b'5', b'col-sm-5'), (b'6', b'col-sm-6'), (b'7', b'col-sm-7'), (b'8', b'col-sm-8'), (b'9', b'col-sm-9'), (b'10', b'col-sm-10'), (b'11', b'col-sm-11'), (b'12', b'col-sm-12')], max_length=50, blank=True, null=True, verbose_name='offset sm')),
                ('size_offset_md', models.CharField(default=None, choices=[(b'1', b'col-md-1'), (b'2', b'col-md-2'), (b'3', b'col-md-3'), (b'4', b'col-md-4'), (b'5', b'col-md-5'), (b'6', b'col-md-6'), (b'7', b'col-md-7'), (b'8', b'col-md-8'), (b'9', b'col-md-9'), (b'10', b'col-md-10'), (b'11', b'col-md-11'), (b'12', b'col-md-12')], max_length=50, blank=True, null=True, verbose_name='offset md')),
                ('size_offset_lg', models.CharField(default=None, choices=[(b'1', b'col-lg-1'), (b'2', b'col-lg-2'), (b'3', b'col-lg-3'), (b'4', b'col-lg-4'), (b'5', b'col-lg-5'), (b'6', b'col-lg-6'), (b'7', b'col-lg-7'), (b'8', b'col-lg-8'), (b'9', b'col-lg-9'), (b'10', b'col-lg-10'), (b'11', b'col-lg-11'), (b'12', b'col-lg-12')], max_length=50, blank=True, null=True, verbose_name='offset lg')),
                ('css_classes', models.CharField(max_length=200, verbose_name='css classes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('css_classes', models.CharField(max_length=200, verbose_name='css classes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
