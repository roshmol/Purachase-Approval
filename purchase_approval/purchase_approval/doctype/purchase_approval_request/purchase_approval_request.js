// Copyright (c) 2025, Roshna and contributors
// For license information, please see license.txt


frappe.ui.form.on('Purchase Approval Request', {

    setup(frm) {
        frm.priority_set_from_mr = false;
    },

    total_amount(frm) {
        if (!frm.doc.total_amount) return;

        if (frm.priority_set_from_mr) return;

        if (frm.doc.total_amount > 100000) {
            frm.set_value('priority', 'High');
            frm.toggle_reqd('justification', true);
        } else {
            frm.set_value('priority', 'Low');
            frm.toggle_reqd('justification', false);
        }
    },

    material_request(frm) {
        if (!frm.doc.material_request) return;

        frappe.call({
            method: 'purchase_approval.api.v1.material_request.get_material_request_details',
            args: {
                mr: frm.doc.material_request
            },
            callback(r) {
                if (!r.message) return;

                // mark that MR logic is active
                frm.priority_set_from_mr = true;

                frm.set_value('total_amount', r.message.total);

                if (r.message.item_count > 5) {
                    frm.set_value('priority', 'High');
                    frm.toggle_reqd('justification', true);
                } else {
                    // allow total_amount logic again
                    frm.priority_set_from_mr = false;
                }
            }
        });
    },

    refresh(frm) {
        if (frm.doc.status === 'Approved') {
            frm.disable_form();
        }

        if (
            frm.doc.status === 'Draft' &&
            frappe.user.has_role('Purchase Manager')
        ) {
            frm.add_custom_button(__('Approve'), () => {
                frappe.call({
                    method: 'purchase_approval.api.v1.material_request.approve_par',
                    args: { name: frm.doc.name },
                    callback() {
                        frm.reload_doc();
                    }
                });
            });
        }
    }
});
