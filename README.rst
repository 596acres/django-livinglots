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
by our experience with making this kind of platform in `New York City
<http://596acres.org/>`_, 
`Philadelphia <http://groundedinphilly.org/>`_,
`New Orleans <http://livinglotsnola.org/>`_,
and `Los Angeles <http://laopenacres.org/>`_.


Sounds great! I want to do this for my city! How?
-------------------------------------------------

Glad you asked: you've come to the right place.

The first thing you should know is that Living Lots is not a box that you turn
on and then runs itself. Installing and running Living Lots is more complicated
than installing other websites (like Wordpress), but once you get going you'll
have a great deal more power over how your site works than with other sites.
Assume that it's going to take around six months to get your site running the 
way you want it to.

We'll be diving into the specifics, but here's an outline of what you need to 
get together before you can have a functional Living Lots site:

* Data
* An understanding of how to gain access to land in your city
* People
* Paid services


Data
^^^^

Living Lots is fundamentally data-driven. While you could theoretically start
with an empty map and fill it in, you're going to have a difficult time getting
people to your site without at least some vacant land to show on the map and
impress everyone with.

Certain kinds of data are required. Ideally you will have:

* the **parcels** that you want to put on your map,
* some way of telling **which are vacant**, and
* data on who **owns** each of those parcels.
  
Try to get the parcels along with their shapes (also known as polygons) as this 
will give viewers a better idea of which land you're mapping. When looking for 
parcels and their shapes, you do not want a spreadsheet or CSV of them, but you 
do want something called a *shapefile*.  You'll need a piece of software called
a GIS to read these, luckily there's a free one called `QGIS <http://qgis.org>`_
that is excellent.

Some data is nice to have but isn't necessarily a dealbreaker. One dataset you
should try to get is **locations of current community-driven projects such as 
community gardens**. This is helpful for two reasons: it will help you avoid
marking those project locations as vacant and it gives you more points to put
on the map.

We find that it's useful to be able to filter the map by **boundary layers**.
These are large shapes that cover your city such as zip codes and city council
districts. These are usually easy enough to find, but now is a good time to
think about other layers you would want to filter with on your map. As with
parcels, you'll be looking for *shapefiles* for these boundaries.


An understanding of how to gain access to land in your city
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Simultaneous to your other tasks, start listing the ways people can legitimately
get access to land your city. Be detailed and work on making these readable for
a general audience. Note which types of parcels the method will work on. Some 
tactics are only suitable for public land, some are only suitable for public 
land under the jurisdiction of a particular agency.

In Living Lots, we call these tactics **pathways**. Vacant parcels have a list 
of these on their page. This is why you want your text to be accessible.

In addition to *pathways* becoming content for your new site, thinking through
them is going to affect the way you think about the data regarding land in your
city. You'll find yourself thinking, for example, "oh, it's sometimes easier to
get access to lots that repeatedly receive fines for litter, can we find that
information somewhere?"


People
^^^^^^

You're going to need some help to get your Living Lots site up and running.

In no particular order, you'll need:

* **A programmer**. Someone who knows Python (the language Living Lots is 
  written in) and Django (a Python module Living Lots depends on) would be 
  ideal. It would also be great to find someone who has worked with data, 
  mapping data, and knows something about the open data situation in your city.
  They're going to help install Living Lots and customize it to meet your needs.
* **A graphic / web designer**. This person is going to help you determine what
  your site is going to look like and how people will interact with the site.
  Having a designer is *not optional*. Plan on working with the designer 
  intensively at the beginning of the project and less intensively over a few 
  iterations as the site is getting closer to being ready to go online.
* **Organizer(s) / support network**. Once the site is online, how are you going
  to handle incoming emails and requests for assistance? Who is going to provide
  outreach and ensure that the site gets used? Who will keep an eye on the data
  in the system to keep it up to date? This document focuses on the technical 
  side of the project you're embarking on, but please don't forget this part!


Paid services
^^^^^^^^^^^^^

At the minimum, you're going to be paying for two services: a domain name and 
room on a server.

The domain name(s) is the URL people will use to get to your site.  It will cost
between $10 and $20 per year. You want to look for a *registrar* (there are tons
of them), and if your organization is already using one just use that.

