import frappe
from frappe.model.document import Document


class MaintenanceSchedule(Document):
	pass

@frappe.whitelist()
def check_equipment_maintenance_due():
	"""Check and notify when maintenance is due."""
	pass
