#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Trevor'
SITENAME = u'Computer Science Interviews'
SITEURL = 'http://csinterviews.com'
TIMEZONE = 'America/New_York'
GITHUB_URL = 'http://github.com/trevor-e/csinterviews'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10
NEWEST_FIRST_ARCHIVES = True
DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['images']
THEME = '/home/trevor/Programming/notmyidea'
PLUGIN_PATH = '/home/trevor/Programming/pelican-plugins'
PLUGINS = ['sitemap','latex']
DISQUS_SITENAME = 'computerscienceinterviews'
GOOGLE_ANALYTICS = 'UA-38564933-1'
TWITTER_USERNAME = 'CSInterviews'
PATH = '/home/trevor/Programming/csinterviews/src/'
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

RELATIVE_URLS = False #for developing

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/trevor-e/csinterviews'),)