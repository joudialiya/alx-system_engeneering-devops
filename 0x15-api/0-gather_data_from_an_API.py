#!/usr/bin/python3

'''This module fetch employes data'''


import requests
import sys



def request(emp_id):
    '''helper function'''
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    user = requests.get(BASE_URL + '/users/{:d}'.format(emp_id)).json()
    todos = requests.get(BASE_URL + '/users/{:d}/todos'.format(emp_id)).json()
    completed_todos = [todo for todo in todos if todo['completed']]

    print("Employee {} is done with".format(user['name']), end=' ')
    print('tasks({}/{}):'.format(len(completed_todos), len(todos)))
    [print('\t {}'.format(todo['title'])) for todo in completed_todos]


if __name__ == "__main__":
    '''entry point'''
    request(int(sys.argv[1]))
