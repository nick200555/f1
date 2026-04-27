import frappe
from frappe import _

def send_membership_expiry_notification(member_email, member_name, expiry_date):
    """Sends membership expiry reminder via email."""
    frappe.sendmail(
        recipients=member_email,
        subject=_("Action Required: Your Membership is Expiring Soon!"),
        template="membership_expiry_reminder",
        args={
            "full_name": member_name,
            "expiry_date": expiry_date
        }
    )

def send_class_booking_confirmation(member_email, class_name, schedule_time):
    """Sends class booking confirmation."""
    frappe.sendmail(
        recipients=member_email,
        subject=_("Booking Confirmed: {0}").format(class_name),
        message=_("Hi, your booking for {0} at {1} has been confirmed.").format(class_name, schedule_time)
    )

def send_emi_reminder(member_email, amount, due_date):
    """Sends EMI due reminder."""
    frappe.sendmail(
        recipients=member_email,
        subject=_("Pending Payment: EMI Installment Due"),
        message=_("Your EMI of {0} is due on {1}. Please ensure timely payment.").format(amount, due_date)
    )
