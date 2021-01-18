import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import constant
from DB_config import config, admin_config
from backup_restore import restore_from_csv

def start_program():
    delete_database(True,True)
    create_database(True)
    delete_admin_table(True,True)
    create_admin_table(True)
    delete_doctor_table(True,True)
    create_doctor_table(True)
    delete_employee_table(True,True)
    create_employee_table(True)
    delete_patient_table(True,True)
    create_patient_table(True)
    add_unique_constraint(True)
    add_check_constraint(True)
    restore_from_csv(True)
    return "You are ready to go!"


def create_database(logged_in):
    if logged_in:
        with psycopg2.connect(**admin_config()) as database_creator:
            database_creator.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur1 = database_creator.cursor()
            cur1.execute("""
                CREATE DATABASE hms;
            """)
            print(cur1.statusmessage)
            cur1.close()
            database_creator.commit()
        database_creator.close()
        return "Database Created"


def delete_database(logged_in, final_decision = False):
    if final_decision and logged_in:
        with psycopg2.connect(**admin_config()) as database_deleter:
            database_deleter.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur1 = database_deleter.cursor()
            cur1.execute("""
                DROP DATABASE IF EXISTS hms;
            """)
            print(cur1.statusmessage)
            cur1.close()
            database_deleter.commit()
        database_deleter.close()
        return "Database Deleted"


