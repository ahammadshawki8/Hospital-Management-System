import psycopg2
from DB_config import config
from constant import grab_constant
import datetime


def recent_notifications(username, logged_in, limit = 1):
    if logged_in:
        with psycopg2.connect(**config()) as latest:
            cur1 = latest.cursor()
            cur1.execute("""
                SELECT notifications FROM employee WHERE username = %s;
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
            cur1 = my_salary.cursor()
            cur1.execute("""
                SELECT work_of_doctors, salary FROM employee WHERE username = %s;
            """, [username])
            bucket = cur1.fetchall()[0]
            string_of_doctors = bucket[0]
            my_price = bucket[1]
            cur1.close()
            list_of_doctors = string_of_doctors.split(", ")
            number_of_doctors = len(list_of_doctors)

            if "hpt" in list_of_doctors:
                initial_salary = (number_of_doctors * my_price) - (my_price*(100-int(grab_constant(True,"PRE_SALARY"))))//100
            else:
                initial_salary = number_of_doctors * my_price
            hospital_cost = (initial_salary * int(grab_constant(True, "CUT_FROM_EMPLOYEE"))) // 100
            final_salary = initial_salary - hospital_cost

        my_salary.close()
        return (initial_salary, hospital_cost, final_salary)

        
def isreceptionist(username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as reception:
            cur1 = reception.cursor()
            cur1.execute("""
                SELECT work FROM employee WHERE username = %s;
            """, [username])
            work = cur1.fetchall()[0][0]
            cur1.close()
        reception.close()
        if work.lower() == "receptionist":
            return True
        else:
            return False


def appoint_doctor(my_username, doctor_username, patient_username, appointment_timestamp, logged_in):
    if logged_in and isreceptionist(my_username, logged_in):
        formated_date = datetime.datetime.strptime(appointment_timestamp, "%Y-%m-%d %H:%M:%S")
        with psycopg2.connect(**config()) as adding_patient:
            cur0 = adding_patient.cursor()
            cur0.execute("""
                UPDATE patient SET approved_doctor_username = %s, appointment_timestamp = TIMESTAMP %s WHERE username = %s;
            """, [doctor_username, formated_date, patient_username]) 
            print(cur0.statusmessage)        
            cur0.close()
            adding_patient.commit()
        adding_patient.close()
        return "Succesfully Appointed"


def see_my_doctors(username, logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as my_doctor:
            cur1 = my_doctor.cursor()
            cur1.execute("""
                SELECT work_of_doctors FROM employee WHERE username = %s;
            """, [username])
            string_of_doctors = cur1.fetchall()[0][0]
            cur1.close()
            list_of_doctors = string_of_doctors.split(", ")

            doctors_bucket = []
            for doctor_username in list_of_doctors:
                cur2 = my_doctor.cursor()
                if doctor_username != "admin":
                    cur2.execute("""
                        SELECT username, fullname, email, date_of_birth, specialty FROM doctor WHERE username = %s;
                    """, [doctor_username])
                    temporary = cur2.fetchall()
                    doctors_bucket.append(temporary[0])
                    cur2.close()
                else:
                    doctors_bucket.append(('adm', 'admin','admin@as8hospitals.gov',"2004-12-28", 'all'))
            
            # print part
            # for row in doctors_bucket:
            #     print("Username:", row[0], "\tFullname:", row[1], "\tEmail:", row[2], "\tspecialty:", row[3])
                
        my_doctor.close()
        return doctors_bucket