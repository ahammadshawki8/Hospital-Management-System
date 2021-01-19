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


patient.notify_admin("Testing 1: This is line number 1", "nrs", "ad1", True)
patient.notify_admin("Testing 2: This is line number 2", "cst", "ad1", True)
doctor.notify_admin("Testing 3: This is line number 3", "brm", "ad1", True)
employee.notify_admin("Testing 4: This is line number 4", "lfb", "ad1", True)
doctor.notify_admin("Testing 5: This is line number 5", "hbt", "ad1", True)
employee.notify_admin("Testing 6: This is line number 6", "jjf", "ad1", True)
admin.add_notification("Testing 0: This is line number 0","patient", "nrs", True)
admin.add_notification("Testing 1: This is line number 1","doctor", "brm", True)
admin.add_notification("Testing 2: This is line number 2", "employee", "lfb", True)