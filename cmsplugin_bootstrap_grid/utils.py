# coding: utf-8
from django.utils import six
from django.utils.encoding import force_str
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.core.validators import EMPTY_VALUES


class HtmlAttributeDict(dict):
    """
    Classe que prove a renderização de attributos html.
    """

    attribute_template = '%s="%s"'

    def __init__(self, *args, **kwargs):
        super(HtmlAttributeDict, self).__init__(*args, **kwargs)
        # get all css classes defined
        html_class = self.get('class')
        self._cached_class = html_class.split(' ') if html_class is not None else []

    def _update_class(self):
        self['class'] = ' '.join(self._cached_class)

    def add_class(self, name):
        """
        Add a new css class in dict
        :param name: class name to add.
        """
        if name is not None and not self.has_class(name):
            self._cached_class.append(name)
            self._update_class()

    def remove_class(self, name):
        """
        Remove a css class of the dict
        :param name: class name to remove.
        """
        if self.has_class(name):
            self._cached_class.remove(name)
            self._update_class()

    def has_class(self, name):
        """
        Check if exists class
        :param name: class name to check.
        """
        return name in self._cached_class

    def attr(self, name, value=None):
        """
        A smart method to get and set attr in `AttributeDict`.
        :param name: attribute name.
        :param value: attribute value.
        """
        name = force_str(name)
        if value is None:
            return self.get(name, None)
        elif name == 'class':
            self.add_class(value)
        else:
            self[name] = value

    def has_attr(self, name):
        """
        Check if exists attr
        :param name: class name to check.
        """
        return name in self and not self[name] in EMPTY_VALUES

    def as_html(self):
        """
        Render to HTML tag attributes.

        Example:

        .. code-block:: python

            >>> from cmsplugin_bootstrap_grid.utils import HtmlAttributeDict
            >>> attrs = HtmlAttributeDict({'class': 'mytable', 'id': 'someid'})
            >>> attrs.as_html()
            'class="mytable" id="someid"'

        :rtype: `~django.utils.safestring.SafeUnicode` object

        """
        return mark_safe(" ".join([
            self.attribute_template % (k, escape(v if not callable(v) else v()))
            for k, v in six.iteritems(self) if not v in EMPTY_VALUES]))

    def update(self, kwargs):
        for key, value in kwargs.items():
            self.attr(key, value)
        return self

    def __str__(self):
        return self.as_html()

    def __repr__(self):
        return "<AttributeDict: %s>" % str(self)