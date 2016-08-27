=========================
Flickr Photostream Sorter
=========================

A command-line tool which sorts your Flickr Photostream by the date each photo
is taken. It accomplishes this by setting the date posted to be the same as
the date taken.

This is not something Flickr's website current can do for you, other than
manually doing it for each photo, `as discussed on the Flickr Help Forum <https://www.flickr.com/help/forum/en-us/72157634003151196/>`_.

- On Mac OS X, all commands can be run in `Terminal.app <https://www.youtube.com/watch?v=zw7Nd67_aFw>`_.
- On Windows, all commands can be run in the `Command Prompt <http://windows.microsoft.com/en-us/windows-vista/open-a-command-prompt-window>`_.
- On Linux, use whatever terminal your window manager supports.

For additional information, see `the announcement thread on the Flickr Help Forum <https://www.flickr.com/help/forum/en-us/72157647859111858/>`_.


Authentication
--------------

You'll need a Flickr API key and secret, which you can
`get on the Flickr website <https://www.flickr.com/services/apps/create/noncommercial/?>`_.

Then set them as environment variables by running the following commands
(make sure to change the values to match what Flickr provided):

::

  echo "export FLICKR_API_KEY=0123456789abcdef0123456789abcdef" >> $HOME/.bash_profile
  echo "export FLICKR_SECRET=0123456789abcdef" >> $HOME/.bash_profile
  source $HOME/.bash_profile


Install
-------

Ensure you have Python 2.7.x installed by running ``python -V``. If Python
isn't installed, or you have a version older than 2.7,
`install the latest version of Python 2.7 <https://www.python.org/downloads/>`_.

::

  pip install flickr_photostream_sorter


Usage
-----

::

  flickr_photostream_sorter

The first time you run this, your default web browser will open to Flickr's
website asking you to authorize this application. Please do - without
authorization, this application cannot sort your photostream.

