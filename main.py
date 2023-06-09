from scheduler import Osch
import time
import datetime

def job_callable():
	with open('log', 'a') as f:
		f.write(f'job started at {datetime.datetime.now()}')
		time.sleep(10)
		f.write(f'job finished at {datetime.datetime.now()}\n\n')

print("main started")
#job_callable()


now = datetime.datetime.now().time()
job = {'callable': job_callable, 'schedule': now.replace(minute=now.minute + 2)}
scheduler = Osch()
scheduler.add_job('alpha', job['callable'], job['schedule'])
scheduler.start()
