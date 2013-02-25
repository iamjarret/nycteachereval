import csv
import os
import sys
sys.path.append("/home/jarret/nycteacher/nycteacher/")
from teachers.models import Teachers
PATH = "/home/jarret/nycteacher/nycteacher/other/"

class Teacher(dict):
	def __init__(self, *args, **kwargs):
		dict.__init__(self, *args, **kwargs)
		self.__dict__ = self
		self.grade = self.cleangrade()

	def cleangrade(self):
		grades = []
		for x in [self.get(h,"NA") for h in ['grade0708', 'grade0809', 'grade0910']]:
			if "NA" not in x:
				toadd = x.split()[0][0]
				try:
					h = int(toadd)
					grades.append(h)
				except:
					0
		return grades

	def merge_data(self, dbndict, name):
		try:
#			print "%s = %f" % (self.dbn, dbndict[self.dbn][name]) 
			self[name] = dbndict[self.dbn][name]
		except:
			self[name] = None

class GraduationData(dict):
	def __init__(self, *args, **kwargs):
		dict.__init__(self, *args, **kwargs)
		self.__dict__ = self
		self.dropoutpercent = self.get_dropoutpercent()

	def get_dropoutpercent(self):
		s1 = self.local_percent_total.replace("s","")[:-1]
		s2 = self.drop_percent.replace("s","")[:-1]
		try:
			return float(s1)+float(s2)
		except:
			return ""

class Demographics(dict):
	def __init__(self, *args, **kwargs):
		dict.__init__(self, *args, **kwargs)
		self.__dict__ = self

def valueadd(teacher1, rawteacher):
	type = rawteacher.subject
	if type=="English Language Arts":
		teacher1.va_0506_eng = rawteacher.va_0506
		teacher1.va_0607_eng = rawteacher.va_0607
		teacher1.va_0708_eng = rawteacher.va_0708
		teacher1.va_0809_eng = rawteacher.va_0809
		teacher1.va_0910_eng = rawteacher.va_0910
		teacher1.va_0506_math = teacher1.va_0506
		teacher1.va_0607_math = teacher1.va_0607
		teacher1.va_0708_math = teacher1.va_0708
		teacher1.va_0809_math = teacher1.va_0809
		teacher1.va_0910_math = teacher1.va_0910
	elif type=="Mathematics":
		teacher1.va_0506_math = rawteacher.va_0506
		teacher1.va_0607_math = rawteacher.va_0607
		teacher1.va_0708_math = rawteacher.va_0708
		teacher1.va_0809_math = rawteacher.va_0809
		teacher1.va_0910_math = rawteacher.va_0910
		teacher1.va_0506_eng = teacher1.va_0506
		teacher1.va_0607_eng = teacher1.va_0607
		teacher1.va_0708_eng = teacher1.va_0708
		teacher1.va_0809_eng = teacher1.va_0809
		teacher1.va_0910_eng = teacher1.va_0910

def CSV2CLASS(fileName, className):
	with open(fileName) as csvfile:
		reader = csv.DictReader(csvfile, delimiter=",", quotechar ="|")
		allClass = []
		for row in reader:
			allClass.append(className(row))
	return allClass

def read_demo_csv(fileName):
	data_dict=dict()
	with open(fileName,'r') as csvfile:
		header=csvfile.next()
		rows = csv.reader(csvfile)
		for temp in rows:
			temp_dict=dict()
			#temp_dict['name'] = temp[1]
			#temp_dict['year'] = temp[2]
			temp_dict['freelunch'] = float(temp[3])
			temp_dict['ell'] = float(temp[4])
			#temp_dict['sped'] = float(temp[5])
			temp_dict['asian'] = float(temp[6])
			temp_dict['black'] = float(temp[7])
			temp_dict['hisp'] = float(temp[8])
			temp_dict['white'] = float(temp[9])
			temp_dict['male'] = float(temp[10])
			temp_dict['female'] = float(temp[11])
			data_dict[temp[0]] = temp_dict
	return data_dict

def read_schools_csv(fileName):
	data_dict=dict()
	with open(fileName,'r') as csvfile:
		header=csvfile.next()
		rows = csv.reader(csvfile)
		for temp in rows:
			temp_dict=dict()
			temp_dict['overall_grade'] = temp[7]
			data_dict[temp[0]] = temp_dict
	return data_dict

