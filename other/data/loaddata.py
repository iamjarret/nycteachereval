import csv
import sys
sys.path.append("/home/jarret/nycteacher/nycteacher/")
from teachers.models import Teachers, School

reader = csv.reader("School_Progress_Report_2010-2011.csv", delimiter=",")


parsed = (({'True':True}.get(row[0], False),
           row[1],
           int(row[2]),
           float(row[3]),
           row[4])
          for row in reader)
