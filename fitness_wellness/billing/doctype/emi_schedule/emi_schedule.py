import frappe
from frappe.model.document import Document
from fitness_wellness.utils.calculations import generate_emi_schedule

class EMISchedule(Document):
    def validate(self):
        if not self.installments:
            self.generate_installments()
    
    def generate_installments(self):
        self.set("installments", [])
        generate_emi_schedule(self, self.total_amount, self.no_of_installments, self.start_date)

@frappe.whitelist()
def process_emi_deductions():
    # Scheduler task logic
    # Find all 'Active' EMI Schedules and check for due installments today
    pass
