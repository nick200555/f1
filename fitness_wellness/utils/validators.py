import frappe
from frappe import _
from frappe.utils import getdate

def validate_member_attendance(member, date):
    """Validates if the member has an active subscription for the given date."""
    member_doc = frappe.get_doc("Member", member)
    if member_doc.status != "Active":
        frappe.throw(_("Member is not active."))
    
    if member_doc.subscription_end_date and getdate(date) > getdate(member_doc.subscription_end_date):
        frappe.throw(_("Member's subscription has expired."))

def validate_class_capacity(class_schedule):
    """Checks if class has reached maximum capacity."""
    schedule = frappe.get_doc("Class Schedule", class_schedule)
    enrolled = frappe.db.count("Class Enrollment", filters={"class_schedule": class_schedule, "status": "Enrolled", "docstatus": 1})
    if enrolled >= schedule.max_capacity:
        return False
    return True

def validate_emi_eligibility(total_amount):
    """Checks if the amount is eligible for EMI."""
    min_emi_amount = frappe.db.get_single_value("Billing Settings", "min_emi_amount") or 5000
    if total_amount < min_emi_amount:
        frappe.throw(_("Total amount {0} is below the minimum EMI eligibility of {1}.").format(total_amount, min_emi_amount))
