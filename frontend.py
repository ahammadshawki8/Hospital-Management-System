# All Imports
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
import webbrowser as web
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.screenmanager import NoTransition
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle
from kivy.uix.scrollview import ScrollView
from kivy.app import runTouchApp

import setup_engine
import login
import constant
import admin
import datetime
import doctor
import patient
import employee






# Common Classes and Window Configuration
class WindowManager(ScreenManager):
    pass

class Holder():
    username = "Default"
    logged_in = True
    counter = 0
    pre_counter = 0

Config.set('graphics', 'height', 600)
Config.set('graphics', 'width', 800)
Config.set('graphics', 'resizable', 0)
Config.write()






# SignUp Classes
class GetStarted(Screen):
    first_start = True if (constant.grab_constant(True, "IS_START")=="0") else False
    def start_program(self):
        if GetStarted.first_start:
            sm.transition = SlideTransition(direction = "up")
            sm.current = "ConstantFixing"
        else:
            sm.transition = SlideTransition(direction = "up")
            sm.current = "PatientSignUp"
            

    def go_to_website(self):
        web.open_new_tab("https://ahammadshawki8.github.io/")



class ConstantFixing(Screen):
    host = ObjectProperty()  
    port = ObjectProperty()   
    user = ObjectProperty()  
    password = ObjectProperty()  
    cut_from_patient = ObjectProperty()   
    cut_from_employee = ObjectProperty()  
    fixed_cost_of_hospital = ObjectProperty()  
    pre_salary = ObjectProperty()  
    doctor_max_checkup_price = ObjectProperty()  
    employee_max_salary = ObjectProperty()  
    hospital_year = ObjectProperty()  
    hospital_total_bed = ObjectProperty()  
    hospital_remaining_bed = ObjectProperty()  
    hospital_total_employee = ObjectProperty()  
    hospital_total_doctor = ObjectProperty()  
    hospital_total_patient = ObjectProperty()  
    hospital_current_patient = ObjectProperty()  
    hospital_motto = ObjectProperty()  
    hospital_location = ObjectProperty()  
    hospital_title = ObjectProperty()  
    restore_previous = ObjectProperty()

    def set_constant_function(self):
        try:
            constants_bucket = dict()
            constants_bucket["HOST"] = self.host.text
            constants_bucket["PORT"] = self.port.text
            constants_bucket["ADMIN_DATABASE"] = "postgres"
            constants_bucket["DATABASE"] ="hms"
            constants_bucket["USER"] = self.user.text
            constants_bucket["PASSWORD"] = self.password.text
            constants_bucket["CUT_FROM_PATIENT"] = self.cut_from_patient.text 
            constants_bucket["CUT_FROM_EMPLOYEE"] = self.cut_from_employee.text
            constants_bucket["FIXED_COST_OF_HOSPITAL"] = self.fixed_cost_of_hospital.text
            constants_bucket["PRE_SALARY"] = self.pre_salary.text
            constants_bucket["DOCTOR_MAX_CHECKUP_PRICE"] = self.doctor_max_checkup_price.text
            constants_bucket["EMPLOYEE_MAX_SALARY"] = self.employee_max_salary.text
            constants_bucket["HOSPITAL_YEAR"] = self.hospital_year.text
            constants_bucket["HOSPITAL_TOTAL_BED"] = self.hospital_total_bed.text
            constants_bucket["HOSPITAL_REMAINING_BED"] = self.hospital_remaining_bed.text
            constants_bucket["HOSPITAL_TOTAL_EMPLOYEE"] = self.hospital_total_employee.text
            constants_bucket["HOSPITAL_TOTAL_DOCTOR"] = self.hospital_total_doctor.text
            constants_bucket["HOSPITAL_TOTAL_PATIENT"] = self.hospital_total_patient.text
            constants_bucket["HOSPITAL_CURRENT_PATIENT"] = self.hospital_current_patient.text
            constants_bucket["HOSPITAL_MOTTO"] = self.hospital_motto.text
            constants_bucket["HOSPITAL_LOCATION"] = self.hospital_location.text
            constants_bucket["HOSPITAL_TITLE"] = self.hospital_title.text
            constants_bucket["IS_START"] = "1"
            constant.set_constant(True, constants_bucket)
            self.proceed()
            if self.restore_previous.text == "yes":
                setup_engine.start_program()
        except:
            show_ConstantFixingPop()

        self.host.text = "localhost"
        self.port.text = "5432"
        self.user.text = "postgres"
        self.password.text = "12345678"
        self.cut_from_patient.text = "50" 
        self.cut_from_employee.text = "20"
        self.fixed_cost_of_hospital.text = "5000"
        self.pre_salary.text = "10"
        self.doctor_max_checkup_price.text = "4000"
        self.employee_max_salary.text = "15000"
        self.hospital_year.text = "2004"
        self.hospital_total_bed.text = "200"
        self.hospital_remaining_bed.text = "120"
        self.hospital_total_employee.text = "16"
        self.hospital_total_doctor.text = "10"
        self.hospital_total_patient.text = "2000"
        self.hospital_current_patient.text = "40"
        self.hospital_motto.text = "serve the nation at large"
        self.hospital_location.text = "Dhaka-Bangladesh"
        self.hospital_title.text = "The AS8 Hospital"
        self.restore_previous.text = "no"

    def proceed(self):
        sm.transition = SlideTransition(direction = "up")
        sm.current = "PatientSignUp"


class ConstantFixingPop(FloatLayout):
    pass


def show_ConstantFixingPop():
    show = ConstantFixingPop()
    popup_window = Popup(title = "Constant Fixing Error", content = show, size_hint = (0.6, 0.3))
    popup_window.open()






class AdminSignUp(Screen):
    username = ObjectProperty()
    fullname = ObjectProperty()
    email = ObjectProperty()
    date_of_birth = ObjectProperty()
    password = ObjectProperty()

    def signup_to_database(self):
        try:
            category = "admin"
            username = self.username.text.strip().lower()
            fullname = self.fullname.text.strip().title()
            email = self.email.text.strip()
            date_of_birth = self.date_of_birth.text.strip()
            password = self.password.text.strip()

            login.signup(category, username, fullname, email, date_of_birth, password)
            sm.current = "AdminLogin"
        except:
            show_SignUpPop()

        self.username.text = ""
        self.fullname.text = ""
        self.email.text = ""
        self.date_of_birth.text = "YYYY-MM-DD"
        self.password.text = ""


class DoctorSignUp(Screen):
    username = ObjectProperty()
    fullname = ObjectProperty()
    email = ObjectProperty()
    date_of_birth = ObjectProperty()
    password = ObjectProperty()
    specialty = ObjectProperty()
    price = ObjectProperty()

    def signup_to_database(self):
        try:
            category = "doctor"
            username = self.username.text.strip().lower()
            fullname = self.fullname.text.strip().title()
            email = self.email.text.strip()
            date_of_birth = self.date_of_birth.text.strip()
            password = self.password.text.strip()
            specialty = self.specialty.text.strip().lower()
            price = int(self.price.text.strip())

            login.signup(category, username, fullname, email, date_of_birth, password, specialty, price)
            sm.current = "DoctorLogin"
        except:
            show_SignUpPop()

        self.username.text = ""
        self.fullname.text = ""
        self.email.text = ""
        self.date_of_birth.text = "YYYY-MM-DD"
        self.password.text = ""
        self.specialty.text = ""
        self.price.text = ""    


class PatientSignUp(Screen):
    username = ObjectProperty()
    fullname = ObjectProperty()
    email = ObjectProperty()
    date_of_birth = ObjectProperty()
    password = ObjectProperty()
    problem = ObjectProperty()

    def signup_to_database(self):
        try:
            category = "patient"
            username = self.username.text.strip().lower()
            fullname = self.fullname.text.strip().title()
            email = self.email.text.strip()
            date_of_birth = self.date_of_birth.text.strip()
            password = self.password.text.strip()
            problem = self.problem.text.strip().lower()

            login.signup(category, username, fullname, email, date_of_birth, password, problem)
            sm.current = "PatientLogin"
        except:
            show_SignUpPop()

        self.username.text = ""
        self.fullname.text = ""
        self.email.text = ""
        self.date_of_birth.text = "YYYY-MM-DD"
        self.password.text = ""
        self.problem.text = ""  


class EmployeeSignUp(Screen):
    username = ObjectProperty()
    fullname = ObjectProperty()
    email = ObjectProperty()
    date_of_birth = ObjectProperty()
    password = ObjectProperty()
    work = ObjectProperty()
    salary = ObjectProperty()

    def signup_to_database(self):
        try:
            category = "employee"
            username = self.username.text.strip().lower()
            fullname = self.fullname.text.strip().title()
            email = self.email.text.strip()
            date_of_birth = self.date_of_birth.text.strip()
            password = self.password.text.strip()
            work = self.work.text.strip().lower()
            salary = int(self.salary.text.strip())

            login.signup(category, username, fullname, email, date_of_birth, password, work, salary)
            sm.current = "EmployeeLogin"
        except:
            show_SignUpPop()

        self.username.text = ""
        self.fullname.text = ""
        self.email.text = ""
        self.date_of_birth.text = "YYYY-MM-DD"
        self.password.text = ""
        self.work.text = ""
        self.salary.text = ""  


class SignUpPop(FloatLayout):
    pass


def show_SignUpPop():
    show = SignUpPop()
    popup_window = Popup(title = "SignUp Error", content = show, size_hint = (0.6, 0.3))
    popup_window.open()






# Login Classes
class AdminLogin(Screen):
    username = ObjectProperty()
    password = ObjectProperty()
    
    def login_to_database(self):
        try:
            category = "admin"
            username = self.username.text.strip().lower()
            Holder.username = username
            password = self.password.text.strip()
            
            logged_in = login.login(category,username,password)
            if logged_in:
                sm.current = "AdminAfterLogin"
            else:
                show_LoginPop()
        except:
            show_LoginPop()
            
        self.username.text = ""
        self.password.text = ""


class DoctorLogin(Screen):    
    username = ObjectProperty()
    password = ObjectProperty()

    def login_to_database(self):
        try:
            category = "doctor"
            username = self.username.text.strip().lower()
            Holder.username = username
            password = self.password.text.strip()

            logged_in = login.login(category,username,password)
            if logged_in:
                sm.current = "DoctorAfterLogin"  
            else:
                show_LoginPop()          
        except:
            show_LoginPop()
            
        self.username.text = ""
        self.password.text = ""


class PatientLogin(Screen):
    username = ObjectProperty()
    password = ObjectProperty()

    def login_to_database(self):
        try:
            category = "patient"
            username = self.username.text.strip().lower()
            Holder.username = username
            password = self.password.text.strip()

            logged_in = login.login(category,username,password)
            print(logged_in)
            if logged_in:
                sm.current = "PatientAfterLogin"
            else:
                show_LoginPop()
        except:
            show_LoginPop()
            
        self.username.text = ""
        self.password.text = ""


class EmployeeLogin(Screen):
    username = ObjectProperty()
    password = ObjectProperty()

    def login_to_database(self):
        try:
            category = "employee"
            username = self.username.text.strip().lower()
            Holder.username = username
            password = self.password.text.strip()
            
            logged_in = login.login(category,username,password)
            if logged_in:
                sm.current = "EmployeeAfterLogin"
            else:
                show_LoginPop()
        except:
            show_LoginPop()
            
        self.username.text = ""
        self.password.text = ""

        
class LoginPop(FloatLayout):
    pass


def show_LoginPop():
    show = LoginPop()
    popup_window = Popup(title = "Login Error", content = show, size_hint = (0.6, 0.3))
    popup_window.open()






# After Login
# Common Functions
def go_to_website(instance):
    web.open_new_tab("https://ahammadshawki8.github.io/")




