django-livinglots
=================

The parent app for Living Lots, a suite of apps by `596 Acres
<http://596acres.org/>`_ for mapping and connecting people to the vacant land 
in their neighborhoods.


What?
-----

Vacant, unused lots exist in every city. We see those lots as an opportunity for
the people who live around them to start community-based projects such as play
areas, gardens, and general spaces for the neighborhood. `596 Acres
<http://596acres.org/>`_ started in Brooklyn, NY, USA, in 2011 to map these
spaces and help neighbors get in touch with each other and the owners to start
projects.

This `Django <http://djangoproject.com>`_ app, along with the `numerous other 
Living Lots apps in our repo <https://github.com/596acres>`_ form the basis of a 
website that maps vacant lots in a city and gives neighbors ways to post extra
information about each lot and start projects on them. These apps are informed
by our experience with making this kind of platform in `New York City, USA 
<http://596acres.org/>`_, 
`Philadelphia, PA, USA <http://groundedinphilly.org/>`_,
`New Orleans, LA, USA <http://livinglotsnola.org/>`_,
and `Los Angeles, CA, USA <http://laopenacres.org/>`_.


Sounds great! I want to do this for my city! How?
-------------------------------------------------

Glad you asked: you've come to the right place. You'll need someone technical
who can set this up and program the bits that inevitably will need to be
customized for wherever you are. Send them here.


Requirements
^^^^^^^^^^^^

You're going to need the following software to run Living Lots:

* `Django <http://djangoproject.com/>`_ (1.5+)
* `GeoDjango <http://geodjango.org/>`_ (included with Django as
  django.contrib.gis)
* A spatial database. Living Lots is tested and known to work with:

  * `PostgreSQL <http://www.postgresql.org/>`_ (9.1+)
  * `PostGIS <http://postgis.net/>`_ (1.5, has not been tested on 2+)

You will need to serve the Django project however you like. We use:

* `gunicorn <http://gunicorn.org/>`_
* `nginx <http://nginx.org/>`_
* `Supervisor <http://supervisord.org/>`_


Hosting
^^^^^^^

We have used and been very happy with `WebFaction
<https://www.webfaction.com/>`_'s shared accounts with 512 MB of RAM. The most
difficult part of finding a shared host is going to be finding support for
PostGIS. Any host with a spatial database that supports Django should work.


Developing your Django project based on Living Lots
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Okay, now that you have the software requirements and hosting figured out, you
can finally get started with making Living Lots for your city.

We recommend starting with `596acres/django-livinglots-template
<https://github.com/596acres/django-livinglots-template>`_ as a Django project
template. For details on starting a project from a template, see the `Django
documentation for django-admin.py
<https://docs.djangoproject.com/en/1.5/ref/django-admin/#startproject-projectname-destination>`_.
(This template, as is the case with the rest of the Living Lots apps, will be 
undergoing changes as we develop Living Lots NOLA, so please be patient.)

From here, you will want to set up a CMS for the content outside of Living Lots.
We use and recommend `FeinCMS 
<http://feincms-django-cms.readthedocs.org/en/latest/>`_ (as is included in the 
project template), but it is not required.

Next, create concrete models. The abstract models are defined in Living Lots
apps such as `django-livinglots-lots
<https://github.com/596acres/django-livinglots-lots>`_. See `livinglots-nola
<https://github.com/596acres/livinglots-nola>`_ for some examples of how this 
works. As you add concrete models, don't forget to define them in your settings
so Living Lots apps can find them.


Development
-----------


Status
^^^^^^

This incarnation of 596 Acres' software is under active development as we work
on `Living Lots NYC <http://livinglotsnyc.org/>`_. Follow along at
`596acres/livinglots-nyc <https://github.com/596acres/livinglots-nyc`_. All
of our Living Lots apps are relatively new but are considered stable enough for
production use.


Organization
^^^^^^^^^^^^

This is the parent app, which ties together the other Living Lots apps. The
intention with the other apps is to make them small and focused. These vary
between apps that provide models (such as `usercontent
<https://github.com/596acres/django-livinglots-usercontent>`_ or `lots
<https://github.com/596acres/django-livinglots-lots>`_) and apps that provide
general utility functions or mixins (eg, `genericviews
<https://github.com/596acres/django-livinglots-genericviews>`_ and `notify
<https://github.com/596acres/django-livinglots-notify>`_).

If an app provides models, unless those models are very generic and unlikely to
be modified, we prefer to make those models abstract and prepend their name with
``Base``. Similarly with views. As you can see in the `Living Lots template
<https://github.com/596acres/django-livinglots-template>`_,
it's then a relatively simple matter to create concrete models and add custom
fields to them in your project.

All apps are versioned using `semver <http://semver.org/>`_. A few of the apps
are currently in `pypi <https://pypi.python.org/pypi>`_, but the current 
preferred way of using them is via their github repositories, for now. All apps'
names start with ``django-livinglots-``.

Here's a current list of apps:

* `django-livinglots-forms <https://github.com/596acres/django-livinglots-forms>`_
* `django-livinglots-generictags <https://github.com/596acres/django-livinglots-generictags>`_
* `django-livinglots-genericviews <https://github.com/596acres/django-livinglots-genericviews>`_
* `django-livinglots-groundtruth <https://github.com/596acres/django-livinglots-groundtruth>`_
* `django-livinglots-lots <https://github.com/596acres/django-livinglots-lots>`_
* `django-livinglots-mailsender <https://github.com/596acres/django-livinglots-mailsender>`_
* `django-livinglots-notify <https://github.com/596acres/django-livinglots-notify>`_
* `django-livinglots-organize <https://github.com/596acres/django-livinglots-organize>`_
* `django-livinglots-owners <https://github.com/596acres/django-livinglots-owners>`_
* `django-livinglots-pathways <https://github.com/596acres/django-livinglots-pathways>`_
* `django-livinglots-steward <https://github.com/596acres/django-livinglots-steward>`_
* `django-livinglots-usercontent <https://github.com/596acres/django-livinglots-usercontent>`_


Code History
^^^^^^^^^^^^

You can find the code for the original 596 Acres site, still in use, at
`ebrelsford/596acres <https://github.com/ebrelsford/596acres>`_.

In early 2013, the site in Philadelphia was created. That repo is at
`ebrelsford/v2v <https://github.com/ebrelsford/v2v>`_. The Living Lots apps are
largely based on the Philadelphia code.


License
-------

django-livinglots is released under the `BSD license
<http://opensource.org/licenses/BSD-3-Clause>`_.
