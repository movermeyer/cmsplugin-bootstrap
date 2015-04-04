.. image:: https://travis-ci.org/arkanister/cmsplugin-bootstrap-carousel.svg?branch=master
    :target: https://travis-ci.org/arkanister/cmsplugin-bootstrap-carousel

CMSPlugin for Bootstrap Carousel
================================

A plugin for creating and managing the component `bootstrap-carousel` in djangoCMS.

`Bootstrap Carousel <http://getbootstrap.com/javascript/#carousel>`_
------------------------------------------------------------------

A slideshow component for cycling through elements, like a carousel. **Nested carousels are not supported.**

Quick start
-----------

1. Add "cmsplugin_bootstrap_carousel" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'cmsplugin_bootstrap_carousel',
    )

2. Run `python manage.py migrate` to create the polls models.

3. Start the development server and visit http://127.0.0.1:8000/
   to create a carousel.
