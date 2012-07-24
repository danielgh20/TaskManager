# coding: utf8
import datetime

#db = DAL("sqlite://storage.sqlite")

db.define_table('task',
   Field('name', unique=True),
   Field('tag'),
   Field('owner'),
   Field('user'),
   Field('passwd','password'),
   Field('host'),
   Field('enable','boolean',default=True),
   Field('cron'),
   Field('command','text'),
   Field('createdOn','datetime',default=datetime.datetime.now),
   format = "%(name)s"
   )

class MyVirtualFields(object):
  def nextRun(self):
    return self.task.cron
            
db.task.virtualfields.append(MyVirtualFields())

db.task.name.requires = IS_NOT_EMPTY()
db.task.owner.requires = IS_NOT_EMPTY()
db.task.user.requires = IS_NOT_EMPTY()
db.task.host.requires = IS_NOT_EMPTY()
db.task.command.requires = IS_NOT_EMPTY()
