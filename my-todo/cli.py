import argparse
from models import todoList, Row
from enums import TaskStatus

class TodoCLI:
    def __init__(self):
       self.tolist = todoList()
    
    def add(self, task):
        task = Row(task)
        self.tolist.Add(task)

    def list(self, status: str= None):
        self.tolist.list_status(status)
    
    def remove(self, task_index):
        self.tolist.Delete(task_index)

    def update(self, task):
        self.tolist.Update(task)
    
    def updateStatus (self, task_index, status):
        self.tolist.UpdateStatus(task_index, status)

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

        # update task 
        update_parser = subparsers.add_parser('update', help='Update a task')
        update_parser.add_argument('index', type=int, help='Index of the task to update')
        update_parser.add_argument('task', type=str, help='task to update')

        # update task_status
        update_status_parser = subparsers.add_parser('status_change', help='Update task status')
        update_status_parser.add_argument('index', type=int, help='Index of the task to update')
        update_status_parser.add_argument('status', type=str, help='status of task')
 
        # Reset 
        reset_parser = subparsers.add_parser('reset', help='Update a task')

        args = parser.parse_args()

        if args.command == 'add':
            self.add(args.task)
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
            #print(new_row.to_dict())
            self.update(new_row)
        elif args.command == 'remove':
            self.remove(args.index)
        elif args.command == 'reset':
            self.reset()
        elif args.command == 'status_change':
            try:
                new_status = TaskStatus[args.status.upper()]
                self.updateStatus(args.index, new_status)
            except KeyError:
                print(f"Warning: '{args.status}' is not a valid status.")
        
if __name__ == "__main__":
    cli = TodoCLI()
    cli.run()

    
