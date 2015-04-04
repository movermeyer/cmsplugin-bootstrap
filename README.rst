.. image:: https://travis-ci.org/arkanister/cmsplugin-bootstrap.svg?branch=master
    :target: https://travis-ci.org/arkanister/cmsplugin-bootstrap

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

1. Add "cmsplugin_bootstrap_carousel" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...

        'cmsplugin_bootstrap',

        # Uncomment plugins
        # 'cmspligin_bootstrap_carousel',
        # 'cmspligin_bootstrap_grid',
        # 'cmspligin_bootstrap_section',
    )

2. Define migrations modules. (Only django >= 1.7)

    MIGRATION_MODULES = {
        ...

        'cmsplugin_bootstrap': 'cmsplugin_bootstrap.migrations_django',

        # Uncomment plugins
        # 'cmspligin_bootstrap_carousel': 'cmsplugin_bootstrap.migrations_django',
        # 'cmspligin_bootstrap_grid': 'cmspligin_bootstrap_grid.migrations_django',
        # 'cmspligin_bootstrap_section': 'cmspligin_bootstrap_section.migrations_django',
    }

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/
   to be happy :).
