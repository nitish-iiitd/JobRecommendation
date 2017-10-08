import csv
import sys
csv.field_size_limit(sys.maxsize)
from pprint import pprint
import pickle

jobdetails = pickle.load(open("../Explore/jobdetails.p","rb"))
appdetails = pickle.load(open("../Explore/appdetails.p","rb"))
user_to_index = pickle.load(open("../Explore/user_to_index.p","rb"))
job_to_index = pickle.load(open("../Explore/job_to_index.p","rb"))

users = len(user_to_index)
jobs = len(job_to_index)

matrix = [[0 for ii in range(jobs)] for jj in range(users)]

progress = 0
for key in user_to_index.keys():
	print "Progress:",progress
	userindex = user_to_index[key]
	hisjobs = appdetails[key]
	for job in hisjobs:
		jobcats = jobdetails[job]
		for jobcat in jobcats:
			jobindex = job_to_index[jobcat]
			matrix[userindex][jobindex] = 1
	progress += 1

pickle.dump(matrix,open("matrix.p","wb"))
pprint(matrix[:100])
			


