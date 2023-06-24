from datetime import datetime, date

class SortTask:
    def __init__(self, threshold):
        self.threshold = threshold
        
    def eisenhower(self, urgent:bool, important:bool):
        if urgent==True and important==True:
            return 1
        elif urgent==False and important==True:
            return 2
        elif urgent==True and important==False:
            return 3
        else:
            return 4
        
    def sort_deadline(self, tasks_list):
        for i in range(len(tasks_list)-1):
            date_i = datetime.strptime(tasks_list[i]["deadline"], '%a %b %d %Y').date()
            date_i1 = datetime.strptime(tasks_list[i+1]["deadline"], '%a %b %d %Y').date()
            # temp = tasks_list[i]
            if date_i > date_i1:
                # temp = tasks_list[i]
                temp = tasks_list[i]
                tasks_list[i] = tasks_list[i+1]
                tasks_list[i+1] = temp

        return tasks_list    
    
    def auto_sort(self, tasks:list):
        group1 = []
        group2 = []
        group3 = []
        group4 = []
        for task in tasks:
            deadline = datetime.strptime(task["deadline"], '%a %b %d %Y').date()
            avail = (deadline - date.today()).days
            
            important = task["importance"]
            urgent = True if avail <= self.threshold else False
            
            eisen = self.eisenhower(urgent, important)
            if eisen == 1: group1.append(task)
            elif eisen == 2: group2.append(task)
            elif eisen == 3: group3.append(task)
            else: group4.append(task)
            
        group1 = self.sort_deadline(group1)
        group2 = self.sort_deadline(group2)
        group3 = self.sort_deadline(group3)
        group4 = self.sort_deadline(group4)
        
        sorted = group1
        sorted.append(group2) 
        sorted.append(group3) 
        sorted.append(group4) 
        
        return sorted
    
tasks_list = [{"taskname": "mua oto",
               "description": "task",
               "deadline": "Wed Mar 1 2000",
               "importance": True},
              
              {"taskname": "mua xe dap",
               "description": "task",
               "deadline": "Wed Mar 2 2000",
               "importance": False},
              
              {"taskname": "di choi",
               "description": "task",
               "deadline": "Wed Mar 3 2000",
               "importance": True}]

sort = SortTask(2)
print(sort.sort_deadline(tasks_list))
print(sort.auto_sort(tasks_list))