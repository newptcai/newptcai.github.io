#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Xing Shi Cai'
SITENAME = u"You don't need to prove this"
SITEURL = 'http://localhost:8000'
AUTHOR_INFO = { 
        'Xing Shi Cai' : "Mathematical, computer scientist, software engineer, reader, walker. Spend too much time on the computer.",
        }

PATH = 'content'

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
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

# PLUGINS = PLUGINS + ['pelican-ipynb.liquid']

from pelican_jupyter import liquid as nb_liquid
PLUGINS = [nb_liquid]

IGNORE_FILES = [".ipynb_checkpoints", ".git", "README.md"] 

LIQUID_CONFIGS = (("IPYNB_EXPORT_TEMPLATE", "basic.tpl", ""), )

# Social media
SOCIAL = [
         ('github', 'https://github.com/newptcai'), 
         ('goodreads', 'https://www.goodreads.com/review/list/4410353-xing-shi?order=d&shelf=read'), 
         ('meetup', 'https://www.meetup.com/members/55719622/'),
         ('skype', 'https://join.skype.com/invite/h4i4wxzWD3i6'),
         ('orcid', 'https://orcid.org/0000-0002-3768-8078'),
         ('researchgate', 'https://www.researchgate.net/profile/Xing_Shi_Cai'),
         ]

SHOW_FOOTER = False

SHARE_BUTTONS = ('twitter', 'facebook', 'whatsapp', 'reddit', 'mail')

# Speed Up
LOAD_CONTENT_CACHE = True
# CACHE_CONTENT = True
