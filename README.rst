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
<http://596acres.org/>`_, and `Philadelphia, PA, USA 
<http://groundedinphilly.org/>`_.


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


Development status
------------------

This incarnation of 596 Acres' software is under active development as we work
on `Living Lots NOLA <http://livinglotsnola.org/>`_. Follow along at
`596acres/livinglots-nola <https://github.com/596acres/livinglots-nola>`_. All
of our Living Lots apps are brand new and will be shifting around while we work
it out.


Code History
------------

You can find the code for the original 596 Acres site, still in use, at
`ebrelsford/596acres <https://github.com/ebrelsford/596acres>`_.

In early 2013, the site in Philadelphia was created. That repo is at
`ebrelsford/v2v <https://github.com/ebrelsford/v2v>`_. The Living Lots apps are
largely based on the Philadelphia code.


License
-------

django-livinglots is released under the `BSD license
<http://opensource.org/licenses/BSD-3-Clause>`_.
