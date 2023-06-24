import sqlite3
connect = sqlite3.connect("Database/Task_DB.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE if not exists Users(
                            USER_TASK TEXT, 
                            USER_DESCRIPTION TEXT, 
                            USER_DEADLINE DATETIME, 
                            USER_IMPORTANCE BOOLEAN
            );""")
connect.commit()
cursor.execute("""

    INSERT INTO Users(USER_TASK,USER_DESCRIPTION, USER_DEADLINE,USER_IMPORTANCE) VALUES('lamviev', 'lamviec','12/3/2023', 'True');
""")
cursor.execute("""

    INSERT INTO Users(USER_TASK,USER_DESCRIPTION, USER_DEADLINE,USER_IMPORTANCE) VALUES('lamviev', 'lamviec','12/3/2023', 'True');
""")
cursor.execute("""

    INSERT INTO Users(USER_TASK,USER_DESCRIPTION, USER_DEADLINE,USER_IMPORTANCE) VALUES('lamviev', 'lamviec','12/3/2023', 'True');
""")
cursor.execute("""

    INSERT INTO Users(USER_TASK,USER_DESCRIPTION, USER_DEADLINE,USER_IMPORTANCE) VALUES('lamviev', 'lamviec','12/3/2023', 'True');
""")

connect.commit()
cursor.execute("SELECT * FROM Users")
# row = cursor.fetchall()

# cursor.execute("DELETE FROM Users WHERE USER_TASK='lamviev' ")
# connect.commit()
tasklist = []
row_datas = cursor.fetchall()
for (taskname, desciption, deadline, importance) in row_datas:
    task = {

        'taskname': taskname,
        'description': desciption,
        'deadline': deadline,
        'importance':importance
    }
    print(task)
    tasklist.append(task)
    for idx, data in enumerate(tasklist):
        print("row: ",idx)
        for idx,  (key, val) in enumerate(data.items()):
            print(idx, val)
# print(tasklist)
connect.close()