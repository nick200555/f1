import frappe
from frappe.model.document import Document


class TrainerCommission(Document):
	pass

@frappe.whitelist()
def generate_trainer_commission_vouchers():
	"""Generate commission vouchers weekly."""
	pass
