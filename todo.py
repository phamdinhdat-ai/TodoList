import os 

from abc import ABC, abstractmethod

class ToDo(ABC):
    
    @abstractmethod
    def create_connect(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def task_completed_database(self):
        pass

    @abstractmethod
    def get_all_tasks(self):
        pass

    @abstractmethod
    def add_task(self):
        pass

    
    @abstractmethod
    def delete_task(self):
        pass

    @abstractmethod
    def search_task(self):
        pass

    @abstractmethod
    def sort_task(self):
        pass

    @abstractmethod
    def display_task(self):
        pass