from django.forms.utils import flatatt
from django.template.base import Node, TemplateSyntaxError, Library
from django.utils.html import format_html


register = Library()


class ImageNode(Node):
    def __init__(self, image):
        self.image = image

    def render(self, context):
        image = self.image.resolve(context)

        attrs = {
            "alt": getattr(image, "alt", ""),
            "title": getattr(image, "caption", ""),
            "src": getattr(image, "url")
        }

        if hasattr(image, "id"):
            attrs["id"] = "id_image-%d" % image.id

        return format_html("<img{0}/>", flatatt(attrs))


@register.tag(name="render_image")
def do_render_image(parser, token):
    """
    Render the image field

    Basic tag Syntax::

        >>> {% render_image image %}
    """
    args = token.split_contents()
    tag = args.pop(0)

    if len(args) < 1:
        raise TemplateSyntaxError("The tag '%s' require image" % tag)

    image = parser.compile_filter(args.pop(0))
    return ImageNode(image)