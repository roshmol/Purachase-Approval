# Copyright (c) 2025, Roshna and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PurchaseApprovalRequest(Document):
	pass


def before_save(self):
    if self.status == "Approved" and not self.is_new():
        frappe.throw("Approved document cannot be edited")
