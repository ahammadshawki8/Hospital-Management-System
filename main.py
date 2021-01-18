import psycopg2
import os
import doctor
import patient
import employee
import login
import admin
import constant
import setup_engine
import backup_restore


employee.appoint_doctor("lfb", "brm", "mtc", "2021-02-15 12:00:00", True)
print(patient.remaining_appointment_time("mtc", True))