import os
import sys 
import sqlite3
from sqlite3 import Error
# import datetime
from datetime import datetime
from PySide2.QtWidgets  import QTableWidgetItem, QMessageBox 
from PySide2.QtCore import *
# from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
# from sort_tasks import SortTask
from sort_tasks_2 import SortTask
from todo import ToDo
class TodoList(ToDo):

    def __init__(self, arg):
        super(TodoList, self).__init__()
        self.arg = arg 


    def create_connect(self,db_file):
        connect = None 
        try: 
            connect = sqlite3.connect(database=db_file)
        except Error as e:
            print(e)


        return connect
    
    def create_table(self, connect, create_table_sql):
        try:
            cursor = connect.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(e)

    

    def sql_database(self, db_Folder):
        create_table_sql = """
            CREATE TABLE Tasklist (
                        TASK TEXT, 
                        DESCRIPTION TEXT, 
                        DEADLINE DATETIME, 
                        IMPORTANCE BOOLEAN

            );
        """
        connect = TodoList.create_connect(self, db_file=db_Folder)

        # create table 

        if connect is not None:
            TodoList.create_table(self,connect=connect, create_table_sql=create_table_sql)
        else:
            print("Error! cannot create tabel of TodoList")
    

    def task_completed_database(self, db_Folder):
        create_table_sql = """
            CREATE TABLE Taskcompleted (
                        TASK TEXT, 
                        DESCRIPTION TEXT, 
                        DEADLINE DATETIME, 
                        IMPORTANCE BOOLEAN

            );
        """
        connect = TodoList.create_connect(self, db_file=db_Folder)

        # create table 

        if connect is not None:
            TodoList.create_table(self,connect=connect, create_table_sql=create_table_sql)
        else:
            print("Error! cannot create tabel of TodoList")

    def get_all_tasks(self, db_Folder):

        connect = TodoList.create_connect(self, db_file=db_Folder)
        get_tsks = """
            SELECT * FROM Tasklist;
        """
        try:
            cursor = connect.cursor()
            cursor.execute(get_tsks)
            return cursor
        
        except Error as e:
            print(e)


    def add_task(self, db_Folder):
        connect = TodoList.create_connect(self, db_file=db_Folder)

        task = self.ui.taskname.text()
        description = self.ui.description.text()
        deadline = self.ui.dateEdit.date().toString()
        importance = self.ui.importance.isChecked()

        # insert_sql_task = f"""
        #     INSERT INTO Users(USER_TASK, USER_DESCRIPTION, USER_DEADLINE, USER_IMPORTANCE) VALUES (
        #     '{task}, '{description}', '{deadline}', '{importance}'
        #     );
        # """

        insert_sql_task = f"""
        INSERT INTO Tasklist(TASK, DESCRIPTION, DEADLINE, IMPORTANCE) VALUES(
        
        '{task}', '{description}', '{deadline}', '{importance}');
        
        """
        #exercute Sql satement
        if not connect.cursor().execute(insert_sql_task):
            print("Can not create table task!")
        else: 

            connect.commit()
            self.ui.taskname.setText("")
            self.ui.description.setText("")
            self.ui.dateEdit.setDate(QDate.currentDate())
            self.ui.importance.setChecked(True)

            # TodoList.displayTask(self, TodoList.get_all_tasks(self, db_Folder=db_Folder))
            TodoList.display_v2(self,db_Folder=db_Folder)


    def delete_task(self, db_Folder, db_folder_cpl):
        # connect = TodoList.create_connect(self, db_file=db_Folder)
        # self.ui.tableWidget.setRowCount(0)
        current_row = self.ui.tableWidget.currentRow()
        if current_row < 0:
            return QMessageBox.warning(self, 'Warning','Please select a record to delete')

        button = QMessageBox.question(
            self,
            'Confirmation',
            'Are you sure that you want to delete the selected row?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if button == QMessageBox.StandardButton.Yes:
            self.ui.tableWidget.removeRow(current_row)
        # self.ui.tableWidget.removeRow(current_row)
        connect = TodoList.create_connect(self, db_file=db_Folder)
        cursor  =  connect.cursor()
        print(self.ui.tableWidget.itemAt(current_row, 0).text())
        completed_sql_task = f"""
            SELECT * FROM Tasklist WHERE TASK='{self.ui.tableWidget.itemAt(current_row - 1, 0).text()}'
        """

        cursor.execute(completed_sql_task)
        cpl_task = cursor.fetchall()
        print(cpl_task)
        del_sql_task = f"""
            DELETE FROM Tasklist WHERE TASK='{self.ui.tableWidget.itemAt(current_row - 1, 0).text()}'
        """
        print(del_sql_task )
        cursor.execute(del_sql_task)
        connect.commit()

        connect_cpl = TodoList.create_connect(self, db_file=db_folder_cpl)
        cursor_cpl = connect_cpl.cursor()
        # .execute(completed_sql_task)
        # data = cursor_cpl.fetchall()


        for (taskname, description, deadline, importance) in cpl_task:
            insert_cpl_task = f"""
            INSERT INTO Taskcompleted(TASK, DESCRIPTION, DEADLINE, IMPORTANCE) VALUES(
            
            '{taskname}', '{description}', '{deadline}', '{importance}');
            
            """
            if not cursor_cpl.execute(insert_cpl_task):
                print("Can not insert completed task!")
            else:
                connect_cpl.commit()
                TodoList.display_cpl_task(self, db_Folder_cpl=db_folder_cpl)
        

    def search_task(self):
        search_task = self.ui.search.text()
        n_rows = self.ui.tableWidget.rowCount()
        if n_rows !=0 and len(search_task) !=0:
            for row in range(0, n_rows):
                if search_task not in self.ui.tableWidget.item(row, 0).text():
                    self.ui.tableWidget.hideRow(row)
        else:
            for row in range(0, n_rows):
                self.ui.tableWidget.showRow(row)




    def sort_task(self,db_folder,  threshold=2, sort_type='sort by deadline'):
        
        connect = TodoList.create_connect(self, db_file=db_folder)
        cursor  =  connect.cursor()
        cursor.execute("SELECT * FROM Tasklist")
        # self.tasklist = []
        # rows_data = cursor.fetchall()
        task_list = []
        row_datas = cursor.fetchall()
        print(row_datas)
        for (taskname, desciption, deadline, importance) in row_datas:
            task = {

            'taskname': taskname,
            'description': desciption,
            'deadline': deadline,
            'importance':importance
            }
        # print(task)
            task_list.append(task)
        sorttask = SortTask(threshold=threshold)
        print("===============================")
        print(task_list)
        if sort_type == 'sort by deadline':
            task_sorted = sorttask.sort_deadline(task_list)
        elif sort_type =='sort by urgent':
            task_sorted = sorttask.auto_sort(task_list)
        else:
            print("pls enter correct sort type:  sort by deadline or sort by urgent")
        n_rows = self.ui.tableWidget.rowCount()
        print("==============================")
        self.ui.tableWidget.setRowCount(0)
        for idx, data in enumerate(task_sorted):
            self.ui.tableWidget.insertRow(idx)
            for col, (key, val) in enumerate(data.items()):
                self.ui.tableWidget.setItem(idx, col, QTableWidgetItem(str(val)))
        
    def displayTask(self, rows ):
        for row  in rows:
            rowPosition = self.ui.tableWidget.rowCount()
            if rowPosition > 0:
                continue

            item_count = 0 
            self.ui.tableWidget.setRowCount(rowPosition + 1)
            qtableWidgetItem = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(rowPosition, qtableWidgetItem)

            for item in row:
                print(item)
                self.qtableWidgetItem = QTableWidgetItem()
                self.ui.tableWidget.setItem(rowPosition, item_count,self.qtableWidgetItem )
                self.qtableWidgetItem = self.ui.tableWidget.item(rowPosition, item_count)
                self.qtableWidgetItem.setText(str(item))

                item_count +=1 
            rowPosition +=1 
    def display_v2(self, db_Folder):
        connect = TodoList.create_connect(self, db_file=db_Folder)
        get_tsks = """
            SELECT * FROM Tasklist;
        """
        try:
            cursor = connect.cursor()
            cursor.execute(get_tsks)
            rows = cursor.fetchall()
            self.ui.tableWidget.setRowCount(0)
            for index, row_data in enumerate(rows):
                self.ui.tableWidget.insertRow(index)
                for col, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(index, col, QTableWidgetItem(str(data)))
        
        except Error as e:
            print(e)



    def display_cpl_task(self, db_Folder_cpl):
        connect = TodoList.create_connect(self, db_file=db_Folder_cpl)
        get_tsks = """
            SELECT * FROM Taskcompleted;
        """
        try:
            cursor = connect.cursor()
            cursor.execute(get_tsks)
            rows = cursor.fetchall()
            self.ui.tableWidget_2.setRowCount(0)
            for index, row_data in enumerate(rows):
                self.ui.tableWidget_2.insertRow(index)
                for col, data in enumerate(row_data):
                    self.ui.tableWidget_2.setItem(index, col, QTableWidgetItem(str(data)))
        
        except Error as e:
            print(e)