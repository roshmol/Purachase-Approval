
import frappe

@frappe.whitelist()
def get_material_request_details(mr):
    items = frappe.get_all(
        "Material Request Item",
        filters={"parent": mr},
        fields=["amount"]
    )

    total = sum(d.amount for d in items)

    return {
        "total": total,
        "item_count": len(items)
    }


@frappe.whitelist()
def approve_par(name):
    doc = frappe.get_doc("Purchase Approval Request", name)

    # Permission check
    if "Purchase Manager" not in frappe.get_roles(frappe.session.user):
        frappe.throw("Not permitted to approve")

    # Justification mandatory check
    if doc.total_amount > 100000 and not doc.justification:
        frappe.throw("Justification is mandatory for high value approvals")

    # Approve
    doc.status = "Approved"
    doc.approved_by = frappe.session.user
    doc.save()
