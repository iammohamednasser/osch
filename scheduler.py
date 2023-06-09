import time
import datetime
from multiprocessing import Process


class Osch:
	
	def __init__(self, jobs=[]):
		# check every job. to-do
		self.jobs = jobs

	def add_job(self, name, job_callable, schedule):
		job = { 'name': name,
				'callable': job_callable,
				'schedule': schedule }
		if Osch.is_valid(job):
			self.jobs.append(job)
		else :
			raise Exception('job object is not valid')


	def is_valid(job):
		# check job structure
		# check schedule format
		# to-do
		return True

	def start(self):
		today = datetime.datetime.now()
		jobs_ = []
		for job in self.jobs:
			schedule = job['schedule']
			temp = { 'name': job['name'],
					 'callable':job['callable'],
					 'next_run': today.replace(hour=schedule.hour, minute=schedule.minute) }
			jobs_.append(temp)

		while True:
			now = datetime.datetime.now().replace(second=0, microsecond=0)
			for job in jobs_:
				print(f"now = {now}, job = {job['name']}, next_run = {job['next_run']}")
				if now > job['next_run']:
					print('yes')
					Process(target=job['callable']).start()
					job['next_run'] = job['next_run'] + datetime.timedelta(days=1)
				else:
					print('no')
			print('scheduler prcess sleeping')
			time.sleep(15)

class Job:
	# to-do
	pass