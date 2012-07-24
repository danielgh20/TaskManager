# coding: utf8
# 尝试
def show(): 
  task_name = request.args(0) 
  if task_name == 'all'or task_name == None :  
    jobs = db().select(db.job.ALL, orderby=db.job.task)
  else:
    jobs = db().select(db.job.task == task_name)
  return dict(jobs=jobs)