# AboutHospital class
class AboutHospital(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text="About Hospital", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.hospital_name_label = Label(text=constant.grab_constant(True,"HOSPITAL_TITLE").upper(), font_size=20, color=(0,0,0,1))
        self.hospital_name_label.pos_hint = {"x":0.21, "top": 1.2}
        self.add_widget(self.hospital_name_label)

        self.hospital_motto_label = Label(text=constant.grab_constant(True,"HOSPITAL_MOTTO").upper(), font_size=18, color=(51/255, 153/255, 255/255,1))
        self.hospital_motto_label.pos_hint = {"x":0.255, "top": 1.16}
        self.add_widget(self.hospital_motto_label)

        self.hospital_location_label = Label(text=constant.grab_constant(True,"HOSPITAL_LOCATION"), font_size=13, color=(0,0,0,1))
        self.hospital_location_label.pos_hint = {"x":0.17, "top": 1.13}
        self.add_widget(self.hospital_location_label)

        self.hospital_info_label = Label(text="""        Our Hospital is a well-known hospital of the country. It provides quality treatment for patients 
        and it has a qualified doctor's faculty. All of the employees are also hardworking.
        This hospital also provides an efficient GUI that can be used from any device.
        Some more information about our hospital:""", font_size=13, color=(0,0,0,1))
        self.hospital_info_label.pos_hint = {"x":0.01, "top": 0.98}
        self.add_widget(self.hospital_info_label)

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        self.info_grid.size_hint = 0.6,0.25
        self.info_grid.pos_hint = {"x": 0.25, "top": 0.4}
        self.year_name = Label(text= "Founded in:", color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.year_name)
        self.year_value = Label(text= constant.grab_constant(True, "HOSPITAL_YEAR"), color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.year_value)
        self.total_bed_name = Label(text= "Total Bed Number:", color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.total_bed_name) 
        self.total_bed_value = Label(text= constant.grab_constant(True,"HOSPITAL_TOTAL_BED"), color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.total_bed_value)
        self.remainning_bed_name = Label(text= "Number of Available Beds:", color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.remainning_bed_name)
        self.remainning_bed_value = Label(text= constant.grab_constant(True,"HOSPITAL_REMAINING_BED"), color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.remainning_bed_value)
        self.doctors_number_name = Label(text= "Total Doctors:", color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.doctors_number_name)
        self.doctors_number_value = Label(text= constant.grab_constant(True,"HOSPITAL_TOTAL_DOCTOR"), color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.doctors_number_value)
        self.patient_number_name = Label(text= "Total Treated Patient:", color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.patient_number_name)
        self.patient_number_value = Label(text= constant.grab_constant(True,"HOSPITAL_TOTAL_PATIENT"), color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.patient_number_value)
        self.patient_current_name = Label(text= "Number of Current Patient:", color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.patient_current_name) 
        self.patient_current_value = Label(text= constant.grab_constant(True,"HOSPITAL_CURRENT_PATIENT"), color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.patient_current_value)
        self.employee_number_name = Label(text= "Total Employee:", color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.employee_number_name)
        self.employee_number_value = Label(text= constant.grab_constant(True,"HOSPITAL_TOTAL_EMPLOYEE"), color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.employee_number_value) 
        self.add_widget(self.info_grid)

    def go_back(self, instance):
        pass



# Subclasses of AboutHospital class
class AdminAboutHospital(AboutHospital):
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "AdminAfterLogin"


class DoctorAboutHospital(AboutHospital):
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "DoctorAfterLogin"


class PatientAboutHospital(AboutHospital):
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "PatientAfterLogin"


class EmployeeAboutHospital(AboutHospital):
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "EmployeeAfterLogin"





# Documentation class
class Documentation(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.category = self.find_my_category()
        with self.canvas:
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text=self.category.capitalize()+ " Documentaion", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.instruction_label = Label(text="Read this documentation clearly and perform your tasks:", font_size=18, color=(51/255, 153/255, 255/255,1))
        self.instruction_label.pos_hint = {"x":-0.1, "top": 1}
        self.add_widget(self.instruction_label)

        self.instruction_body = Label(text=self.all_instructions(), font_size = 14, color = (0,0,0,1))
        self.instruction_body.size_hint = 0.8 , 0.5
        self.instruction_body.pos_hint = {"x":0.1, "top": 0.57}
        self.add_widget(self.instruction_body)

    def go_back(self):
        pass

    def find_my_category(self):
        return "Doctor"
    
    def all_instructions(self):
        return "Default"



# Subclasses of Documentation class
class AdminDocumentation(Documentation):
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "AdminAfterLogin"

    def find_my_category(self):
        return "admin"

    def all_instructions(self):
        text = """
        00. SignUp or Login to the application to use it.
        01. Send others notification using + button.
        02. See all of your notification as well as profile.
        03. In "Functions" secion, you have a set of functions. 
        04. Use those functions providing necessary information.
        05. In "Settings" you can edit your profile.
        06. Read more about the hospital in "About Hospital" section.
        07. You are currently reading the docs in the "Documentation" section.
        08. Visit creators webpage by clicking on his name at the bottom-right corner.
        09. Promote this "Hospital Management System" application in social network.
        10. Be active in your workflow and have a great day.
        """
        return text


class DoctorDocumentation(Documentation):
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "DoctorAfterLogin"

    def find_my_category(self):
        return "doctor"

    def all_instructions(self):
        text = """
        00. SignUp or Login to the application to use it.
        01. Send notifications to admin using + button.
        02. See all of your notification as well as profile.
        03. In "Functions" secion, you have a set of functions. 
        04. Use those functions providing necessary information.
        05. In "Settings" you can edit your profile.
        06. Read more about the hospital in "About Hospital" section.
        07. You are currently reading the docs in the "Documentation" section.
        08. Visit creators webpage by clicking on his name at the bottom-right corner.
        09. Promote this "Hospital Management System" application in social network.
        10. Be active in your workflow and have a great day.
        """
        return text


class PatientDocumentation(Documentation):
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "PatientAfterLogin"

    def find_my_category(self):
        return "patient"

    def all_instructions(self):
        text = """
        00. SignUp or Login to the application to use it.
        01. Send notifications to admin using + button.
        02. See all of your notification as well as profile.
        03. In "Functions" secion, you have a set of functions. 
        04. Use those functions providing necessary information.
        05. In "Settings" you can edit your profile.
        06. Read more about the hospital in "About Hospital" section.
        07. You are currently reading the docs in the "Documentation" section.
        08. Visit creators webpage by clicking on his name at the bottom-right corner.
        09. Promote this "Hospital Management System" application in social network.
        10. Be active in your workflow and have a great day.
        """
        return text


class EmployeeDocumentation(Documentation):
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "EmployeeAfterLogin"

    def find_my_category(self):
        return "employee"

    def all_instructions(self):
        text = """
        00. SignUp or Login to the application to use it.
        01. Send notifications to admin using + button.
        02. See all of your notification as well as profile.
        03. In "Functions" secion, you have a set of functions. 
        04. Use those functions providing necessary information.
        05. In "Settings" you can edit your profile.
        06. Read more about the hospital in "About Hospital" section.
        07. You are currently reading the docs in the "Documentation" section.
        08. Visit creators webpage by clicking on his name at the bottom-right corner.
        09. Promote this "Hospital Management System" application in social network.
        10. Be active in your workflow and have a great day.
        """
        return text





# Profile class
class Profile(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = self.find_my_category()
        if self.category == "admin":
            self.fullname, self.email, self.date_of_birth, *others = self.get_my_profile(self.username, self.category)[0][1:]
            self.password, self.notifications = others
        elif self.category == "doctor":
            self.fullname, self.email, self.date_of_birth, *others = self.get_my_profile(self.username, self.category)[0][1:]
            self.password, self.specialty, self.price, self.notifications = others
        elif self.category == "patient":
            self.fullname, self.email, self.date_of_birth, *others = self.get_my_profile(self.username, self.category)[0][1:]
            self.password, self.problem, self.requested_doctor_username, self.approved_doctor_username, self.appointment_timestamp, self.reports, self.notifications = others
        else:
            self.fullname, self.email, self.date_of_birth, *others = self.get_my_profile(self.username, self.category)[0][1:]
            self.password, self.work, self.work_of_doctors, self.salary, self.notifications = others

        with self.canvas:
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text=self.find_my_category().capitalize()+ " Profile", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        self.info_grid.size_hint = 0.6,0.3
        self.info_grid.pos_hint = {"x": 0.2, "top": 0.5}
        self.username_name = Label(text = "Username:", color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.username_name)
        self.username_value = Label(text = self.username, color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.username_value)
        self.fullname_name = Label(text = "Fullname:", color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.fullname_name)
        self.fullname_value = Label(text = self.fullname, color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.fullname_value)
        self.email_name = Label(text = "Email Address:", color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.email_name)
        self.email_value = Label(text = self.email, color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.email_value)
        self.date_of_birth_name = Label(text = "Date of Birth", color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.date_of_birth_name)
        self.date_of_birth_value = Label(text = datetime.datetime.strftime(self.date_of_birth, format = "%d %b,%Y" ), color = (0,0,0,1), font_size=13)
        self.info_grid.add_widget(self.date_of_birth_value)
        if self.category == "doctor":
            self.specialty_name = Label(text = "Specialty:", color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.specialty_name)
            self.specialty_value = Label(text = self.specialty, color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.specialty_value)
            self.price_name = Label(text = "Per CheckUp Fee:", color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.price_name)
            self.price_value = Label(text = str(self.price), color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.price_value)
        elif self.category == "patient":
            self.problem_name = Label(text = "Problem:", color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.problem_name)
            self.problem_value = Label(text = self.problem, color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.problem_value)
            self.requested_doctor_username_name = Label(text = "Requested Doctor:", color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.requested_doctor_username_name)
            self.requested_doctor_username_value = Label(text = (self.requested_doctor_username if not self.requested_doctor_username==None else "None"), color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.requested_doctor_username_value)
            self.approved_doctor_username_name = Label(text = "Approved Doctor:", color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.approved_doctor_username_name)
            self.approved_doctor_username_value = Label(text = (self.approved_doctor_username if not self.approved_doctor_username==None else "None"), color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.approved_doctor_username_value)
            self.appointment_timestamp_name = Label(text = "Appointment Timestamp:", color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.appointment_timestamp_name)
            self.appointment_timestamp_value = Label(text=(datetime.datetime.strftime(self.appointment_timestamp, format="%d %b, %Y %H:%M:%S") if self.appointment_timestamp != None else "None"), color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.appointment_timestamp_value)
            self.reports_name = Label(text = "Reports:", color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.reports_name)
            self.report_bucket = self.reports.split("+++")
            self.report_string = [item.replace("++", ",") for item in self.report_bucket]
            self.reports_value = Label(text = str(self.report_string), color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.reports_value)
        elif self.category =="employee":
            self.work_name = Label(text = "Work:", color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.work_name)
            self.work_value = Label(text = self.work, color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.work_value)
            self.work_of_doctors_name = Label(text = "Work of Doctors:", color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.work_of_doctors_name)
            self.work_of_doctors_value = Label(text = self.work_of_doctors, color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.work_of_doctors_value)
            self.salary_name = Label(text = "Salary:", color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.salary_name)
            self.salary_value = Label(text = str(self.salary), color = (0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.salary_value)
        self.add_widget(self.info_grid)

    def get_my_profile(self, username, category):
        return admin.see_info(True, category, username)

    def find_my_category(self):
        return "doctor"
    
    def find_my_username(self):
        return "hpt"
    
    def go_back(self):
        pass



# Subclasses of Profile class
class AdminProfile(Profile):
    def find_my_category(self):
        return "admin"
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "AdminProfile":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "AdminAfterLogin"


class DoctorProfile(Profile):
    def find_my_category(self):
        return "doctor"
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "DoctorProfile":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "DoctorAfterLogin"


class PatientProfile(Profile):
    def find_my_category(self):
        return "patient"

    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "PatientProfile":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "PatientAfterLogin"


class EmployeeProfile(Profile):
    def find_my_category(self):
        return "employee"

    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "EmployeeProfile":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "EmployeeAfterLogin"
        




# Notifications class
class Notifications(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = self.find_my_category()
        self.notifications = self.get_my_notification(self.username, self.category)

        with self.canvas:
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text=self.find_my_category().capitalize()+ " Notifications", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        self.info_grid.pos_hint = {"x": 0.2, "top": 0.5}
        self.note_length = len(self.notifications)
        if self.note_length > 6:
            self.changable = 0.3
        elif self.note_length > 3:
            self.changable = 0.2
        else:
            self.changable = 0.1
        self.info_grid.size_hint = 0.6, self.changable

        for item in self.notifications:
            self.new_notice = Label(text=str(item), color=(0,0,0,1), font_size=13)
            self.info_grid.add_widget(self.new_notice)

        self.add_widget(self.info_grid)

    def get_my_notification(self, username, category):
        return "Default"

    def find_my_category(self):
        return "doctor"
    
    def find_my_username(self):
        return "hpt"
    
    def go_back(self):
        pass



# Subclasses of Notifications class
class AdminNotifications(Notifications):
    def find_my_category(self):
        return "admin"
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "AdminNotifications":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "AdminAfterLogin"
    
    def get_my_notification(self, username, category):
        return admin.recent_notifications(username, True, limit = 10)


class DoctorNotifications(Notifications):
    def find_my_category(self):
        return "doctor"
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "DoctorNotifications":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "DoctorAfterLogin"
    
    def get_my_notification(self, username, category):
        return doctor.recent_notifications(username, True, limit = 10)


class PatientNotifications(Notifications):
    def find_my_category(self):
        return "patient"

    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "PatientNotifications":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "PatientAfterLogin"
    
    def get_my_notification(self, username, category):
        return patient.recent_notifications(username, True, limit = 10)


class EmployeeNotifications(Notifications):
    def find_my_category(self):
        return "employee"

    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "EmployeeNotifications":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "EmployeeAfterLogin" 

    def get_my_notification(self, username, category):
        return employee.recent_notifications(username, True, limit = 10)





# AddNotifications class
class AddNotifications(Screen):
    receiver = ObjectProperty()
    body = ObjectProperty()
    receiver_category = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = self.find_my_category()
        with self.canvas:
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text=self.find_my_category().capitalize()+ " Add Notifications", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        self.info_grid.pos_hint = {"x": 0.2, "top": 0.7}
        self.info_grid.size_hint = 0.6, 0.3
        if self.category == "admin":
            self.receiver_username_name = Label(text= "Receiver's username:", font_size=15, color = (0,0,0,1))
            self.info_grid.add_widget(self.receiver_username_name)
            self.receiver_username_value = TextInput(multiline = False)
            self.info_grid.add_widget(self.receiver_username_value)            
            self.receiver_category_name = Label(text= "Receiver's category:", font_size=15, color = (0,0,0,1))
            self.info_grid.add_widget(self.receiver_category_name)
            self.receiver_category_value = TextInput(multiline = False)
            self.info_grid.add_widget(self.receiver_category_value)
        else:
            self.receiver_username_name = Label(text= "Admin's username:", font_size=15, color = (0,0,0,1))
            self.info_grid.add_widget(self.receiver_username_name)
            self.receiver_username_value = TextInput(multiline = False)
            self.info_grid.add_widget(self.receiver_username_value)
        self.notification_body_name = Label(text= "Notification's Body: ", font_size=15, color = (0,0,0,1))
        self.info_grid.add_widget(self.notification_body_name)
        self.notification_body_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.notification_body_value)
        self.add_widget(self.info_grid)

        self.submit = Button(text = "Send")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1,1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.2}
        self.add_widget(self.submit)
        self.submit.bind(on_release = self.pre_notifications)

    def pre_notifications(self, instance):
        receiver = self.receiver_username_value.text
        body = self.notification_body_value.text
        username = self.username
        
        self.send_notifications(body, receiver, username)
        
        self.receiver_username_value.text = ""
        self.notification_body_value.text = ""

    def send_notifications(self,body,receiver,username):
        return "Default"

    def find_my_category(self):
        return "doctor"
    
    def find_my_username(self):
        return "hpt"
    
    def go_back(self):
        pass



# Subclasses of AddNotifications class
class AdminAddNotifications(AddNotifications):
    def find_my_category(self):
        return "admin"
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "AdminAddNotifications":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "AdminAfterLogin"

    def pre_notifications(self, instance):
        receiver = self.receiver_username_value.text
        receiver_cat = self.receiver_category_value.text
        body = self.notification_body_value.text
        username = self.username
        
        self.send_notifications(body, receiver, username, receiver_cat)
        
        self.receiver_username_value.text = ""
        self.notification_body_value.text = ""
        self.receiver_category_value.text = ""
    
    def send_notifications(self, body, receiver, username, category):
        self.body = body
        self.receiver = receiver
        self.username = username
        self.category = category

        try:
            admin.add_notification(body,category,receiver, True)
        except: 
            show_NotificationPop()


class DoctorAddNotifications(AddNotifications):
    def find_my_category(self):
        return "doctor"
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "DoctorAddNotifications":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "DoctorAfterLogin"
    
    def send_notifications(self, body, receiver, username):
        self.body = body
        self.receiver = receiver
        self.username = username

        try:
            return doctor.notify_admin(self.body, self.username, self.receiver, True)
        except:
            show_NotificationPop()


class PatientAddNotifications(AddNotifications):
    def find_my_category(self):
        return "patient"

    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "PatientAddNotifications":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "PatientAfterLogin"
    
    def send_notifications(self, body, receiver, username):
        self.body = body
        self.receiver = receiver
        self.username = username

        try:
            return patient.notify_admin(self.body, self.username, self.receiver, True)
        except:
            show_NotificationPop()


class EmployeeAddNotifications(AddNotifications):
    def find_my_category(self):
        return "employee"

    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "EmployeeAddNotifications":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "EmployeeAfterLogin" 

    def send_notifications(self, body, receiver, username):
        self.body = body
        self.receiver = receiver
        self.username = username

        try:
            return employee.notify_admin(self.body, self.username, self.receiver, True)
        except:
            show_NotificationPop()


class NotificationPop(FloatLayout):
    pass


def show_NotificationPop():
    show = NotificationPop()
    popup_window = Popup(title = "Add Notification Error", content = show, size_hint = (0.6, 0.3))
    popup_window.open()





# Settings class
class Settings(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = self.find_my_category()
        with self.canvas:
            Color(1, 1, 1,1,mode="rgba")
            Rectangle(pos = self.pos, size = (800,600))
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text=self.find_my_category().capitalize()+ " Settings", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.poster = Image(source='resources/settings_pic.png', size_hint= (0.7,0.3), pos_hint= {"x": 0.16, "top": 0.85})
        self.add_widget(self.poster)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.notice = Label(text= "Only change the profile values which you need to change. Otherswise, leave it blank.", font_size=15, color = (51/255, 153/255, 255/255,1))
        self.notice.pos_hint = {"x": 0.015, "top": 1}
        self.add_widget(self.notice)

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        self.info_grid.pos_hint = {"x": 0.2, "top": 0.45}
        self.info_grid.size_hint = 0.6, 0.2

        self.fullname_name = Label(text= "Fullname:", font_size=15, color = (0,0,0,1))
        self.info_grid.add_widget(self.fullname_name)
        self.fullname_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.fullname_value)            
        self.email_name = Label(text= "Email Address:", font_size=15, color = (0,0,0,1))
        self.info_grid.add_widget(self.email_name)
        self.email_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.email_value)
        self.date_of_birth_name = Label(text= "Date of Birth:", font_size=15, color = (0,0,0,1))
        self.info_grid.add_widget(self.date_of_birth_name)
        self.date_of_birth_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.date_of_birth_value)
        self.add_widget(self.info_grid)

        self.submit = Button(text = "Save Settings")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = self.save_settings)

    def find_my_category(self):
        return "doctor"
    
    def find_my_username(self):
        return "hpt"
    
    def go_back(self):
        pass

    def save_settings(self, instance):
        fullname = self.fullname_value.text
        email = self.email_value.text
        date_of_birth = self.date_of_birth_value.text

        fullname_pass = False
        email_pass = False
        date_of_birth_pass = False

        if fullname != "":
            fullname_pass = True
        if email != "":
            email_pass = True
        if date_of_birth != "":
            date_of_birth_pass = True

        if fullname_pass:
            admin.update_db(self.category, self.username, "fullname", fullname, True)
        if email_pass:
            admin.update_db(self.category, self.username, "email", email, True)
        if date_of_birth_pass:
            admin.update_db(self.category, self.username, "date_of_birth", date_of_birth, True)

        

