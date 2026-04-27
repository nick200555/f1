import frappe
from frappe import _
from frappe.utils import getdate, add_months, flt, date_diff

def calculate_prorated_amount(total_amount, start_date, end_date):
    """Calculates prorated amount based on days active."""
    total_days = date_diff(end_date, start_date) + 1
    if total_days <= 0:
        return 0
    # Logic for proration can be specific, but here we assume linear
    return total_amount

def generate_emi_schedule(parent_doc, total_amount, no_of_installments, start_date):
    """Generates EMI installments in the child table."""
    if not no_of_installments or no_of_installments <= 0:
        return
    
    amount_per_installment = flt(total_amount / no_of_installments, 2)
    for i in range(no_of_installments):
        due_date = add_months(start_date, i)
        parent_doc.append("installments", {
            "due_date": due_date,
            "amount": amount_per_installment,
            "payment_status": "Pending"
        })

def calculate_trainer_commission(trainer_id, from_date, to_date):
    """Calculates commission based on sessions taken."""
    trainer = frappe.get_doc("Trainer Profile", trainer_id)
    # Mock logic: find sessions in Class Attendance and Trainer Assignment
    # This will be refined as DocTypes are created
    return 0.0

def calculate_bmi(weight_kg, height_cm):
    """Calculates BMI."""
    if not height_cm or height_cm <= 0:
        return 0
    height_m = height_cm / 100.0
    return flt(weight_kg / (height_m * height_m), 2)

def calculate_goal_progress(baseline, current, target):
    """Calculates percentage progress towards a goal."""
    if target == baseline:
        return 100.0
    total_change_needed = target - baseline
    current_change = current - baseline
    progress = (current_change / total_change_needed) * 100.0
    return flt(min(max(progress, 0), 100), 2)

def calculate_nutrition_macros(item_name, quantity):
    """Calculates macros for a food item."""
    food = frappe.get_doc("Food Item", item_name)
    return {
        "calories": flt(food.calories_per_unit * quantity),
        "protein": flt(food.protein_per_unit * quantity),
        "carbs": flt(food.carbs_per_unit * quantity),
        "fats": flt(food.fats_per_unit * quantity)
    }
