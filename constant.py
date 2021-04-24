MAIN_FILE = os.getcwd()
CONSTANT_FILE = os.path.join(MAIN_FILE, "backup_&_restore_folder", "constant.csv")
constants ={}
condition = True
with open(CONSTANT_FILE, "r") as read_constant:
	while condition:
		try:
			reader = read_constant.readline()
			reader_split = reader.split(",")
			name, value = reader_split
			constants[name] = value[:-1]
		except:
			condition = False

def grab_constant(logged_in, name):
	if logged_in:
		name = name.upper()
		value = constants.get(name)
		return value

def set_constant(logged_in, constants_dict):
	with open(CONSTANT_FILE, "w") as write_constant:
		for key, value in constants_dict.items():
			write_constant.write(key.upper() + "," + value + "\n")
