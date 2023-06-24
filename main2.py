########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
# from ui_if2 import *
from ui_interface_2 import *
########################################################################
import QSS_Resources_rc
########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################

from Custom_Widgets.Widgets import QCustomSlideMenu
from function import TodoList
from PySide2.QtCore import *
########################################################################
## MAIN WINDOW CLASS
########################################################################


# import sqlite3
# connect = sqlite3.connect("Database/Task_DB.db")
# cursor = connect.cursor()

# cursor.execute("""CREATE TABLE if not exists Users(
#                             USER_TASK TEXT, 
#                             USER_DESCRIPTION TEXT, 
#                             USER_DEADLINE DATETIME, 
#                             USER_IMPORTANCE BOOLEAN
#             );""")

# connect.commit()
# connect.close()
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        # loadJsonStyle(self, self.ui, jsonFiles = {
        #     "mystyle.json", "style.json"
        #     }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 
        
        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)

        # TodoList.create_connect(self, db_file)
        ##########################################################################
        db_Folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "Database/user_2/Task_2.db"))
        db_Folder_cpl = os.path.abspath(os.path.join(os.path.dirname(__file__), "Database/user_2/Completed_2.db"))
        TodoList.sql_database(self, db_Folder=db_Folder)
        TodoList.task_completed_database(self, db_Folder=db_Folder_cpl)
        TodoList.display_v2(self, db_Folder)
        TodoList.display_cpl_task(self, db_Folder_cpl)
        self.ui.addtask.clicked.connect(lambda: TodoList.add_task(self, db_Folder=db_Folder))
        self.ui.deletetaskbtn.clicked.connect(lambda: TodoList.delete_task(self, db_Folder=db_Folder,db_folder_cpl=db_Folder_cpl))
        # TodoList.displayTask(self, TodoList.get_all_tasks(self, db_Folder=db_Folder))
        self.ui.sorttaskbtn.clicked.connect(lambda: TodoList.sort_task(self,db_folder=db_Folder, sort_type='sort by urgent'))
        self.ui.searchbtn.clicked.connect(lambda: TodoList.search_task(self))





########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
