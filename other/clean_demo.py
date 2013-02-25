'''
This is a custom-made cleaner that goes through the demo.csv file and imports it 
into the SQL db
'''
import os
import sys
import csv
sys.path.append("/home/jarret/nycteacher/nycteacher/")
from teachers.models import Teachers, School
PATH = "/home/jarret/nycteacher/nycteacher/other/"

def get_teacherid(line):
	return "%s_%s_%s"%(get_lastname(line), get_firstname(line), get_dbn(line))

def get_grade(line):
	return None

def dec3(thing):
	return "%0.1f"%float(thing)

def get(line, num, funtoconvert):
	got = line[num]
	if got=="NA":
		return None
	else:
		return funtoconvert(got)

def main():
	PROJECT_PATH = os.getcwd()
	with open(PROJECT_PATH+'/other/rawdata/demo.csv') as csvfile:
		reader = csv.reader(csvfile, delimiter=",", quotechar ="|")
		reader.next() # skip header
		count = 0
		for line in reader:
			if count>15:
				assert False
			else:
				dbn = get(line, 0, str)
				print dbn
				try:
					match = School.objects.get(dbn=dbn)
				except:
					match = School(dbn=dbn)
				match.name = get(line, 1, str)
    			match.freelunch = get(line, 3, dec3)
    			match.ell = get(line, 4, dec3)
    			match.sped = get(line, 5, dec3)
    			match.asian = get(line, 6, dec3)
    			match.black = get(line, 7, dec3)
    			match.hisp = get(line, 8, dec3)
    			match.white = get(line, 9, dec3)
    			match.male = get(line, 10, dec3)
    			match.female = get(line, 11, dec3)
    			match.save()
			count +=1