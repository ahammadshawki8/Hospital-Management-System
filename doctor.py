import psycopg2
from DB_config import config
import constant
import webbrowser as web


def recent_notifications(username, logged_in, limit = 1):
    if logged_in:
        with psycopg2.connect(**config()) as latest:
            cur1 = latest.cursor()
            cur1.execute("""
                SELECT notifications FROM doctor WHERE username = %s;
            """, [username])
            notifications_string = cur1.fetchall()[0][0]
            list_of_notifications = notifications_string.split(", ")
            cur1.close()
        latest.close()
        return list_of_notifications[-limit:] if limit < len(list_of_notifications) else list_of_notifications[-len(list_of_notifications):]


def notify_admin(notification, my_username, admin_username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as add_notifications:
            cur1 = add_notifications.cursor()
            cur1.execute(f"""
                SELECT notifications FROM admin WHERE username = '{admin_username}';
            """)
            notifications_string = cur1.fetchall()[0][0]
            list_of_notifications = notifications_string.split(", ")
            notification = "From: " + my_username + " " + notification
            list_of_notifications.append(notification)
            new_notifications_string = ", ".join(list_of_notifications)
            cur1.close()
            cur2 = add_notifications.cursor()
            cur2.execute(f"""
                UPDATE admin SET notifications = '{new_notifications_string}' WHERE username = '{admin_username}';
            """)
            print(cur2.statusmessage)
            cur2.close()
            add_notifications.commit()
        add_notifications.close()
        return "Notification Added"


def salary(username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as my_salary:
            cur0 = my_salary.cursor()
            cur0.execute("""
                SELECT * FROM patient WHERE approved_doctor_username = %s;
            """, [username])
            
            total_patient = len(cur0.fetchall())
            cur0.close()

            cur1 = my_salary.cursor()
            cur1.execute("""
                SELECT price FROM doctor WHERE username = %s;
            """, [username])
            
            my_price = cur1.fetchall()[0][0]
            cur1.close()
            total_earning = total_patient * int(my_price)

            cur2 = my_salary.cursor()
            cur2.execute(f"""
                SELECT salary FROM employee WHERE work_of_doctors LIKE '%{username}%';
            """) 
            salary_list = cur2.fetchall()
            total_cost = 0
            if username == "hpt":
                for salary in salary_list:
                    total_cost += (int(salary[0])*int(constant.grab_constant(True,"PRE_SALARY")))//100
            else:
                for salary in salary_list:
                    total_cost += int(salary[0])
            cur2.close()

            nit_salary = total_earning - total_cost

        my_salary.close()
        return (total_earning, total_cost, nit_salary)


def show_all_employee(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as all_employee:
            cur1 = all_employee.cursor()
            cur1.execute("""
                SELECT username, fullname, email, date_of_birth, work, salary FROM employee;
            """)

            rows = cur1.fetchall()
            # print part
            # for row in rows:
            #     print("Username:", row[0], "\tFullname:", row[1], "\tEmail:", row[2], "\tSalary:", row[3])
            cur1.close()
        all_employee.close()
        return rows


def add_employee(my_username, employee_username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as adding_employee:
            cur0 = adding_employee.cursor()
            cur0.execute("""
                SELECT work_of_doctors FROM employee WHERE username = %s;
            """, [employee_username])

            temporary = cur0.fetchall()
            work_of_doctors = temporary[0][0]
            work_of_doctors += ", " + my_username
            cur0.close()

            cur1 = adding_employee.cursor()
            cur1.execute("""
                UPDATE employee SET work_of_doctors = %s WHERE username = %s;
            """, [work_of_doctors, employee_username]) 
            print(cur1.statusmessage)        
            cur1.close()
            adding_employee.commit()
        adding_employee.close()
        return "Employee Added"


def see_my_employee(username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as my_employee:
            cur1 = my_employee.cursor()
            cur1.execute(f"""
                SELECT username, fullname, email, date_of_birth, work, salary FROM employee WHERE work_of_doctors LIKE '%{username}%'
            """)
            list_of_employees = cur1.fetchall()
            # print part
            # for row in list_of_employees:
            #     print("Username:", row[0], "\tFullname:", row[1], "\tEmail:", row[2], "\tWork:", row[3], "\tSalary:", row[4])
            cur1.close()
        my_employee.close()
        return list_of_employees


def remove_employee(my_username, employee_username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as removing_employee:
            cur0 = removing_employee.cursor()
            cur0.execute("""
                SELECT work_of_doctors FROM employee WHERE username = %s;
            """, [employee_username])

            work_of_doctors_string = cur0.fetchall()[0][0]
            work_of_doctors_list = work_of_doctors_string.split(", ")

            work_of_doctors_list.remove(my_username)
            new_work_of_doctors_string = ", ".join(work_of_doctors_list)
            cur0.close()

            cur1 = removing_employee.cursor()
            cur1.execute("""
                UPDATE employee SET work_of_doctors = %s WHERE username = %s;
            """, [new_work_of_doctors_string, employee_username]) 
            print(cur1.statusmessage)        
            cur1.close()
            removing_employee.commit()
        removing_employee.close()
        return "Employee Removed"


def see_all_requested_patient(username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as all_requested_patient:
            cur0 = all_requested_patient.cursor()
            cur0.execute("""
                SELECT username, fullname, email, date_of_birth, problem FROM patient WHERE requested_doctor_username = %s;
            """, [username])
            
            rows = cur0.fetchall()
            # print part
            # for row in rows:
            #     print("Username:", row[0], "\tFullname:", row[1], "\tEmail:", row[2], "\tProblem:", row[3])
            cur0.close()
        all_requested_patient.close()
        return rows


def see_all_patients_of_my_specialty(username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as all_under_specialty:
            cur0 = all_under_specialty.cursor()
            cur0.execute("""
                SELECT specialty FROM doctor WHERE username = %s;
            """, [username])
            specialty = str(cur0.fetchall()[0][0]).lower()
            cur0.close()

            cur1 = all_under_specialty.cursor()
            cur1.execute("""
                SELECT username, fullname, email, date_of_birth, requested_doctor_username, approved_doctor_username FROM patient WHERE problem = %s;
            """, [specialty])
            
            rows = cur1.fetchall()
            # for row in rows:
            #     print("Username:", row[0], "\tFullname:", row[1], "\tEmail:", row[2], "\tRequested Doctor:", row[3], "\tApproved Doctor:", row[4])
            cur1.close()
        all_under_specialty.close()
        return rows


def see_my_patient(username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as my_patient:
            cur0 = my_patient.cursor()
            cur0.execute("""
                SELECT username, fullname, email, date_of_birth, problem, appointment_timestamp FROM patient WHERE approved_doctor_username = %s;
            """, [username])
            
            rows = cur0.fetchall()
            # print part
            # for row in rows:
            #     print("Username:", row[0], "\tFullname:", row[1], "\tEmail:", row[2], "\tProblem:", row[3])
            cur0.close()
        my_patient.close()
        return rows


def see_patients_report(patient_username,report_name,logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as report:
            cur1 = report.cursor()
            cur1.execute("""
                SELECT reports FROM patient WHERE username = %s;
            """, [patient_username])
            reports_string = cur1.fetchall()[0][0]
            reports_list = reports_string.split("+++")
            for reports_substring in reports_list:
                report_tuple_without_b = reports_substring[1:-1]
                report_sublist = report_tuple_without_b.split("++")
                name = report_sublist[0]
                url = report_sublist[1]
                if name.lower() == report_name.lower(): 
                    web.open(url)
                    return ("Opening",name,"In Web Browser")


def remove_patient(patient_username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as removing_patient:
            cur0 = removing_patient.cursor()
            cur0.execute("""
                UPDATE patient SET approved_doctor_username = %s, appointment_timestamp = %s WHERE username = %s;
            """, [None, None, patient_username]) 
            print(cur0.statusmessage)        
            cur0.close()
            removing_patient.commit()
        removing_patient.close()
        return "Patient Removed"