from . import __version__ as app_version

app_name = "jctkorp_express"
app_title = "Jctkorp Express"
app_publisher = "jctkorp.com"
app_description = "Jctkorp Express Services"
app_email = "info@jctkorp.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jctkorp_express/css/jctkorp_express.css"
# app_include_js = "/assets/jctkorp_express/js/jctkorp_express.js"

# include js, css files in header of web template
# web_include_css = "/assets/jctkorp_express/css/jctkorp_express.css"
# web_include_js = "/assets/jctkorp_express/js/jctkorp_express.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "jctkorp_express/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "jctkorp_express.utils.jinja_methods",
#	"filters": "jctkorp_express.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "jctkorp_express.install.before_install"
# after_install = "jctkorp_express.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "jctkorp_express.uninstall.before_uninstall"
# after_uninstall = "jctkorp_express.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jctkorp_express.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"jctkorp_express.tasks.all"
#	],
#	"daily": [
#		"jctkorp_express.tasks.daily"
#	],
#	"hourly": [
#		"jctkorp_express.tasks.hourly"
#	],
#	"weekly": [
#		"jctkorp_express.tasks.weekly"
#	],
#	"monthly": [
#		"jctkorp_express.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "jctkorp_express.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "jctkorp_express.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "jctkorp_express.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["jctkorp_express.utils.before_request"]
# after_request = ["jctkorp_express.utils.after_request"]

# Job Events
# ----------
# before_job = ["jctkorp_express.utils.before_job"]
# after_job = ["jctkorp_express.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"jctkorp_express.auth.validate"
# ]
