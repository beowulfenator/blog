AUTHOR = 'Konstantin Sirotkin'
SITENAME = 'DIY Blog'
BIO = 'Noise, dust, and endorphins.'
SITEURL = ""
PROFILE_IMAGE = "workshoppe.png"
THEME = "theme"
PATH = "content"

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None

ARCHIVES_SAVE_AS = None
AUTHOR_SAVE_AS = None
AUTHORS_SAVE_AS = None
CATEGORY_SAVE_AS = None
CATEGORIES_SAVE_AS = None

ARTICLE_URL = 'articles/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = 'articles/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'

TIMEZONE = 'UTC'
LOCALE = 'usa'

DEFAULT_DATE_FORMAT = '%d %b %Y'
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ["images"]
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["articles"]

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'summary',
    'pelican.plugins.image_process',
    'pelican.plugins.jinja2content',
]

SUMMARY_END_MARKER = '<!--more-->'

IMAGE_PROCESS = {
    "article-image": {'type': 'responsive-image',
    'sizes': '(min-width: 1200px) 800px, (min-width: 992px) 650px, \
              (min-width: 768px) 718px, 100vw',
    'srcset': [('600w', ["scale_in 600 450 True"]),
               ('800w', ["scale_in 800 600 True"]),
               ('1600w', ["scale_in 1600 1200 True"]),
               ],
    'default': '800w',
    },
}
