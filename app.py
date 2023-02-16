from flask import Flask, app, render_template, request, jsonify
import os, csv
from helperfuctions import *

#path for the csv file
dir_path = os.path.dirname(__file__)
csv_path = "Database csv/database.csv"

# Final path for the csv file i.e., our database
database_path = os.path.join(dir_path, csv_path)

#creating a flask app
app = Flask(__name__)

#Route for add task
@app.route('/add-task', methods=['POST'])
def add_task():
    #getting the data from the request
    data = request.get_json()

    try:
        with open(database_path, 'a', newline="") as file:
            #creating a writer object
            writer = csv.writer(file)


            #writing the data to the csv file with 0 as the status of the task i.e., incomplete
            writer.writerow([data['id'], data['Task'], 0])
    except FileNotFoundError:
        return server_error()
    except Exception as e:
        return exception_handler(e)
        
    return jsonify({'message': 'Task added successfully'})


#Route for get all tasks
@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    #creating a list to store the tasks
    tasks = []

    try:
        with open(database_path, 'r') as file:
            #creating a reader object
            reader = csv.reader(file)

            #iterating through the rows
            for row in reader:
                #creating a dictionary to store the data
                task = {
                    'id': row[0],
                    'Task': row[1],
                    'Status': row[2]
                }

                #appending the dictionary to the list
                tasks.append(task)
    except FileNotFoundError:
        return server_error()
    except Exception as e:
        return exception_handler(e)
        
    return jsonify({'tasks': tasks})


#Route for get a task
@app.route('/get-task/<id>', methods=['GET'])
def get_task(id):

    try:
        with open(database_path, 'r') as file:
            #creating a reader object
            reader = csv.reader(file)

            #iterating through the rows
            for row in reader:
                #checking if the id is equal to the id of the row
                if id == row[0]:
                    #creating a dictionary to store the data
                    task = {
                        'id': row[0],
                        'Task': row[1],
                        'Status': row[2]
                    }

                    #returning the dictionary
                    return jsonify({'task': task})
    except FileNotFoundError:
        return server_error()

    except Exception as e:
        return exception_handler(e)

    return jsonify({'message': 'Task not found'})


#Route for update a task
@app.route('/update-task/<id>', methods=['PUT'])
def update_task(id):
    #getting the data from the request
    data = request.get_json()

    try:
        with open(database_path, 'r') as file:
            #creating a reader object
            reader = csv.reader(file)

            #creating a list to store the rows
            rows = []
            found = False

            #iterating through the rows
            for row in reader:
                #checking if the id is equal to the id of the row
                if id == row[0]:
                    found = True
                    #updating the status of the task
                    if(data['Task'] != ""):
                        row[1] = data['Task']
                    
                    if(data['Status'] != ""):
                        row[2] = data['Status']

                #appending the row to the list
                if(row):
                    rows.append(row)

            
        if(found == False):
            return jsonify({'message': 'Task not found'})

        with open(database_path, 'w',newline='') as file:
            #creating a writer object
            writer = csv.writer(file)
            #writing the rows to the csv file
            writer.writerows(rows)
    except FileNotFoundError:
        return server_error()
    except Exception as e:
        return exception_handler(e)
        
    return jsonify({'message': 'Task updated successfully'})


#Route for delete a task
@app.route('/delete-task/<id>', methods=['DELETE'])
def delete_task(id):
    
        try:
            with open(database_path, 'r') as file:
                #creating a reader object
                reader = csv.reader(file)
    
                #creating a list to store the rows
                rows = []
                found = False

                #iterating through the rows
                for row in reader:
                    #checking if the id is equal to the id of the row
                    if id == row[0]:
                        found = True

                    if id != row[0]:
                        #appending the row to the list
                        rows.append(row)

            
            if(found == False):
                return jsonify({'message': 'Task not found'})

            with open(database_path, 'w',newline='') as file:
                #creating a writer object
                writer = csv.writer(file)
    
                #writing the rows to the csv file
                writer.writerows(rows)
        except FileNotFoundError:
            return server_error()
        except Exception as e:
            return exception_handler(e)
            
        return jsonify({'message': 'Task deleted successfully'})


#Route for mark as complete
@app.route('/mark-task-complete/<id>', methods=['PUT'])
def mark_task_complete(id):

    try:
        with open(database_path, 'r') as file:
            #creating a reader object
            reader = csv.reader(file)

            #creating a list to store the rows
            rows = []
            found = False
            #iterating through the rows
            for row in reader:
                #checking if the id is equal to the id of the row
                if id == row[0]:
                    #updating the status of the task
                    row[2] = 1
                    found = True
                
            

                #appending the row to the list
                rows.append(row) 

        if(found == False):
            return jsonify({'message': 'Task not found'})
        
        with open(database_path, 'w',newline='') as file:
            #creating a writer object
            writer = csv.writer(file)

            #writing the rows to the csv file
            writer.writerows(rows)

    except FileNotFoundError:
        return server_error()
    except Exception as e:
        return exception_handler(e)
        
    return jsonify({'message': 'Task marked as complete'})


#Route for mark as incomplete
@app.route('/mark-task-incomplete/<id>', methods=['PUT'])
def mark_task_incomplete(id):    
    try:
        with open(database_path, 'r') as file:
            #creating a reader object
            reader = csv.reader(file)

            #creating a list to store the rows
            rows = []
            found = False
            #iterating through the rows
            for row in reader:
                #checking if the id is equal to the id of the row
                if id == row[0]:
                    #updating the status of the task
                    row[2] = 0
                    found = True

                #appending the row to the list
                rows.append(row)

        if(found == False):
            return jsonify({'message': 'Task not found'})

        with open(database_path, 'w',newline='') as file:
            #creating a writer object
            writer = csv.writer(file)

            #writing the rows to the csv file
            writer.writerows(rows)
    except FileNotFoundError:
        return server_error()
    except Exception as e:
        return exception_handler(e)
        
    return jsonify({'message': 'Task marked as incomplete'})


if __name__ == '__main__':
    app.run(debug=True)