# Fitness & Wellness Management System

Enterprise-grade fitness management solution built on Frappe and ERPNext v15.

## Modules
- **Member Management**: Registration, plans, subscriptions, and referrals.
- **Class Management**: Scheduling, enrollment, and capacity management.
- **Trainer Management**: Profiles, commissions, and assignments.
- **Facility Management**: Equipment register, maintenance, and AMC tracking.
- **Health Assessment**: BMI, body metrics, and goal tracking.
- **Nutrition**: Diet plans and food item calorie tracking.
- **Billing**: Membership invoices, EMI schedules, and reconciliations.

## Installation

1. Get the app from the repository:
   ```bash
   bench get-app https://github.com/nick200555/fitness.git
   ```

2. Install the app on your site:
   ```bash
   bench --site [your-site-name] install-app fitness_wellness
   ```

3. Run migrations:
   ```bash
   bench migrate
   ```

4. Build assets:
   ```bash
   bench build
   ```

## Features
- Automated Membership Expiry Reminders.
- Integrated Sales Invoice generation via ERPNext Accounts.
- EMI engine for subscription payments.
- Member Portal for class booking and progress tracking.
- Trainer Commission automation.
