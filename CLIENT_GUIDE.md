# Client Guide: Managing Schemes on Sovereign Chits Website

This guide will help you manage chit fund schemes through the Django admin panel.

## Table of Contents

1. [Logging In](#logging-in)
2. [Dashboard Overview](#dashboard-overview)
3. [Adding a New Scheme](#adding-a-new-scheme)
4. [Editing an Existing Scheme](#editing-an-existing-scheme)
5. [Deleting a Scheme](#deleting-a-scheme)
6. [Understanding Scheme Fields](#understanding-scheme-fields)
7. [Tips and Best Practices](#tips-and-best-practices)
8. [Troubleshooting](#troubleshooting)

---

## Logging In

### Step 1: Access the Admin Panel

1. Open your web browser (Chrome, Firefox, Safari, or Edge)
2. Go to your website's admin URL:
   - If your website is `www.sovereignchits.com`
   - Admin URL will be: `www.sovereignchits.com/admin/`
   - Or: `https://yourdomain.com/admin/`

### Step 2: Enter Your Credentials

1. You will see a login page with two fields:
   - **Username**: Enter your admin username (admin)
   - **Password**: Enter your admin password (admin)
2. Click the **"Log in"** button

### Step 3: Successful Login

- If credentials are correct, you'll see the Django admin dashboard
- If incorrect, you'll see an error message - try again

**Forgot Password?** Contact your website administrator to reset it.

---

## Dashboard Overview

After logging in, you'll see the admin dashboard with:

- **WEBSITE** section (on the left sidebar)
  - **Schemes** - Click here to manage schemes
- **AUTHENTICATION AND AUTHORIZATION** section
  - **Users** - Manage user accounts (admin only)
  - **Groups** - Manage user groups (admin only)

---

## Adding a New Scheme

### Step 1: Navigate to Schemes

1. In the left sidebar, find **WEBSITE**
2. Click on **Schemes**
3. You'll see a list of all existing schemes (if any)

### Step 2: Add New Scheme

1. Click the **"Add Scheme"** button (top right, green button)
2. You'll see a form with multiple fields

### Step 3: Fill in Scheme Details

#### Basic Information Section

- **Name** (Required):

  - Enter the scheme name
  - Example: `50*20000(1000000)` or `Monthly Savings Plan`
  - This will be displayed as the scheme title

- **Is Active** (Checkbox):

  - ✅ Checked = Scheme will appear on the website
  - ☐ Unchecked = Scheme will be hidden from the website
  - **Default**: Checked

- **Coming Soon** (Checkbox):
  - ✅ Checked = Shows "Coming soon..." message (use when details are incomplete)
  - ☐ Unchecked = Shows full scheme details
  - **Default**: Unchecked

#### Scheme Details Section

- **Sala Amount (₹)**:

  - Enter the total sala amount
  - Example: `1000000` (for ₹10,00,000)
  - Can be left empty for "Coming Soon" schemes

- **No. of Instalments**:

  - Enter the number of instalments
  - Example: `50` (for 50 months)
  - Can be left empty for "Coming Soon" schemes

- **Auction Bid**:

  - Enter auction bid information
  - Example: `25%` or `30%`
  - Can be left empty for "Coming Soon" schemes

- **Period (Weeks/Months)**:

  - Enter the period type
  - Example: `Months` or `Weeks`
  - Can be left empty for "Coming Soon" schemes

- **Instalment Amount (₹)**:

  - Enter the monthly instalment amount
  - Example: `20000` (for ₹20,000)
  - Can be left empty for "Coming Soon" schemes

- **Auction Date Info**:
  - Enter information about auction dates
  - Example: `Every 9th day of the month` or `First Monday of every month`
  - Can be left empty for "Coming Soon" schemes

#### Display Section

- **Header Color**:
  - Enter a CSS color class
  - Common options:
    - `gradient-primary` (Blue gradient - default)
    - `bg-gradient-to-r from-green-500 to-emerald-600` (Green)
    - `bg-gradient-to-r from-purple-500 to-pink-600` (Purple)
    - `bg-gradient-to-r from-orange-500 to-amber-600` (Orange)
    - `bg-gray-800` (Dark gray)
  - **Default**: `gradient-primary`

### Step 4: Save the Scheme

1. Review all the information you entered
2. Click one of these buttons at the bottom:
   - **"Save"** - Saves and returns to schemes list
   - **"Save and add another"** - Saves and opens a new form
   - **"Save and continue editing"** - Saves and stays on the same form

### Step 5: Verify

1. After saving, you'll see a success message
2. The scheme will appear in the schemes list
3. Visit your website's `/schemes/` page to see it live
4. New schemes appear **at the end** of the list (after older schemes)

---

## Editing an Existing Scheme

### Step 1: Find the Scheme

1. Go to **WEBSITE** → **Schemes**
2. Browse the list to find the scheme you want to edit
3. You can use the search box to find schemes by name

### Step 2: Open the Scheme

1. Click on the **scheme name** (it will be a clickable link)
2. Or click the **"Change"** link next to the scheme

### Step 3: Make Changes

1. Update any fields you want to change
2. All fields work the same as when adding a new scheme

### Step 4: Save Changes

1. Click **"Save"** at the bottom
2. You'll see a success message: "Scheme was changed successfully"
3. Changes will appear on the website immediately

---

## Deleting a Scheme

### Method 1: Delete from List View

1. Go to **WEBSITE** → **Schemes**
2. Find the scheme you want to delete
3. Check the checkbox next to the scheme name
4. From the **"Action"** dropdown at the top, select **"Delete selected schemes"**
5. Click **"Go"**
6. Confirm the deletion

### Method 2: Delete from Edit View

1. Open the scheme you want to delete (click on its name)
2. Scroll to the bottom of the page
3. Click the red **"Delete"** button
4. You'll see a confirmation page
5. Click **"Yes, I'm sure"** to confirm

⚠️ **Warning**: Deletion is permanent! The scheme will be removed from the website immediately.

---

## Understanding Scheme Fields

### When to Use "Coming Soon"

Mark a scheme as "Coming Soon" when:

- You're planning a new scheme but don't have all details yet
- You want to announce a scheme before it's fully ready
- Some key information (like instalments or auction bid) is missing

**Coming Soon schemes will show:**

- Scheme name
- Sala amount (if provided)
- "Coming soon..." message
- No detailed information

### When to Use "Is Active"

- **Checked (Active)**: Scheme appears on the website for customers to see
- **Unchecked (Inactive)**: Scheme is hidden from the website but kept in the database

**Use Inactive when:**

- Temporarily hiding a scheme
- Archiving old schemes
- Testing new schemes before making them public

### Header Color Examples

Here are some ready-to-use header color options:

| Color          | Code to Enter                                    |
| -------------- | ------------------------------------------------ |
| Blue (Default) | `gradient-primary`                               |
| Green          | `bg-gradient-to-r from-green-500 to-emerald-600` |
| Purple         | `bg-gradient-to-r from-purple-500 to-pink-600`   |
| Orange         | `bg-gradient-to-r from-orange-500 to-amber-600`  |
| Teal           | `bg-gradient-to-r from-teal-500 to-cyan-600`     |
| Pink           | `bg-gradient-to-r from-pink-500 to-rose-600`     |
| Dark Gray      | `bg-gray-800`                                    |

---

## Tips and Best Practices

### 1. Naming Schemes

- Use clear, descriptive names
- Include key numbers if helpful (e.g., `50*20000(1000000)`)
- Keep names consistent for similar schemes

### 2. Completing Information

- Fill in all fields for active schemes
- Double-check numbers (amounts, instalments)
- Use clear, readable text for auction dates

### 3. Organizing Schemes

- New schemes automatically appear at the end
- Oldest schemes appear first
- Use "Is Active" to control visibility

### 4. Testing

- After adding/editing, always check the website
- Visit `/schemes/` page to see how it looks
- Test on mobile devices too

### 5. Regular Updates

- Keep scheme information current
- Update auction dates if they change
- Mark completed schemes as inactive

---

## Troubleshooting

### Problem: Can't log in

**Solutions:**

- Double-check username and password (case-sensitive)
- Make sure Caps Lock is off
- Contact administrator if password is forgotten

### Problem: Scheme not appearing on website

**Check:**

- Is "Is Active" checkbox checked?
- Did you save the scheme?
- Try refreshing the website page (Ctrl+F5 or Cmd+Shift+R)

### Problem: Changes not showing

**Solutions:**

- Make sure you clicked "Save"
- Clear browser cache and refresh
- Check if you're editing the correct scheme

### Problem: Can't delete a scheme

**Check:**

- Make sure you have admin permissions
- Try refreshing the page
- Contact administrator if issue persists

### Problem: Numbers not displaying correctly

**Solutions:**

- Enter numbers without commas (e.g., `1000000` not `1,000,000`)
- Don't include currency symbols in number fields
- Use only digits and decimal points

### Problem: Header color not working

**Solutions:**

- Make sure you entered the exact code (case-sensitive)
- Try using `gradient-primary` as a test
- Check for typos in the color code

---

## Quick Reference

### Common Tasks

| Task                 | Steps                                     |
| -------------------- | ----------------------------------------- |
| **Add Scheme**       | Schemes → Add Scheme → Fill form → Save   |
| **Edit Scheme**      | Schemes → Click scheme name → Edit → Save |
| **Delete Scheme**    | Schemes → Check box → Action: Delete → Go |
| **Hide Scheme**      | Edit scheme → Uncheck "Is Active" → Save  |
| **Show Coming Soon** | Edit scheme → Check "Coming Soon" → Save  |

### Important URLs

- **Admin Login**: `yourdomain.com/admin/`
- **Schemes Page**: `yourdomain.com/schemes/`
- **Home Page**: `yourdomain.com/`

---

## Getting Help

If you encounter any issues:

1. **Check this guide** first
2. **Try the troubleshooting section**
3. **Contact your website administrator**
4. **Take a screenshot** of any error messages

---

## Security Reminder

- **Never share** your admin login credentials
- **Log out** when finished (click your username → Log out)
- **Use strong passwords**
- **Don't leave admin panel open** on shared computers

---

**Last Updated**: December 2024

For technical support, contact your website administrator.
