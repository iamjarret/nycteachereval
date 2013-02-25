'''
This is a custom-made cleaner that goes through the teachers_matched.csv file and imports it 
into the SQL db
'''


import os
import sys
sys.path.append("/home/jarret/nycteacher/nycteacher/")
from teachers.models import Teachers, School
PATH = "/home/jarret/nycteacher/nycteacher/other/"

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

def get_va(line, num):
	va = line[num]
	if va=="NA":
		return None
	else:
		return float(va)

def get_va0910(line):
	return get_va(line, 15)

def get_va0809(line):
	return get_va(line, 14)

def get_va0708(line):
	return get_va(line, 13)

def get_va0607(line):
	return get_va(line, 12)

def get_va0506(line):
	return get_va(line, 11)

def main():
	PROJECT_PATH = os.getcwd()
	with open(PROJECT_PATH+'/other/rawdata/teachers_matched.csv') as csvfile:
		reader = csv.reader(csvfile, delimiter=",", quotechar ="|")
		reader.next() # skip header
		count = 0
		for line in reader:
			if count<15:
				teachid = get_teacherid(line)
				s = Teachers(
					teacherid = teachid,
		    		dbn = get_dbn(line),
		    		grade = get_grade(line),
		    		last_name = get_lastname(line),
		    		first_name = get_firstname(line)
					)
				try:
					s.save()
				except:
					print "%s, %s"%(get_lastname(line),get_firstname(line))
				print line[4]
				if line[4]=="Mathematics":
					matched = Teachers.objects.get(teacherid = teachid)
					matched.va_0910_math = get_va0910(line) 
					matched.va_0809_math = get_va0809(line) 
					matched.va_0708_math = get_va0708(line) 
					matched.va_0607_math = get_va0607(line)
					matched.save()

				elif line[4]=="English Language Arts":
					matched = Teachers.objects.get(teacherid = teachid)
					matched.va_0910_eng = get_va0910(line) 
    				matched.va_0809_eng = get_va0809(line) 
    				matched.va_0708_eng = get_va0708(line) 
    				matched.va_0607_eng = get_va0607(line)
    				matched.save()
			count +=1

			#update value add scores


main()