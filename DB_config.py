import constant
HOST = constant.grab_constant(True,"HOST")
PORT = int(constant.grab_constant(True,"PORT"))
ADMIN_DATABASE = constant.grab_constant(True,"ADMIN_DATABASE")
DATABASE = constant.grab_constant(True,"DATABASE")
USER = constant.grab_constant(True,"USER")
PASSWORD = constant.grab_constant(True,"PASSWORD")


def admin_config():
    config_dict = {"host":HOST, "port":PORT, "database":ADMIN_DATABASE, "user":USER, "password":PASSWORD}
    return config_dict


def config():
    config_dict = {"host":HOST, "port":PORT, "database":DATABASE, "user":USER, "password":PASSWORD}
    return config_dict