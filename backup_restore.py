import psycopg2
from DB_config import config
from constant import MAIN_FILE


def backup_to_csv(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as backup:
            ADMIN_FILE = os.path.join(MAIN_FILE, "backup_&_restore_folder", "admin.csv")
            DOCTOR_FILE = os.path.join(MAIN_FILE, "backup_&_restore_folder", "doctor.csv")
            PATIENT_FILE = os.path.join(MAIN_FILE, "backup_&_restore_folder", "patient.csv")
            EMPLOYEE_FILE = os.path.join(MAIN_FILE, "backup_&_restore_folder", "employee.csv")

            cur0 = backup.cursor()
            cur0.execute("""
                COPY (SELECT * FROM admin) TO %s DELIMITER ',' CSV; 
            """, [ADMIN_FILE])
            cur0.close()
            
            cur1 = backup.cursor()
            cur1.execute("""
                COPY (SELECT * FROM doctor) TO %s DELIMITER ',' CSV; 
            """, [DOCTOR_FILE])
            cur1.close()

            cur2 = backup.cursor()
            cur2.execute("""
                COPY (SELECT * FROM patient) TO %s DELIMITER ',' CSV; 
            """, [PATIENT_FILE])
            cur2.close()

            cur3 = backup.cursor()
            cur3.execute("""
                COPY (SELECT * FROM employee) TO %s DELIMITER ',' CSV; 
            """, [EMPLOYEE_FILE])
            cur3.close()

            backup.commit()
        backup.close()
    return "Backup Successful"


def restore_from_csv(logged_in):
    if logged_in:
        with psycopg2.connect(**config()) as restore:
            ADMIN_FILE = os.path.join(MAIN_FILE, "backup_&_restore_folder", "admin.csv")
            DOCTOR_FILE = os.path.join(MAIN_FILE, "backup_&_restore_folder", "doctor.csv")
            PATIENT_FILE = os.path.join(MAIN_FILE, "backup_&_restore_folder", "patient.csv")
            EMPLOYEE_FILE = os.path.join(MAIN_FILE, "backup_&_restore_folder", "employee.csv")

            cur0 = restore.cursor()
            cur0.execute("""
                COPY admin FROM %s DELIMITER ',' CSV NULL AS '';
            """, [ADMIN_FILE])
            cur0.close()

            cur1 = restore.cursor()
            cur1.execute("""
                COPY doctor FROM %s DELIMITER ',' CSV NULL AS '';
            """, [DOCTOR_FILE])
            cur1.close()

            cur2 = restore.cursor()
            cur2.execute("""
                COPY patient FROM %s DELIMITER ',' CSV NULL AS '';
            """, [PATIENT_FILE])
            cur2.close()

            cur3 = restore.cursor()
            cur3.execute("""
                COPY employee FROM %s DELIMITER ',' CSV NULL AS '';
            """, [EMPLOYEE_FILE])
            cur3.close()

            restore.commit()
        restore.close()
    return "Restoration Successful"
