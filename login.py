import psycopg2
import os
from getpass import getpass
from DB_config import config
import datetime


def DB_pass(username, category):
    with psycopg2.connect(**config()) as find_pass:
        cur1 = find_pass.cursor()
        cur1.execute(f"""
            SELECT password FROM {category} WHERE username = '{username.lower()}';
        """)
        rows = cur1.fetchall() 
        cur1.close()
    find_pass.close()
    return rows[0][0]


def login(category, username, password):
    logged_in = False
    if password == DB_pass(username,category):
        logged_in = True
    return logged_in


def signup(category, *args):
    if category == "admin":
        username, fullname, email, date_of_birth, password = args
        date_of_birth = datetime.datetime.strptime(date_of_birth,"%Y-%m-%d")
        notifications = "Logged in"

        with psycopg2.connect(**config()) as default_admin:
            cur0 = default_admin.cursor()
            cur0.execute("""
                INSERT INTO admin (
                    username,
                    fullname,
                    email,
                    date_of_birth,
                    password,
                    notifications
                )
                VALUES (
                    %s, %s, %s, DATE %s, %s, %s
                ) ON CONFLICT(username) DO NOTHING;
            """, (username, fullname, email, date_of_birth, password, notifications))


    elif category == "doctor":
        username, fullname, email, date_of_birth, password, specialty, price = args
        date_of_birth = datetime.datetime.strptime(date_of_birth.strip(),"%Y-%m-%d")
        notifications = "Logged in"

        with psycopg2.connect(**config()) as doctor_signup:
            cur1 = doctor_signup.cursor()
            cur1.execute("""
                INSERT INTO doctor (
                    username,
                    fullname,
                    email,
                    date_of_birth,
                    password,
                    specialty,
                    price,
                    notifications
                )
                VALUES (
                    %s, %s, %s, DATE %s, %s, %s, %s, %s
                ) ON CONFLICT(username) DO NOTHING;
            """, (username, fullname, email, date_of_birth, password, specialty, price, notifications))
            print(cur1.statusmessage)
            print("Successfully Signed Up")
            cur1.close()
            doctor_signup.commit()
        doctor_signup.close()
    
    elif category == "patient":
        username, fullname, email, date_of_birth, password, problem = args
        date_of_birth = datetime.datetime.strptime(date_of_birth.strip(),"%Y-%m-%d")
        reports = "(initial_registration++This_frontend_url_will_be_generated_automatically)"
        notifications = "Logged in"
        requested_doctor_username = None
        appointment_timestamp = None
        approved_doctor_username = "hpt"

        with psycopg2.connect(**config()) as patient_signup:
            cur1 = patient_signup.cursor()
            cur1.execute("""
                INSERT INTO patient (
                    username,
                    fullname,
                    email,
                    date_of_birth,
                    password,
                    problem,
                    requested_doctor_username,
                    approved_doctor_username,
                    appointment_timestamp,
                    reports,
                    notifications
                )
                VALUES (
                    %s, %s, %s, DATE %s, %s, %s, %s, %s, %s, %s, %s
                ) ON CONFLICT(username) DO NOTHING;
            """, (username, fullname, email, date_of_birth, password, problem, requested_doctor_username, approved_doctor_username, appointment_timestamp, reports, notifications))
            print(cur1.statusmessage)
            print("Successfully Signed Up")
            cur1.close()
            patient_signup.commit()
        patient_signup.close()

    else:
        username, fullname, email, date_of_birth, password, work, salary = args
        date_of_birth = datetime.datetime.strptime(date_of_birth.strip(),"%Y-%m-%d")
        work_of_doctors = "hpt"
        notifications = "Logged in"

        with psycopg2.connect(**config()) as employee_signup:
            cur1 = employee_signup.cursor()
            cur1.execute("""
                INSERT INTO employee (
                    username,
                    fullname,
                    email,
                    date_of_birth,
                    password,
                    work,
                    work_of_doctors,
                    salary,
                    notifications
                )
                VALUES (
                    %s, %s, %s, DATE %s, %s, %s, %s, %s, %s
                );
            """, (username, fullname, email, date_of_birth, password, work, work_of_doctors, salary, notifications))
            print(cur1.statusmessage)
            print("Successfully Signed Up")
            cur1.close()
            employee_signup.commit()
        employee_signup.close()
    
    return True