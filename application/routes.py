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

@app.route('/update')
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

@app.route('/delete')
def deletelist():
    tasks = Tasks.query.all()
    return render_template('delist.html', tasks=tasks)

@app.route('/delete/<int:tid>')
def delete(tid):
    task_to_delete = Tasks.query.get(tid)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('deletelist'))

@app.route('/set-complete/<int:tid>')
def set_complete(tid):
    task_to_set = Tasks.query.get(tid)
    task_to_set.status = 'complete'
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/set-incomplete/<int:tid>')
def set_incomplete(tid):
    task_to_set = Tasks.query.get(tid)
    task_to_set.status = 'incomplete'
    db.session.commit()
    return redirect(url_for('complete'))

