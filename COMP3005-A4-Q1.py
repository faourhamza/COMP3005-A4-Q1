import psycopg2
from psycopg2 import sql

# Prompt the user for database connection params
def get_db_params():
    dbname = input("Enter the database name: ")
    user = input("Enter the username: ")
    password = input("Enter the password: ")
    host = input("Enter the host: ")
    port = input("Enter the port: ")

    return {
        'dbname': dbname,
        'user': user,
        'password': password,
        'host': host,
        'port': port
    }

# Connect to the database
def connect():
    try:
        db_params = get_db_params()
        conn = psycopg2.connect(**db_params)
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database.")
        print(e)
        return None

# Display all records from the students table
def get_all_students(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM students;')
            rows = cursor.fetchall()
            for row in rows:
                # Convert the date to a string in the format YYYY-MM-DD
                formatted_date = row[4].strftime('%Y-%m-%d')
                print(row[0], row[1], row[2], row[3], formatted_date)
    except psycopg2.Error as e:
        print("Error fetching all students.")
        print(e)

# Add a student to the table
def add_student(conn):
    try:
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        email = input("Enter the email: ")
        enrollment_date = input("Enter the enrollment date (YYYY-MM-DD): ")

        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s)
                RETURNING student_id;
            ''', (first_name, last_name, email, enrollment_date))
            new_student_id = cursor.fetchone()[0]
        conn.commit()
        print(f"Student with ID {new_student_id} added successfully.")
    except psycopg2.IntegrityError as e:
        print("Error adding student. Email already exists or invalid data.")
    except psycopg2.Error as e:
        print("Error adding student.")
        print(e)


# Update the email address for a student
def update_student_email(conn):
    try:
        student_id = input("Enter the student ID to update: ")
        new_email = input("Enter the new email: ")

        with conn.cursor() as cursor:
            cursor.execute('''
                UPDATE students
                SET email = %s
                WHERE student_id = %s
                RETURNING student_id;
            ''', (new_email, student_id))
            updated_student_id = cursor.fetchone()

        if updated_student_id:
            conn.commit()
            print(f"Email updated successfully for student with ID {updated_student_id}.")
        else:
            print(f"Invalid student ID. Student with ID {student_id} doesn't exist.")
    except psycopg2.IntegrityError as e:
        print("Error updating email. New email already exists or invalid data.")
    except psycopg2.Error as e:
        print("Error updating email.")
        print(e)

# Delete a student from the table
def delete_student(conn):
    try:
        student_id = input("Enter the student ID to delete: ")

        with conn.cursor() as cursor:
            cursor.execute('''
                DELETE FROM students
                WHERE student_id = %s
                RETURNING student_id;
            ''', (student_id,))
            deleted_student_id = cursor.fetchone()

        if deleted_student_id:
            conn.commit()
            print(f"Student with ID {deleted_student_id} deleted successfully.")
        else:
            print(f"Invalid student ID. Student with ID {student_id} doesn't exist.")
    except psycopg2.Error as e:
        print("Error deleting student.")
        print(e)

# Main function
def main():
    # Connect to the database
    conn = connect()
    if conn is None:
        return

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Update Student Email")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student(conn)
        elif choice == '2':
            update_student_email(conn)
        elif choice == '3':
            delete_student(conn)
        elif choice == '4':
            get_all_students(conn)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()