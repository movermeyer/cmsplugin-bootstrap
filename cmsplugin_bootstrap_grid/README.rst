CMSPlugin for Bootstrap Section
===============================

A plugin for creating and managing the component ``bootstrap-grid`` in djangoCMS.

`Bootstrap Grid <http://getbootstrap.com/css/#grid>`_
-----------------------------------------------------

Bootstrap includes a responsive, mobile first fluid grid system that appropriately scales up to 12 columns as the device or viewport size increases.

Quick start
-----------

1. Add ``cmsplugin_bootstrap_grid`` to your ``INSTALLED_APPS`` setting like this::

    INSTALLED_APPS = (
        ...

        # Bootstrap plugins
        'cmsplugin_bootstrap',
        'cmsplugin_bootstrap_grid',
    )

2. Define migrations modules. (Only django >= 1.7)::

    MIGRATION_MODULES = {
        ...

        'cmsplugin_bootstrap': 'cmsplugin_bootstrap.migrations_django',

        # uncomment the plugins you want
        # 'cmspligin_bootstrap_grid': 'cmspligin_bootstrap_grid.migrations_django',
    }

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server ``python manage.py runserver`` and visit http://localhost:8000/
   to be happy :).
