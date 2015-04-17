.. image:: https://travis-ci.org/arkanister/cmsplugin-bootstrap.svg?branch=master
    :target: https://travis-ci.org/arkanister/cmsplugin-bootstrap

.. image:: https://pypip.in/v/cmsplugin-bootstrap/badge.png
   :target: https://pypi.python.org/pypi/cmsplugin-bootstrap

.. image:: https://pypip.in/d/cmsplugin-bootstrap/badge.png
   :target: https://pypi.python.org/pypi/cmsplugin-bootstrap
   
.. image:: https://badge.waffle.io/arkanister/cmsplugin-bootstrap.svg?label=ready&title=Ready
   :target: https://waffle.io/arkanister/cmsplugin-bootstrap
   :alt: 'Stories in Ready' 

DjangoCMS Plugins for Bootstrap
===============================

A plugin for creating and managing the component `bootstrap` in djangoCMS.

`Bootstrap <http://getbootstrap.com/>`_
---------------------------------------

Bootstrap is the most popular HTML, CSS, and JS framework for developing responsive, mobile first projects on the web.

Features
--------

- `Carousel <https://github.com/arkanister/cmsplugin-bootstrap/tree/master/cmsplugin_bootstrap_carousel>`_
- `Grid <https://github.com/arkanister/cmsplugin-bootstrap/tree/master/cmsplugin_bootstrap_grid>`_
- `Section <https://github.com/arkanister/cmsplugin-bootstrap/tree/master/cmsplugin_bootstrap_section>`_

Quick start
-----------

1. Add ``cmsplugin_bootstrap`` to your INSTALLED_APPS and all the plugins you want, setting like this::

    INSTALLED_APPS = (
        ...

        'cmsplugin_bootstrap',

        # uncomment the plugins you want
        # 'cmspligin_bootstrap_carousel',
        # 'cmspligin_bootstrap_grid',
        # 'cmspligin_bootstrap_section',
    )

2. Define migrations modules. (Only django >= 1.7)::

    MIGRATION_MODULES = {
        ...

        'cmsplugin_bootstrap': 'cmsplugin_bootstrap.migrations_django',

        # uncomment the plugins you want
        # 'cmspligin_bootstrap_carousel': 'cmsplugin_bootstrap.migrations_django',
        # 'cmspligin_bootstrap_grid': 'cmspligin_bootstrap_grid.migrations_django',
        # 'cmspligin_bootstrap_section': 'cmspligin_bootstrap_section.migrations_django',
    }

3. Run ``python manage.py migrate`` or ``python manage.py syncdb``.

4. Start the development server ``python manage.py runserver`` and visit http://localhost:8000/
   to be happy :).