# Settings sub classes
class AdminSettings(Settings):
    def find_my_category(self):
        return "admin"
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "AdminSettings":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "AdminAfterLogin"
    

class DoctorSettings(Settings):
    def find_my_category(self):
        return "doctor"
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "DoctorSettings":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "DoctorAfterLogin"
    

class PatientSettings(Settings):
    def find_my_category(self):
        return "patient"

    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "PatientSettings":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "PatientAfterLogin"


class EmployeeSettings(Settings):
    def find_my_category(self):
        return "employee"

    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "EmployeeSettings":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "EmployeeAfterLogin" 






# Admin Functions
class AdminFunctions(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = "admin"
        with self.canvas:
            Color(1, 1, 1,1,mode="rgba")
            Rectangle(pos = self.pos, size = (800,600))
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text="Admin Functions", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        self.info_grid.pos_hint = {"x": 0.2, "top": 0.82}
        self.info_grid.size_hint = 0.6, 0.7

        self.total_earning_button = Button(text="Total Earning", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.total_earning_button.bind(on_release = lambda x:self.set_function("total_earning_function"))
        self.info_grid.add_widget(self.total_earning_button)
        self.add_employee_button = Button(text="Add Employee", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.add_employee_button.bind(on_release = lambda x:self.set_function("add_employee_function"))
        self.info_grid.add_widget(self.add_employee_button)
        self.see_my_employee_button = Button(text="See My Employee", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.see_my_employee_button.bind(on_release = lambda x:self.set_function("see_my_employee_function"))
        self.info_grid.add_widget(self.see_my_employee_button)
        self.remove_employee_button = Button(text="Remove Employee", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.remove_employee_button)
        self.remove_employee_button.bind(on_release = lambda x:self.set_function("remove_employee_function"))
        self.show_all_doctor_button = Button(text="Show All Doctor", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.show_all_doctor_button)
        self.show_all_doctor_button.bind(on_release = lambda x:self.set_function("show_all_doctor_function"))
        self.show_all_patient_button = Button(text="Show All Patient", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.show_all_patient_button)
        self.show_all_patient_button.bind(on_release = lambda x:self.set_function("show_all_patient_function"))
        self.show_all_employee_button = Button(text="Show All Employee", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.show_all_employee_button)
        self.show_all_employee_button.bind(on_release = lambda x:self.set_function("show_all_employee_function"))
        self.remove_doctor_parmanently_button = Button(text="Remove Doctor Parmanently", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.remove_doctor_parmanently_button)
        self.remove_doctor_parmanently_button.bind(on_release = lambda x:self.set_function("remove_doctor_parmanently_function"))
        self.remove_patient_parmanently_button = Button(text="Remove Patient Parmanently", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.remove_patient_parmanently_button)
        self.remove_patient_parmanently_button.bind(on_release = lambda x:self.set_function("remove_patient_parmanently_function"))
        self.remove_employee_parmanently_button = Button(text="Remove Employee Parmanently", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.remove_employee_parmanently_button)
        self.remove_employee_parmanently_button.bind(on_release = lambda x:self.set_function("remove_employee_parmanently_function"))
        self.patient_joins_doctor_button = Button(text="Patient Joins Doctor", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.patient_joins_doctor_button)
        self.patient_joins_doctor_button.bind(on_release = lambda x:self.set_function("patient_joins_doctor_function"))

        self.add_widget(self.info_grid)
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "AdminFunctions":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "AdminAfterLogin"

    def set_function(self, function_name):
        sm.add_widget(AdminDisplayFunction(function_name, name="AdminDisplayFunction"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "AdminDisplayFunction"
        


class AdminDisplayFunction(Screen):
    def __init__(self, function_name, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = "admin"
        self.function_name = function_name
        with self.canvas:
            Color(1, 1, 1,1,mode="rgba")
            Rectangle(pos = self.pos, size = (800,600))
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text="Admin Functions", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)        

        if self.function_name == "total_earning_function":
            final_function = self.total_earning_function
        elif self.function_name == "add_employee_function":
            final_function = self.add_employee_function
        elif self.function_name == "see_my_employee_function":
            final_function = self.see_my_employee_function
        elif self.function_name == "remove_employee_function":
            final_function = self.remove_employee_function
        elif self.function_name == "show_all_doctor_function":
            final_function = self.show_all_doctor_function
        elif self.function_name == "show_all_patient_function":
            final_function = self.show_all_patient_function
        elif self.function_name == "show_all_employee_function":
            final_function = self.show_all_employee_function
        elif self.function_name == "remove_doctor_parmanently_function":
            final_function = self.remove_doctor_parmanently_function
        elif self.function_name == "remove_patient_parmanently_function":
            final_function = self.remove_patient_parmanently_function
        elif self.function_name == "remove_employee_parmanently_function":
            final_function = self.remove_employee_parmanently_function
        else:
            final_function = self.patient_joins_doctor_function

        self.value, size_hint, pos_hint = final_function()
        self.value.size_hint = size_hint
        self.value.pos_hint = pos_hint
        self.add_widget(self.value)
        if (self.function_name == "show_all_patient_function") or (self.function_name == "patient_joins_doctor_function"):
            self.previous_button = Button()
            self.previous_button.font_size = 18
            self.previous_button.color = (1, 1, 1, 1)
            self.previous_button.italic = True
            self.previous_button.background_color = (1,1,1,0)
            self.previous_button.size_hint = (0, 0)
            self.previous_button.pos_hint = {"x":0.05, "top": 0.14}
            self.add_widget(self.previous_button)
            self.previous_button.bind(on_release = lambda x: self.next_button_function(function_name), on_press = lambda x: self.add_Holder_counter(-1))

            self.next_button = Button(text = "Next")
            self.next_button.font_size = 18
            self.next_button.color = (1, 1, 1, 1)
            self.next_button.italic = True
            self.next_button.background_color = (0/255, 153/255, 204/255, 1)
            self.next_button.size_hint = (0.1,0.05)
            self.next_button.pos_hint = {"x":0.85, "top": 0.14}
            self.add_widget(self.next_button)
            self.next_button.bind(on_release = lambda x: self.next_button_function(function_name))
            Holder.counter += 1


    def next_button_function(self,function_name):
        self.remove_widget(self.previous_button)
        self.remove_widget(self.next_button)

        if self.function_name == "total_earning_function":
            final_function = self.total_earning_function
        elif self.function_name == "add_employee_function":
            final_function = self.add_employee_function
        elif self.function_name == "see_my_employee_function":
            final_function = self.see_my_employee_function
        elif self.function_name == "remove_employee_function":
            final_function = self.remove_employee_function
        elif self.function_name == "show_all_doctor_function":
            final_function = self.show_all_doctor_function
        elif self.function_name == "show_all_patient_function":
            final_function = self.show_all_patient_function
        elif self.function_name == "show_all_employee_function":
            final_function = self.show_all_employee_function
        elif self.function_name == "remove_doctor_parmanently_function":
            final_function = self.remove_doctor_parmanently_function
        elif self.function_name == "remove_patient_parmanently_function":
            final_function = self.remove_patient_parmanently_function
        elif self.function_name == "remove_employee_parmanently_function":
            final_function = self.remove_employee_parmanently_function
        else:
            final_function = self.patient_joins_doctor_function

        self.remove_widget(self.info_grid)
        self.value, size_hint, pos_hint = final_function()
        self.value.size_hint = size_hint
        self.value.pos_hint = pos_hint
        self.add_widget(self.value)
        if (self.function_name == "show_all_patient_function") or (self.function_name == "patient_joins_doctor_function"):
            if Holder.counter != 0:
                self.previous_button = Button(text = "Previous")
                self.previous_button.font_size = 18
                self.previous_button.color = (1, 1, 1, 1)
                self.previous_button.italic = True
                self.previous_button.background_color = (0/255, 153/255, 204/255, 1)
                self.previous_button.size_hint = (0.1,0.05)
                self.previous_button.pos_hint = {"x":0.05, "top": 0.14}
                self.add_widget(self.previous_button)
                self.previous_button.bind(on_release = lambda x: self.next_button_function(function_name), on_press = lambda x: self.add_Holder_counter(-1))

            if Holder.counter != -1:
                self.next_button = Button(text = "Next")
                self.next_button.font_size = 18
                self.next_button.color = (1, 1, 1, 1)
                self.next_button.italic = True
                self.next_button.background_color = (0/255, 153/255, 204/255, 1)
                self.next_button.size_hint = (0.1,0.05)
                self.next_button.pos_hint = {"x":0.85, "top": 0.14}
                self.add_widget(self.next_button)
                self.next_button.bind(on_release = lambda x: self.next_button_function(function_name), on_press = lambda x : self.add_Holder_counter(1))                


    def add_Holder_counter(self,add_int):
        if Holder.counter == -1:
            Holder.counter = Holder.pre_counter 
        Holder.counter += add_int


    def find_my_username(self):
        return Holder.username
    

    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "AdminDisplayFunction":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "AdminFunctions"
        Holder.counter = 0


    def total_earning_function(self):
        total_earning_list = admin.total_earning(True)
        earned_from_employee = total_earning_list[0]
        earned_from_patient = total_earning_list[1]
        fixed_cost_of_hospital = total_earning_list[2]
        employee_pre_salary = total_earning_list[3]
        given_to_employees = total_earning_list[4]
        initial_earning = total_earning_list[5]

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        size_hint = 0.6, 0.5
        pos_hint = {"x": 0.2, "top": 0.715}

        self.label1 = Label(text = "Earned From Employee", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label1)
        self.label2 = Label(text = "+" + str(earned_from_employee), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label2)
        self.label3 = Label(text = "Earned From Patient", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label3)
        self.label4 = Label(text = "+" + str(earned_from_patient), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label4)
        self.label5 = Label(text = "Fixed Cost of Hospital", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label5)
        self.label6 = Label(text = "-" + str(fixed_cost_of_hospital), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label6)
        self.label7 = Label(text = "Employee_pre_salary", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label7)
        self.label8 = Label(text = "-" + str(employee_pre_salary), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label8)
        self.label9 = Label(text = "Given to Employees", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label9)
        self.label10 = Label(text = "-" + str(given_to_employees), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label10)
        self.label11 = Label(text = "Final Earning", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label11)
        self.label12 = Label(text = str(initial_earning), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label12)
        
        return (self.info_grid, size_hint, pos_hint)


    def add_employee_function(self):
        def current_function():
            try:
                admin.add_employee(self.employee_username.text, True)
            except:
                show_add_employee_popup()
            self.employee_username.text = ""

        def show_add_employee_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Add Employee Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.6}

        self.question = Label(text = "Enter the Employee Username You Want to Add", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question)
        self.employee_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.employee_username)

        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)


    def see_my_employee_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 6
        pos_hint = {"x": 0.05, "top": 0.75}

        employee_infos = admin.see_my_employee(True)
        if len(employee_infos) > 7:
            size_hint = 0.9, 0.6
        elif len(employee_infos) > 3:
            size_hint = 0.9, 0.45
        else:
            size_hint = 0.9, 0.2
        
        self.username_topic = Button(text = "Username", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.email_topic = Button(text = "Email", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.email_topic)
        self.date_of_birth_topic = Button(text = "Date of Birth", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.work_topic = Button(text = "Work", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.work_topic)
        self.salary_topic = Button(text = "Salary", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.salary_topic)

        for employee in employee_infos:
            self.username_info = Label(text = str(employee[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(employee[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.email_info = Label(text = str(employee[2]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.email_info)
            self.date_of_birth_info = Label(text = str(employee[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.date_of_birth_info)
            self.work_info = Label(text = str(employee[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.work_info)
            self.salary_info = Label(text = str(employee[5]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.salary_info)

        return (self.info_grid, size_hint, pos_hint)


    def remove_employee_function(self):
        def current_function():
            try:
                admin.remove_employee(self.employee_username.text, True)
            except:
                show_remove_employee_popup()
            self.employee_username.text = ""

        def show_remove_employee_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Remove Employee Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.6}

        self.question = Label(text = "Enter the Employee Username You Want to Remove", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question)
        self.employee_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.employee_username)

        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)


    def show_all_doctor_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 7
        pos_hint = {"x": 0.05, "top": 0.85}

        user_infos = admin.show_all_doctor(True)
        if len(user_infos) > 15:
            size_hint = 0.9, 0.8
        elif len(user_infos) > 8:
            size_hint = 0.9, 0.5
        else:
            size_hint = 0.9, 0.3
        
        self.username_topic = Button(text = "Username", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.email_topic = Button(text = "Email", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.email_topic)
        self.date_of_birth_topic = Button(text = "Date of Birth", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.specialty_topic = Button(text = "Specialty", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.specialty_topic)
        self.price_topic = Button(text = "Price", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.price_topic)
        self.total_earned_topic = Button(text = "Total Earned", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.total_earned_topic)

        for user in user_infos:
            self.username_info = Label(text = str(user[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(user[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.email_info = Label(text = str(user[2]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.email_info)
            self.date_of_birth_info = Label(text = str(user[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.date_of_birth_info)
            self.specialty_info = Label(text = str(user[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.specialty_info)
            self.price_info = Label(text = str(user[5]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.price_info)
            self.total_earned_info = Label(text = str(user[6]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.total_earned_info)

        return (self.info_grid, size_hint, pos_hint)


    def show_all_patient_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 8
        pos_hint = {"x": 0.05, "top": 0.85}
        counter = Holder.counter

        old_user_infos = admin.show_all_patient(True)
        user_infos = old_user_infos[counter*15 : counter*15 + 15]
        if len(old_user_infos) < (counter*15+15):
            Holder.pre_counter = Holder.counter
            Holder.counter = -1
        size_hint = 0.9,0.7
        if len(user_infos) < 5:
            size_hint = 0.9, 0.35
        
        self.username_topic = Button(text = "Username", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.email_topic = Button(text = "Email", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.email_topic)
        self.date_of_birth_topic = Button(text = "D O B", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.problem_topic = Button(text = "Problem", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.problem_topic)
        self.requested_doctor_username_topic = Button(text = "Requested", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.requested_doctor_username_topic)
        self.approved_doctor_username_topic = Button(text = "Approved", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.approved_doctor_username_topic)
        self.total_cost_topic = Button(text = "Cost", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.total_cost_topic)

        for user in user_infos:
            self.username_info = Label(text = str(user[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(user[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.email_info = Label(text = str(user[2]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.email_info)
            self.date_of_birth_info = Label(text = str(user[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.date_of_birth_info)
            self.problem_info = Label(text = str(user[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.problem_info)
            self.requested_doctor_username_info = Label(text = str(user[5]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.requested_doctor_username_info)
            self.approved_doctor_username_info = Label(text = str(user[6]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.approved_doctor_username_info)
            self.total_cost_info = Label(text = str(user[7]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.total_cost_info)

        return (self.info_grid, size_hint, pos_hint)


    def show_all_employee_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 8
        pos_hint = {"x": 0.05, "top": 0.85}

        user_infos = admin.show_all_employee(True)
        if len(user_infos) > 20:
            size_hint = 0.9, 8
        elif len(user_infos) > 10:
            size_hint = 0.9, 0.6
        else:
            size_hint = 0.9, 0.35
        
        self.username_topic = Button(text = "Username", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.email_topic = Button(text = "Email", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.email_topic)
        self.date_of_birth_topic = Button(text = "D O B", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.work_topic = Button(text = "Work", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.work_topic)
        self.work_of_doctors_topic = Button(text = "W O D", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.work_of_doctors_topic)
        self.salary_topic = Button(text = "Salary", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.salary_topic)
        self.total_earned_topic = Button(text = "Earned", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.total_earned_topic)

        for user in user_infos:
            self.username_info = Label(text = str(user[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(user[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.email_info = Label(text = str(user[2]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.email_info)
            self.date_of_birth_info = Label(text = str(user[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.date_of_birth_info)
            self.work_info = Label(text = str(user[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.work_info)
            self.work_of_doctors_info = Label(text = str(user[5]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.work_of_doctors_info)
            self.salary_info = Label(text = str(user[6]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.salary_info)
            self.total_earned_info = Label(text = str(user[7]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.total_earned_info)

        return (self.info_grid, size_hint, pos_hint)


    def remove_doctor_parmanently_function(self):
        def current_function():
            if self.final_decision_answer.text == "yes":
                final_decision = True
            else:
                final_decision = False
            
            if self.doctor_username.text not in admin.all_doctor_username(True):
                show_remove_doctor_parmanently_popup()
            else:
                admin.remove_doctor_parmanently(self.doctor_username.text, True, final_decision)
                
            self.doctor_username.text = ""
            self.final_decision_answer.text = ""

        def show_remove_doctor_parmanently_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Remove Doctor Parmanently Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.65}

        self.question = Label(text = "Doctor Username", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question)
        self.doctor_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.doctor_username)
        self.final_decision_question = Label(text = "Are You Sure? (yes/no)", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.final_decision_question)
        self.final_decision_answer = TextInput(multiline = False)
        self.info_grid.add_widget(self.final_decision_answer) 

        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)


    def remove_patient_parmanently_function(self):
        def current_function():
            if self.final_decision_answer.text == "yes":
                final_decision = True
            else:
                final_decision = False
            
            if self.patient_username.text not in admin.all_patient_username(True):
                show_remove_patient_parmanently_popup()
            else:
                admin.remove_patient_parmanently(self.patient_username.text, True, final_decision)
                
            self.patient_username.text = ""
            self.final_decision_answer.text = ""

        def show_remove_patient_parmanently_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Remove Patient Parmanently Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.65}

        self.question = Label(text = "Patient Username", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question)
        self.patient_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.patient_username)
        self.final_decision_question = Label(text = "Are You Sure? (yes/no)", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.final_decision_question)
        self.final_decision_answer = TextInput(multiline = False)
        self.info_grid.add_widget(self.final_decision_answer) 

        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)


    def remove_employee_parmanently_function(self):
        def current_function():
            if self.final_decision_answer.text == "yes":
                final_decision = True
            else:
                final_decision = False
            
            if self.employee_username.text not in admin.all_employee_username(True):
                show_remove_employee_parmanently_popup()
            else:
                admin.remove_employee_parmanently(self.employee_username.text, True, final_decision)
                
            self.employee_username.text = ""
            self.final_decision_answer.text = ""

        def show_remove_employee_parmanently_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Remove Employee Parmanently Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.65}

        self.question = Label(text = "Employee Username", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question)
        self.employee_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.employee_username)
        self.final_decision_question = Label(text = "Are You Sure? (yes/no)", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.final_decision_question)
        self.final_decision_answer = TextInput(multiline = False)
        self.info_grid.add_widget(self.final_decision_answer) 

        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)


    def patient_joins_doctor_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 6
        pos_hint = {"x": 0.05, "top": 0.85}
        counter = Holder.counter

        old_user_infos = admin.patient_joins_doctor(True)
        user_infos = old_user_infos[counter*15 : counter*15 + 15]
        if len(old_user_infos) < (counter*15+15):
            Holder.pre_counter = Holder.counter
            Holder.counter = -1
        size_hint = 0.9,0.7
        if len(user_infos) < 5:
            size_hint = 0.9, 0.35
        
        self.username_topic = Button(text = "Username", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.problem_topic = Button(text = "Problem", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.problem_topic)
        self.appointment_topic = Button(text = "Appoint Date", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.appointment_topic)
        self.dusername_topic = Button(text = "D Username", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.dusername_topic)
        self.dfullname_topic = Button(text = "D Fullname", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.dfullname_topic)

        for user in user_infos:
            self.username_info = Label(text = str(user[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(user[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.problem_info = Label(text = str(user[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.problem_info)
            self.appoint_info = Label(text = str(user[4]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.appoint_info)
            self.dusername_info = Label(text = str(user[5]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.dusername_info)
            self.dfullname_info = Label(text = str(user[6]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.dfullname_info) 
        return (self.info_grid, size_hint, pos_hint)





# Doctor Functions
class DoctorFunctions(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = "doctor"
        with self.canvas:
            Color(1, 1, 1,1,mode="rgba")
            Rectangle(pos = self.pos, size = (800,600))
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text="Doctor Functions", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        self.info_grid.pos_hint = {"x": 0.2, "top": 0.82}
        self.info_grid.size_hint = 0.6, 0.7

        self.salary_button = Button(text="Salary", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.salary_button)
        self.salary_button.bind(on_release = lambda x: self.set_function("salary_function"))
        self.show_all_employee_button = Button(text="Show All Employee", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.show_all_employee_button)
        self.show_all_employee_button.bind(on_release = lambda x: self.set_function("show_all_employee_function"))
        self.add_employee_button = Button(text="Add Employee", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.add_employee_button)
        self.add_employee_button.bind(on_release = lambda x: self.set_function("add_employee_function"))
        self.see_my_employee_button = Button(text="See My Employee", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.see_my_employee_button)
        self.see_my_employee_button.bind(on_release = lambda x: self.set_function("see_my_employee_function"))
        self.remove_employee_button = Button(text="Remove Employee", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.remove_employee_button)
        self.remove_employee_button.bind(on_release = lambda x: self.set_function("remove_employee_function"))
        self.see_all_requested_patient_button = Button(text="See All Requested Patient", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.see_all_requested_patient_button)
        self.see_all_requested_patient_button.bind(on_release = lambda x: self.set_function("see_all_requested_patient_function"))
        self.see_all_patients_of_my_specialty_button = Button(text="See All Patients of My Specialty", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.see_all_patients_of_my_specialty_button)
        self.see_all_patients_of_my_specialty_button.bind(on_release = lambda x: self.set_function("see_all_patients_of_my_specialty_function"))
        self.see_my_patient_button = Button(text="See My Patient", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.see_my_patient_button)
        self.see_my_patient_button.bind(on_release = lambda x: self.set_function("see_my_patient_function"))
        self.see_patients_report_button = Button(text="See Patients Report", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.see_patients_report_button)
        self.see_patients_report_button.bind(on_release = lambda x: self.set_function("see_patients_report_function"))
        self.remove_patient_button = Button(text="Remove Patient", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.remove_patient_button)    
        self.remove_patient_button.bind(on_release = lambda x: self.set_function("remove_patient_function"))    

        self.add_widget(self.info_grid)
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "DoctorFunctions":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "DoctorAfterLogin"

    def set_function(self, function_name):
        sm.add_widget(DoctorDisplayFunction(function_name, name="DoctorDisplayFunction"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "DoctorDisplayFunction"



class DoctorDisplayFunction(Screen):
    def __init__(self, function_name, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = "doctor"
        self.function_name = function_name
        with self.canvas:
            Color(1, 1, 1,1,mode="rgba")
            Rectangle(pos = self.pos, size = (800,600))
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text="Doctor Functions", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)        

        if self.function_name == "salary_function":
            final_function = self.salary_function
        elif self.function_name == "show_all_employee_function":
            final_function = self.show_all_employee_function
        elif self.function_name == "add_employee_function":
            final_function = self.add_employee_function
        elif self.function_name == "see_my_employee_function":
            final_function = self.see_my_employee_function
        elif self.function_name == "remove_employee_function":
            final_function = self.remove_employee_function
        elif self.function_name == "see_all_requested_patient_function":
            final_function = self.see_all_requested_patient_function
        elif self.function_name == "see_all_patients_of_my_specialty_function":
            final_function = self.see_all_patients_of_my_specialty_function
        elif self.function_name == "see_my_patient_function":
            final_function = self.see_my_patient_function
        elif self.function_name == "see_patients_report_function":
            final_function = self.see_patients_report_function
        else:
            final_function = self.remove_patient_function        

        self.value, size_hint, pos_hint = final_function()
        self.value.size_hint = size_hint
        self.value.pos_hint = pos_hint
        self.add_widget(self.value)

    
    def find_my_username(self):
        return Holder.username
    

    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "DoctorDisplayFunction":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "DoctorFunctions"
        Holder.counter = 0




    def salary_function(self):
        total_earning_list = doctor.salary(Holder.username, True)
        total_earning = total_earning_list[0]
        total_cost = total_earning_list[1]
        nit_salary = total_earning_list[2]

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        size_hint = 0.6, 0.3
        pos_hint = {"x": 0.2, "top": 0.6}

        self.label1 = Label(text = "Total Earning", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label1)
        self.label2 = Label(text = "+" + str(total_earning), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label2)
        self.label3 = Label(text = "Total Cost", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label3)
        self.label4 = Label(text = "-" + str(total_cost), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label4)
        self.label5 = Label(text = "Nit Salary", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label5)
        self.label6 = Label(text = str(nit_salary), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label6)

        return (self.info_grid, size_hint, pos_hint)

    def show_all_employee_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 6
        pos_hint = {"x": 0.05, "top": 0.85}

        user_infos = doctor.show_all_employee(True)
        if len(user_infos) > 20:
            size_hint = 0.9, 8
        elif len(user_infos) > 10:
            size_hint = 0.9, 0.6
        else:
            size_hint = 0.9, 0.35
        
        self.username_topic = Button(text = "Username", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.email_topic = Button(text = "Email", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.email_topic)
        self.date_of_birth_topic = Button(text = "D O B", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.work_topic = Button(text = "Work", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.work_topic)
        self.salary_topic = Button(text = "Salary", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.salary_topic)

        for user in user_infos:
            self.username_info = Label(text = str(user[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(user[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.email_info = Label(text = str(user[2]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.email_info)
            self.date_of_birth_info = Label(text = str(user[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.date_of_birth_info)
            self.work_info = Label(text = str(user[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.work_info)
            self.salary_info = Label(text = str(user[5]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.salary_info)

        return (self.info_grid, size_hint, pos_hint)

        

    def add_employee_function(self):
        def current_function():
            try:
                doctor.add_employee(self.username,self.employee_username.text, True)
            except:
                show_add_employee_popup()
            self.employee_username.text = ""

        def show_add_employee_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Add Employee Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.6}

        self.question = Label(text = "Enter the Employee Username You Want to Add", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question)
        self.employee_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.employee_username)

        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)


    def see_my_employee_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 6
        pos_hint = {"x": 0.05, "top": 0.75}

        employee_infos = doctor.see_my_employee(self.username,True)
        if len(employee_infos) > 7:
            size_hint = 0.9, 0.6
        elif len(employee_infos) > 3:
            size_hint = 0.9, 0.45
        else:
            size_hint = 0.9, 0.2
        
        self.username_topic = Button(text = "Username", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.email_topic = Button(text = "Email", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.email_topic)
        self.date_of_birth_topic = Button(text = "Date of Birth", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.work_topic = Button(text = "Work", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.work_topic)
        self.salary_topic = Button(text = "Salary", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.salary_topic)

        for employee in employee_infos:
            self.username_info = Label(text = str(employee[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(employee[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.email_info = Label(text = str(employee[2]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.email_info)
            self.date_of_birth_info = Label(text = str(employee[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.date_of_birth_info)
            self.work_info = Label(text = str(employee[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.work_info)
            self.salary_info = Label(text = str(employee[5]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.salary_info)

        return (self.info_grid, size_hint, pos_hint)


    def remove_employee_function(self):
        def current_function():
            try:
                doctor.remove_employee(self.username, self.employee_username.text, True)
            except:
                show_remove_employee_popup()
            self.employee_username.text = ""

        def show_remove_employee_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Remove Employee Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.6}

        self.question = Label(text = "Enter the Employee Username You Want to Remove", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question)
        self.employee_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.employee_username)

        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)

    
    def see_all_requested_patient_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 5
        pos_hint = {"x": 0.05, "top": 0.75}

        patient_infos = doctor.see_all_requested_patient(self.username,True)
        if len(patient_infos) > 7:
            size_hint = 0.9, 0.6
        elif len(patient_infos) > 3:
            size_hint = 0.9, 0.45
        else:
            size_hint = 0.9, 0.2
        
        self.username_topic = Button(text = "Username", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.email_topic = Button(text = "Email", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.email_topic)
        self.date_of_birth_topic = Button(text = "Date of Birth", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.problem_topic = Button(text = "Problem", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.problem_topic)

        for patient in patient_infos:
            self.username_info = Label(text = str(patient[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(patient[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.email_info = Label(text = str(patient[2]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.email_info)
            self.date_of_birth_info = Label(text = str(patient[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.date_of_birth_info)
            self.problem_info = Label(text = str(patient[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.problem_info)

        return (self.info_grid, size_hint, pos_hint)


    def see_all_patients_of_my_specialty_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 6
        pos_hint = {"x": 0.05, "top": 0.75}

        patient_infos = doctor.see_all_patients_of_my_specialty(self.username,True)
        if len(patient_infos) > 7:
            size_hint = 0.9, 0.6
        elif len(patient_infos) > 3:
            size_hint = 0.9, 0.45
        else:
            size_hint = 0.9, 0.2
        
        self.username_topic = Button(text = "Username", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.email_topic = Button(text = "Email", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.email_topic)
        self.date_of_birth_topic = Button(text = "Date of Birth", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.requested_topic = Button(text = "Requested", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.requested_topic)
        self.approved_topic = Button(text = "Approved", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.approved_topic)

        for patient in patient_infos:
            self.username_info = Label(text = str(patient[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(patient[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.email_info = Label(text = str(patient[2]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.email_info)
            self.date_of_birth_info = Label(text = str(patient[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.date_of_birth_info)
            self.requested_info = Label(text = str(patient[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.requested_info)
            self.approved_info = Label(text = str(patient[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.approved_info)

        return (self.info_grid, size_hint, pos_hint)


    def see_my_patient_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 6
        pos_hint = {"x": 0.05, "top": 0.75}

        patient_infos = doctor.see_my_patient(self.username,True)
        if len(patient_infos) > 7:
            size_hint = 0.9, 0.6
        elif len(patient_infos) > 3:
            size_hint = 0.9, 0.45
        else:
            size_hint = 0.9, 0.2
        
        self.username_topic = Button(text = "Username", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.email_topic = Button(text = "Email", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.email_topic)
        self.date_of_birth_topic = Button(text = "Date of Birth", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.problem_topic = Button(text = "Problem", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.problem_topic)
        self.appointment_timestamp_topic = Button(text = "Appoint TS", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=150)
        self.info_grid.add_widget(self.appointment_timestamp_topic)

        for patient in patient_infos:
            self.username_info = Label(text = str(patient[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(patient[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.email_info = Label(text = str(patient[2]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.email_info)
            self.date_of_birth_info = Label(text = str(patient[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.date_of_birth_info)
            self.problem_info = Label(text = str(patient[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.problem_info)
            self.appointment_timestamp_info = Label(text = str(patient[5]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=150)
            self.info_grid.add_widget(self.appointment_timestamp_info)

        return (self.info_grid, size_hint, pos_hint)


    def see_patients_report_function(self):
        def current_function():
            try:
                doctor.see_patients_report(self.patient_username.text, self.report_name.text, True)
            except:
                show_see_patients_report_popup()
            self.patient_username.text = ""
            self.report_name.text = ""

        def show_see_patients_report_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username or Report Name", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Show Patient Report Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.62}

        self.question = Label(text = "Patient Username", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question)
        self.patient_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.patient_username)

        self.question2 = Label(text = "Report Name", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question2)
        self.report_name = TextInput(multiline = False)
        self.info_grid.add_widget(self.report_name)

        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)

    
    def remove_patient_function(self):
        def current_function():
            try:
                doctor.remove_patient(self.patient_username.text, True)
            except:
                show_remove_patient_popup()
            self.patient_username.text = ""

        def show_remove_patient_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Remove Patient Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.6}

        self.question = Label(text = "Enter the Patient Username You Want to Remove", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question)
        self.patient_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.patient_username)

        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)





# Patient Functions
class PatientFunctions(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = "patient"
        with self.canvas:
            Color(1, 1, 1,1,mode="rgba")
            Rectangle(pos = self.pos, size = (800,600))
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text="Patient Functions", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        self.info_grid.pos_hint = {"x": 0.2, "top": 0.82}
        self.info_grid.size_hint = 0.6, 0.7

        self.cost_button = Button(text="Total Cost", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.cost_button)
        self.cost_button.bind(on_release = lambda x: self.set_function("cost_function"))
        self.remaining_appointment_time_button = Button(text="Remaining Appointment Time", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.remaining_appointment_time_button)
        self.remaining_appointment_time_button.bind(on_release = lambda x: self.set_function("remaining_appointment_time_function"))
        self.add_report_button = Button(text="Add Report", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.add_report_button)
        self.add_report_button.bind(on_release = lambda x: self.set_function("add_report_function"))
        self.see_all_doctors_for_my_problem_button = Button(text="See All Doctors for My Problem", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.see_all_doctors_for_my_problem_button)
        self.see_all_doctors_for_my_problem_button.bind(on_release = lambda x: self.set_function("see_all_doctors_for_my_problem_function"))
        self.request_doctor_button = Button(text="Request Doctor", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.request_doctor_button)  
        self.request_doctor_button.bind(on_release = lambda x: self.set_function("request_doctor_function"))  
        self.remove_request_button = Button(text="Remove Request", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.remove_request_button)
        self.remove_request_button.bind(on_release = lambda x: self.set_function("remove_request_function"))
        self.see_my_doctors_stat_button = Button(text="See My Doctors Stat", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.see_my_doctors_stat_button)    
        self.see_my_doctors_stat_button.bind(on_release = lambda x: self.set_function("see_my_doctors_stat_function"))    

        self.add_widget(self.info_grid)
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "PatientFunctions":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "PatientAfterLogin"

    def set_function(self, function_name):
        sm.add_widget(PatientDisplayFunction(function_name, name="PatientDisplayFunction"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "PatientDisplayFunction"



class PatientDisplayFunction(Screen):
    def __init__(self, function_name, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = "patient"
        self.function_name = function_name
        with self.canvas:
            Color(1, 1, 1,1,mode="rgba")
            Rectangle(pos = self.pos, size = (800,600))
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text="Patient Functions", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)        

        if self.function_name == "cost_function":
            final_function = self.cost_function
        elif self.function_name == "remaining_appointment_time_function":
            final_function = self.remaining_appointment_time_function
        elif self.function_name == "add_report_function":
            final_function = self.add_report_function
        elif self.function_name == "see_all_doctors_for_my_problem_function":
            final_function = self.see_all_doctors_for_my_problem_function
        elif self.function_name == "request_doctor_function":
            final_function = self.request_doctor_function
        elif self.function_name == "remove_request_function":
            final_function = self.remove_request_function
        else:
            final_function = self.see_my_doctors_stat_function        

        self.value, size_hint, pos_hint = final_function()
        self.value.size_hint = size_hint
        self.value.pos_hint = pos_hint
        self.add_widget(self.value)

    
    def find_my_username(self):
        return Holder.username
    

    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "PatientDisplayFunction":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "PatientFunctions"
        Holder.counter = 0

    def cost_function(self):
        total_earning_list = patient.cost(Holder.username, True)
        doctor_charge = total_earning_list[0]
        hospital_charge = total_earning_list[1]
        total_charge = total_earning_list[2]

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        size_hint = 0.6, 0.3
        pos_hint = {"x": 0.2, "top": 0.6}

        self.label1 = Label(text = "Doctor's Charge:", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label1)
        self.label2 = Label(text = "+" + str(doctor_charge), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label2)
        self.label3 = Label(text = "Hospital's Charge:", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label3)
        self.label4 = Label(text = "+" + str(hospital_charge), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label4)
        self.label5 = Label(text = "Total Charge:", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label5)
        self.label6 = Label(text = str(total_charge), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label6)

        return (self.info_grid, size_hint, pos_hint)

    def remaining_appointment_time_function(self):
        timestamp = str(patient.remaining_appointment_time(Holder.username, True))

        day, time = timestamp.split(", ")
        hour, minute, sec = time.split(":")

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        size_hint = 0.6, 0.3
        pos_hint = {"x": 0.2, "top": 0.62}

        self.label1 = Label(text = "Day:", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label1)
        self.label2 = Label(text = str(day), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label2)
        self.label3 = Label(text = "Hour:", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label3)
        self.label4 = Label(text = str(hour) + " hours", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label4)
        self.label5 = Label(text = "Minute:", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label5)
        self.label6 = Label(text = str(minute)+ " minutes", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label6)

        return (self.info_grid, size_hint, pos_hint)

    def add_report_function(self):
        def current_function():
            if self.report_name.text == "" or self.report_url.text == "":
                show_add_report_popup()
            try:
                patient.add_report(self.report_name.text, self.report_url.text, self.username, True)
            except:
                show_add_report_popup()
            self.report_name.text = ""
            self.report_url.text = ""

        def show_add_report_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username or Report Name", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Add Report Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.62}

        self.question1 = Label(text = "Report Name", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question1)
        self.report_name = TextInput(multiline = False)
        self.info_grid.add_widget(self.report_name)

        self.question2 = Label(text = "Report Url", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question2)
        self.report_url = TextInput(multiline = False)
        self.info_grid.add_widget(self.report_url)

        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)

    def see_all_doctors_for_my_problem_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 5
        pos_hint = {"x": 0.05, "top": 0.75}

        doctor_infos = patient.see_all_doctors_for_my_problem(self.username,True)
        if len(doctor_infos) > 7:
            size_hint = 0.9, 0.6
        elif len(doctor_infos) > 3:
            size_hint = 0.9, 0.45
        else:
            size_hint = 0.9, 0.2
        
        self.username_topic = Button(text = "Username", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.email_topic = Button(text = "Email", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.email_topic)
        self.date_of_birth_topic = Button(text = "Date of Birth", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.salary_topic = Button(text = "Salary", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.salary_topic)


        for doctor in doctor_infos:
            self.username_info = Label(text = str(doctor[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(doctor[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.email_info = Label(text = str(doctor[2]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.email_info)
            self.date_of_birth_info = Label(text = str(doctor[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.date_of_birth_info)
            self.salary_info = Label(text = str(doctor[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.salary_info)

        return (self.info_grid, size_hint, pos_hint)

    def request_doctor_function(self):
        def current_function():
            try:
                patient.request_doctor(self.username,self.doctor_username.text, True)
            except:
                show_request_doctor_popup()
            self.doctor_username.text = ""

        def show_request_doctor_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Request Doctor Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.6}

        self.question = Label(text = "Enter the Doctor Username You Want to Request", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question)
        self.doctor_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.doctor_username)

        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)


    def remove_request_function(self):
        patient.remove_request(self.username, True)

        self.info_grid = Label(text = "Successfully removed request :)", font_size = 25, color = (0/255, 153/255, 204/255, 1))
        size_hint = 0,0
        pos_hint = {"x": 0.52, "top": 0.5}

        return(self.info_grid, size_hint, pos_hint)


    def see_my_doctors_stat_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        pos_hint = {"x": 0.31, "top": 0.65}

        doctor_info = patient.see_my_doctors_stat(self.username,True)
        size_hint = 0.5, 0.4
        
        self.username_topic = Button(text = "Username", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.username_info = Label(text = str(doctor_info[0]), font_size = 12, color = (0,0,0,1))
        self.info_grid.add_widget(self.username_info)
        self.fullname_topic = Button(text = "Fullname", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.fullname_info = Label(text = str(doctor_info[1]), font_size = 12, color = (0,0,0,1))
        self.info_grid.add_widget(self.fullname_info)
        self.email_topic = Button(text = "Email", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.email_topic)
        self.email_info = Label(text = str(doctor_info[2]), font_size = 12, color = (0,0,0,1))
        self.info_grid.add_widget(self.email_info)
        self.date_of_birth_topic = Button(text = "Date of Birth", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.date_of_birth_info = Label(text = str(doctor_info[3]), font_size = 12, color = (0,0,0,1))
        self.info_grid.add_widget(self.date_of_birth_info)
        self.salary_topic = Button(text = "Salary", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.salary_topic)
        self.salary_info = Label(text = str(doctor_info[4]), font_size = 12, color = (0,0,0,1))
        self.info_grid.add_widget(self.salary_info)
        self.appointment_timestamp_topic = Button(text = "Appointment Timestamp", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.appointment_timestamp_topic)
        self.appointment_timestamp_info = Label(text = str(doctor_info[5]), font_size = 12, color = (0,0,0,1))
        self.info_grid.add_widget(self.appointment_timestamp_info)            

        return (self.info_grid, size_hint, pos_hint)
        




# Employee Functions
class EmployeeFunctions(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = "employee"
        self.is_receptionist = employee.isreceptionist(self.username, True)
        with self.canvas:
            Color(1, 1, 1,1,mode="rgba")
            Rectangle(pos = self.pos, size = (800,600))
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text="Employee Functions", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        self.info_grid.pos_hint = {"x": 0.2, "top": 0.82}
        self.info_grid.size_hint = 0.6, 0.7

        self.salary_button = Button(text="Salary", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.salary_button)
        self.salary_button.bind(on_release = lambda x: self.set_function("salary_function"))
        self.see_my_doctors_button = Button(text="See My Doctors", background_color = (0.75, 0.75, 0.75, 1), color= (1,1,1,1), font_size = 14)
        self.info_grid.add_widget(self.see_my_doctors_button)   
        self.see_my_doctors_button.bind(on_release = lambda x: self.set_function("see_my_doctors_function"))
        if self.is_receptionist:
            self.appoint_doctor_button = Button(text="Appoint Doctor", background_color = (0/255, 153/255, 204/255, 1), color= (1,1,1,1), font_size = 14)
            self.info_grid.add_widget(self.appoint_doctor_button)
            self.appoint_doctor_button.bind(on_release = lambda x: self.set_function("appoint_doctor_function"))


        self.add_widget(self.info_grid)
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "EmployeeFunctions":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "EmployeeAfterLogin"

    def set_function(self, function_name):
        sm.add_widget(EmployeeDisplayFunction(function_name, name="EmployeeDisplayFunction"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "EmployeeDisplayFunction"



class EmployeeDisplayFunction(Screen):
    def __init__(self, function_name, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = "employee"
        self.function_name = function_name
        with self.canvas:
            Color(1, 1, 1,1,mode="rgba")
            Rectangle(pos = self.pos, size = (800,600))
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text="Employee Functions", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"x":0.05, "top": 1.45}
        self.add_widget(self.title)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.close_button = Button(background_normal="resources/close.png", background_down="resources/close_down.png") 
        self.close_button.size_hint = (None, None)
        self.close_button.width = 60
        self.close_button.height = 60
        self.close_button.color = (0,0,0,1)
        self.close_button.pos_hint = {"x": 0.85, "top": 0.99}
        self.add_widget(self.close_button)
        self.close_button.bind(on_release = self.go_back)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline= Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)        

        if self.function_name == "salary_function":
            final_function = self.salary_function
        elif self.function_name == "see_my_doctors_function":
            final_function = self.see_my_doctors_function
        else:
            final_function = self.appoint_doctor_function        

        self.value, size_hint, pos_hint = final_function()
        self.value.size_hint = size_hint
        self.value.pos_hint = pos_hint
        self.add_widget(self.value)

    
    def find_my_username(self):
        return Holder.username
    

    def go_back(self, instance):
        for screen in sm.screens:
            if screen.name == "EmployeeDisplayFunction":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "EmployeeFunctions"
        Holder.counter = 0


    def salary_function(self):
        total_earning_list = employee.salary(Holder.username, True)
        initial_salary = total_earning_list[0]
        hospital_cost = total_earning_list[1]
        nit_salary = total_earning_list[2]

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        size_hint = 0.6, 0.3
        pos_hint = {"x": 0.2, "top": 0.6}

        self.label1 = Label(text = "Initial Salary", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label1)
        self.label2 = Label(text = "+" + str(initial_salary), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label2)
        self.label3 = Label(text = "Hospital Cost", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label3)
        self.label4 = Label(text = "-" + str(hospital_cost), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label4)
        self.label5 = Label(text = "Nit Salary", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label5)
        self.label6 = Label(text = str(nit_salary), color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.label6)

        return (self.info_grid, size_hint, pos_hint)


    def see_my_doctors_function(self):
        self.info_grid = GridLayout()
        self.info_grid.cols = 5
        pos_hint = {"x": 0.05, "top": 0.75}

        doctor_infos = employee.see_my_doctors(self.username,True)
        if len(doctor_infos) > 7:
            size_hint = 0.9, 0.6
        elif len(doctor_infos) > 3:
            size_hint = 0.9, 0.45
        else:
            size_hint = 0.9, 0.2
        
        self.username_topic = Button(text = "Username", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.username_topic)
        self.fullname_topic = Button(text = "Fullname", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.fullname_topic)
        self.email_topic = Button(text = "Email", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1), size_hint_x=None, width=200)
        self.info_grid.add_widget(self.email_topic)
        self.date_of_birth_topic = Button(text = "Date of Birth", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.date_of_birth_topic)
        self.specialty_topic = Button(text = "Specialty", font_size = 15, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.specialty_topic)

        for doctor in doctor_infos:
            self.username_info = Label(text = str(doctor[0]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.username_info)
            self.fullname_info = Label(text = str(doctor[1]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.fullname_info)
            self.email_info = Label(text = str(doctor[2]), font_size = 12, color = (0,0,0,1), size_hint_x=None, width=200)
            self.info_grid.add_widget(self.email_info)
            self.date_of_birth_info = Label(text = str(doctor[3]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.date_of_birth_info)
            self.specialty_info = Label(text = str(doctor[4]), font_size = 12, color = (0,0,0,1))
            self.info_grid.add_widget(self.specialty_info)

        return (self.info_grid, size_hint, pos_hint)


    def appoint_doctor_function(self):
        def current_function():
            try:
                employee.appoint_doctor(self.username, self.doctor_username.text, self.patient_username.text, self.appointment_timestamp.text, True)
            except:
                show_appoint_doctor_popup()
            self.doctor_username.text = ""
            self.patient_username.text = ""
            self.appointment_timestamp.text = "YYYY-MM-DD HH:MM:SS"

        def show_appoint_doctor_popup():
            popup_layout = FloatLayout()
            first_line = Label(text = "Sorry, Something went Wrong :(", size_hint= (0.6, 0.2), pos_hint= {"x": 0.2, "top":0.9})
            popup_layout.add_widget(first_line)
            second_line = Label(text="Invalid Username or Date Format", size_hint= (0.6, 0.2), pos_hint= {"x": 0.21, "top":0.5})
            popup_layout.add_widget(second_line)
            popup_window = Popup(title = "Appoint Doctor Error", content = popup_layout, size_hint = (0.6, 0.3))
            popup_window.open()

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        size_hint = 0.6, 0.2
        pos_hint = {"x": 0.2, "top": 0.65}

        self.question1 = Label(text = "Doctor Username:", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question1)
        self.doctor_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.doctor_username)

        self.question2 = Label(text = "Patient Username:", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question2)
        self.patient_username = TextInput(multiline = False)
        self.info_grid.add_widget(self.patient_username)

        self.question3 = Label(text = "Appointment Timestamp:", color = (0,0,0,1), font_size = 16)
        self.info_grid.add_widget(self.question3)
        self.appointment_timestamp = TextInput(text = "YYYY-MM-DD HH:MM:SS", multiline = False)
        self.info_grid.add_widget(self.appointment_timestamp)


        self.submit = Button(text = "Submit")
        self.submit.font_size = 18
        self.submit.color = (1, 1, 1, 1)
        self.submit.italic = True
        self.submit.background_color = (0/255, 153/255, 204/255, 1)
        self.submit.size_hint = (0.3,0.08)
        self.submit.pos_hint = {"x":0.36, "top": 0.175}
        self.add_widget(self.submit)
        self.submit.bind(on_release = lambda x: current_function())

        return (self.info_grid, size_hint, pos_hint)







# AdminAfterLogin Class
class AdminAfterLogin(Screen, Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
            Color(0.4, 0.4, 0.4,1,mode="rgba")
            Line(points = ((410, 80),(410, 280)), width = 2)
            Line(points = ((180, 175),(620, 175)), width = 2)
        self.title = Label(text="Admin Panel", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"top": 1.45}
        self.add_widget(self.title)

        self.add_notifications_button = Button(background_normal="resources/add_notifications.png", background_down="resources/add_notifications_down.png") 
        self.add_notifications_button.size_hint = (None, None)
        self.add_notifications_button.width = 70
        self.add_notifications_button.height = 70
        self.add_notifications_button.color = (0,0,0,1)
        self.add_notifications_button.pos_hint = {"x": 0.72, "top": 1}
        self.add_widget(self.add_notifications_button)
        self.add_notifications_button.bind(on_release = self.go_to_add_notifications)

        self.notifications_button = Button(background_normal="resources/notifications.png", background_down="resources/notifications_down.png") 
        self.notifications_button.size_hint = (None, None)
        self.notifications_button.width = 70
        self.notifications_button.height = 70
        self.notifications_button.color = (0,0,0,1)
        self.notifications_button.pos_hint = {"x": 0.80, "top": 1}
        self.add_widget(self.notifications_button)
        self.notifications_button.bind(on_release = self.go_to_notifications)

        self.profile_button = Button(background_normal="resources/profile.png", background_down="resources/profile_down.png") 
        self.profile_button.size_hint = (None, None)
        self.profile_button.width = 70
        self.profile_button.height = 70
        self.profile_button.color = (0,0,0,1)
        self.profile_button.pos_hint = {"x": 0.88, "top": 1}
        self.add_widget(self.profile_button)
        self.profile_button.bind(on_release = self.go_to_profile)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline = Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.functions_label = Label(text="Functions", font_size=15, color=(0,0,0,1))
        self.functions_label.pos_hint = {"x":-0.19, "top": 0.82}
        self.add_widget(self.functions_label)

        self.about_hospital_label = Label(text="About Hospital", font_size=15, color=(0,0,0,1))
        self.about_hospital_label.pos_hint = {"x":-0.187, "top": 0.61}
        self.add_widget(self.about_hospital_label)

        self.settings_label = Label(text="Settings", font_size=15, color=(0,0,0,1))
        self.settings_label.pos_hint = {"x":0.213, "top": 0.825}
        self.add_widget(self.settings_label)

        self.documentation_label = Label(text="Documentation", font_size=15, color=(0,0,0,1))
        self.documentation_label.pos_hint = {"x":0.215, "top": 0.615}
        self.add_widget(self.documentation_label)

    def go_to_profile(self, instance):
        sm.add_widget(AdminProfile(name = "AdminProfile"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "AdminProfile"
    
    def go_to_notifications(self, instance):
        sm.add_widget(AdminNotifications(name = "AdminNotifications"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "AdminNotifications"

    def go_to_add_notifications(self, instance):
        sm.add_widget(AdminAddNotifications(name = "AdminAddNotifications"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "AdminAddNotifications"

    def go_to_settings(self):
        Window.clearcolor = (1,1,1,1)
        sm.add_widget(AdminSettings(name = "AdminSettings"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "AdminSettings"

    def go_to_functions(self):
        sm.add_widget(AdminFunctions(name = "AdminFunctions"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "AdminFunctions"
        

        


# DoctorAfterLogin Class
class DoctorAfterLogin(Screen, Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
            Color(0.4, 0.4, 0.4,1,mode="rgba")
            Line(points = ((410, 80),(410, 280)), width = 2)
            Line(points = ((180, 175),(620, 175)), width = 2)
        self.title = Label(text="Doctor Panel", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"top": 1.45}
        self.add_widget(self.title)

        self.add_notifications_button = Button(background_normal="resources/add_notifications.png", background_down="resources/add_notifications_down.png") 
        self.add_notifications_button.size_hint = (None, None)
        self.add_notifications_button.width = 70
        self.add_notifications_button.height = 70
        self.add_notifications_button.color = (0,0,0,1)
        self.add_notifications_button.pos_hint = {"x": 0.72, "top": 1}
        self.add_widget(self.add_notifications_button)
        self.add_notifications_button.bind(on_release = self.go_to_add_notifications)

        self.notifications_button = Button(background_normal="resources/notifications.png", background_down="resources/notifications_down.png") 
        self.notifications_button.size_hint = (None, None)
        self.notifications_button.width = 70
        self.notifications_button.height = 70
        self.notifications_button.color = (0,0,0,1)
        self.notifications_button.pos_hint = {"x": 0.80, "top": 1}
        self.add_widget(self.notifications_button)
        self.notifications_button.bind(on_release = self.go_to_notifications)

        self.profile_button = Button(background_normal="resources/profile.png", background_down="resources/profile_down.png") 
        self.profile_button.size_hint = (None, None)
        self.profile_button.width = 70
        self.profile_button.height = 70
        self.profile_button.color = (0,0,0,1)
        self.profile_button.pos_hint = {"x": 0.88, "top": 1}
        self.add_widget(self.profile_button)
        self.profile_button.bind(on_release = self.go_to_profile)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline = Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.functions_label = Label(text="Functions", font_size=15, color=(0,0,0,1))
        self.functions_label.pos_hint = {"x":-0.19, "top": 0.82}
        self.add_widget(self.functions_label)

        self.about_hospital_label = Label(text="About Hospital", font_size=15, color=(0,0,0,1))
        self.about_hospital_label.pos_hint = {"x":-0.187, "top": 0.61}
        self.add_widget(self.about_hospital_label)

        self.settings_label = Label(text="Settings", font_size=15, color=(0,0,0,1))
        self.settings_label.pos_hint = {"x":0.213, "top": 0.825}
        self.add_widget(self.settings_label)

        self.documentation_label = Label(text="Documentation", font_size=15, color=(0,0,0,1))
        self.documentation_label.pos_hint = {"x":0.215, "top": 0.615}
        self.add_widget(self.documentation_label)

    def go_to_profile(self, instance):
        sm.add_widget(DoctorProfile(name = "DoctorProfile"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "DoctorProfile"

    def go_to_notifications(self, instance):
        sm.add_widget(DoctorNotifications(name = "DoctorNotifications"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "DoctorNotifications"

    def go_to_add_notifications(self, instance):
        sm.add_widget(DoctorAddNotifications(name = "DoctorAddNotifications"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "DoctorAddNotifications"

    def go_to_settings(self):
        sm.add_widget(DoctorSettings(name = "DoctorSettings"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "DoctorSettings"

    def go_to_functions(self):
        sm.add_widget(DoctorFunctions(name = "DoctorFunctions"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "DoctorFunctions"





# PatientAfterLogin Class
class PatientAfterLogin(Screen, Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
            Color(0.4, 0.4, 0.4,1,mode="rgba")
            Line(points = ((410, 80),(410, 280)), width = 2)
            Line(points = ((180, 175),(620, 175)), width = 2)
        self.title = Label(text="Patient Panel", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"top": 1.45}
        self.add_widget(self.title)

        self.add_notifications_button = Button(background_normal="resources/add_notifications.png", background_down="resources/add_notifications_down.png") 
        self.add_notifications_button.size_hint = (None, None)
        self.add_notifications_button.width = 70
        self.add_notifications_button.height = 70
        self.add_notifications_button.color = (0,0,0,1)
        self.add_notifications_button.pos_hint = {"x": 0.72, "top": 1}
        self.add_widget(self.add_notifications_button)
        self.add_notifications_button.bind(on_release = self.go_to_add_notifications)

        self.notifications_button = Button(background_normal="resources/notifications.png", background_down="resources/notifications_down.png") 
        self.notifications_button.size_hint = (None, None)
        self.notifications_button.width = 70
        self.notifications_button.height = 70
        self.notifications_button.color = (0,0,0,1)
        self.notifications_button.pos_hint = {"x": 0.80, "top": 1}
        self.add_widget(self.notifications_button)
        self.notifications_button.bind(on_release = self.go_to_notifications)        

        self.profile_button = Button(background_normal="resources/profile.png", background_down="resources/profile_down.png") 
        self.profile_button.size_hint = (None, None)
        self.profile_button.width = 70
        self.profile_button.height = 70
        self.profile_button.color = (0,0,0,1)
        self.profile_button.pos_hint = {"x": 0.88, "top": 1}
        self.add_widget(self.profile_button)
        self.profile_button.bind(on_release = self.go_to_profile)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline = Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.functions_label = Label(text="Functions", font_size=15, color=(0,0,0,1))
        self.functions_label.pos_hint = {"x":-0.19, "top": 0.82}
        self.add_widget(self.functions_label)

        self.about_hospital_label = Label(text="About Hospital", font_size=15, color=(0,0,0,1))
        self.about_hospital_label.pos_hint = {"x":-0.187, "top": 0.61}
        self.add_widget(self.about_hospital_label)

        self.settings_label = Label(text="Settings", font_size=15, color=(0,0,0,1))
        self.settings_label.pos_hint = {"x":0.213, "top": 0.825}
        self.add_widget(self.settings_label)

        self.documentation_label = Label(text="Documentation", font_size=15, color=(0,0,0,1))
        self.documentation_label.pos_hint = {"x":0.215, "top": 0.615}
        self.add_widget(self.documentation_label)

    def go_to_profile(self, instance):
        sm.add_widget(PatientProfile(name = "PatientProfile"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "PatientProfile"

    def go_to_notifications(self, instance):
        sm.add_widget(PatientNotifications(name = "PatientNotifications"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "PatientNotifications"
    
    def go_to_add_notifications(self, instance):
        sm.add_widget(PatientAddNotifications(name = "PatientAddNotifications"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "PatientAddNotifications"

    def go_to_settings(self):
        sm.add_widget(PatientSettings(name = "PatientSettings"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "PatientSettings"

    def go_to_functions(self):
        sm.add_widget(PatientFunctions(name = "PatientFunctions"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "PatientFunctions"





# EmployeeAfterLogin Class
class EmployeeAfterLogin(Screen, Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
            Color(0.4, 0.4, 0.4,1,mode="rgba")
            Line(points = ((410, 80),(410, 280)), width = 2)
            Line(points = ((180, 175),(620, 175)), width = 2)
        self.title = Label(text="Employee Panel", font_size=40, color=(1,1,1,1))
        self.title.pos_hint= {"top": 1.45}
        self.add_widget(self.title)

        self.add_notifications_button = Button(background_normal="resources/add_notifications.png", background_down="resources/add_notifications_down.png") 
        self.add_notifications_button.size_hint = (None, None)
        self.add_notifications_button.width = 70
        self.add_notifications_button.height = 70
        self.add_notifications_button.color = (0,0,0,1)
        self.add_notifications_button.pos_hint = {"x": 0.72, "top": 1}
        self.add_widget(self.add_notifications_button)
        self.add_notifications_button.bind(on_release = self.go_to_add_notifications)        

        self.notifications_button = Button(background_normal="resources/notifications.png", background_down="resources/notifications_down.png") 
        self.notifications_button.size_hint = (None, None)
        self.notifications_button.width = 70
        self.notifications_button.height = 70
        self.notifications_button.color = (0,0,0,1)
        self.notifications_button.pos_hint = {"x": 0.80, "top": 1}
        self.add_widget(self.notifications_button)
        self.notifications_button.bind(on_release = self.go_to_notifications)

        self.profile_button = Button(background_normal="resources/profile.png", background_down="resources/profile_down.png") 
        self.profile_button.size_hint = (None, None)
        self.profile_button.width = 70
        self.profile_button.height = 70
        self.profile_button.color = (0,0,0,1)
        self.profile_button.pos_hint = {"x": 0.88, "top": 1}
        self.add_widget(self.profile_button)
        self.profile_button.bind(on_release = self.go_to_profile)

        self.logo = Button(background_normal="resources/short_logo.png", background_down="resources/short_logo.png") 
        self.logo.size_hint = (None, None)
        self.logo.width = 120
        self.logo.height = 90
        self.logo.color = (0,0,0,1)
        self.logo.pos_hint = {"x": 0.1, "top": 1.02}
        self.add_widget(self.logo)

        self.tagline = Label(text="Built with Python, PostgreSQL, Psycopg2, and Kivy", font_size=13, color=(1,1,1,1))
        self.tagline.pos_hint = {"x":-0.27, "top": 0.525}
        self.add_widget(self.tagline)

        self.creatorline = Button(text="About Creator: Ahammad Shawki 8", font_size=13, color=(1,1,1,1))
        self.creatorline.pos_hint = {"x":0.7, "top": 0.05}
        self.creatorline.size_hint = (0.28,0.05)
        self.creatorline.background_color = (1,1,1,0)
        self.add_widget(self.creatorline)
        self.creatorline.bind(on_press = go_to_website)

        self.functions_label = Label(text="Functions", font_size=15, color=(0,0,0,1))
        self.functions_label.pos_hint = {"x":-0.19, "top": 0.82}
        self.add_widget(self.functions_label)

        self.about_hospital_label = Label(text="About Hospital", font_size=15, color=(0,0,0,1))
        self.about_hospital_label.pos_hint = {"x":-0.187, "top": 0.61}
        self.add_widget(self.about_hospital_label)

        self.settings_label = Label(text="Settings", font_size=15, color=(0,0,0,1))
        self.settings_label.pos_hint = {"x":0.213, "top": 0.825}
        self.add_widget(self.settings_label)

        self.documentation_label = Label(text="Documentation", font_size=15, color=(0,0,0,1))
        self.documentation_label.pos_hint = {"x":0.215, "top": 0.615}
        self.add_widget(self.documentation_label)

    def go_to_profile(self, instance):
        sm.add_widget(EmployeeProfile(name = "EmployeeProfile"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "EmployeeProfile"

    def go_to_notifications(self, instance):
        sm.add_widget(EmployeeNotifications(name = "EmployeeNotifications"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "EmployeeNotifications"
    
    def go_to_add_notifications(self, instance):
        sm.add_widget(EmployeeAddNotifications(name = "EmployeeAddNotifications"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "EmployeeAddNotifications"

    def go_to_settings(self):
        sm.add_widget(EmployeeSettings(name = "EmployeeSettings"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "EmployeeSettings"

    def go_to_functions(self):
        sm.add_widget(EmployeeFunctions(name = "EmployeeFunctions"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "EmployeeFunctions"








# Some tasks before the running the file
kv = Builder.load_file("frontend.kv")
sm = WindowManager(transition = SlideTransition())
screens = [
    GetStarted(name="GetStarted"), ConstantFixing(name="ConstantFixing"),
    AdminSignUp(name="AdminSignUp"), DoctorSignUp(name="DoctorSignUp"), PatientSignUp(name="PatientSignUp"), EmployeeSignUp(name="EmployeeSignUp"),
    AdminLogin(name="AdminLogin"), DoctorLogin(name="DoctorLogin"), PatientLogin(name="PatientLogin"), EmployeeLogin(name="EmployeeLogin"),
    AboutHospital(name="AboutHospital"), Documentation(name="Documentation"),
    AdminAfterLogin(name="AdminAfterLogin"), AdminAboutHospital(name="AdminAboutHospital"), AdminDocumentation(name="AdminDocumentation"),
    DoctorAfterLogin(name="DoctorAfterLogin"), DoctorAboutHospital(name="DoctorAboutHospital"), DoctorDocumentation(name="DoctorDocumentation"),
    PatientAfterLogin(name="PatientAfterLogin"), PatientAboutHospital(name="PatientAboutHospital"), PatientDocumentation(name="PatientDocumentation"),
    EmployeeAfterLogin(name="EmployeeAfterLogin"), EmployeeAboutHospital(name="EmployeeAboutHospital"), EmployeeDocumentation(name="EmployeeDocumentation"),
    Profile(name="Profile"), Notifications(name="Notifications"), AddNotifications(name="AddNotifications"), Settings(name="Settings")
    ]

for screen in screens:
    sm.add_widget(screen)
sm.current = "GetStarted"



# Main Class
class HMSApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return sm



# Running the entire file
if __name__ == "__main__":
    HMSApp().run()