''''
This is the major workhorse for the backend of NYC teacher evaluations.

1) loads API functions from loadfromAPI
2) imports teacher evaluation data
3) for each teacher, if there's no school in the db it creates
one and populates the data

'''
from models import *
from loadfromAPI import *
import os, csv

def get_teacherid(line):
	return "%s_%s_%s"%(get_lastname(line), get_firstname(line), get_dbn(line))

def get_grade(line):
	return None

def get_dbn(line):
	return line[17].upper()

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

def loadDistrict(dbnid):
	distID = dbnid[0:2]
	try:
		d=District.objects.get(name=distID)

	except:
		d = District(
			name = distID,
    		classsize_dist = None,
    		avgclasssize = get_district_avgclasssize(distID),
		)
	d.save()
	return d

def loadCity(dbnid):
	cityName = "New York City"
	try:
		c=City.objects.get(name=cityName)

	except:
		c = City(
			name = cityName,
    		classsize_dist = None,
    		avgclasssize = None,
		)
	c.save()
	return c

def loadBorough(dbnid):
	bID = dbnid[2]
	try:
		b=Borough.objects.get(name=bID)

	except:
		b = Borough(
			name = bID,
    		classsize_dist = None,
    		avgclasssize = None,
		)
	b.save()
	return b

def loadSchool(dbnid):
	try:
		s=School.objects.get(dbn=dbnid)

	except:
		s = School(
			dbn = dbnid,
		    name = get_school_name(dbnid),
		    
		    #contact, location
		    address = None,
		    phone = None,
		    email = None,
		    url = None,
		    district = loadDistrict(dbnid),
		    city = loadCity(dbnid),
		    borough = loadBorough(dbnid),
		    zipcode = None,
		    x_geo = None,
		    y_geo = None,

		    #administative
		    principal = get_principal(dbnid),
		    
		    #demographics
		    freelunch = None,
		    sped = None,
		    ell = None,
		    asian = None,
		    black = None,
		    hisp = None,
		    white = None,
		    male = None,
		    female = None,
		    size = get_school_size(dbnid),
		    schooltype = get_schooltype(dbnid),
		    dropout = get_schoolgrad(dbnid),
		    avgclasssize = get_school_avgclasssize(dbnid),
		    teachpupilratio = get_school_teacherpupilratio(dbnid),

		    #published evaluations
		    reportcardgrade = get_grade(dbnid),
		    reportcardgrade_adj = None
		)
	s.save()
	return s

def loadTeacher(filestring):
	#PROJECT_PATH = os.getcwd()
	with open(filestring) as csvfile:
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
				    school = loadSchool(get_dbn(line)),
				    grade = get_grade(line),
				    last_name = get_lastname(line),
				    first_name = get_firstname(line),
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

#loadTeacher(os.getcwd()+'/teachers/teachers_matched.csv')