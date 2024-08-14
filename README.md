"""
Module: Admin Menu Management

This module provides various administrative functionalities for managing teachers, students, and groups within the system.

Functions:
-----------
1. teacher_management():
   - Provides an interactive menu for managing teachers. Options include:
     1. Creating a new teacher account.
     2. Viewing all teachers.
     3. Adding teachers to groups.
     4. Removing teachers from groups.
     5. Deleting a teacher account.
     6. Returning to the previous menu.
   - After each action, the menu is re-displayed.

2. student_management():
   - Provides an interactive menu for managing students. Options include:
     1. Creating a new student account.
     2. Adding students to groups.
     3. Removing students from groups.
     4. Deleting a student account.
     5. Viewing all students.
     6. Returning to the previous menu.
   - After each action, the menu is re-displayed.

3. group_management():
   - Provides an interactive menu for managing groups. Options include:
     1. Creating a new group.
     2. Viewing all groups.
     3. Deleting a group.
     4. Returning to the previous menu.
   - After each action, the menu is re-displayed.

4. show_admin_menu():
   - Displays the main admin menu with options to:
     1. Access teacher management.
     2. Access student management.
     3. Access group management.
     4. Quit the application.
   - Depending on user choice, it navigates to the relevant management function or quits the application.

Usage:
-------
- Each management function (`teacher_management`, `student_management`, `group_management`) includes options for creating, viewing, updating, and deleting entities within the respective category (teachers, students, groups).
- The `show_admin_menu` function provides the main entry point for admin operations, allowing admins to choose between different management functions or exit the application.
- When performing actions like adding or removing entities from groups, the system will interactively prompt for the necessary details and update the data accordingly.
- The management functions are designed to loop until the user chooses to return to the main menu or quit the application, ensuring a continuous interaction flow.

Notes:
------
- Ensure that all required data files (e.g., `student_manager`, `teacher_manager`) and functions (e.g., `create_teacher`, `show_all_teachers`) are correctly implemented and imported for full functionality.
- Error handling and validation checks are included to ensure the robustness of user inputs and actions.

"""
