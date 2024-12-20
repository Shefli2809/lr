Cost Minimization Approach

1. Problem Overview:
    The problem involves minimizing the cost of transporting goods based on available boxes with specific volumes and associated costs for different cities. 
    Given a certain time and capacity, the task is to find the optimal way to fill the capacity with boxes that minimize the overall cost.

2. Steps Taken:
    a. The initial input consists of time and capacity.
    b. We have predefined data for different box types (XS, S, M, L, XL, XXL), each with a specified volume and cost for each city.
    c. The cities we consider are: Delhi, Mumbai, Kolkata.

3. Cost Calculation:
    a. For each city, I filter out boxes that have a "None" cost (i.e., unavailable boxes).
    b. I then calculate the cost per volume ratio for the remaining boxes.
    c. I sort these boxes based on the cost per unit volume in ascending order.
    d. I then begin filling the remaining capacity with the sorted boxes, prioritizing cheaper boxes (lower cost per unit volume).
    e. If the remaining capacity is not zero after filling it with available boxes, I add the box with the lowest cost to complete the capacity.

4. Dictionary for Storing Results:
    a. I used a dictionary to store the boxes and their respective costs for each city, ensuring no redundant entries.
    b. If a box type is used more than once to fill the capacity, it’s accounted for in the dictionary with the correct count of boxes.

5. Edge Cases:
    a. If either time or capacity is zero, I return zero costs for all cities.
    b. If there’s no available box for the remaining capacity, I simply choose the one with the lowest cost to minimize the total cost.

6. Output:
    The final result is a dictionary containing the total cost for each city, along with the number of boxes used for each box type.

7. Code Summary:
    The function iterates through each city, processes the box data, and calculates the minimum cost while keeping track of the boxes chosen to fill the capacity.

    The approach ensures that we minimize the cost by filling the remaining capacity with the most cost-effective boxes, and also handles edge cases like zero capacity or time.



Django Project Approach - Employee Management System
This document outlines the approach for implementing an Employee Management System in Django. The system allows an admin user to create, edit, and delete employee records, while employees can edit their personal details. The implementation is done using Django views, forms, and templates.
Approach:
1. Setup Django Project and App:
   - Created a Django project called "companyProject".
   - Created an app called "companyApp" to handle the employee management system.
2. Models:
   - Created two models, "Employee" and "User", to store employee information and user account details.
   - Established a one-to-one relationship between the Employee model and Django's default User model.
3. Authentication:
   - Utilized Django's built-in authentication system to handle user login and permissions.
   - Users can log in using their email and password. Admins can manage employees via the Django admin interface.
4. CRUD Operations for Employees:
   - Admin users have the ability to create, read, update, and delete employee records via the Django admin interface.
   - A custom view was created to allow employees to edit their personal details (e.g., email, position, etc.) via a form.
   - The admin user can also edit employee details through a dedicated employee edit page.
5. Views and Templates:
   - The system includes several views for managing employee data, including a dashboard, login, and employee profile editing pages.
   - Django templates are used to display employee details and forms for editing.
   - Admins can use the employee edit page to change employee details and a "Save Changes" button redirects to the admin dashboard after updates.
6. Redirect After Save Changes:
   - After making changes to an employee's details, admins are redirected to the admin dashboard to ensure seamless workflow.
   - The edit_employee view checks the form submission and performs a redirect using Django's redirect function.
7. Handling Permissions and Access Control:
   - Ensured that only logged-in users can access the edit profile and employee management views.
   - The view uses the @login_required decorator to prevent unauthorized access.
