from application import app, db, AddTask, UpdateTask
from application.models import Tasks
from flask import render_template, request, redirect, url_for

@app.route('/home')
def home():
    tasks = Tasks.query.filter_by(status='incomplete').all()
    return render_template('home.html', tasks=tasks)

@app.route('/add', methods=['GET','POST'])
def add():
    form = AddTask()
    if request.method == 'POST':
        task_name = form.task_name.data
        task_desc = form.task_desc.data
        task_stat = form.task_stat.data
        newtask = Tasks(name = task_name, desc = task_desc, status = task_stat)
        db.session.add(newtask)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route('/update-list')
def updatelist():
    tasks = Tasks.query.all()
    return render_template('uplist.html', tasks=tasks)

@app.route('/update/<int:tid>', methods=['GET','POST'])
def update(tid):
    task = Tasks.query.filter_by(id=tid).first()
    form = UpdateTask()
    if request.method == 'POST':
        task_name = form.task_name.data
        task_desc = form.task_desc.data
        task_stat = form.task_stat.data
        tasktoupdate = Tasks.query.filter_by(id=tid).first()
        tasktoupdate.name = task_name
        tasktoupdate.desc = task_desc
        tasktoupdate.status = task_stat
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', form=form, task=task.name)

@app.route('/complete')
def complete():
    completed_tasks = Tasks.query.filter_by(status='complete').all()
    return render_template('complete.html', tasks = completed_tasks)

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    t_string = ""
    for task in all_tasks:
        t_string += "<br>"+ f"{task.name}| {task.desc}| {task.status}"
    return t_string

@app.route('/update/status/<tid>-<tstat>')
def updatestat(tid, tstat):
    task = Tasks.query.get(tid)
    task.status = tstat
    db.session.commit()
    return task.status

@app.route('/update/desc/<tid>-<tdesc>')
def updatedesc(tid, tdesc):
    task = Tasks.query.get(tid)
    task.desc = tdesc
    db.session.commit()
    return task.desc

@app.route('/delete/<tid>')
def delete(tid):
    task_to_delete = Tasks.query.get(tid)
    db.session.delete(task_to_delete)
    db.session.commit()
    return f"Deleted task number {tid}"


