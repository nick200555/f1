import frappe
from frappe.model.document import Document


class MembershipInvoice(Document):
	pass

@frappe.whitelist()
def auto_generate_monthly_invoices():
	"""Automatically generate invoices for active subscriptions."""
	pass
