from crontab import CronTab

cron = CronTab(user='pi')
job = cron.new(command='python temp_humidity_04_2019.py')
job.minute.every(5)

cron.write()