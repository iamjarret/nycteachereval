'''
This code runs off the configuration file in the same folder.  It accesses the socrata
API and pulls data into the models.
'''
import requests
import ConfigParser
#from models import Teachers, School
import json
import pprint
import os

def SocrataRequest(endpointname, where="", order=""):
	cfg = ConfigParser.ConfigParser()
	#cfg.read(os.getcwd()+'/socrata.ini')
	cfg.read(os.getcwd()+'/teachers/socrata.ini')
	host_name = cfg.get('server', 'host')
	app_token= cfg.get('credentials', 'app_token')
	user = cfg.get('credentials','user')
	password = cfg.get('credentials','password')
	viewID = cfg.get('dataendpoints', endpointname)
	url = "%s/resource/%s.json" %(host_name, viewID)
	headers = { 'Content-type': 'application/json',
              'X-App-Token': app_token}
	payload = {}
	if where:
		payload['$where']=where
	if order:
		payload['$order']=order
	auth = (user, password)
	r = requests.get(url, 
		headers=headers,
		auth=auth,
		params=payload)
	
	fields = r.headers.get('x-soda2-fields')
	types = r.headers.get('x-soda2-types')
	
	#print fields
	#print types
	return r.json()

def get_district_avgclasssize(district):
	endpointname = 'district_classsize'
	whererequest = "csd='%s' and grade_level>='04' and grade_level<='08'"%district
	jsondump1 = SocrataRequest(endpointname, where=whererequest)
	total = 0
	wtdclasssize=0
	for x in jsondump1:
		students = x.get('number_of_students',0)
		class_size = x.get("class_size", "14") #bottom coded as 14
		wtdclasssize += int(students)*int(class_size) 
		total+=int(students)
	return "%0.1f"%(wtdclasssize/float(total))

def get_school_avgclasssize(schooldbn):
	endpointname = 'school_classsize'
	district = schooldbn[0:2]
	schoolid = schooldbn[2:6]
	print district, schoolid
	whererequest = "csd='%s' and school_code='%s' and grade_>='04' and grade_<='08' and program_type='GEN ED'"%(district,schoolid)
	jsondump1 = SocrataRequest(endpointname, where=whererequest)
	total = 0
	wtdclasssize=0
	for x in jsondump1:
		students = x.get('number_of_students_seats_filled',0)
		class_size = x.get("average_class_size", "14") #bottom coded as 14
		wtdclasssize += int(students)*float(class_size) 
		total+=int(students)
	return "%0.1f"%(wtdclasssize/float(total))

def get_school_size(schooldbn):
	endpointname = 'school_classsize'
	district = schooldbn[0:2]
	schoolid = schooldbn[2:6]
	print district, schoolid
	whererequest = "csd='%s' and school_code='%s'"%(district,schoolid)
	jsondump1 = SocrataRequest(endpointname, where=whererequest)
	total = 0
	wtdclasssize=0
	for x in jsondump1:
		students = x.get('number_of_students_seats_filled',0)
		total+=int(students)
	return total

def get_school_name(schooldbn):
	endpointname = 'school_classsize'
	district = schooldbn[0:2]
	schoolid = schooldbn[2:6]
	whererequest = "csd='%s' and school_code='%s'"%(district,schoolid)
	jsondump1 = SocrataRequest(endpointname, where=whererequest)
	name = jsondump1[0].get('school_name',None)
	return name

def get_principal(schooldbn):
	endpointname = 'school_progress'
	whererequest = "dbn='%s'"%(schooldbn)
	jsondump1 = SocrataRequest(endpointname, where=whererequest)
	principal = jsondump1[0].get('principal',None)
	return principal

def get_grade(schooldbn):
	endpointname = 'school_progress'
	whererequest = "dbn='%s'"%(schooldbn)
	jsondump1 = SocrataRequest(endpointname, where=whererequest)
	reportcard_grade = jsondump1[0].get('_2010_2011_overall_grade',None)
	return reportcard_grade

def get_schooltype(schooldbn):
	endpointname = 'school_progress'
	whererequest = "dbn='%s'"%(schooldbn)
	jsondump1 = SocrataRequest(endpointname, where=whererequest)
	schooltype = jsondump1[0].get('school_level',None)
	return schooltype

def get_schoolgrad(schooldbn):
	endpointname = 'school_grad'
	whererequest = "demographic='%s' and dbn='%s'"%("Total Cohort", schooldbn)
	jsondump1 = SocrataRequest(endpointname, where=whererequest, order="cohort")
	if len(jsondump1)>1:
		gradrates = jsondump1[-1].get('dropped_out_of_cohort',None)
	else:
		gradrates = jsondump1[0].get('dropped_out_of_cohort',None)
	return gradrates


def get_school_teacherpupilratio(schooldbn):
	endpointname = 'school_classsize'
	district = schooldbn[0:2]
	schoolid = schooldbn[2:6]
	whererequest = "csd='%s' and school_code='%s'"%(district,schoolid)
	jsondump1 = SocrataRequest(endpointname, where=whererequest)
	
	temp = jsondump1[-1].get('schoolwide_pupil_teacher_ratio',0)
	if temp:
		toout = temp
	else:
		for x in jsondump1:
			ratio = x.get('schoolwide_pupil_teacher_ratio',0)
			if ratio:
				toout = ratio
	return toout

print os.getcwd()

#print get_district_avgclasssize('01') #WORKS
print get_district_avgclasssize('14') #WORKS
print get_school_avgclasssize('14K586') #WORKS
print get_school_size('14K586') #WORKS
print get_school_teacherpupilratio('14K586')
print get_principal('14K586')
print get_grade('14K586')
print get_schoolgrad('14K586')
#print json.dumps( jsondump1, indent=10)
#print 
