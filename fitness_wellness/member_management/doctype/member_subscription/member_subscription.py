import frappe
from frappe.model.document import Document
from frappe.utils import add_months, getdate, flt
from fitness_wellness.utils.calculations import calculate_prorated_amount

class MemberSubscription(Document):
    def validate(self):
        self.set_end_date()
        self.set_amounts()
    
    def set_end_date(self):
        if self.membership_plan and self.start_date:
            plan = frappe.get_doc("Membership Plan", self.membership_plan)
            self.end_date = add_months(self.start_date, plan.duration_months)
    
    def set_amounts(self):
        if self.membership_plan:
            plan = frappe.get_doc("Membership Plan", self.membership_plan)
            self.total_amount = plan.total_amount
            # Balance calculation logic
            self.balance_amount = flt(self.total_amount) - flt(self.paid_amount)

    def on_submit(self):
        self.create_sales_invoice()
        self.update_member()

    def create_sales_invoice(self):
        # Integration with ERPNext Accounts
        if not self.sales_invoice:
            invoice = frappe.get_doc({
                "doctype": "Sales Invoice",
                "customer": self.member, # Assuming Member is linked as Customer or logic to find customer
                "posting_date": getdate(),
                "items": [{
                    "item_name": self.membership_plan,
                    "qty": 1,
                    "rate": self.total_amount
                }],
                "is_pos": 0
            })
            invoice.insert(ignore_permissions=True)
            invoice.submit()
            self.db_set("sales_invoice", invoice.name)

    def update_member(self):
        member = frappe.get_doc("Member", self.member)
        member.current_membership_plan = self.membership_plan
        member.subscription_end_date = self.end_date
        member.status = "Active"
        member.save(ignore_permissions=True)

@frappe.whitelist()
def send_membership_expiry_reminders():
    # Scheduler task logic
    expiry_date = add_months(getdate(), 1) # Remind 1 month before
    members = frappe.get_all("Member", filters={"subscription_end_date": ["<=", expiry_date], "status": "Active"}, fields=["name", "email", "full_name"])
    for member in members:
        # Send notification logic
        pass
