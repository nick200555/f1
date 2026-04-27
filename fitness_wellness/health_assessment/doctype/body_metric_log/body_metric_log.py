import frappe
from frappe.model.document import Document
from fitness_wellness.utils.calculations import calculate_bmi

class BodyMetricLog(Document):
    def validate(self):
        self.calculate_metrics()
    
    def calculate_metrics(self):
        if self.weight and self.height:
            self.bmi = calculate_bmi(self.weight, self.height)
