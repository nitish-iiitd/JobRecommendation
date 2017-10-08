import csv
import sys
csv.field_size_limit(sys.maxsize)
from pprint import pprint
import pickle

def exploreJobs():
	count=0
	jobdetails = {}
	alljobs = []
	with open("../Dataset/wuzzuf/Wuzzuf_Job_Posts_Sample.csv",'rb') as csvfile:
		a = csv.reader(csvfile,delimiter=',')
		for row in a:
			if count == 0:
				count+=1
				continue # skip the first heading row
			jobid = row[0]
			jobtitle = row[2]
			jobcat1,jobcat2,jobcat3 = row[3],row[4],row[5]
			jobind1,jobind2,jobind3 = row[6],row[7],row[8] 
			jobdetails[jobid] = [jobcat1,jobcat2,jobcat3,jobind1,jobind2,jobind3]
			alljobs +=  jobdetails[jobid]
			count+=1
		#print count

	#pprint(jobdetails) 
	alljobs = sorted(list(set(alljobs)))
	#print "All Jobs = ",alljobs
	print "Number of diff jobs : ",len(alljobs)

	## jobcat to index, index to jobcat
	job_to_index,index_to_job = {},{}
	for ii in range(len(alljobs)):
		job_to_index[alljobs[ii]] = ii
		index_to_job[ii] = alljobs[ii]

	#print "job_to_index:",job_to_index
	#print "index_to_job:",index_to_job		

	## saving jobdetails
	pickle.dump(jobdetails,open("jobdetails.p","wb"))

	## saving jobcat to index, index to jobcat
	pickle.dump(job_to_index,open("job_to_index.p","wb"))
	pickle.dump(index_to_job,open("index_to_job.p","wb"))


def exploreApplications():
	count=0
	appdetails = {} # userid : [jobids]
	with open("../Dataset/wuzzuf/Wuzzuf_Applications_Sample.csv",'rb') as csvfile:
		a = csv.reader(csvfile,delimiter=',')
		for row in a:
			if count == 0:
				count+=1
				continue # skip the first heading row
			userid = row[1]
			jobid = row[2]
			try:
				appdetails[userid] += [jobid]
			except KeyError:
				appdetails[userid] = [jobid]
			count+=1
		#print count

	pprint(appdetails) 

	print "Number of diff users : ",len(appdetails)

	## jobcat to index, index to jobcat
	user_to_index,index_to_user = {},{}
	ii = 0
	for key in appdetails.keys():
		user_to_index[key] = ii
		index_to_user[ii] = key
		ii += 1		

	print "user_to_index:",user_to_index
	print "index_to_user:",index_to_user

	## saving jobdetails
	pickle.dump(appdetails,open("appdetails.p","wb"))

	## saving jobcat to index, index to jobcat
	pickle.dump(user_to_index,open("user_to_index.p","wb"))
	pickle.dump(index_to_user,open("index_to_user.p","wb"))


if __name__ == "__main__":
	#exploreJobs()
	exploreApplications()
