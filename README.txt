Hamza Faour
101195438
COMP3005
Assignment 4
Question 1

--VIDEO LINK--
https://youtu.be/lUIiwbc9IUM

--DATABASE SETUP INSTRUCTIONS--
1. Create a new database in pgAdmin 4
2. Run the following query in the database to add the Student table:
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    enrollment_date DATE
);
3. Run the following query in the database to insert students into the table:
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
4. Run the following query to display the students in the table:
SELECT * FROM students;

--STEPS TO COMPILE AND RUN THE APPLICATION--
1. Open the command prompt
2. Change your directory to the same directory with the COMP3005-A4-Q1.py file
3. Type "python COMP3005-A4-Q1.py" in the command prompt and hit enter
4. You will be prompted for the database name, username, password, host, and port, enter the values and hit enter after each one
5. A menu will pop up with 5 options (Add Student, Update Student Email, Delete Student, Display All Students, Exit)
6. Type the number of the option you want and hit enter to run it

--EXPLANATION OF FUNCTIONS--
1. def get_db_params(): prompts the user to enter the information for the database they want to connect to
2. def connect(): uses the acquired databse parameters to connect to the database
3. def get_all_students(conn): displays all the students in the Students table
4. def add_student(conn): adds a student to the Students table based on input from the user
5. def update_student_email(conn): updates the email of a student in the Students table based on input from the user
6. def delete_student(conn): deletes a student in the Students table based on input from the user
7. def main(): main function, runs the menu and calls the other functions