import frappe
from frappe.model.document import Document


class PurchaseApprovalRequest(Document):
  def validate(self):
    old_doc = self.get_doc_before_save()
    if old_doc and old_doc.status == "Approved":
        frappe.throw("Approved document cannot be edited")



def get_permission_query_conditions(user):
    # Purchase Managers can see all records
    if "Purchase Manager" in frappe.get_roles(user):
        return None

    # Normal users: own or assigned records only
    return f"""
        (
            `tabPurchase Approval Request`.requester = {frappe.db.escape(user)}
            OR `tabPurchase Approval Request`.name IN (
                SELECT reference_name
                FROM `tabToDo`
                WHERE reference_type = 'Purchase Approval Request'
                AND allocated_to = {frappe.db.escape(user)}
            )
        )
    """


def has_permission(doc, ptype, user):
    # Purchase Managers have full access
    if "Purchase Manager" in frappe.get_roles(user):
        return True

    # Own record
    if doc.requester == user:
        return True

    # Assigned record
    assigned = frappe.db.exists(
        "ToDo",
        {
            "reference_type": "Purchase Approval Request",
            "reference_name": doc.name,
            "allocated_to": user,
        },
    )

    return bool(assigned)
