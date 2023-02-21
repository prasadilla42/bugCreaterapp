import json

from bson import ObjectId
from flask import Flask, request, render_template, Response
from bug_tracker.bug_app.user import User
from bug_tracker.bug_app.bug import Bug

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Landing page
    """
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)


@app.route('/create_bug', methods=['GET', 'POST'])
def create_bug():
    """
    Create a new bug
    """
    if request.method == 'GET':
        try:
            return render_template('create_bug.html')
        except Exception as e:
            return str(e)
    elif request.method == 'POST':
        try:
            title = request.form['title']
            description = request.form['description']
            severity = request.form['severity']
            steps = request.form['steps']
            expected = request.form['expected']
            actual = request.form['actual']
            bug = Bug()
            newbug = {"title": title, "description": description, "severity": severity, "steps": steps,
                      "expected": expected, "actual": actual}
            return bug.create_bug(newbug)
        except Exception as e:
            return str(e)

@app.route('/delete_bug', methods=['DELETE'])
def delete_bug():
    """
    Delete the bug previously stored in database
    """
    data = json.loads(request.get_data().decode('utf-8'))
    rowid = data.get("id")
    query={"_id" : ObjectId(rowid)}
    bug = Bug()
    try:
        return bug.close_bug(query)
    except Exception as e:
        return str(e)

@app.route('/view_bug', methods=['GET', 'POST'])
def view_bug():
    """
    Bugs table listed
    """
    try:
        bug = Bug()
        bugs = bug.list_bug()
        user = User()
        users = user.list_user()
        usernames = []
        if not bugs:
            return "No bugs for assignment"
        if not users:
            return "create user for assign bugs"
        for user in users:
            usernames.append(user['username'])
        return render_template('view_bug.html', bugs=bugs, users=usernames)
    except Exception as e:
        return str(e)


@app.route('/create_user', methods=['GET'])
def create_user():
    """
    Create a new user
    """
    if request.method == 'GET':
        try:
            return render_template('create_user.html')
        except Exception as e:
            return str(e)
    elif request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            birthdate = request.form['birthdate']
            gender = request.form['gender']
            newuser = {"username": username, "email": email, "password": password, "birthdate": birthdate,
                       "gender": gender}
            user = User()
            return user.create_user(newuser)
        except Exception as e:
            return str(e)

@app.route("/update_bug", methods=['PUT'])
def update_bug():
    """
    Update bug with an assigned user
    """
    try:
        updated_bug = json.loads(request.get_data().decode('utf-8'))
        bug = Bug()
        bug.change_user(updated_bug["username"], updated_bug["id"])
        return Response(status=200)
    except Exception as e:
        return str(e)

@app.route('/view_users', methods=['GET'])
def view_users():
    """
    Basic view of all users
    """
    try:
        user = User()
        users = user.list_user()
        return render_template('view_users.html', users=users)
    except Exception as e:
        return str(e)

@app.route('/update_user',methods=['PUT'])
def update_user():
    """
    This method update exisitng user with a new user name supplied
    """
    try:
        updated_user = json.loads(request.get_data().decode('utf-8'))
        user = User()
        user.update_user(updated_user["id"], updated_user["newuser"])
        return Response(status=200)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run()