def create_admin_table(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as create_admin:
            cur1 = create_admin.cursor()
            cur1.execute("""
                CREATE TABLE admin (
                    username VARCHAR(5) NOT NULL PRIMARY KEY,
                    fullname TEXT NOT NULL,
                    email VARCHAR(32) NOT NULL,
                    date_of_birth DATE NOT NULL,
                    password VARCHAR(15) NOT NULL,
                    notifications TEXT NOT NULL
            );
            """)
            print(cur1.statusmessage)
            cur1.close()
            create_admin.commit()
        create_admin.close()
        return "Admin Table Created"


def delete_admin_table(logged_in, final_decision = False):
    if final_decision and logged_in:
        with psycopg2.connect(**config()) as delete_admin:
            cur0 = delete_admin.cursor()
            cur0.execute("""
                DROP TABLE IF EXISTS admin;
            """)
            print(cur0.statusmessage)
            cur0.close()
            delete_admin.commit()
        delete_admin.close()
        return "Admin Table Deleted"


def create_doctor_table(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as create_doctor:
            cur1 = create_doctor.cursor()
            cur1.execute("""
                CREATE TABLE doctor (
                    username VARCHAR(5) NOT NULL PRIMARY KEY,
                    fullname TEXT NOT NULL,
                    email VARCHAR(32) NOT NULL,
                    date_of_birth DATE NOT NULL,
                    password VARCHAR(5) NOT NULL,
                    specialty TEXT NOT NULL,
                    price INT NOT NULL,
                    notifications TEXT NOT NULL
            );
            """)
            print(cur1.statusmessage)
            cur1.close()
            create_doctor.commit()
        create_doctor.close()
        return "Doctor Table Created"


def delete_doctor_table( logged_in, final_decision = False):
    if final_decision and logged_in:
        with psycopg2.connect(**config()) as delete_doctor:
            cur0 = delete_doctor.cursor()
            cur0.execute("""
                DROP TABLE IF EXISTS doctor;
            """)
            print(cur0.statusmessage)
            cur0.close()
            delete_doctor.commit()
        delete_doctor.close()
        return "Doctor Table Deleted"


def create_patient_table(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as create_patient:
            cur1 = create_patient.cursor()
            cur1.execute("""
                CREATE TABLE patient (
                    username VARCHAR(5) NOT NULL PRIMARY KEY,
                    fullname TEXT NOT NULL,
                    email VARCHAR(32) NOT NULL,
                    date_of_birth DATE NOT NULL,
                    password VARCHAR(5) NOT NULL,
                    problem TEXT NOT NULL,
                    requested_doctor_username VARCHAR(5),
                    approved_doctor_username VARCHAR(5) REFERENCES doctor (username),
                    appointment_timestamp TIMESTAMP,
                    reports TEXT,
                    notifications TEXT NOT NULL
            );
            """)
            print(cur1.statusmessage)
            cur1.close()
            create_patient.commit()
        create_patient.close()
        return "Patient Table Created"


def delete_patient_table(logged_in, final_decision = False):
    if final_decision and logged_in:
        with psycopg2.connect(**config()) as delete_patient:
            cur0 = delete_patient.cursor()
            cur0.execute("""
                DROP TABLE IF EXISTS patient;
            """)
            print(cur0.statusmessage)
            cur0.close()
            delete_patient.commit()
        delete_patient.close()
        return "Patient Table Deleted"


def create_employee_table(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as create_employee:
            cur1 = create_employee.cursor()
            cur1.execute("""
                CREATE TABLE employee (
                    username VARCHAR(5) NOT NULL PRIMARY KEY,
                    fullname TEXT NOT NULL,
                    email VARCHAR(32) NOT NULL,
                    date_of_birth DATE NOT NULL,
                    password VARCHAR(5) NOT NULL,
                    work TEXT NOT NULL,
                    work_of_doctors TEXT,
                    salary INT NOT NULL,
                    notifications TEXT NOT NULL
            );
            """)
            print(cur1.statusmessage)
            cur1.close()
            create_employee.commit()
        create_employee.close()
        return "Employee Table Created"



def delete_employee_table(logged_in, final_decision = False):
    if final_decision and logged_in:
        with psycopg2.connect(**config()) as delete_employee:
            cur0 = delete_employee.cursor()
            cur0.execute("""
                DROP TABLE IF EXISTS employee;
            """)
            print(cur0.statusmessage)
            cur0.close()
            delete_employee.commit()
        delete_employee.close()
        return "Employee Table Deleted"


def add_unique_constraint(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as admin_constraint:
            cur1 = admin_constraint.cursor()
            cur1.execute("""
                ALTER TABLE admin ADD CONSTRAINT unique_admin_email UNIQUE(email);
            """)
            cur1.close()
            admin_constraint.commit()
        admin_constraint.close()

        with psycopg2.connect(**config()) as doctor_constraint:
            cur1 = doctor_constraint.cursor()
            cur1.execute("""
                ALTER TABLE doctor ADD CONSTRAINT unique_doctor_email UNIQUE(email);
            """)
            cur1.close()
            doctor_constraint.commit()
        doctor_constraint.close()

        with psycopg2.connect(**config()) as employee_constraint:
            cur1 = employee_constraint.cursor()
            cur1.execute("""
                ALTER TABLE employee ADD CONSTRAINT unique_employee_email UNIQUE(email);
            """)
            cur1.close()
            employee_constraint.commit()
        employee_constraint.close()

        with psycopg2.connect(**config()) as patient_constraint:
            cur1 = patient_constraint.cursor()
            cur1.execute("""
                ALTER TABLE patient ADD CONSTRAINT unique_patient_email UNIQUE(email);
            """)
            cur1.close()
            patient_constraint.commit()
        patient_constraint.close()


def add_check_constraint(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as doctor_salary_constraint:
            cur1 = doctor_salary_constraint.cursor()
            cur1.execute(f"""
                ALTER TABLE doctor ADD CONSTRAINT doctor_price_check_constraint CHECK(price < {int(constant.grab_constant(True,"DOCTOR_MAX_CHECKUP_PRICE"))})
            """)
            doctor_salary_constraint.commit()
        doctor_salary_constraint.close()

        with psycopg2.connect(**config()) as employee_salary_constraint:
            cur1 = employee_salary_constraint.cursor()
            cur1.execute(f"""
                ALTER TABLE employee ADD CONSTRAINT employee_salary_check_constraint CHECK(salary < {int(constant.grab_constant(True,"EMPLOYEE_MAX_SALARY"))})
            """)
            employee_salary_constraint.commit()
        employee_salary_constraint.close()