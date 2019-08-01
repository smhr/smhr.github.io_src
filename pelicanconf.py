#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
## smhr
import os
##
#####################
AUTHOR = u'S.Mohammad Hosseinirad'
SITENAME = u'S.Mohammad Hosseinirad'

TIMEZONE = 'Asia/Tehran'
DEFAULT_LANG = u'en'

SITEURL = 'https://smhr.gitlab.com'
PATH = 'content'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU =False
MENUITEMS = (
    ('Research', '/pages/research.html'),
    ('CV', '/pages/cv.html'), ('Codes', '/pages/codes.html'),
    ('Publications', '/pages/publications.html'),
    ('Teaching', '/pages/teaching.html')
    #('Blog','/category/blog.html')
)

# Blogroll
LINKS = (('Bookmarked paper', 'http://cosmocoffee.info/bookmark.php?club=120'),
         ('astrobites', 'http://www.astrobites.com/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         ('Dark matter crisis', 'http://www.scilogs.com/the-dark-matter-crisis'),)
         #('NBODY6 code', 'http://www.ast.cam.ac.uk/\%7Esverre/web/pages/nbody.htm'),)

# Social widget
SOCIAL = (\
          #('ResearchGate', 'http://www.researchgate.net/profile/Seyed_Mohammad_Hoseini-Rad'),
          ('github', 'http://github.com/smhr'),)
          #('twitter', 'http://twitter.com/DaanDebie'),)
          #('linkedin', 'http://www.linkedin.com/in/danieldebie'),
          #('github', 'http://github.com/DandyDev'),
          #('stackoverflow', 'http://stackoverflow.com/users/872397/dandydev'),)

CC_LICENSE="CC-BY"
DEFAULT_PAGINATION = 6

#use URLs that match old wordpress site
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
#ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
#ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'pdfs', 'extra/robots.txt', 'extra/favicon.ico', 'extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css':{'path':'static/custom.css'}
}

################### plugins
PLUGIN_PATHS = ['pelican-plugins']

#PLUGINS = ['pandoc_reader', 'tag_cloud', 'pelican-bibtex']
PLUGINS = ['tag_cloud', 'pelican-bibtex']

#PANDOC_ARGS = [ '--from=markdown+smart', '--mathjax', '--filter=pandoc-citeproc', '--toc', '--toc-depth=2', '--number-sections', '--bibliography=MYHOMEPAGESRCPATH/references.bib',\
#  '--csl=MYHOMEPAGESRCPATH/journal-for-the-history-of-astronomy.csl', '--citation-abbreviations=MYHOMEPAGESRCPATH/abbreviation.json']

###################

################ Theme
#THEME = 'pelican-bootstrap3'
THEME = 'pelican-bootstrap3-beneth'
BOOTSTRAP_THEME = "cosmo"
#BANNER = 'images/gc_ban_0.5.jpg'
#BANNER_ALL_PAGES = True
#BANNER_SUBTITLE = 'This is my subtitle'
#SITELOGO = 'images/logo.png'
#SITELOGO_SIZE = 32
#CUSTOM_CSS = 'static/custom.css'
#ABOUT_ME = "Whatever you want to say about yourself"

#DISPLAY_ARTICLE_INFO_ON_INDEX = True
#DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

SHOW_ARTICLE_CATEGORY = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 8
######################
##ARTICLE_URL = '{category}/{slug}/'
##ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'
######################
#TEMPLATE_PAGES = {'content/pages/publications.htmll': 'pages/books.html'}

PUBLICATIONS_SRC = 'content/pubs.bib'
DIRECT_TEMPLATES = ['publications', 'archives', 'index', 'search']
######################

# Contacts
EMAIL_ADDR = 'hosseinirad@um.ac.ir'

####### Options to change index.html pages
####### home.md must be added in pagess folder
#DISPLAY_PAGES_ON_MENU = False
##DISPLAY_CATEGORIES_ON_MENU = True
#USE_FOLDER_AS_CATEGORY = True 
#MENUITEMS = (
    #('Research', '/pages/research.html'),
    #('CV', '/pages/cv.html'), ('Codes', '/pages/codes.html'),
    #('Publications', 'publications.html'),
    ##('Blog','/category/blog.html')
#)
#DEFAULT_CATEGORY = 'blog'
