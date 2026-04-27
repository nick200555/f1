import frappe
from frappe.model.document import Document
from frappe import _

class ClassEnrollment(Document):
    def validate(self):
        self.check_capacity()

    def check_capacity(self):
        if self.class_schedule:
            schedule = frappe.get_doc("Class Schedule", self.class_schedule)
            enrolled_count = frappe.db.count("Class Enrollment", filters={"class_schedule": self.class_schedule, "status": "Enrolled", "docstatus": 1})
            
            if enrolled_count >= schedule.max_capacity:
                if schedule.allow_waitlist:
                    self.status = "Waitlisted"
                else:
                    frappe.throw(_("Class is full and waitlist is not allowed."))
