import frappe

@frappe.whitelist()
def get_material_request_total(mr):
    items = frappe.get_all(
        "Material Request Item",
        filters={"parent": mr},
        fields=["amount"]
    )

    total = sum(i.amount or 0 for i in items)

    return {
        "total": total,
        "item_count": len(items)
    }
@frappe.whitelist()
def approve_par(name):
    doc = frappe.get_doc("Purchase Approval Request", name)

    # Extra safety check
    if "Purchase Manager" not in frappe.get_roles(frappe.session.user):
        frappe.throw("Not permitted")

    doc.status = "Approved"
    doc.approved_by = frappe.session.user
    doc.save()
    
@frappe.whitelist()
def get_material_request_item_count(mr):
    if not mr:
        return 0

    return frappe.db.count(
        "Material Request Item",
        {"parent": mr}
    )
