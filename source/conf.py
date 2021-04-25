project = 'Telephone Bot'
author = 'Telephone Bot team & contributors'
copyright = '2018-2021 the Telephone Bot team & contributors'

exclude_patterns = []
templates_path = ['_templates']

primary_domain = ''

extensions = [
	'sphinx.ext.extlinks',
	'sphinx_rtd_theme',
	'sphinxcontrib.httpdomain',
	'sphinxemoji.sphinxemoji',
]

html_static_path = ['_static']
html_extra_path = []
html_title = "Telephone Bot User's Guide"
html_short_title = "Telephone bot"
#html_logo = ''
#html_favicon = ''
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
	'display_version': False,
}
html_css_files=[
	("style/visual-extras.css", {'type':"text/css",'media':"screen, print"}),
	("style/visual-tweaks.css", {'type':"text/css",'media':"screen, print"}),
]

highlight_language = 'markdown'
highlight_options = {
	'php':{
		'startinline': True
	},
}
pygments_style = 'material'
