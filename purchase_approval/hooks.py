app_name = "purchase_approval"
app_title = "Purchase Approval"
app_publisher = "Roshna"
app_description = "Custom app for purchase approval workflow"
app_email = "roshnatnbr@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "purchase_approval",
# 		"logo": "/assets/purchase_approval/logo.png",
# 		"title": "Purchase Approval",
# 		"route": "/purchase_approval",
# 		"has_permission": "purchase_approval.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/purchase_approval/css/purchase_approval.css"
# app_include_js = "/assets/purchase_approval/js/purchase_approval.js"

# include js, css files in header of web template
# web_include_css = "/assets/purchase_approval/css/purchase_approval.css"
# web_include_js = "/assets/purchase_approval/js/purchase_approval.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "purchase_approval/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "purchase_approval/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "purchase_approval.utils.jinja_methods",
# 	"filters": "purchase_approval.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "purchase_approval.install.before_install"
after_install = "purchase_approval.setup.install.after_install"


# Uninstallation
# ------------

# before_uninstall = "purchase_approval.uninstall.before_uninstall"
# after_uninstall = "purchase_approval.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "purchase_approval.utils.before_app_install"
# after_app_install = "purchase_approval.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "purchase_approval.utils.before_app_uninstall"
# after_app_uninstall = "purchase_approval.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "purchase_approval.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Purchase Approval Request": "purchase_approval.purchase_approval.doctype.purchase_approval_request.purchase_approval_request.get_permission_query_conditions"
}

has_permission = {
	"Purchase Approval Request": "purchase_approval.purchase_approval.doctype.purchase_approval_request.purchase_approval_request.has_permission"
}

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"purchase_approval.tasks.all"
# 	],
# 	"daily": [
# 		"purchase_approval.tasks.daily"
# 	],
# 	"hourly": [
# 		"purchase_approval.tasks.hourly"
# 	],
# 	"weekly": [
# 		"purchase_approval.tasks.weekly"
# 	],
# 	"monthly": [
# 		"purchase_approval.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "purchase_approval.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "purchase_approval.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "purchase_approval.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["purchase_approval.utils.before_request"]
# after_request = ["purchase_approval.utils.after_request"]

# Job Events
# ----------
# before_job = ["purchase_approval.utils.before_job"]
# after_job = ["purchase_approval.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"purchase_approval.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

