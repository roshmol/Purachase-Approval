// Copyright (c) 2025, Roshna and contributors
// For license information, please see license.txt

frappe.ui.form.on('Purchase Approval Request', {
    total_amount(frm) {
        if (!frm.doc.total_amount) return;

        if (frm.doc.total_amount > 100000) {
            frm.set_value('priority', 'High');
            frm.toggle_reqd('justification', true);
        } else {
            frm.set_value('priority', 'Low');
            frm.toggle_reqd('justification', false);
        }
    }
});



frappe.ui.form.on('Purchase Approval Request', {
    material_request(frm) {
        if (frm.doc.material_request) {
            frappe.call({
                method: 'purchase_approval.api.v1.material_request.get_material_request_total',

                args: {
                    mr: frm.doc.material_request
                },
                callback(r) {
                    if (r.message) {
                        frm.set_value('total_amount', r.message.total);

                        if (r.message.item_count > 5) {
                            frm.set_value('priority', 'High');
                        }
                    }
                }
            });
        }
    }
});
frappe.ui.form.on('Purchase Approval Request', {
    refresh(frm) {
        if (frm.doc.status === 'Approved') {
            frm.disable_form();
        }
    }
});


frappe.ui.form.on('Purchase Approval Request', {
    refresh(frm) {
        // Approve button ONLY for Purchase Manager
        if (
            frm.doc.status === 'Draft' &&
            frappe.user.has_role('Purchase Manager')
        ) {
            frm.add_custom_button(__('Approve'), () => {
                frappe.call({
                    method: 'purchase_approval.api.approve_par',
                    args: {
                        name: frm.doc.name
                    },
                    callback() {
                        frm.reload_doc();
                    }
                });
            });
        }
    }
});


frappe.ui.form.on('Purchase Approval Request', {
    material_request(frm) {
        if (!frm.doc.material_request) return;

        frappe.call({
            method: 'purchase_approval.api.v1.material_request.get_material_request_item_count',
            args: {
                mr: frm.doc.material_request
            },
            callback(r) {
                if (r.message > 5) {
                    frm.set_value('priority', 'High');
                }
            }
        });
    }
});
