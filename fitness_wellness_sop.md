# 📘 Fitness & Wellness Management System — Standard Operating Procedure (SOP)
### Functional Guide for Fitness Centres, Gyms & Wellness Studios

---

> **Document Version:** 1.0  
> **Application:** Fitness & Wellness Management System on ERPNext v15  
> **Audience:** Fitness Managers, Gym Owners, Front Desk Teams, Trainers, Dietitians, Accounts Teams, Facility Supervisors  
> **Support:** support@fitness-wellness.com

---

## 📋 Table of Contents

1. [Getting Started — First Login](#1-getting-started--first-login)
2. [Module 1 — Member & Subscription Management](#2-module-1--member--subscription-management)
3. [Module 2 — Class & Schedule Management](#3-module-2--class--schedule-management)
4. [Module 3 — Trainer & Staff Management](#4-module-3--trainer--staff-management)
5. [Module 4 — Facility & Equipment Management](#5-module-4--facility--equipment-management)
6. [Module 5 — Health & Fitness Assessment](#6-module-5--health--fitness-assessment)
7. [Module 6 — Nutrition & Diet Management](#7-module-6--nutrition--diet-management)
8. [Module 7 — Billing & Finance](#8-module-7--billing--finance)
9. [Module 8 — Reports & Analytics](#9-module-8--reports--analytics)
10. [Daily / Weekly / Monthly Operating Checklist](#10-daily--weekly--monthly-operating-checklist)
11. [User Roles & Who Does What](#11-user-roles--who-does-what)
12. [Frequently Asked Questions](#12-frequently-asked-questions)
13. [Support & Contact](#13-support--contact)

---

## 1. Getting Started — First Login

### 1.1 Access the Application

1. Open your browser and go to your Fitness & Wellness URL:  
   `https://fit.yourdomain.org`
2. Login with your ERPNext credentials (provided by your administrator).
3. On the left sidebar, click the **Fitness Wellness** workspace.
4. You will see the **Fitness Manager Dashboard** with 4 quick-access shortcuts at the top:
   - 🟠 Active Members
   - 🔵 Class Occupancy
   - 🟢 Revenue Today
   - 🟣 Equipment Downtime

---

### 1.2 Initial System Setup (One-Time — Admin Only)

> **Who does this:** System Administrator or Gym Owner (first time only)

| Step | Action | Where |
|---|---|---|
| 1 | Create your Company | ERPNext → Accounting → Company |
| 2 | Set your Financial Year | ERPNext → Accounting → Fiscal Year |
| 3 | Configure Workflow States | Fitness Wellness → Workflow → Member Onboarding Workflow |
| 4 | Setup Default Workspaces | Fitness Wellness → Workspace |

---

### 1.3 Assign User Roles

> **Who does this:** Administrator

Go to **ERPNext → HR → User** and assign each person their role:

| Role | Assign To |
|---|---|
| System Manager | Gym Owner / IT Admin |
| Fitness Manager | Operations Head / Branch Manager |
| Front Desk Executive | Receptionist / Customer Service |
| Trainer | Personal Trainers / Yoga Instructors |
| Dietitian | Nutritionist / Health Expert |
| Facility Supervisor | Maintenance Lead / Floor Manager |
| Accounts Executive | Cashier / Finance Manager |

---

## 2. Module 1 — Member & Subscription Management

> **Purpose:** Handle the complete lifecycle of a member from lead conversion to active subscription, attendance tracking, and retention.

---

### 2.1 SOP — Member Onboarding & Verification

**Who:** Front Desk Executive / Fitness Manager  
**When:** When a new client joins the facility

**Workflow Diagram:**
```text
Draft ──► Pending Verification ──► Active ✅
                                └── Inactive ❌
```

| Step | Action |
|---|---|
| 1 | Go to **Member Management → Member** |
| 2 | Click **+ New** |
| 3 | Enter **First Name**, **Last Name**, **Gender**, and **Date of Birth** |
| 4 | Fill in **Contact Information** (Email, Phone) and **Emergency Contact** |
| 5 | Select **Referral Source** (if walked in via reference, select 'Referred By') |
| 6 | Set the **Joining Date** |
| 7 | Save the document (Status becomes *Draft*) |
| 8 | Submit for Verification (Status changes to *Pending Verification*) |
| 9 | **Fitness Manager** opens the document, verifies details, and approves |

✅ **Expected Result:** Member status updates to *Active*. System generates a Member ID (e.g., MEM-2026-0001).

---

### 2.2 SOP — Creating Membership Plans

**Who:** Fitness Manager  
**When:** When introducing new gym packages or pricing

| Step | Action |
|---|---|
| 1 | Go to **Member Management → Membership Plan** |
| 2 | Click **+ New** |
| 3 | Enter **Plan Name** (e.g., "Annual Gold Plan") |
| 4 | Enter **Total Amount** (₹) |
| 5 | Set **Duration (Months)** |
| 6 | Add features to the **Features Included** child table |
| 7 | Check **Is Active** to make it available for sale |
| 8 | Save |

✅ **Expected Result:** Plan becomes available in the dropdown when selling subscriptions.

---

### 2.3 SOP — Activating a Subscription

**Who:** Front Desk Executive  
**When:** After member pays for a plan

| Step | Action |
|---|---|
| 1 | Go to **Member Management → Member Subscription** |
| 2 | Click **+ New** |
| 3 | Select the **Member** and the desired **Membership Plan** |
| 4 | Enter **Start Date** |
| 5 | System automatically calculates **End Date** and **Total Amount** |
| 6 | Enter **Paid Amount** |
| 7 | Save and **Submit** |

✅ **Expected Result:** A Sales Invoice is auto-generated. Member record updates with `Current Membership Plan` and `Subscription End Date`.

---

### 2.4 SOP — Freezing Subscriptions

**Who:** Front Desk Executive / Fitness Manager  
**When:** When a member requests a temporary hold on their account

| Step | Action |
|---|---|
| 1 | Go to **Member Management → Subscription Freeze** |
| 2 | Click **+ New** |
| 3 | Select the **Member** |
| 4 | Set **Freeze Start Date** and **Freeze End Date** |
| 5 | Enter the **Reason** for the freeze |
| 6 | The system calculates **Days Frozen** |
| 7 | Save and **Submit** |

✅ **Expected Result:** The member's original Subscription End Date is automatically extended by the number of Days Frozen. Status changes to *Active*.

---

### 2.5 SOP — Attendance Tracking (QR / Biometric)

**Who:** Facility Supervisor / System  
**When:** Daily when members enter the gym

| Step | Action |
|---|---|
| 1 | Go to **Member Management → Member Attendance** |
| 2 | Click **+ New** |
| 3 | Set the **Attendance Date** (default is Today) |
| 4 | (Manual Mode) In the **Attendance Lines** table, add the member and mark **Status** as *Present* |
| 5 | (Automated Mode) API calls from the QR Scanner/Biometric automatically populate this document |
| 6 | Save and **Submit** at the end of the day |

---

### 2.6 SOP — Managing Referral Rewards

**Who:** Front Desk Executive  
**When:** A member successfully converts a lead

| Step | Action |
|---|---|
| 1 | Go to **Member Management → Referral Record** |
| 2 | Click **+ New** |
| 3 | Select the **Referrer** (Existing Member) |
| 4 | Enter the **Referred Name**, **Email**, and **Contact** |
| 5 | Enter **Reward Points** earned |
| 6 | Set **Status** to *Converted* once standard purchase happens |
| 7 | Save |

---

## 3. Module 2 — Class & Schedule Management

> **Purpose:** Manage group exercises, yoga sessions, trainer assignments, and member bookings smoothly.

---

### 3.1 SOP — Creating Class Types

**Who:** Fitness Manager  
**When:** When introducing a new class category

| Step | Action |
|---|---|
| 1 | Go to **Class Management → Class Type** |
| 2 | Click **+ New** |
| 3 | Enter **Class Name** (e.g., "Zumba Advanced") |
| 4 | Set **Max Capacity** |
| 5 | Enter **Credit Cost** (number of credits required per session) |
| 6 | Add **Description** and Save |

---

### 3.2 SOP — Configuring Class Schedules

**Who:** Fitness Manager  
**When:** Setting up the weekly timetable

| Step | Action |
|---|---|
| 1 | Go to **Class Management → Class Schedule** |
| 2 | Click **+ New** |
| 3 | Select **Class Type** |
| 4 | Assign the **Trainer** and select the **Facility** (Room/Studio) |
| 5 | Choose the **Day of Week** |
| 6 | Enter **Start Time** and **End Time** |
| 7 | Set **Status** to *Active* |
| 8 | Save |

---

### 3.3 SOP — Member Booking & Waitlist Flow

**Who:** Front Desk / Member (Portal)  
**When:** A member wants to attend a scheduled class

| Step | Action |
|---|---|
| 1 | Go to **Class Management → Class Enrollment** |
| 2 | Click **+ New** |
| 3 | Select the **Member** and the **Class Schedule** |
| 4 | Enter the specific **Enrollment Date** |
| 5 | If the class is full, system forces **Status** to *Waitlisted* |
| 6 | If space available, set **Status** to *Confirmed* |
| 7 | Save and **Submit** |

✅ **Expected Result:** Member credits are deducted. System updates the class occupancy count.

---

### 3.4 SOP — Class Cancelation & No-Show Handling

**Who:** Front Desk Executive  
**When:** Member absentee verification

| Step | Action |
|---|---|
| 1 | Open the existing **Class Enrollment** document |
| 2 | If member calls to cancel early, click **Cancel** |
| 3 | If member didn't show up, change status or handle credit refund per business logic |
| 4 | Waitlisted members automatically notify Front Desk to move them to *Confirmed* |

---

## 4. Module 3 — Trainer & Staff Management

> **Purpose:** Oversee trainer availability, certifications, personal training sessions, and calculate commissions accurately.

---

### 4.1 SOP — Trainer Profile Setup

**Who:** Fitness Manager / HR  
**When:** Hiring a new trainer

| Step | Action |
|---|---|
| 1 | Go to **Trainer Management → Trainer Profile** |
| 2 | Click **+ New** |
| 3 | Enter **Trainer Name**, **Specialization**, and **Contact Info** |
| 4 | Under **Certifications**, list all active certs and their **Expiry Dates** |
| 5 | Select whether they are **In House** or **Freelance** |
| 6 | Set their **Base Commission Rate (%)** |
| 7 | Save |

✅ **Expected Result:** Trainer is visible in scheduling. System will alert when certifications near expiry.

---

### 4.2 SOP — PT Assignment & Availability

**Who:** Fitness Manager  
**When:** Allocating a trainer to a specific member

| Step | Action |
|---|---|
| 1 | Go to **Trainer Management → PT Assignment** |
| 2 | Click **+ New** |
| 3 | Select **Member** and **Trainer** |
| 4 | Enter **Start Date**, **End Date**, and **Total Sessions** |
| 5 | Save and Submit |

---

### 4.3 SOP — Trainer Commission Review

**Who:** Accounts Executive / Fitness Manager  
**When:** End of the week/month to disburse pay

| Step | Action |
|---|---|
| 1 | Go to **Trainer Management → Trainer Commission** |
| 2 | Click **+ New** |
| 3 | Select the **Trainer** and define the **Period Start** and **Period End** |
| 4 | System calculates **Total Sessions Taken** |
| 5 | System auto-calculates **Calculated Commission** |
| 6 | Set **Status** to *Approved* |
| 7 | Save and Submit |

---

## 5. Module 4 — Facility & Equipment Management

> **Purpose:** Track equipment health, manage AMCs, log breakdowns, and reduce facility downtime.

---

### 5.1 SOP — Equipment Registration

**Who:** Facility Supervisor  
**When:** Buying new gym equipment

| Step | Action |
|---|---|
| 1 | Go to **Facility Management → Equipment Register** |
| 2 | Click **+ New** |
| 3 | Enter **Equipment Name**, **Category**, and **Serial Number** |
| 4 | Enter **Purchase Date** and link the **Asset Reference** |
| 5 | Set **Status** to *Operational* |
| 6 | Save |

---

### 5.2 SOP — Maintenance Scheduling & AMC Review

**Who:** Facility Supervisor  
**When:** Setting up preventive maintenance

| Step | Action |
|---|---|
| 1 | Go to **Facility Management → Maintenance Schedule** |
| 2 | Click **+ New** |
| 3 | Select the **Facility** |
| 4 | In the **Equipment Involved** table, add all relevant items |
| 5 | Set **Scheduled Date** and assign a **Maintenance Vendor** |
| 6 | Set **Status** to *Scheduled* |
| 7 | Save |

---

### 5.3 SOP — Equipment Breakdown Logging

**Who:** Trainer / Front Desk  
**When:** A machine breaks on the floor

| Step | Action |
|---|---|
| 1 | Go to **Equipment Register** → Open the broken item |
| 2 | Change **Status** from *Operational* to *Out of Service* |
| 3 | Create a **Maintenance Schedule** ticket as an immediate repair task |
| 4 | Inform the Facility Supervisor |

---

## 6. Module 5 — Health & Fitness Assessment

> **Purpose:** Provide value to members by tracking their body metrics, fitness tests, and long-term goals.

---

### 6.1 SOP — Initial Health Assessment

**Who:** Trainer / Dietitian  
**When:** During member orientation

| Step | Action |
|---|---|
| 1 | Go to **Health Assessment → Assessment Goal** |
| 2 | Click **+ New** |
| 3 | Select **Member** and enter **Target Weight** |
| 4 | Define the **Target Date** |
| 5 | Choose **Goal Type** (e.g., Weight Loss, Hypertrophy) |
| 6 | Set **Status** to *In Progress* |
| 7 | Save |

---

### 6.2 SOP — Body Metric Logging

**Who:** Trainer / Member (Portal)  
**When:** Every 2 weeks / monthly weigh-in

| Step | Action |
|---|---|
| 1 | Go to **Health Assessment → Body Metric Log** |
| 2 | Click **+ New** |
| 3 | Select **Member** and select **Log Date** |
| 4 | Enter **Weight (kg)**, **Height (cm)** |
| 5 | System auto-calculates **BMI** |
| 6 | Fill in advanced metrics: **Body Fat %**, **Muscle Mass**, measurements |
| 7 | Attach progress photos if requested |
| 8 | Save |

---

## 7. Module 6 — Nutrition & Diet Management

> **Purpose:** Generate structured meal plans, calculate macros, and track dietary compliance.

---

### 7.1 SOP — Food Item Creation

**Who:** Dietitian  
**When:** Expanding the nutrition database

| Step | Action |
|---|---|
| 1 | Go to **Nutrition → Food Item** |
| 2 | Click **+ New** |
| 3 | Enter **Food Name** (e.g., "Boiled Egg") |
| 4 | Provide **Calories**, **Protein**, **Carbs**, and **Fats** per standard serving |
| 5 | Save |

---

### 7.2 SOP — Diet Plan Assignment

**Who:** Dietitian  
**When:** Crafting a regimen for a member

| Step | Action |
|---|---|
| 1 | Go to **Nutrition → Diet Plan** |
| 2 | Click **+ New** |
| 3 | Select **Member** |
| 4 | In the **Meals Table**, select: **Food Item**, **Quantity**, **Meal Type** (Breakfast/Lunch/Dinner) |
| 5 | System automatically calculates total **Macros** and **Calories** |
| 6 | Save and Submit |
| 7 | Print or Email the structured PDF to the member |

---

## 8. Module 7 — Billing & Finance

> **Purpose:** Handle cash reconciliations, walk-in revenues, EMIs, and formal invoicing efficiently.

---

### 8.1 SOP — Membership Invoice Generation

**Who:** Accounts Executive / System  
**When:** Collecting payment for subscription

| Step | Action |
|---|---|
| 1 | Go to **Billing → Membership Invoice** |
| 2 | Most invoices auto-generate when a **Member Subscription** is submitted. |
| 3 | If manual, click **+ New** |
| 4 | Select **Member**, **Subscription**, and enter **Amount** |
| 5 | Record the **Paid Amount**. System calculates **Outstanding** |
| 6 | Select **Payment Mode** (Cash, Card, UPI) |
| 7 | Change **Status** to *Paid* or *Partially Paid* |
| 8 | Save and Submit |

---

### 8.2 SOP — Walk-in POS Billing

**Who:** Front Desk Executive  
**When:** Guest wants a day-pass

| Step | Action |
|---|---|
| 1 | Go to **Billing → Walk-In Payment** |
| 2 | Click **+ New** |
| 3 | Enter **Guest Name** and **Contact Detail** |
| 4 | Enter **Service Details** (e.g., "Day Pass") |
| 5 | Enter **Amount** |
| 6 | Save and Submit |

---

### 8.3 SOP — Handling EMI Payments

**Who:** Accounts Executive  
**When:** Member purchases an Annual plan via installments

| Step | Action |
|---|---|
| 1 | Go to **Billing → EMI Schedule** |
| 2 | Click **+ New** |
| 3 | Select **Member** and enter **Total Amount** |
| 4 | Specify **No. of Installments** and **Start Date** |
| 5 | Save. System auto-generates the **EMI Instalment** child rows with Due Dates. |
| 6 | When the member pays an installment, change the specific row's **Payment Status** from *Pending* to *Paid*. |
| 7 | Submit once all are paid |

---

### 8.4 SOP — Daily Cash Reconciliation

**Who:** Front Desk Executive / Accounts  
**When:** End of the shift

| Step | Action |
|---|---|
| 1 | Go to **Billing → Daily Cash Reconciliation** |
| 2 | Click **+ New** |
| 3 | Enter **Opening Balance** |
| 4 | System pulls all Walk-In and Invoice payments to fill **Cash Received**, **Card Received**, **Total Received** |
| 5 | Verify physical cash matches **Closing Balance** |
| 6 | Add any discrepancy remarks |
| 7 | Save and Submit |

---

## 9. Module 8 — Reports & Analytics

> **Purpose:** High-level dashboard overviews of operational and financial health.

**Key Reports to Review:**

| Report Name | Who Reviews | When | Purpose |
|---|---|---|---|
| Active Members Report | Fitness Manager | Weekly | Ensure list matches active subscriptions |
| Attendance Summary | Facility Supervisor | Weekly | Identify peak gym hours |
| Revenue Summary | Gym Owner / CFO | Monthly | Check total inflows across modes |
| Subscription Expiry | Front Desk | Daily | Call members whose plans expire in 7 days |
| Trainer Performance | Fitness Manager | Monthly | Evaluate PT conversions and class ratings |

---

## 10. Daily / Weekly / Monthly Operating Checklist

### 10.1 Daily (10 minutes)

| Task | Who | Where |
|---|---|---|
| ☐ Review Daily Cash Reconciliation | Accounts | Daily Cash Reconciliation |
| ☐ Process all new Walk-in Payments | Front Desk | Walk-In Payment |
| ☐ Check Subscription Expiry Report and call leads | Front Desk | Reports |
| ☐ Mark Class Attendance | Trainer | Class Enrollment |

---

### 10.2 Weekly (30 minutes)

| Task | Who | Where |
|---|---|---|
| ☐ Approve Trainer Commissions | Fitness Mgr | Trainer Commission |
| ☐ Review Equipment breakdown tickets | Facility | Equipment Register |
| ☐ Review Waitlisted Class Enrollments | Front Desk | Class Enrollment |

---

### 10.3 Monthly (2 hours)

| Task | Who | Where |
|---|---|---|
| ☐ Track Unpaid EMI defaults and restrict entry | Accounts | EMI Schedule |
| ☐ Review overall Revenue Summary report | Owner | Reports |
| ☐ Update Member Body Metrics | Trainer | Body Metric Log |
| ☐ Review overall Member Retention rate | Owner | Dashboard |

---

### 10.4 Quarterly & Annually

| Task | Who | Where |
|---|---|---|
| ☐ Evaluate AMC Renewals for Equipment | Facility | Maintenance Schedule |
| ☐ Review Trainer Certification Expirations | HR | Trainer Profile |
| ☐ Branch Profitability Analysis | Accounts | Reports |
| ☐ Annual Memberships Audit | Owner | Member Subscription |

---

## 11. User Roles & Who Does What

| Feature | Fitness Manager | Front Desk | Trainer | Dietitian | Accounts |
|---|---|---|---|---|---|
| Member Management | ✅ Full | ✅ Create | 👁 Read | 👁 Read | 👁 Read |
| Member Subscription | ✅ Full | ✅ Create | ❌ | ❌ | 👁 Read |
| Class Schedule | ✅ Full | 👁 Read | 👁 View Own | ❌ | ❌ |
| Class Enrollment | ✅ Full | ✅ Create | 👁 Read | ❌ | ❌ |
| Trainer Profile | ✅ Full | 👁 Read | 👁 View Own | ❌ | 👁 Read |
| Equipment Register | 👁 Read | 👁 Read | 👁 Read | ❌ | ❌ |
| Maintenance Status | 👁 Read | 👁 Read | ❌ | ❌ | 👁 Read |
| Body Metric Log | 👁 Read | ❌ | ✅ Full | ✅ Full | ❌ |
| Diet Plan | 👁 Read | ❌ | 👁 Read | ✅ Full | ❌ |
| Membership Invoice | 👁 Read | 👁 Read | ❌ | ❌ | ✅ Full |
| EMI Schedule | 👁 Read | ❌ | ❌ | ❌ | ✅ Full |
| Cash Reconciliation | 👁 Read | ✅ Create | ❌ | ❌ | ✅ Full |

---

## 12. Frequently Asked Questions

**Q1: A subscription expired, but the member wants 1 day grace access. How?**  
A: Create an overriding "Walk-in Payment" for zero cost, or manually extend the End Date in their Member Subscription document by 1 day as an exception.

---

**Q2: How do I refund a member?**  
A: Open **Refund Request**, link their original Membership Invoice or Payment Entry, set the Refund Amount and Status to "Approved". Issue the refund via your bank portal and mark it "Completed".

---

**Q3: How does the class waitlist work?**  
A: If a class capacity is 20 and the 21st person books, their `Class Enrollment` stays status "Waitlisted". If someone cancels, the Front Desk selects the next waitlisted user and changes their status to "Confirmed".

---

**Q4: How do I update body metrics?**  
A: Go to `Body Metric Log`, create a new document for the member, enter Date, Weight, and Height. Hit Save. The system will auto-calculate BMI and keep historical records.

---

**Q5: How are trainer commissions calculated?**  
A: By pulling the `Base Commission Rate` from their `Trainer Profile`, and multiplying it by the number of completed PT assignments or Classes taken in that specific date range within the `Trainer Commission` document.

---

**Q6: Why didn't attendance sync?**  
A: Ensure the Biometric/QR tool API is pointed to the correct endpoint `/api/resource/Member Attendance` and that the Member ID exactly matches the biometric ID in the system.

---

**Q7: How to handle an EMI default?**  
A: Open the `EMI Schedule`, find the overdue `EMI Instalment` row, and change its Payment Status to "Failed". The Accounts Executive must then follow up. You may temporarily change the `Member` status to "Suspended" to revoke access.

---

**Q8: How to handle a last-minute class cancellation by a trainer?**  
A: Open the `Class Schedule`, change Status to "Cancelled". Open the related `Class Enrollment` records and refund credits or change the schedule link manually, then notify members.

---

**Q9: How do I renew a membership?**  
A: Create a NEW `Member Subscription` document for the member with the new Start Date. The system handles overlapping logic and updates the member's profile automatically.

---

**Q10: How do I generate an invoice manually?**  
A: Go to `Membership Invoice`, click New, select the member, and enter the amount and due date. Once saved and submitted, it will impact the accounts LEDGER directly.

---

**Q11: How do I reset a member's QR access?**  
A: Go to the `Member` profile, verify their status is `Active`. If the QR code is lost, re-send the welcome email via the print menu or regenerate the QR via custom script button (if configured).

---

**Q12: How to track equipment under AMC?**  
A: In `Equipment Register`, log the vendor details and link the AMC Contract under references. Set up recurring `Maintenance Schedule` records for the quarterly visits.

---

**Q13: How do I view who owes the gym money?**  
A: Go to the `Revenue Summary` report or filter `Membership Invoice` where Status is "Unpaid" or "Overdue".

---

**Q14: How does a member pause their gym membership for travel?**  
A: Use the `Subscription Freeze` DocType. Input the start and end dates of travel. The system automatically pushes their membership expiry date forward.

---

**Q15: How do I export my active members list to Mailchimp?**  
A: Go to the `Member` list view, filter by `Status = Active`, click Menu (⋮) -> Export -> Download as CSV.

---

## 13. Support & Contact

| Channel | Details |
|---|---|
| 📧 Email | support@fitness-wellness.com |
| 📖 Documentation | https://docs.fitness-wellness.com |
| 🐛 Ticketing | Dashboard -> Help -> Report Issue |
| 📱 WhatsApp | +91-XXXXXXXXXX (Support Hotline) |

---

*© 2026 Fitness & Wellness Systems — Built with ❤️ for Health Centres*  
*Powered by Frappe Framework & ERPNext v15*
