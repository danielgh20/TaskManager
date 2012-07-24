# coding: utf8
# 尝试

from gluon.tools import Crud
crud = Crud(db)

#@auth.requires_login()
def all():
    #tasks= db(auth.accessible_query('read', db.task)).select(db.task.ALL)
    tasks = db().select(db.task.ALL, orderby=db.task.tag)
    return dict(tasks=tasks)

def edit():
   record = db.task(request.args(0)) or redirect(URL('all'))
   form = SQLFORM(db.task, record,deletable=True)
   if form.process().accepted:
       response.flash = 'form accepted'
   elif form.errors:
       response.flash = 'form has errors'
   return dict(form=form)

def add():
   form = crud.create(db.task)
   if form.process().accepted:
     response.flash = "the task is add"
     redirect(URL("all"))
   return dict(form=form)

def manage():
   grid = SQLFORM.grid(db.task,
             fields=[db.task.tag,db.task.name,db.task.enable,db.task.user,db.task.host,db.task.cron,db.task.command],
             orderby=db.task.tag,
             searchable=True,
             sortable=True,
             deletable=True,
             editable=True,
             details=True,
             create=True,
             csv=True,
             paginate=20,
             user_signature=True
             )
   return dict(grid=grid)
