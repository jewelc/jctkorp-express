# Copyright (c) 2023, jctkorp.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ShipmentDetails(Document):
	def validate(self):
		# If Others selected
		if ((self.unit_nos == 0) and (self.weight_per_unit == 0)) or ((self.unit_nos == 0) or (self.weight_per_unit == 0)):
			frappe.throw("Unit Nos and Weight Per Unit value Must be greater than 0")
		
		# if Box Selected

		if (self.shipment_unit =="Box"):
			if (((self.length_cm ==0) and (self.width_cm ==0) and (self.height_cm ==0) and (self.total_cbm ==0)) or ((self.length_cm ==0) or (self.width_cm==0) or (self.height_cm==0) or (self.total_cbm ==0))):
				frappe.throw("Lenght/Width/Height/Total CBM value Must be greater than 0")
		# if Bag Selected
		if (self.shipment_unit =="Bag"):
			if (((self.length_cm ==0) and (self.width_cm ==0) and (self.height_cm ==0) and (self.total_cbm ==0)) or ((self.length_cm ==0) or (self.width_cm==0) or (self.height_cm==0) or (self.total_cbm ==0))):
				frappe.throw("Lenght/Width/Height/Total CBM value Must be greater than 0")

	def before_save(self):
		self.total_units = self.unit_nos
		
	# 	self.set_value()

	
	# def set_value(self):
	# 	total_units = frappe.db.set_value("ShipmentDetails", "Units Nos", "Units Nos")