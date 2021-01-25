import psycopg2
from doctor import salary as doctor_salary
from patient import cost as patient_cost
from employee import salary as employee_salary
from DB_config import config
import constant


def see_info(logged_in,category,username):
    if logged_in:
        username = username.strip().lower()
        with psycopg2.connect(**config()) as info_check:
            cur1 = info_check.cursor()
            cur1.execute(f"""
                SELECT * FROM {category} WHERE username = '{username}';
            """)
            info = cur1.fetchall()
            cur1.close()
        info_check.close()
        return info


def update_db(category, username, fieldname, updated_value, logged_in):
    if logged_in:
        date = "DATE" if fieldname == "date_of_birth" else ""
        with psycopg2.connect(**config()) as updating:
            cur1 = updating.cursor()
            cur1.execute(f"""
                UPDATE {category} SET {fieldname} = '{updated_value}' WHERE username = {date}'{username}';
            """)
            print(cur1.statusmessage)
            cur1.close()
            updating.commit()
        updating.close()
        return "Database Updated"


def recent_notifications(username, logged_in, limit = 1):
    if logged_in:
        with psycopg2.connect(**config()) as latest:
            cur1 = latest.cursor()
            cur1.execute("""
                SELECT notifications FROM admin WHERE username = %s;
            """, [username])
            notifications_string = cur1.fetchall()[0][0]
            list_of_notifications = notifications_string.split(", ")
            cur1.close()
        latest.close()
        return list_of_notifications[-limit:] if limit < len(list_of_notifications) else list_of_notifications[-len(list_of_notifications):]