def merge_data(teachersList, grad_list, name):
	DBNdict = {}
	for gd in grad_list:
		temp = gd.enrolled_num.replace("s","10")
		if "%" in temp:
			temp =10
		if int(temp) < 9:
			DBNdict[gd.dbn]=gd
	for t in teachersList:
		t.merge_data(DBNdict,name)

def Raw2Clean(teacherlist):
	remadekeys = {}
	realTeachers = []
	for x in teacherlist:
		keyid = x.teacher_name_first_1 + x.teacher_name_last_1 + x.school_name
		
		if keyid in remadekeys.keys():
			valueadd(remadekeys[keyid],x)
		
		else:
			remadekeys[keyid]=x
	#for h in remadekeys.keys():
	#	realTeachers.append(remadekeys[h])
	return remadekeys.values()

def CRUTCH(datatosend, attribs):
	length = len(datatosend[datatosend.keys()[0]])
	#return [h for h in datatosend.get(attribs,[""]*length)]
	try:
		return map(float,datatosend.get(attribs,[""]*length).values())
	except:
		return datatosend.get(attribs,[""]*length)


def printClass(teachers, filename, keylist=[], othdict={}, otherkeys=[]):
	f = csv.writer(open(filename, "w"))
	f.writerow(keylist + otherkeys)
	for t in teachers:
		toout = []
		for x in keylist:
			try:
				temp = t[x]
			except:
				temp = ""
			if temp == "NA":
				temp=""
			toout.append(temp)
		other = othdict.get(t.dbn,([]*len(otherkeys)))
		toout=toout + other
		f.writerow(toout)

#def addtoschools(schools, stufflist, toadd=[]):
#	for x in stufflist:
#		if x.dbn not in schools.keys():
#			schools[x.dbn]={}
#		for add in toadd:
#			schools[x.dbn][add]=stufflist[add]

def cleanfloat(temp):
	if temp=="NA":
		return None
	else:
		return float(temp)

def cleanandimport():
	RawTeachers = CSV2CLASS(PATH+'rawdata/teachers_matched.csv', Teacher)
	rawteacher = Raw2Clean(RawTeachers)

	for h in rawteacher:
		try:
			h.va_0910_eng=cleanfloat(h.va_0910_eng)
		except:
			0
		try:
			h.va_0910_math=cleanfloat(h.va_0910_math)
		except:
			0
		try:
			h.va_0809_eng=cleanfloat(h.va_0809_eng)
		except:
			0
		try:
			h.va_0809_math=cleanfloat(h.va_0809_math)
		except:
			0
		try:
			h.va_0708_eng=cleanfloat(h.va_0708_eng)
		except:
			0
		try:
			h.va_0708_math=cleanfloat(h.va_0708_math)
		except:
			0
		try:
			h.va_0607_eng= cleanfloat(h.va_0607_eng)
		except:
			0
		try:
			h.va_0607_math = cleanfloat(h.va_0607_math)
		except:
			0
		#h.school_name=h.school_name.replace("NA","")
		try:
			h.teacherid = h.teacherid.replace("NA","")
		except:
			0

	allGraduation = CSV2CLASS(PATH+'rawdata/grads.csv', GraduationData)
	grads_data=dict()
	for x in allGraduation:
		grads_data[vars(x).get('dbn')]={'dropoutpercent':vars(x).get('dropoutpercent')}


	keylist = ["dbn", "va_0910_eng", "va_0910_math", "va_0809_eng", "va_0809_math", 
		"va_0708_eng", "va_0708_math","va_0607_eng", "va_0607_math","school_name", "grade", 
		"teacherid", "teacher_name_last_1", "teacher_name_first_1"]


	demo_data = read_demo_csv(PATH+'rawdata/demo.csv')
	school_data = read_schools_csv(PATH+ 'rawdata/schools.csv')


	toout = [keylist + ['freelunch','ell', 'asian', 'black', 'hisp', 'white','male','female','overall_grade','dropoutpercent']]
	header = toout
	for teacher in rawteacher:
		attrib_dict = vars(teacher)
		toout.append([attrib_dict.get(h,"") for h in keylist] + 
			CRUTCH(demo_data, attrib_dict['dbn']) +
			CRUTCH(school_data, attrib_dict['dbn']) +
			CRUTCH(grads_data, attrib_dict['dbn']))
	print toout
	#f = csv.writer(open(PATH +'data/finaldata.csv', "w"))
	for line in toout[1:]:
		for i in range(len(line)):
			if line[i] == "":
				line[i] = None

		s = Teachers(
			dbn = line[0],
			va_0910_eng = line[1],
			va_0910_math = line[2],
			va_0809_eng = line[3],
			va_0809_math = line[4],
			va_0708_eng = line[5],
			va_0708_math = line[6],
			va_0607_eng = line[7],
			va_0607_math = line[8],
			school_name = line[9],
			grade = line[10],
			teacherid = line[11],
			last_name = line[12],
			first_name = line[13],
			freelunch = line[14],
			ell = line[15],
			asian = line[16],
			black = line[17],
			hisp = line[18],
			white = line[19],
			male = line[20],
			female = line[21],
			overall_grade = line[22],
			dropout = line[23])
		s.save()




