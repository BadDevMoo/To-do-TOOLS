# Todo CLI

A simple command-line interface for managing your tasks.

## Features
- **Add tasks**  
  To add a new task:
  ```bash
  python3 cli.py add 'task'
  ```

- **List tasks**  
  To list all tasks:
  ```bash
  python3 cli.py list
  ```

- **List tasks based on status**  
  To list tasks with a specific status (e.g., 'Done'):
  ```bash
  python3 cli.py list 'Done'
  ```

- **Update task status**  
  To change the status of a task:
  ```bash
  python3 cli.py status_change <id> '<status>'
  ```

- **Update tasks**  
  To update the task description:
  ```bash
  python3 cli.py update <id> '<changed_task>'
  ```

- **Remove tasks**  
  To remove a task by its ID:
  ```bash
  python3 cli.py remove <id>
  ```

- **Reset task list**  
  To reset the entire task list:
  ```bash
  python3 cli.py reset
  ```

## Installation

Clone the repository:

```bash
git clone https://github.com/BadDevMoo/To-do-TOOLS.git
cd To-do-TOOLS
```

## Usage

After cloning the repository and navigating to the project directory, you can run the CLI commands as described in the Features section.

## Contributing

Feel free to submit issues and pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License.