def add_notification(notification, category, receiver_username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as add_notifications:
            cur1 = add_notifications.cursor()
            cur1.execute(f"""
                SELECT notifications FROM {category} WHERE username = '{receiver_username}';
            """)
            notifications_string = cur1.fetchall()[0][0]
            list_of_notifications = notifications_string.split(", ")
            list_of_notifications.append(notification)
            new_notifications_string = ", ".join(list_of_notifications)
            cur1.close()
            cur2 = add_notifications.cursor()
            cur2.execute(f"""
                UPDATE {category} SET notifications = '{new_notifications_string}' WHERE username = '{receiver_username}';
            """)
            print(cur2.statusmessage)
            cur2.close()
            add_notifications.commit()
        add_notifications.close()
        return "Notification Added"


def total_earning(logged_in):
    if logged_in:
        initial_earning = 0
        with psycopg2.connect(**config()) as earning:
            cur1 = earning.cursor()
            cur1.execute("""
                SELECT username FROM employee;
            """)
            list_of_employee = cur1.fetchall()
            cur1.close()
            earned_from_employee = 0
            for row in list_of_employee:
                earned_from_employee += int(employee_salary(row[0],True)[1])
            initial_earning += earned_from_employee
            cur2 = earning.cursor()
            cur2.execute("""
                SELECT username FROM patient;
            """)
            list_of_patient = cur2.fetchall()
            cur2.close()
            earned_from_patient = 0
            for row in list_of_patient:
                earned_from_patient += int(patient_cost(row[0],True)[1])
            initial_earning += earned_from_patient
            initial_earning -= int(constant.grab_constant(True,"FIXED_COST_OF_HOSPITAL"))            

            given_to_employees = 0
            cur3 = earning.cursor()
            cur3.execute("""
                SELECT salary FROM employee WHERE work_of_doctors LIKE '%admin%';
            """)
            salary_list = cur3.fetchall()
            for salary in salary_list:
                given_to_employees += int(salary[0])
            cur3.close()
            initial_earning -= given_to_employees

            employee_pre_salary = int(doctor_salary("hpt", True)[1])
            initial_earning -= employee_pre_salary

        earning.close()
    return (earned_from_employee, earned_from_patient, int(constant.grab_constant(True,"FIXED_COST_OF_HOSPITAL")), employee_pre_salary, given_to_employees, initial_earning)


def add_employee(employee_username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as adding_employee:
            cur0 = adding_employee.cursor()
            cur0.execute("""
                SELECT work_of_doctors FROM employee WHERE username = %s;
            """, [employee_username])

            work_of_doctors = cur0.fetchall()[0][0]
            work_of_doctors += ", " + "admin"
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


def see_my_employee(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as my_employee:
            cur1 = my_employee.cursor()
            cur1.execute("""
                SELECT username, fullname, email, date_of_birth, work, salary FROM employee WHERE work_of_doctors LIKE '%admin%'
            """)
            list_of_employees = cur1.fetchall()
            # print part
            # for row in list_of_employees:
            #     print("Username:", row[0], "\tFullname:", row[1], "\tEmail:", row[2], "\tWork:", row[3], "\tSalary:", row[4])
            cur1.close()
        my_employee.close()
        return list_of_employees


def remove_employee(employee_username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as removing_employee:
            cur0 = removing_employee.cursor()
            cur0.execute("""
                SELECT work_of_doctors FROM employee WHERE username = %s;
            """, [employee_username])

            work_of_doctors_string = cur0.fetchall()[0][0]
            work_of_doctors_list = work_of_doctors_string.split(", ")

            work_of_doctors_list.remove("admin")
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


def show_all_doctor(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as doctor:
            cur1 = doctor.cursor()
            cur1.execute("""
                SELECT username, fullname, email, date_of_birth, specialty, price FROM doctor;
            """)
            rows = cur1.fetchall()
            new_rows = []
            for row in rows:
                row = list(row)
                row.append(doctor_salary(row[0],True)[2])
                new_rows.append(row)
            # print(part)
            # for row in rows:
            #     print("Username:", row[0], "\tFullname:", row[1], "\tEmail:", row[2], "\tspecialty:", row[3], "\tPrice:", row[4], "\tTotal Earned:", row[5])
            cur1.close()
        doctor.close()
        return new_rows


def show_all_patient(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as patient:
            cur1 = patient.cursor()
            cur1.execute("""
                SELECT username, fullname, email, date_of_birth, problem, requested_doctor_username, approved_doctor_username FROM patient;
            """)
            rows = cur1.fetchall()
            new_rows = []
            for row in rows:
                row = list(row)
                row.append(patient_cost(row[0], True)[2])
                new_rows.append(row)
            # print part
            # for row in rows:
            #     print("Username:", row[0], "\tFullname:", row[1], "\tEmail:", row[2], "\tProblem:", row[3], "\tRequested:", row[4], "\tApproved:", row[5], "\tTotal Cost:", row[6])
            cur1.close()
        patient.close()
        return new_rows


def show_all_employee(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as employee:
            cur1 = employee.cursor()
            cur1.execute("""
                SELECT username, fullname, email, date_of_birth, work, work_of_doctors, salary FROM employee;
            """)
            rows = cur1.fetchall()
            new_rows = []
            for row in rows:
                row = list(row)
                row.append(employee_salary(row[0],True)[2])
                new_rows.append(row)
            # print part
            # for row in rows:
            #     print("Username:", row[0], "\tFullname:", row[1], "\tEmail:", row[2], "\tWork:", row[3], "\tDoctors:", row[4], "\tSalary:", row[5], "\tTotal Earned:", row[6])
            cur1.close()
        employee.close()
        return new_rows


def all_doctor_username(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as doctor:
            cur1 = doctor.cursor()
            cur1.execute("""
                SELECT username FROM doctor;
            """)
            rows = cur1.fetchall()
            new_rows = []
            for row in rows:
                new_rows.append(row[0])
            cur1.close()
        doctor.close()
        return new_rows


def all_patient_username(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as patient:
            cur1 = patient.cursor()
            cur1.execute("""
                SELECT username FROM patient;
            """)
            rows = cur1.fetchall()
            new_rows = []
            for row in rows:
                new_rows.append(row[0])
            cur1.close()
        patient.close()
        return new_rows


def all_employee_username(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as employee:
            cur1 = employee.cursor()
            cur1.execute("""
                SELECT username FROM employee;
            """)
            rows = cur1.fetchall()
            new_rows = []
            for row in rows:
                new_rows.append(row[0])
            cur1.close()
        employee.close()
        return new_rows


def remove_doctor_parmanently(doctor_username, logged_in, final_decision = False):
    if final_decision and logged_in:
        with psycopg2.connect(**config()) as remove_doctor:
            cur1 = remove_doctor.cursor()
            cur1.execute("""
                DELETE FROM doctor WHERE username = %s;
            """, [doctor_username])
            print(cur1.statusmessage)
            remove_doctor.commit()
            cur1.close()
        remove_doctor.close()
        return "Doctor Parmanently Removed"


def remove_patient_parmanently(patient_username, logged_in, final_decision = False):
    if final_decision and logged_in:
        with psycopg2.connect(**config()) as remove_patient:
            cur1 = remove_patient.cursor()
            cur1.execute("""
                DELETE FROM patient WHERE username = %s;
            """, [patient_username])
            print(cur1.statusmessage)
            remove_patient.commit()
            cur1.close()
        remove_patient.close()
        return "Patient Parmanently Removed"


def remove_employee_parmanently(employee_username, logged_in, final_decision = False):
    if final_decision and logged_in:
        with psycopg2.connect(**config()) as remove_employee:
            cur1 = remove_employee.cursor()
            cur1.execute("""
                DELETE FROM employee WHERE username = %s;
            """, [employee_username])
            print(cur1.statusmessage)
            remove_employee.commit()
            cur1.close()
        remove_employee.close()
        return "Employee Parmanently Removed"


def patient_joins_doctor(logged_in, left = False):
    join_type = "LEFT JOIN" if left else "JOIN"
    if logged_in:
        with psycopg2.connect(**config()) as viewer:
            cur_first = viewer.cursor()
            cur_first.execute("""
                DROP VIEW IF EXISTS final_view;
            """)
            cur_first.close()
            viewer.commit()

            cur0 = viewer.cursor()
            cur0.execute("""
                DROP VIEW IF EXISTS patient_view;
            """)
            cur0.close()
            viewer.commit()

            cur1 = viewer.cursor()
            cur1.execute("""
                CREATE VIEW patient_view AS SELECT username, fullname, email, date_of_birth, problem, approved_doctor_username, appointment_timestamp FROM patient WHERE approved_doctor_username != 'hpt';
            """)
            cur1.close()

            cur2 = viewer.cursor()
            cur2.execute("""
                DROP VIEW IF EXISTS doctor_view;
            """)
            cur2.close()
            viewer.commit()

            cur3 = viewer.cursor()
            cur3.execute("""
                CREATE VIEW doctor_view AS SELECT username AS doctor_username, fullname AS doctor_fullname, email AS doctor_email, specialty, price FROM doctor;
            """)
            cur3.close()

            viewer.commit()
        viewer.close()

        with psycopg2.connect(**config()) as joiner:

            cur1 = joiner.cursor()
            cur1.execute(f"""
                CREATE VIEW final_view AS (SELECT * FROM patient_view {join_type} doctor_view ON patient_view.approved_doctor_username = doctor_view.doctor_username);
            """)
            cur1.close()
            joiner.commit()
        joiner.close()

        with psycopg2.connect(**config()) as final:
            cur1 = final.cursor()
            cur1.execute("""
                SELECT username, fullname, email, problem, appointment_timestamp, doctor_username, doctor_fullname, doctor_email, specialty, price FROM final_view;
            """)
            rows = cur1.fetchall()
            cur1.close()

            # print part
            # for row in rows:
            #     print(row)

        joiner.close()
        return rows