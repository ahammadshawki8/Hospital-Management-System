# Kivy Imports
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
import setup_engine
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.screenmanager import SlideTransition
from kivy.config import Config

# Backend Imports
import login
import constant
import admin
import datetime
import doctor
import patient
import employee


# Common Classes 
class WindowManager(ScreenManager):
    pass

class Holder():
    username = "Default"
    logged_in = True

Config.set('graphics', 'height', 600)
Config.set('graphics', 'resizable', 0)
Config.write()



# SignUp Classes
class GetStarted(Screen):
    first_start = False
    def start_program(self):
        if GetStarted.first_start:
            setup_engine.start_program()

    def change_first_start(self, value=False):
        GetStarted.first_start = value

    def go_to_website(self):
        web.open_new_tab("https://ahammadshawki8.github.io/")



class AdminSignUp(Screen):
    username = ObjectProperty()
    fullname = ObjectProperty()
    email = ObjectProperty()
    date_of_birth = ObjectProperty()
    password = ObjectProperty()
    salary = ObjectProperty()

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
class Temporary(Screen):
    pass

def go_to_website(instance):
    web.open_new_tab("https://ahammadshawki8.github.io/")


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

        self.tagline = Label(text="Built with Python, PostgreSQL and Kivy by Ahammad", font_size=13, color=(1,1,1,1))
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


class Documentation(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(51/255, 153/255, 255/255,1,mode="rgba")
            Line(points = ((0, 580),(1000, 580)), width = 50)
            Line(points = ((0, 0),(1000, 0)), width = 35)
        self.title = Label(text=self.first_title().capitalize()+ " Documentaion", font_size=40, color=(1,1,1,1))
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

        self.tagline = Label(text="Built with Python, PostgreSQL and Kivy by Ahammad", font_size=13, color=(1,1,1,1))
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

    def first_title(self):
        return "Default"
    
    def all_instructions(self):
        return "Default"


class AdminDocumentation(Documentation):
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "AdminAfterLogin"

    def first_title(self):
        return "admin"

    def all_instructions(self):
        text = """
        00. SignUp or Login to the application to use it.
        01. Send others notification using + button.
        02. See all of your notification as well as profile.
        03. In "Functions" secion, you have a set of functions. 
        04. Use those functions providing necessary information.
        05. In "Settings" you can change some useful constants.
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

    def first_title(self):
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

    def first_title(self):
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

    def first_title(self):
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


class Profile(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = self.find_my_category()
        try:
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

            self.tagline = Label(text="Built with Python, PostgreSQL and Kivy by Ahammad", font_size=13, color=(1,1,1,1))
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
        except:
            pass


    def get_my_profile(self, username, category):
        return admin.see_info(True, category, username)

    def find_my_category(self):
        return "doctor"
    
    def find_my_username(self):
        return "hpt"
    
    def go_back(self):
        pass

class AdminProfile(Profile):
    def find_my_category(self):
        return "admin"
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "AdminAfterLogin"

class DoctorProfile(Profile):
    def find_my_category(self):
        return "doctor"
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "DoctorAfterLogin"

class PatientProfile(Profile):
    def find_my_category(self):
        return "patient"

    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "PatientAfterLogin"

class EmployeeProfile(Profile):
    def find_my_category(self):
        return "employee"

    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
        sm.transition = SlideTransition(direction = "right")
        sm.current = "EmployeeAfterLogin"
        


class Notifications(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username = self.find_my_username()
        self.category = self.find_my_category()
        self.notifications = self.get_my_notification(self.username, self.category)
        print(self.notifications)

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

        self.tagline = Label(text="Built with Python, PostgreSQL and Kivy by Ahammad", font_size=13, color=(1,1,1,1))
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

class AdminNotifications(Notifications):
    def find_my_category(self):
        return "admin"
    
    def find_my_username(self):
        return Holder.username
    
    def go_back(self, instance):
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
        sm.transition = SlideTransition(direction = "right")
        sm.current = "EmployeeAfterLogin" 

    def get_my_notification(self, username, category):
        return employee.recent_notifications(username, True, limit = 10)







# Admin Classes
class AdminAfterLoginWidgets(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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

        self.tagline = Label(text="Built with Python, PostgreSQL and Kivy by Ahammad", font_size=13, color=(1,1,1,1))
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


# Doctor Classes
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

        self.tagline = Label(text="Built with Python, PostgreSQL and Kivy by Ahammad", font_size=13, color=(1,1,1,1))
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


# Patient Classes
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

        self.tagline = Label(text="Built with Python, PostgreSQL and Kivy by Ahammad", font_size=13, color=(1,1,1,1))
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

# Employee Classes
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

        self.tagline = Label(text="Built with Python, PostgreSQL and Kivy by Ahammad", font_size=13, color=(1,1,1,1))
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




# Main Class
kv = Builder.load_file("frontend.kv")
sm = WindowManager(transition = SlideTransition())
screens = [
    GetStarted(name="GetStarted"),
    AdminSignUp(name="AdminSignUp"), DoctorSignUp(name="DoctorSignUp"), PatientSignUp(name="PatientSignUp"), EmployeeSignUp(name="EmployeeSignUp"),
    AdminLogin(name="AdminLogin"), DoctorLogin(name="DoctorLogin"), PatientLogin(name="PatientLogin"), EmployeeLogin(name="EmployeeLogin"),
    Temporary(name="Temporary"), AboutHospital(name="AboutHospital"), Documentation(name="Documentation"),
    AdminAfterLogin(name="AdminAfterLogin"), AdminAboutHospital(name="AdminAboutHospital"), AdminDocumentation(name="AdminDocumentation"),
    DoctorAfterLogin(name="DoctorAfterLogin"), DoctorAboutHospital(name="DoctorAboutHospital"), DoctorDocumentation(name="DoctorDocumentation"),
    PatientAfterLogin(name="PatientAfterLogin"), PatientAboutHospital(name="PatientAboutHospital"), PatientDocumentation(name="PatientDocumentation"),
    EmployeeAfterLogin(name="EmployeeAfterLogin"), EmployeeAboutHospital(name="EmployeeAboutHospital"), EmployeeDocumentation(name="EmployeeDocumentation"),
    Profile(name="Profile"), Notifications(name = "Notifications")
    ]

for screen in screens:
    sm.add_widget(screen)
sm.current = "GetStarted"

class HMSApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return sm



# Run file
if __name__ == "__main__":
    HMSApp().run()