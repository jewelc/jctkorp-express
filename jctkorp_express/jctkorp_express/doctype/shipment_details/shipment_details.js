// Copyright (c) 2023, jctkorp.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shipment Details', {
	// refresh: function(frm) {

	// }
	validate:function(frm){
		if (frm.doc.unit_nos==0){frappe.throw("Unit Nos Value cannot be 0.")}
		if (frm.doc.weight_per_unit==0){frappe.throw("Weight Value Cannot be 0")}
		if ((frm.doc.shipment_unit=="Box") && (frm.doc.lenght_cm==0)){frappe.throw("Lenght Value Cannot be 0")}
		if ((frm.doc.shipment_unit=="Box") && (frm.doc.width_cm==0)){frappe.throw("Width Value Cannot be 0")}
		if ((frm.doc.shipment_unit=="Box") && (frm.doc.height_cm==0)){frappe.throw("Height Value Cannot be 0")}
	}

	
});
