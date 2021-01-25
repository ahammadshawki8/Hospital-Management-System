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


employee.appoint_doctor("lfb","brm","kml","2021-05-05 10:03:00",True)
employee.appoint_doctor("lfb","coz","abc","2021-05-06 12:13:00",True)
employee.appoint_doctor("lfb","mrh","mtc","2021-05-08 11:03:00",True)
employee.appoint_doctor("lfb","ddb","rrt","2021-07-05 12:03:00",True)
employee.appoint_doctor("lfb","btc","tsc","2021-05-10 12:08:00",True)
employee.appoint_doctor("lfb","ssc","abb","2021-09-11 12:03:00",True)