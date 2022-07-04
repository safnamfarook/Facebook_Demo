import mysql.connector
from . models import *

class Db:
    def __init__(self):
        self.db_connection = mysql.connector.connect(user="root", password="Password.123", 
                                                host="127.0.0.1", database="facebook_db" )
        self.cursor = self.db_connection.cursor()

def login_db(user):
    db = Db()
    cursor = db.cursor
    sql = "SELECT * FROM login WHERE username = '"+user.username+"'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        if result[2] == user.password:
            return('Login success')
        else:
            return('Incorrect password')
        
    else:
        return('Username doesnot exist')

def register_db(user):
    db = Db()
    cursor = db.cursor
    sql = "INSERT INTO users VALUES(null, '"+user.first_name+"', '"+user.last_name+"', '"+user.gender+"', '"+user.dob+"', '"+user.email+"', '"+user.phone+"')"
    cursor.execute(sql)
    user_id = cursor.lastrowid
    db.db_connection.commit()
    if user_id:
        return user_id
    else:
        return 0 

def insertLogin_db(userid, user):
    db = Db()
    cursor = db.cursor
    sql = "INSERT INTO login VALUES(null, '"+user.username+"', '"+user.password+"')"
    cursor.execute(sql)
    login_id = cursor.lastrowid
    db.db_connection.commit()
    if login_id:
        return ("Login success")
    else:
        return 0

def update_password_db(username, current_password, new_password):
    status = " "
    db = Db()
    cursor = db.cursor
    sql = "SELECT * FROM login where username = '"+username+"'"
    cursor.execute(sql)
    result = cursor.fetchone()
    print("username", username)
    if result:
        current_pass_og = result[2]
        if current_pass_og == current_password:
            sql1 = "UPDATE login SET password = '"+new_password+"' WHERE username = '"+username+"'"
            cursor.execute(sql1)
            db.db_connection.commit()
            if cursor.rowcount == 1:
                status = "Password updated successfully"
            else:
                status = "Try a new password"
        else:
            status = "Password is incorrect"
    else:
        status = "Username does not exist"
    return status

def insertPost_db(post):
    status = " "
    db = Db()
    cursor = db.cursor
    post_id = cursor.lastrowid
    sql = "SELECT * FROM users where email= '"+post.username+"'"
    cursor.execute(sql)
    result = cursor.fetchone()
    userid = result[0]
    sql = 'INSERT INTO posts(pk_post_id, fk_user_id, content, create_time) VALUES (%s,%s,%s,%s)'
    cursor.execute(sql, (post_id, userid, post.content, post.created_time))
    db.db_connection.commit()
    if cursor.rowcount == 1:
        status = "Post Added"
    else:
        status = "There is an error in uploading your post"
    return status

def deletePost_db(post_id):
    status = " "
    db = Db()
    cursor = db.cursor 
    sql = "DELETE FROM posts WHERE pk_post_id = '%d'" %(post_id)
    cursor.execute(sql)
    db.db_connection.commit()
    if cursor.rowcount == 1:
        status = "Post Deleted"
    else:
        status = "There is an error in deleting your post"
    return status