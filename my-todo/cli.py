import argparse
from models import todoList, Row
from enums import TaskStatus

class TodoCLI:
    def __init__(self):
       self.tolist = todoList()
    
    def add(self, task):
        self.tolist.Add(task)

    def list(self, status: str= None):
        self.tolist.list_status(status)
    
    def remove(self, task_index):
        self.tolist.Delete(task_index)

    def update(self, task):
        self.tolist.Update(task)

    def reset(self):
        self.tolist.reset()
    
    def run(self):
        parser = argparse.ArgumentParser(description="Simple Todo CLI")
        subparsers = parser.add_subparsers(dest='command')
        # Add task command
        add_parser = subparsers.add_parser('add', help='Add a new task')
        add_parser.add_argument('task', type=str, help='Task to be added')

        # List tasks command
        list_parser = subparsers.add_parser('list', help='List all tasks')
        list_parser.add_argument('status', type=str, nargs='?', default=None, help='specific status or all')

        # Remove task command
        remove_parser = subparsers.add_parser('remove', help='Remove a task by index')
        remove_parser.add_argument('index', type=int, help='Index of the task to remove')

        # Remove task command
        update_parser = subparsers.add_parser('update', help='Update a task')
        update_parser.add_argument('index', type=int, help='Index of the task to update')
        update_parser.add_argument('task', type=str, help='task to update')
 
        # Reset 
        reset_parser = subparsers.add_parser('reset', help='Update a task')

        args = parser.parse_args()

        if args.command == 'add':
            row = Row(args.task)
            self.add(row)
        elif args.command == 'list':
            new_status = None
            if args.status is not None:
                try:
                    new_status = TaskStatus[args.status.upper()] 
                except KeyError:
                    print(f"Warning: '{args.status}' is not a valid status. Setting status to None.")
                self.list(new_status) 
        elif args.command == 'update':
            new_row=Row(args.task)
            new_row.UpdateID(args.index)
            self.update(new_row)
        elif args.command == 'remove':
            self.remove(args.index)
        elif args.command == 'reset':
            self.reset()
        


    
