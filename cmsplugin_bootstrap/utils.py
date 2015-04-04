# coding: utf-8
from django.utils import six
from django.utils.html import escape
from django.utils.safestring import mark_safe


def split_classes(classes, separator=' '):
    return classes.split(separator) if not classes in ('', None) else []


def join_classes(iterable, *args):
    iterable += args
    return ' '.join(iterable)


class AttributeDict(dict):
    """
    A wrapper around `dict` that knows how to render itself as HTML
    style tag attributes.

    The returned string is marked safe, so it can be used safely in a template.
    See `.as_html` for a usage example.
    """

    def __str__(self):
        return self.as_html()

    def as_html(self):
        """
        Render to HTML tag attributes.

        Example:

        .. code-block:: python

            >>> from cmsplugin_bootstrap_carousel.utils import AttributeDict
            >>> attrs = AttributeDict({'class': 'mytable', 'id': 'someid'})
            >>> attrs.as_html()
            'class="mytable" id="someid"'

        :rtype: `~django.utils.safestring.SafeUnicode` object

        """
        return mark_safe(' '.join(['%s="%s"' % (k, escape(v if not callable(v) else v()))
                                   for k, v in six.iteritems(self)]))