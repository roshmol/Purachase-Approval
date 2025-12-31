import frappe

def after_install():
    # Create dummy Purchase Approval Request
    if not frappe.db.exists("Purchase Approval Request", "PAR-DUMMY-001"):
        doc = frappe.get_doc({
            "doctype": "Purchase Approval Request",
            "requester": frappe.session.user,
            "total_amount": 150000,
            "priority": "High",
            "justification": "Dummy data for assessment",
            "status": "Approved",
            "approved_by": frappe.session.user
        })
        doc.insert(ignore_permissions=True)
