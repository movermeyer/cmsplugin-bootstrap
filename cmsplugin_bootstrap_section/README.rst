CMSPlugin for Bootstrap Section
===============================

A plugin for creating and managing the component ``bootstrap-section`` in djangoCMS.

Quick start
-----------

1. Add ``cmsplugin_bootstrap_carousel`` to your ``INSTALLED_APPS`` setting like this::

    INSTALLED_APPS = (
        ...

        # Bootstrap plugins
        'cmsplugin_bootstrap',
        'cmsplugin_bootstrap_section',
    )

2. Define migrations modules. (Only django >= 1.7)::

    MIGRATION_MODULES = {
        ...

        'cmsplugin_bootstrap': 'cmsplugin_bootstrap.migrations_django',

        # uncomment the plugins you want
        # 'cmspligin_bootstrap_section': 'cmspligin_bootstrap_section.migrations_django',
    }

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server ``python manage.py runserver`` and visit http://localhost:8000/
   to be happy :).
