"""
This example demonstrates the use of the SQLAlchemy job store.
On each run, it adds a new alarm that fires after ten seconds.
You can exit the program, restart it and observe that any previous alarms that have not fired yet
are still active. You can also give it the database URL as an argument.
See the SQLAlchemy documentation on how to construct those.
"""

from datetime import datetime, timedelta
import time
import sys
import os

from apscheduler.schedulers.background import BackgroundScheduler


def alarm(time):
    print(datetime.now())
    print('Alarm! This alarm was scheduled at %s.' %time)
    #os.system('calc')



if __name__ == '__main__':
    scheduler = BackgroundScheduler({
        'apscheduler.jobstores.default': {
            'type': 'sqlalchemy',
            'url': 'sqlite:///example.db',
            'tablename': 'apscheduler_jobs'
        },
        'apscheduler.executors.default': {
            'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
            'max_workers': '3'
        },

        'apscheduler.job_defaults.coalesce': True,
        'apscheduler.job_defaults.max_instances': 10,
        'apscheduler.job_defaults.misfire_grace_time':2,

    })
    jb1 = scheduler.add_job(alarm, 'interval',id='jbid1', seconds=3,args=[datetime.now()])
    #jb2 = scheduler.add_job(alarm, 'cron', id='jobid2', hour=22,minute=51, args=[datetime.now()])
    try:
        scheduler.start()
        print('ok')
        char = input('exit\n')
        #scheduler.remove_job(job_id='jbid1')
        #jb1.remove()
    except (KeyboardInterrupt, SystemExit):
        pass