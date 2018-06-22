
=============
Configuration
=============

This section contains information about how to configure your Django projects
to use *django-taggit-autocomplete-modified* and also contains a quick reference of the available
*settings* that can be used in order to customize the functionality of this
application.


Configuring your project
========================

In the Django project's ``settings`` module, add ``taggit_autocomplete_modified`` to the
``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'taggit_autocomplete_modified',
    )


Finally, edit the ``urls.py`` file of your project to add the
*django-taggit-autocomplete-modified* urls::

    # URLs for taggit_autocomplete_modified
    urlpatterns += patterns('',
        url(r'^taggit_autocomplete_modified/', include('taggit_autocomplete_modified.urls')),
    )

Modify your template/s
======================

Ensure that jQuery is linked to before the {{ form.media }} is rendered in your template/s

Reference of the application settings
=====================================

The following settings can be specified in the Django project's ``settings``
module to customize the functionality of *django-taggit-autocomplete-modified*.

``TAGGIT_AUTOCOMPLETE_TAG_MODEL``
    Define a custom Tag model. Accepts a string and the syntax is
    ``'app_label.model_calss'``. By default this is ``taggit.Tag``.
``TAGGIT_AUTOCOMPLETE_MEDIA_URL``
    Customize the location of the CSS and javascript files required for
    autocomplete operation. By default this is set to
    ``STATIC_URL/taggit_autocomplete_modified/``
    If this does not have a trailing forward slash, one will be automatically appended.