# allgrade = CSV2CLASS('schools.csv', Demographics)

# Schools = {}
# TOEXTRACT = ['freelunch', 'ell', 'asian', 'black', 'hisp', 'white', 'male', 'female_percentmale']
# for h in alldemographics:
# 	Schools[h.dbn]= [vars(h).get(x,"") for x in TOEXTRACT]
# for m in allGraduation:
# 	if Schools.get(m.dbn,""):
# 		Schools[m.dbn] = Schools[m.dbn]+[vars(m).get("dropoutpercent","")]
# 	else:
# 		if vars(m).get("dropoutpercent",""):
# 			print vars(m).get("dropoutpercent",[""])
# 			Schools[m.dbn]= [""]*len(TOEXTRACT)+[vars(m).get("dropoutpercent","")]
# 		else:
# 			Schools[m.dbn]= [""]*(len(TOEXTRACT)+1)
# for m in allgrade:
# 	if Schools.get(m.dbn,""):
# 		Schools[m.dbn] = Schools[m.dbn]+[vars(m).get("2011-2012 OVERALL GRADE","")]
# 	else:
# 		if vars(m).get("2011-2012 OVERALL GRADE",""):
# 			#print vars(m).get("2011-2012 OVERALL GRADE",[""])
# 			Schools[m.dbn]= [""]*len(TOEXTRACT)+[vars(m).get("2011-2012 OVERALL GRADE","")]
# 		else:
# 			Schools[m.dbn]= [""]*(len(TOEXTRACT)+1)
# print Schools

# ALLEXTRACT = TOEXTRACT + ["dropoutpercent","2011-2012 OVERALL GRADE"]

# #addtoschools(Schools, allGraduation, toadd=["dropoutpercent"])
# #print Schools

# #merge_data(Teachers, allGraduation, "dropoutpercent")
# printClass(Teachers, "out.csv", keylist = ["dbn", "va_0910_eng", "va_0910_math", "va_0809_eng", "va_0809_math", 
# 	"va_0708_eng", "va_0708_math","va_0607_eng", "va_0607_math","school_name", "grade", 
# 	"teacherid", "teacher_name_last_1", "teacher_name_first_1"], othdict = Schools, otherkeys = ALLEXTRACT)

# #printClass(allGraduation, "grad_out.csv", keylist=["dbn", "dropoutpercent"])
# #printClass(alldemographics, 'demo_out.csv')



#for line in f2.readlines()[1:]:
#	cols = [item for item in line.split(',')][1:]
#	t = Teacher()
#	t.teacher_name_first_1 = ''.join([c for c in cols[0] if c != '"'])
#	t.teacher_name_last_1 = ''.join([c for c in cols[1] if c != '"'])
#	if cols[2] != 'NA':
#		t.teacher_id = cols[2]
#	t.dbn = ''.join([c for c in cols[-10] if c != '"'])

	# t.dbn = ''.join([c for c in cols[0][:10] if c != '"'])
	# t.school_name = cols[1]
	# t.teacher_name_first_1 = ''.join([c for c in cols[2] if c != '"'])
	# t.teacher_name_last_1 = ''.join([c for c in cols[3] if c != '"'])
# 	# t.grade0708 = cols[-12]
# 	# t.grade0809 = cols[-11]models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     		va_0910_math = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     		va_0809_eng = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
# 			va_0809_math = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     		va_0708_eng = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     		va_0708_math = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     		va_0607_eng = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     		va_0607_math = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     		school_name = models.CharField(max_length=100)
#     		grade = models.CharField(max_length=100, blank=True, null=True)
#     		teacherid = models.CharField(max_length=15, blank=True, null=True)
#     		last_name = models.CharField(max_length=40)
#     		first_name = models.CharField(max_length=40)
#     		freelunch = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
#     		ell = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
#     		asian = models.DecimalField(max_digits=3,   decimal_places=1, blank=True, null=True)
#     		black = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
#     		hisp = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
#     		white = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
#     		male = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
#     		female = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
#     		overall_grade = models.CharField(max_length=1, blank=True, null=True)
#     		dropout = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)






