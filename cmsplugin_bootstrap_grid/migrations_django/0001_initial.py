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
                ('size_xs', models.CharField(default=None, choices=[(b'1', b'col-xs-1'), (b'2', b'col-xs-2'), (b'3', b'col-xs-3'), (b'4', b'col-xs-4'), (b'5', b'col-xs-5'), (b'6', b'col-xs-6'), (b'7', b'col-xs-7'), (b'8', b'col-xs-8'), (b'9', b'col-xs-9'), (b'10', b'col-xs-10'), (b'11', b'col-xs-11'), (b'12', b'col-xs-12')], max_length=50, blank=True, help_text='Extra small devices Phones (<768px)', null=True, verbose_name='Size xs')),
                ('size_sm', models.CharField(default=None, choices=[(b'1', b'col-sm-1'), (b'2', b'col-sm-2'), (b'3', b'col-sm-3'), (b'4', b'col-sm-4'), (b'5', b'col-sm-5'), (b'6', b'col-sm-6'), (b'7', b'col-sm-7'), (b'8', b'col-sm-8'), (b'9', b'col-sm-9'), (b'10', b'col-sm-10'), (b'11', b'col-sm-11'), (b'12', b'col-sm-12')], max_length=50, blank=True, help_text='Small devices Tablets (\u2265768px)', null=True, verbose_name='Size sm')),
                ('size_md', models.CharField(default=None, choices=[(b'1', b'col-md-1'), (b'2', b'col-md-2'), (b'3', b'col-md-3'), (b'4', b'col-md-4'), (b'5', b'col-md-5'), (b'6', b'col-md-6'), (b'7', b'col-md-7'), (b'8', b'col-md-8'), (b'9', b'col-md-9'), (b'10', b'col-md-10'), (b'11', b'col-md-11'), (b'12', b'col-md-12')], max_length=50, blank=True, help_text='Medium devices Desktops (\u2265992px)', null=True, verbose_name='Size md')),
                ('size_lg', models.CharField(default=None, choices=[(b'1', b'col-lg-1'), (b'2', b'col-lg-2'), (b'3', b'col-lg-3'), (b'4', b'col-lg-4'), (b'5', b'col-lg-5'), (b'6', b'col-lg-6'), (b'7', b'col-lg-7'), (b'8', b'col-lg-8'), (b'9', b'col-lg-9'), (b'10', b'col-lg-10'), (b'11', b'col-lg-11'), (b'12', b'col-lg-12')], max_length=50, blank=True, help_text='Large devices Desktops (\u22651200px)', null=True, verbose_name='Size lg')),
                ('size_offset_xs', models.CharField(default=None, choices=[(b'0', b'col-xs-offset-0'), (b'1', b'col-xs-offset-1'), (b'2', b'col-xs-offset-2'), (b'3', b'col-xs-offset-3'), (b'4', b'col-xs-offset-4'), (b'5', b'col-xs-offset-5'), (b'6', b'col-xs-offset-6'), (b'7', b'col-xs-offset-7'), (b'8', b'col-xs-offset-8'), (b'9', b'col-xs-offset-9'), (b'10', b'col-xs-offset-10'), (b'11', b'col-xs-offset-11'), (b'12', b'col-xs-offset-12')], max_length=50, blank=True, help_text='Extra small devices Phones (<768px)', null=True, verbose_name='Offset xs')),
                ('size_offset_sm', models.CharField(default=None, choices=[(b'0', b'col-sm-offset-0'), (b'1', b'col-sm-offset-1'), (b'2', b'col-sm-offset-2'), (b'3', b'col-sm-offset-3'), (b'4', b'col-sm-offset-4'), (b'5', b'col-sm-offset-5'), (b'6', b'col-sm-offset-6'), (b'7', b'col-sm-offset-7'), (b'8', b'col-sm-offset-8'), (b'9', b'col-sm-offset-9'), (b'10', b'col-sm-offset-10'), (b'11', b'col-sm-offset-11'), (b'12', b'col-sm-offset-12')], max_length=50, blank=True, help_text='Small devices Tablets (\u2265768px)', null=True, verbose_name='Offset sm')),
                ('size_offset_md', models.CharField(default=None, choices=[(b'0', b'col-md-offset-0'), (b'1', b'col-md-offset-1'), (b'2', b'col-md-offset-2'), (b'3', b'col-md-offset-3'), (b'4', b'col-md-offset-4'), (b'5', b'col-md-offset-5'), (b'6', b'col-md-offset-6'), (b'7', b'col-md-offset-7'), (b'8', b'col-md-offset-8'), (b'9', b'col-md-offset-9'), (b'10', b'col-md-offset-10'), (b'11', b'col-md-offset-11'), (b'12', b'col-md-offset-12')], max_length=50, blank=True, help_text='Medium devices Desktops (\u2265992px)', null=True, verbose_name='Offset md')),
                ('size_offset_lg', models.CharField(default=None, choices=[(b'0', b'col-lg-offset-0'), (b'1', b'col-lg-offset-1'), (b'2', b'col-lg-offset-2'), (b'3', b'col-lg-offset-3'), (b'4', b'col-lg-offset-4'), (b'5', b'col-lg-offset-5'), (b'6', b'col-lg-offset-6'), (b'7', b'col-lg-offset-7'), (b'8', b'col-lg-offset-8'), (b'9', b'col-lg-offset-9'), (b'10', b'col-lg-offset-10'), (b'11', b'col-lg-offset-11'), (b'12', b'col-lg-offset-12')], max_length=50, blank=True, help_text='Large devices Desktops (\u22651200px)', null=True, verbose_name='Offset lg')),
                ('css_classes', models.CharField(help_text='Add extra classes to bootstrap column. (Separate classes with space)', max_length=200, verbose_name='css classes', blank=True)),
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
                ('css_classes', models.CharField(help_text='Add extra classes to bootstrap row. (Separate classes with space)', max_length=200, verbose_name='css classes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
