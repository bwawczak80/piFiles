
from crontab import *

cron = CronTab(user='pi')
job = cron.new(command='python example1.py')
job.minute.every(1)

cron.write()