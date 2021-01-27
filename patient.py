import psycopg2
from constant import grab_constant
from DB_config import config
import datetime


def remaining_appointment_time(username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as remaining:
            cur1 = remaining.cursor()
            cur1.execute("""
                SELECT appointment_timestamp FROM patient WHERE username = %s;
            """, [username])
            appointment_timestamp = cur1.fetchall()[0][0]
            if appointment_timestamp != None:
                remaining_time = appointment_timestamp - datetime.datetime.now()
            else:
                remaining_time = "Your appointment isn't fixed yet."
            cur1.close()
        remaining.close()
        return remaining_time

def recent_notifications(username, logged_in, limit = 1):
    if logged_in:
        with psycopg2.connect(**config()) as latest:
            cur1 = latest.cursor()
            cur1.execute("""
                SELECT notifications FROM patient WHERE username = %s;
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


def cost(username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as total_cost:
            cur1 = total_cost.cursor()
            cur1.execute("""
                SELECT approved_doctor_username FROM patient WHERE username = %s;
            """, [username])
            approved_doctor_username = cur1.fetchall()[0][0]
            print(approved_doctor_username)
            cur1.close()

            cur2 = total_cost.cursor()
            if approved_doctor_username != "hpt":
                cur2.execute("""
                    SELECT price FROM doctor WHERE username = %s;
                """, [approved_doctor_username])
                doctors_salary = int(cur2.fetchall()[0][0])
                final_cost = (doctors_salary * (100 + int(grab_constant(True,"CUT_FROM_PATIENT"))))//100
            else:
                doctors_salary = 0
                final_cost = 0

        total_cost.close() 
        hospital_cost = final_cost - doctors_salary        
        
        return (doctors_salary, hospital_cost, final_cost)


def add_report(report_name, report_url, username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as add_reports:
            cur1 = add_reports.cursor()
            cur1.execute("""
                SELECT reports FROM patient WHERE username = %s;
            """, [username])
            reports_string = cur1.fetchall()[0][0]
            reports_info = "(" + report_name + "++" + report_url + ")"
            reports_string += "+++" + str(reports_info)
            cur1.close()
            cur2 = add_reports.cursor()
            cur2.execute("""
                UPDATE patient SET reports = %s WHERE username = %s;
            """,  [reports_string, username])
            print(cur2.statusmessage)
            cur2.close()
            add_reports.commit()
        add_reports.close()
        return "Report Added"


def see_all_doctors_for_my_problem(username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as doctors_as_problem:
            cur1 = doctors_as_problem.cursor()
            cur1.execute("""
                SELECT problem FROM patient WHERE username = %s;
            """, [username])
            problem = cur1.fetchall()[0][0]
            cur1.close()

            cur2 = doctors_as_problem.cursor()
            cur2.execute("""
                SELECT username, fullname, email, date_of_birth, price FROM doctor WHERE specialty = %s;
            """, [problem])
            rows = cur2.fetchall()
            # print part
            # for row in rows:
            #     print("Username:", row[0], "\tFullname:", row[1], "\tEmail:", row[2], "\tPrice:", row[3])
            cur2.close()
        doctors_as_problem.close()
        return rows


def request_doctor(my_username, doctor_username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as requesting_doctor:
            cur1 = requesting_doctor.cursor()
            cur1.execute("""
                UPDATE patient SET requested_doctor_username = %s WHERE username = %s;
            """, [doctor_username, my_username])
            print(cur1.statusmessage)
            cur1.close()
            requesting_doctor.commit()
        requesting_doctor.close()
        return "Successfully Requested"


def remove_request(my_username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as removing_request:
            cur1 = removing_request.cursor()
            cur1.execute("""
                UPDATE patient SET requested_doctor_username = NULL WHERE username = %s;
            """, [my_username])
            print(cur1.statusmessage)
            cur1.close()
            removing_request.commit()
        removing_request.close()
        return "Request Removed"


def see_my_doctors_stat(username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as my_doctor:
            cur1 = my_doctor.cursor()
            cur1.execute("""
                SELECT approved_doctor_username, appointment_timestamp FROM patient WHERE username = %s;
            """, [username])
            temp = cur1.fetchall()[0]
            approved_doctor_username = temp[0]
            appointment_timestamp = temp[1]
            cur1.close()

            cur2 = my_doctor.cursor()
            cur2.execute("""
                SELECT username, fullname, email, date_of_birth, specialty, price FROM doctor WHERE username = %s;
            """, [approved_doctor_username])
            
            rows = list(cur2.fetchall()[0])
            rows.append(appointment_timestamp)
            # print part
            # for row in rows:
            #     print("Doctor's Information")
            #     print("Fullname:", row[1])
            #     print("Email:", row[2])
            #     print("specialty:", row[3])
            #     print("Price:", row[4])
            #     print("Appointment Timestamp:", row[5])
            cur2.close()
        my_doctor.close()
        return rows