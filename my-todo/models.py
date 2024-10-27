import os
import glob
import json
import hashlib
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
            if status == None or todo.get("status") == status.value:
                print(f"{todo.get('id')} {todo.get('task')} {todo.get('status')}")

    def write(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.todos, file)

    def Update(self, row):
        for i in range(len(self.todos)):
            if self.todos[i].get("id") == row.id:
                self.todos[i]["task"] = row.task 
        self.write()

    def UpdateStatus(self, id, status):
        for i in range(len(self.todos)):
            if self.todos[i].get("id") == id:
                self.todos[i]["status"] = status.value
        self.write()

    def Add(self, row):
        self.todos.append(row.to_dict())
        self.write()

    def Delete(self, id):
        for i in range(len(self.todos)):
            if self.todos[i].get("id") == id: 
                del self.todos[i]
                break
        self.write()
                
class Row:
    def __init__(self, task):
        if not isinstance(task, str):
            raise ValueError("Task must be a string")
        hash_object = hashlib.md5(task.encode())
        self.id=int.from_bytes(hash_object.digest(), 'little') % 100 
        self.status = 'TODO'
        self.task = task

    def UpdateID(self, id):
        self.id = id
    
    def UpdateStatus(self, status):
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "status": self.status,
            "task": self.task
        }


