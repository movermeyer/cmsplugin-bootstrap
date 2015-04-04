# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('cmsplugin_bootstrap_carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='css_classes',
            field=models.CharField(help_text='Add extra classes to bootstrap carousel. (Separate classes with space)', max_length=255, null=True, verbose_name='CSS Classes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carousel',
            name='effect',
            field=models.CharField(default=b'', choices=[(b'', b'slide'), (b'carousel-fade', b'fade')], max_length=20, blank=True, help_text='Transiction items effect.', verbose_name='Effect'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Image to carousel item.', null=True),
            preserve_default=True,
        ),
    ]