# 				).save
# 			f.writerow(line)
# 		count+=1
# 	f.save()




# # allgrade = CSV2CLASS('schools.csv', Demographics)

# # Schools = {}
# # TOEXTRACT = ['freelunch', 'ell', 'asian', 'black', 'hisp', 'white', 'male', 'female_percentmale']
# # for h in alldemographics:
# # 	Schools[h.dbn]= [vars(h).get(x,"") for x in TOEXTRACT]
# # for m in allGraduation:
# # 	if Schools.get(m.dbn,""):
# # 		Schools[m.dbn] = Schools[m.dbn]+[vars(m).get("dropoutpercent","")]
# # 	else:
# # 		if vars(m).get("dropoutpercent",""):
# # 			print vars(m).get("dropoutpercent",[""])
# # 			Schools[m.dbn]= [""]*len(TOEXTRACT)+[vars(m).get("dropoutpercent","")]
# # 		else:
# # 			Schools[m.dbn]= [""]*(len(TOEXTRACT)+1)
# # for m in allgrade:
# # 	if Schools.get(m.dbn,""):
# # 		Schools[m.dbn] = Schools[m.dbn]+[vars(m).get("2011-2012 OVERALL GRADE","")]
# # 	else:
# # 		if vars(m).get("2011-2012 OVERALL GRADE",""):
# # 			#print vars(m).get("2011-2012 OVERALL GRADE",[""])
# # 			Schools[m.dbn]= [""]*len(TOEXTRACT)+[vars(m).get("2011-2012 OVERALL GRADE","")]
# # 		else:
# # 			Schools[m.dbn]= [""]*(len(TOEXTRACT)+1)
# # print Schools

# # ALLEXTRACT = TOEXTRACT + ["dropoutpercent","2011-2012 OVERALL GRADE"]

# # #addtoschools(Schools, allGraduation, toadd=["dropoutpercent"])
# # #print Schools

# # #merge_data(Teachers, allGraduation, "dropoutpercent")
# # printClass(Teachers, "out.csv", keylist = ["dbn", "va_0910_eng", "va_0910_math", "va_0809_eng", "va_0809_math", 
# # 	"va_0708_eng", "va_0708_math","va_0607_eng", "va_0607_math","school_name", "grade", 
# # 	"teacherid", "teacher_name_last_1", "teacher_name_first_1"], othdict = Schools, otherkeys = ALLEXTRACT)

# #printClass(allGraduation, "grad_out.csv", keylist=["dbn", "dropoutpercent"])
# #printClass(alldemographics, 'demo_out.csv')



#for line in f2.readlines()[1:]:
#	cols = [item for item in line.split(',')][1:]
#	t = Teacher()
#	t.teacher_name_first_1 = ''.join([c for c in cols[0] if c != '"'])
#	t.teacher_name_last_1 = ''.join([c for c in cols[1] if c != '"'])
#	if cols[2] != 'NA':
#		t.teacher_id = cols[2]
#	t.dbn = ''.join([c for c in cols[-10] if c != '"'])

	# t.dbn = ''.join([c for c in cols[0][:10] if c != '"'])
	# t.school_name = cols[1]
	# t.teacher_name_first_1 = ''.join([c for c in cols[2] if c != '"'])
	# t.teacher_name_last_1 = ''.join([c for c in cols[3] if c != '"'])
	# t.grade0708 = cols[-12]
	# t.grade0809 = cols[-11]
	# t.grade0910 = cols[-10]
	# t.va_0506 = clean_num(cols[-5])
	# t.va_0607 = clean_num(cols[-4])
	# t.va_0708 = clean_num(cols[-3])
	# t.va_0809 = clean_num(cols[-2])
	# if cols[15] not in ('NA\n', 'NA'):
	# 	t.va_0910 = cols[-1]
	# s_list = School.objects.filter(dbn=t.dbn)
	# if s_list:
	# 	t.school = s_list[0]
