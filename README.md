# studentenrollmentapp

1) Login screen: The first screen/view should be a login/authentication screen.
You should not be able to access any other screen within the app unless the user has
authenticated himself. So all unauthenticated users should be redirected to the login
page.

2) Base HTML: The base HTML should have all the navigation links. Think Navbar or
Sidebar. This should be common for all individual HTML pages you will be developing.
Django allows you to do this by “extending base.html”

3) Dashboard – Home/Main screen: The main screen/view after login should be a
dashboard. The dashboard can contain information about number of enrolled students,
average GPA, number of seniors, juniors and freshmen, number of courses offered etc.
Try to be innovative with your dashboard designs.

4) Student details: This screen will be an info screen that displays student information (first
name, last name, major, year and GPA). You can use a table to display this info. Use
pagination to limit a single view to show only 10 students at a time. Since there are 20
students, this information would be displayed in two pages.

5) Student Enrollment: This screen shows all the courses a particular student is enrolled in
(Use a drop down to switch between different students). This screen should allow the
users to enroll into courses.

 Each student cannot have more than 3 enrolled courses.
 User should not be able to enroll a student in the same course more than once.

6) Course details: This an info screen that shows all the courses available. You can use a
table to display this information. Paginate this information so that data is displayed in
two pages.

