MAIN_FILE = "H:\\Study_Work\\Python\\Python WorkSpace\\# Projects\\Hospital Management system"
CONSTANT_FILE = MAIN_FILE + "\\backup_&_restore_folder\\constant.csv"
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
