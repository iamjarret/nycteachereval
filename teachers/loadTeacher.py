from models import *



def get_teacherid(line):
	return "%s_%s_%s"%(get_lastname(line), get_firstname(line), get_dbn(line))

def get_grade(line):
	return None

def get_dbn(line):
	dbn = line[17]
	try:
		matchschool = School.objects.get(dbn=dbn)
	except:
		matchschool = School(dbn=dbn)
		matchschool.save()
	return matchschool

def get_lastname(line):
	return line[2]

def get_firstname(line):
	return line[1]

def get(line, num, funtoconvert):
	got = line[num]
	if got=="NA":
		return None
	else:
		return funtoconvert(got)

def va_convert(thing):
	return "%0.2f"%(float(thing))

def loadTeacherData(filestring):
	PROJECT_PATH = os.getcwd()
	with open(PROJECT_PATH + filestring) as csvfile:
		reader = csv.reader(csvfile, delimiter=",", quotechar ="|")
		reader.next() # skip header
		count = 0
		for line in reader:
			if count>15:
				assert False
			else:
				teachid = get_teacherid(line)
				try:
					s=Teachers.objects.get(teacherid=teachid)	
				except:
					s = Teachers(
					teacherid = teachid,
		    		dbn = get_dbn(line),
		    		grade = get_grade(line),
		    		last_name = get_lastname(line),
		    		first_name = get_firstname(line),
		    		va_0910_math = None,
		    		va_0809_math = None,
		    		va_0708_math = None,
		    		va_0607_math = None,
		    		va_0910_eng = None,
		    		va_0809_eng = None,
		    		va_0708_eng = None,
		    		va_0607_eng = None
					)
				s.save()

				print "%s, %s, %s, %s"%(get_lastname(line), get_firstname(line), get(line, 13, va_convert), line[4])
				if line[4]=="Mathematics":
					s.va_0910_math = get(line, 15, va_convert)
					s.va_0809_math = get(line, 14, va_convert)
					s.va_0708_math = get(line, 13, va_convert) 
					s.va_0607_math = get(line, 12, va_convert)

				elif line[4]=="English Language Arts":
					s.va_0910_eng = get(line, 15, va_convert)
    				s.va_0809_eng = get(line, 14, va_convert)
    				s.va_0708_eng = get(line, 13, va_convert)
    				s.va_0607_eng = get(line, 12, va_convert)

    			s.save()
			count +=1