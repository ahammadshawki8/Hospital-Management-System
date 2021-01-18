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

# Backend Imports
import login
import constant




# Common Classes 
class WindowManager(ScreenManager):
    pass





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

        self.profile_button = Button(background_normal="resources/profile.png", background_down="resources/profile_down.png") 
        self.profile_button.size_hint = (None, None)
        self.profile_button.width = 70
        self.profile_button.height = 70
        self.profile_button.color = (0,0,0,1)
        self.profile_button.pos_hint = {"x": 0.88, "top": 1}
        self.add_widget(self.profile_button)

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

        self.profile_button = Button(background_normal="resources/profile.png", background_down="resources/profile_down.png") 
        self.profile_button.size_hint = (None, None)
        self.profile_button.width = 70
        self.profile_button.height = 70
        self.profile_button.color = (0,0,0,1)
        self.profile_button.pos_hint = {"x": 0.88, "top": 1}
        self.add_widget(self.profile_button)

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

        self.profile_button = Button(background_normal="resources/profile.png", background_down="resources/profile_down.png") 
        self.profile_button.size_hint = (None, None)
        self.profile_button.width = 70
        self.profile_button.height = 70
        self.profile_button.color = (0,0,0,1)
        self.profile_button.pos_hint = {"x": 0.88, "top": 1}
        self.add_widget(self.profile_button)

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

        self.profile_button = Button(background_normal="resources/profile.png", background_down="resources/profile_down.png") 
        self.profile_button.size_hint = (None, None)
        self.profile_button.width = 70
        self.profile_button.height = 70
        self.profile_button.color = (0,0,0,1)
        self.profile_button.pos_hint = {"x": 0.88, "top": 1}
        self.add_widget(self.profile_button)

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
    EmployeeAfterLogin(name="EmployeeAfterLogin"), EmployeeAboutHospital(name="EmployeeAboutHospital"), EmployeeDocumentation(name="EmployeeDocumentation"),]

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