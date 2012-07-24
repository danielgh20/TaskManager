# coding: utf8
import datetime

#db = DAL("sqlite://storage.sqlite")

db.define_table('job',
   Field('status'),
   Field('task','reference task'),
   Field('startTime','datetime',default=datetime.datetime.now),
   Field('endTime','datetime',default=datetime.datetime.now),
   Field('startBy'),
   Field('log')
   )
   
db.job.task.requires = IS_IN_DB(db,'task.name')
