import os
import glob
import json
class todoList:
    def __init__(self):
        self.folder_path = os.getcwd()
        self.file_path = os.path.join(self.folder_path, "todo.json")
        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)
        with open(self.file_path, 'r') as file:
            self.todos = json.load(file)

    def reset(self):
        json_files = glob.glob(os.path.join(self.folder_path, "*.json"))
        for json_file in json_files:
            try:
                os.remove(json_file)
                print(f"Reset To-do list")
            except Exception as e:
                print(f"Error resetting: {e}")

    def list_status(self, status: str= None):
        for todo in self.todos:
            if status is None or todo.get("status") == status:
                print(todo)

    def write(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.todos, file, indent=4)

    def Update(self, row):
        for i in range(len(self.todos)):
            if self.todos[i].get("id") == row.id:
                self.todos[i] = row
        self.write()

    def Add(self, row):
        self.todos.append(row)
        self.write()

    def Delete(self, id):
        for i in range(len(self.todos)):
            if self.todos[i].get("id") == id: 
                del self.todos[i]
        self.write()
        self.list_status('Progress')
                

class Row:
    def __init__(self, task):
        self.id=id
        self.status = 'TODO'
        self.task = task

    def UpdateID(self, id):
        self.id = id
    
    def UpdateStatus(self, status):
        self.status = status