#	try:
#		t.save()
#	except:
#		print traceback.print_exc(file=sys.stdout)

	# Graduation.objects.all().delete()
	# f3 = open('data/grads.csv')

	# for line in f3.readlines():
	# 	cols = [item for item in line.split(',')]
	# 	g = Graduation()
	# 	g.dbn = ''.join([c for c in cols[0][:10] if c != '"'])
	# 	g.name = cols[1]
	# 	g.grads_percent = cols[6].replace('%','')
	# 	s_list = School.objects.filter(dbn=g.dbn)
	# 	if s_list:
	# 		g.school = s_list[0]
	# 	try:
	# 		g.save()
	# 	except:
	# 		print traceback.print_exc(file=sys.stdout)

	# Demographic.objects.all().delete()
	# f4 = open('data/demo.csv')
	# for line in f4.readlines()[1:]:
	# 	cols = [item for item in line.split(',')]
	# 	d = Demographic()
	# 	d.dbn = ''.join([c for c in cols[0][:10] if c != '"'])
	# 	d.name = cols[1]
	# 	d.year = cols[2]
	# 	#d.freelunch_reduced_percent = float(cols[4] or 0)
	# 	# d.black_percent = cols[8]
	# 	try:
	# 		d.save()
	# 	except:
	# 		print traceback.print_exc(file=sys.stdout)

	# schools = School.objects.all()
	# teachers = Teacher.objects.all()
	# grads = Graduation.objects.all()
	#return render(
    #	request,
    #	'index.html')
	# ,
 #    	{'schools': schools,
 #    	'teachers': teachers,
 #    	'grads': grads})

#def clean_num(s):
#	if s in ('NA', 'NA\n', '', None):
#		return None
#	else:
#		return s

	# dbn = models.CharField(max_length=10, blank=True)
 #    name = models.CharField(max_length=100, blank=True)
 #    year = models.CharField(max_length=30, blank=True)
 #    freelunch_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    freelunch_reduced_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    ell_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    sped_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    asian_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    black_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    hispanic_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    white_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    male_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    female_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    # dbn = models.CharField(max_length=10)
    # name = models.CharField(max_length=100)
    # year = models.IntegerField(blank=True, null=True)
    # cohort_category = models.CharField(max_length=30)
    # cohort_size = models.IntegerField(blank=True, null=True)
    # grads_num = models.IntegerField(blank=True, null=True)
    # grads_percent = models.CharField(max_length=30)
    # regents_num = models.IntegerField(blank=True, null=True)
    # regents_percent_total = models.CharField(max_length=30)
    # regents_percent_grad = models.CharField(max_length=30)
    # advregents_num = models.IntegerField(blank=True, null=True)
    # advregents_percent_total = models.CharField(max_length=30)
    # advregents_percent_grad = models.CharField(max_length=30)
    # othregents_num = models.IntegerField(blank=True, null=True)
    # othregents_percent_total = models.CharField(max_length=30)
    # othregents_percent_grad = models.CharField(max_length=30)
    # local_num = models.IntegerField(blank=True, null=True)
    # local_percent_total = models.CharField(max_length=30)
    # local_percent_grad = models.CharField(max_length=30)
    # enrolled_num = models.IntegerField(blank=True, null=True)
    # enrolled_percent = models.CharField(max_length=30)
    # drop_num = models.IntegerField(blank=True, null=True)
    # drop_percent = models.CharField(max_length=30)


    # school_name = models.CharField(max_length=500)
    # teacher_name_first_1 = models.CharField(max_length=500)
    # teacher_name_last_1 = models.CharField(max_length=500)

    # name = models.CharField(max_length=100)
    # principal = models.CharField(max_length=100)
    # progress_report_type = models.CharField(max_length=5)
    # school_level = models.CharField(max_length=30)
    # peer_index = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    # grade2012 = models.CharField(max_length=1, blank=True)
    # score2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # percent2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # prog_score2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # prog_grade2012 = models.CharField(max_length=1, blank=True)
    # perf_category2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # perf_grade2012 = models.CharField(max_length=1, blank=True)
    # environ_score = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # environ_grade = models.CharField(max_length=1, blank=True)
    # readiness_score2012 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    # readiness_grade2012 = models.CharField(max_length=1, blank=True)
    # additional_credit2012 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    # prog_grade2011 = models.CharField(max_length=1, blank=True)
    # prog_grade2010 = models.CharField(max_length=1, blank=True)
	# t.grade0910 = cols[-10]
	# t.va_0506 = clean_num(cols[-5])
	# t.va_0607 = clean_num(cols[-4])
	# t.va_0708 = clean_num(cols[-3])
	# t.va_0809 = clean_num(cols[-2])
	# if cols[15] not in ('NA\n', 'NA'):
	# 	t.va_0910 = cols[-1]
	# s_list = School.objects.filter(dbn=t.dbn)
	# if s_list:
	# 	t.school = s_list[0]
