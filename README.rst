================
deform_select2
================

``deform_select2`` provides select2 <http://ivaynberg.github.com/select2/> based widgets for deform

How to use it
=============

In your Paste Deploy configuration file (e.g. ``development.ini``) add
``deform_select2`` to the list of ``pyramid_includes``, or add a
this line if a ``pyramid.includes`` setting does not exist::

  [app:main]
  ...
  pyramid.includes = deform_select2

This will put the templates in ``deform_select2/templates`` into the
`deform search path
<http://docs.pylonsproject.org/projects/deform/en/latest/templates.html>`_.
