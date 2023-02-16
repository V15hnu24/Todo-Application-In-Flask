# Simple Todo-Application-In-Flask

This is a simple Python Flask application with a simple todo list. Where we can create, delete, update and view the tasks and mark task as complete or imcomplete.


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

Requeriments:

- Python 3.6 or later
- Flask 1.1.2 or later
- csv 1.0 or later


## Installation

1. Clone the repository
```bash

git clone https://github.com/V15hnu24/Todo-Application-In-Flask.git

```

2. Change the directory

```bash
cd Todo-Application-In-Flask

```


3. Install the requirements

```bash

pip install -r requirements.txt

```


## Usage


1. Run the application

```bash

python app.py

```

As this is a simple backend application, it will run on the localhost:5000
To test this use services like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/)


## API Endpoints

1. POST /add-task - To add a task 

2. DELETE /delete-task/<int:id> - To delete a task

3. PUT /update-task/<int:id> - To update a task

4. GET /get-tasks - To view all the tasks

5. GET /get-task/<int:id> - To view a specific task 

6. PUT /mark-task-complete/<int:id> - To mark a task as complete 

7. PUT /mark-task-incomplete/<int:id> - To mark a task as incomplete


## Sample Request and Response

1. POST /add-task - To add a task 

The id should be unique and the task should be a string. The request body should be in the following format:

```json
{
    "id": "Task Title",
    "Task": "Task Description"
}
```

Returns json message of showing the whether the api has executed or not if successfully executed it will return the following message:

```json
{
    "message": "Task added successfully"
}
```

If not error according to the error will be returned


2. DELETE /delete-task/<int:id> - To delete a task

No body just id in the url

Returns json message of showing the whether the api has executed or not if successfully executed it will return the following message:

```json
{
    "message": "Task deleted successfully"
}
```
If not error according to the error will be returned


3. PUT /update-task/<int:id> - To update a task

The request body should be in the following format:

Status should be 0 or 1 where 0 is incomplete and 1 is complete


```json
{
    "Status": 0 ,
    "Task": "task"
}
```

4. GET /get-tasks - To view all the tasks

No body just the url

Returns all the tasks in json format


5. GET /get-task/<int:id> - To view a specific task 

No body just id in the url

Returns specific task in json format


6. PUT /mark-task-complete/<int:id> - To mark a task as complete 

id in the url

Returns json message of showing the whether the api has executed or not if successfully executed it will return the following message:

```json
{
    "message": "Task marked as complete"
}
```

If not error according to the error will be returned


7. PUT /mark-task-incomplete/<int:id> - To mark a task as incomplete

id in the url

Returns json message of showing the whether the api has executed or not if successfully executed it will return the following message:

```json
{
    "message": "Task marked as incomplete"
}
```

If not error according to the error will be returned



## Contributor
- [Vishnu](https://github.com/V15hnu24)
