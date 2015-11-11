# project/db_create.py

from views import db
from models import Task
from datetime import date

#create DB and table
db.create_all()

#insert data
#db.session.add(Task("FInish this tutorial", date(2015,3,13), 10, 1))
#db.session.add(Task("Finish Real Python", date(2015,3,13), 10, 1))
db.session.commit()

