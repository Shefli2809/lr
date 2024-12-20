# Cost Minimization Approach & Django Employee Management System

This project consists of two parts:

1. **Cost Minimization Approach**: A solution to minimize the cost of transporting goods based on available boxes with different volumes and costs for different cities.
2. **Django Project for Employee Management**: A web application to manage employee records, allowing admins to create, edit, and delete employee records, while employees can update their personal information.

## Table of Contents

1. [Cost Minimization Approach](#cost-minimization-approach)
    - [Problem Overview](#problem-overview)
    - [Steps Taken](#steps-taken)
    - [Cost Calculation](#cost-calculation)
    - [Dictionary for Storing Results](#dictionary-for-storing-results)
    - [Edge Cases](#edge-cases)
    - [Code Summary](#code-summary)
  
2. [Django Employee Management System](#django-employee-management-system)
    - [Project Setup](#project-setup)
    - [Models](#models)
    - [Authentication](#authentication)
    - [CRUD Operations](#crud-operations)
    - [Views and Templates](#views-and-templates)
    - [Redirect After Save Changes](#redirect-after-save-changes)
    - [Permissions and Access Control](#permissions-and-access-control)

---

## Cost Minimization Approach

### Problem Overview
The goal of this approach is to minimize the transportation cost for goods, given various boxes with different volumes and costs for different cities. The objective is to fill the given capacity optimally with the available boxes while minimizing the cost.

### Steps Taken
1. **Input**: The system takes in the transportation time and capacity.
2. **Box Types**: The boxes come in predefined sizes (XS, S, M, L, XL, XXL), each associated with a cost and volume for each city.
3. **Cities**: The cities considered in this system are **Delhi**, **Mumbai**, and **Kolkata**.
4. **Cost Minimization**: The algorithm:
   - Filters out boxes with no cost (i.e., unavailable boxes).
   - Calculates the cost per unit volume for each available box.
   - Sorts the boxes based on their cost-efficiency (lowest cost per unit volume).
   - Fills the capacity with the cheapest boxes until it's full.
   - If there’s remaining capacity, it adds the box with the lowest cost to complete the capacity.

### Cost Calculation
- **Cost per Volume Ratio**: For each box in a city, we compute the cost per volume (i.e., `cost/volume`).
- **Sorting Boxes**: We prioritize filling the capacity with boxes that have the lowest cost per volume.
- **Filling Capacity**: Start with the cheapest box and fill the remaining capacity. If the remaining capacity is non-zero, the algorithm selects the lowest-cost box to complete the remaining volume.

### Dictionary for Storing Results
- The program uses a dictionary to store box types and their respective costs for each city.
- It ensures no redundant entries are stored and keeps track of the number of boxes used to fill the total capacity.

### Edge Cases
- If the **time** or **capacity** is zero, the system returns zero costs for all cities.
- If there’s no available box that fits the remaining capacity, it chooses the box with the lowest cost to minimize the total cost.

### Code Summary
The algorithm iterates over each city, processes the box data, calculates the minimum cost, and tracks the number of boxes used. This ensures an optimal and cost-effective way to fill the transportation capacity while handling edge cases.

---

## Django Employee Management System

### Project Setup
1. **Django Project Setup**:
   - The project is named `companyProject`.
   - An app called `companyApp` handles employee management functionalities.
  
2. **App Structure**:
   - The main application (`companyApp`) manages the employee-related models, views, and templates.
   - The project utilizes Django's built-in authentication system for managing users and employee data.

### Models
1. **Employee Model**: Stores employee information (e.g., name, position, salary).
2. **User Model**: Uses Django’s default `User` model to manage user accounts.
3. **Relationship**: A one-to-one relationship is established between the `Employee` model and Django's default `User` model.

### Authentication
1. **Login System**: Employees and admins can log in using their email and password.
2. **Admin Interface**: Admins can manage employees through the Django admin interface, which provides full CRUD functionality (create, read, update, delete).

### CRUD Operations
1. **Admin CRUD Operations**:
   - Admin users can create, read, update, and delete employee records via the Django admin interface.
2. **Employee Profile Editing**:
   - Employees can edit their personal information (e.g., email, position) via a custom form.
3. **Admin Edit**:
   - Admins can modify employee details on a dedicated employee edit page.

### Views and Templates
1. **Dashboard**:
   - A user-friendly dashboard for both admins and employees to manage their profile and employee records.
2. **Edit Profile**:
   - Employees can edit their profile using a form linked to their account.
3. **Admin Dashboard**:
   - Admins have a special dashboard for managing employee records.
4. **Templates**:
   - Django templates are used to render views for displaying employee details and forms.

### Redirect After Save Changes
1. **Admin Redirection**:
   - After updating an employee’s details, admins are redirected to the admin dashboard.
   - The system uses Django’s `redirect()` function to handle post-update redirection.
  
### Permissions and Access Control
1. **Access Control**:
   - The `@login_required` decorator ensures that only logged-in users can access certain views, such as employee profile editing or employee management by admins.
2. **Authorization**:
   - Different user roles (admin, employee) have different levels of access to views and functionalities.

---

## How to Run the Projects

### Cost Minimization Approach
1. **Input Data**:
   - Provide the time and capacity along with the box data (volume, cost for each city).
2. **Run the Algorithm**:
   - The algorithm will compute the minimum cost for transporting goods.

### Django Employee Management System
1. **Setup Django**:
   - Install Django: `pip install django`
   - Create a project and app: `django-admin startproject companyProject` and `python manage.py startapp companyApp`
2. **Database Migrations**:
   - Run migrations: `python manage.py migrate`
3. **Create Superuser**:
   - Create an admin user to access the Django admin interface: `python manage.py createsuperuser`
4. **Run Server**:
   - Start the development server: `python manage.py runserver`

---
