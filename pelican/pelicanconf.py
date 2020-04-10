#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Xing Shi Cai'
SITENAME = u'Xing Shi Cai/蔡醒诗'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'images', 
    'doc', 
    'notebook',
    'authors',
#    'extra/robots.txt', 
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

THEME = '../../pelican-themes/minimalX'

SUMMARY_MAX_LENGTH = 20

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['../../pelican-plugins']
PLUGINS = ['summary', 'render_math', 'assets', 'tag_cloud']

TAG_CLOUD_BADGE = True
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 50
TAG_CLOUD_BADGE = True
TAG_CLOUD_SORTING = 'size'

SUMMARY_END_MARKER = '<!-- END_SUMMARY -->'

DISPLAY_CATEGORIES_ON_MENU = True

DEFAULT_METADATA = {
    'status': 'draft',
}

PAGE_ORDER_BY = 'page-order'

# Jupyter integration
MARKUP = ('md')

PLUGINS = PLUGINS + ['pelican-ipynb.liquid']

# Social media
SOCIAL = [
         ('github', 'https://github.com/newptcai')
         ]

SHARE_BUTTONS = ('twitter', 'facebook', 'whatsapp', 'mail')