There a number of options for servers, and we list the requirements below
(Technical Requirements). You'll want the programmer you're working with to help
pick a server. Depending on the type of web hosting you have now you *might* be
able to use that one, but in our experience you're better off getting a new
hosting account specifically for your Living Lots site.


Actually building the site
^^^^^^^^^^^^^^^^^^^^^^^^^^

You'll need someone with programming experience to do the rest. Once you find a
programmer as specified above, send them here (to the next section). It doesn't
hurt to get going on most of these tasks simultaneously, so don't feel like you
need to get all of the above done before you send a programmer here.


Technical Requirements
----------------------

Oh hi, welcome! This section should have enough technical information to get you
up and running with Living Lots.

You're going to need the following software to run Living Lots:

* `Django <http://djangoproject.com/>`_ (1.7+)
* `GeoDjango <http://geodjango.org/>`_ (included with Django as
  django.contrib.gis)
* A spatial database. Living Lots is tested and known to work with:

  * `PostgreSQL <http://www.postgresql.org/>`_ (9.1+)
  * `PostGIS <http://postgis.net/>`_

You will need to serve the Django project however you like. We use:

* `gunicorn <http://gunicorn.org/>`_ and `nginx <http://nginx.org/>`_ to serve
  the sites, and
* `Supervisor <http://supervisord.org/>`_ to keep them running.


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
<https://docs.djangoproject.com/en/1.7/ref/django-admin/#startproject-projectname-destination>`_.

From here, you will want to set up a CMS for the content outside of Living Lots.
We use and recommend `FeinCMS 
<http://feincms-django-cms.readthedocs.org/en/latest/>`_ (as is included in the 
project template), but it is not required. In theory any CMS app for Django
should work.

Next, create concrete models. The abstract models are defined in Living Lots
apps such as `django-livinglots-lots
<https://github.com/596acres/django-livinglots-lots>`_. See `livinglots-nyc
<https://github.com/596acres/livinglots-nyc`_ for some examples of how this 
works. As you add concrete models, don't forget to define them in your settings
so Living Lots apps can find them. Most of these are stubbed out for you in the
template project, so you shouldn't have to write much from scratch.


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

* `django-livinglots-activities <https://github.com/596acres/django-livinglots-activities>`_
* `django-livinglots-flatblockspreview <https://github.com/596acres/django-livinglots-flatblockspreview>`_
* `django-livinglots-forms <https://github.com/596acres/django-livinglots-forms>`_
* `django-livinglots-friendlyowners <https://github.com/596acres/django-livinglots-friendlyowners>`_
* `django-livinglots-generictags <https://github.com/596acres/django-livinglots-generictags>`_
* `django-livinglots-genericviews <https://github.com/596acres/django-livinglots-genericviews>`_
* `django-livinglots-groundtruth <https://github.com/596acres/django-livinglots-groundtruth>`_
* `django-livinglots-lots <https://github.com/596acres/django-livinglots-lots>`_
* `django-livinglots-mailings <https://github.com/596acres/django-livinglots-mailings`_
* `django-livinglots-mailreader <https://github.com/596acres/django-livinglots-mailreader>`_
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

In early 2013, `Grounded in Philly <http://groundedinphilly.org>`_ 
(`repo <https://github.com/596acres/livinglots-philly>`_) was created.
The Living Lots apps were originally largely based on the Philadelphia code.

In late 2013 `Living Lots NOLA <http://livinglotsnola.org/>`_
(`repo <https://github.com/596acres/livinglots-nola>`_) was created and Living
Lots evolved to become more modular and more common functionality was added to
it.

In the first half of 2014 `LA Open Acres <http://laopenacres.org/>`_
(`repo <https://github.com/596acres/livinglots-la>`_) was created using Living
Lots.

In late 2014, Grounded in Philly was updated to take advantage of many of
the improvements made to Living Lots, and the framework was further refined.

Also in late 2014, the framework came full circle: the site in NYC was 
rewritten, became `Living Lots NYC <http://livinglotsnyc.org>`_ 
(`repo <https://github.com/596acres/livinglots-nyc`_), and is now based on 
Living Lots.


License
-------

django-livinglots is released under the `BSD license
<http://opensource.org/licenses/BSD-3-Clause>`_.
