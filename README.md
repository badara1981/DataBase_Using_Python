
## Setup instructions

- virtual env is a must
- install requirements
- migrate your database after with: `python manage.py migrate`
- You do not need to change to another RDBMS (Relational Database Management system). We use SQLITE3 in this test.

Boilerplate code has been provided for you. Extra help such as "TODO" statements have been left in `reminders/views.py`. You do not need to change any url configuration to complete this code.

Create some sample reminders using Postman or Django shell.

e.g. via shell command: `python manage.py shell_plus`

To create a new Reminder do something like:

`Reminder.objects.create(title="Test", description="Some description")`


## Tasks
=====


1. Add a DELETE route to the reminders application, send back a JSON response with the words `{"message": "Successfully deleted"}`. An example of a delete route might look like this: `http://localhost:8000/reminders/2/delete`. This issues an instruction to delete a reminder with an id (primary key) of 2.

2. Design a GET route which performs some mathematical operations such as addition and subtraction

e.g. `http://127.0.0.1:8000/reminders/math/?operation=add&a=1&b=2` should give back an HTTPResponse string with the value of 3 for example, the value of `a` being 1 and `b` being 2. It now means that `if` the operation is `add`, you want to add `a` and `b` to get the total. Minimum math operation here will be `add`.

Other optional posibilities are

- subtract
- divide
- multiply

Optional Question
=================

3. Write a test case for your DELETE reminder route.