#	try:
#		t.save()
#	except:
#		print traceback.print_exc(file=sys.stdout)

	# Graduation.objects.all().delete()
	# f3 = open('data/grads.csv')

	# for line in f3.readlines():
	# 	cols = [item for item in line.split(',')]
	# 	g = Graduation()
	# 	g.dbn = ''.join([c for c in cols[0][:10] if c != '"'])
	# 	g.name = cols[1]
	# 	g.grads_percent = cols[6].replace('%','')
	# 	s_list = School.objects.filter(dbn=g.dbn)
	# 	if s_list:
	# 		g.school = s_list[0]
	# 	try:
	# 		g.save()
	# 	except:
	# 		print traceback.print_exc(file=sys.stdout)

	# Demographic.objects.all().delete()
	# f4 = open('data/demo.csv')
	# for line in f4.readlines()[1:]:
	# 	cols = [item for item in line.split(',')]
	# 	d = Demographic()
	# 	d.dbn = ''.join([c for c in cols[0][:10] if c != '"'])
	# 	d.name = cols[1]
	# 	d.year = cols[2]
	# 	#d.freelunch_reduced_percent = float(cols[4] or 0)
	# 	# d.black_percent = cols[8]
	# 	try:
	# 		d.save()
	# 	except:
	# 		print traceback.print_exc(file=sys.stdout)

	# schools = School.objects.all()
	# teachers = Teacher.objects.all()
	# grads = Graduation.objects.all()
	#return render(
    #	request,
    #	'index.html')
	# ,
 #    	{'schools': schools,
 #    	'teachers': teachers,
 #    	'grads': grads})

#def clean_num(s):
#	if s in ('NA', 'NA\n', '', None):
#		return None
#	else:
#		return s

	# dbn = models.CharField(max_length=10, blank=True)
 #    name = models.CharField(max_length=100, blank=True)
 #    year = models.CharField(max_length=30, blank=True)
 #    freelunch_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    freelunch_reduced_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    ell_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    sped_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    asian_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    black_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    hispanic_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    white_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    male_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    female_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    # dbn = models.CharField(max_length=10)
    # name = models.CharField(max_length=100)
    # year = models.IntegerField(blank=True, null=True)
    # cohort_category = models.CharField(max_length=30)
    # cohort_size = models.IntegerField(blank=True, null=True)
    # grads_num = models.IntegerField(blank=True, null=True)
    # grads_percent = models.CharField(max_length=30)
    # regents_num = models.IntegerField(blank=True, null=True)
    # regents_percent_total = models.CharField(max_length=30)
    # regents_percent_grad = models.CharField(max_length=30)
    # advregents_num = models.IntegerField(blank=True, null=True)
    # advregents_percent_total = models.CharField(max_length=30)
    # advregents_percent_grad = models.CharField(max_length=30)
    # othregents_num = models.IntegerField(blank=True, null=True)
    # othregents_percent_total = models.CharField(max_length=30)
    # othregents_percent_grad = models.CharField(max_length=30)
    # local_num = models.IntegerField(blank=True, null=True)
    # local_percent_total = models.CharField(max_length=30)
    # local_percent_grad = models.CharField(max_length=30)
    # enrolled_num = models.IntegerField(blank=True, null=True)
    # enrolled_percent = models.CharField(max_length=30)
    # drop_num = models.IntegerField(blank=True, null=True)
    # drop_percent = models.CharField(max_length=30)


    # school_name = models.CharField(max_length=500)
    # teacher_name_first_1 = models.CharField(max_length=500)
    # teacher_name_last_1 = models.CharField(max_length=500)

    # name = models.CharField(max_length=100)
    # principal = models.CharField(max_length=100)
    # progress_report_type = models.CharField(max_length=5)
    # school_level = models.CharField(max_length=30)
    # peer_index = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    # grade2012 = models.CharField(max_length=1, blank=True)
    # score2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # percent2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # prog_score2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # prog_grade2012 = models.CharField(max_length=1, blank=True)
    # perf_category2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # perf_grade2012 = models.CharField(max_length=1, blank=True)
    # environ_score = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # environ_grade = models.CharField(max_length=1, blank=True)
    # readiness_score2012 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    # readiness_grade2012 = models.CharField(max_length=1, blank=True)
    # additional_credit2012 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    # prog_grade2011 = models.CharField(max_length=1, blank=True)
    # prog_grade2010 = models.CharField(max_length=1, blank=True)