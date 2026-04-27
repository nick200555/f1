import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": _("Date"), "fieldname": "posting_date", "fieldtype": "Date", "width": 120},
        {"label": _("Invoice"), "fieldname": "name", "fieldtype": "Link", "options": "Sales Invoice", "width": 150},
        {"label": _("Customer"), "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 150},
        {"label": _("Amount"), "fieldname": "base_grand_total", "fieldtype": "Currency", "width": 120},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100}
    ]

def get_data(filters):
    conditions = {"docstatus": 1}
    if filters.get("from_date"):
        conditions["posting_date"] = [">=", filters.get("from_date")]
    if filters.get("to_date"):
        conditions["posting_date"] = ["<=", filters.get("to_date")]
    
    return frappe.get_all("Sales Invoice", 
        filters=conditions, 
        fields=["posting_date", "name", "customer", "base_grand_total", "status"]
    )
