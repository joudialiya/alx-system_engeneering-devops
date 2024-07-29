#!/usr/bin/python3
'''This module fetch employes data'''
import json
import requests
import sys


def request(emp_id):
    '''helper function'''
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    user = requests.get(BASE_URL + '/users/{:d}'.format(emp_id)).json()
    todos = requests.get(BASE_URL + '/users/{:d}/todos'.format(emp_id)).json()
    todo_dic = [{
        'task': todo['title'],
        'completed': todo['completed'],
        'username': user['username']
    } for todo in todos]
    with open("{}.json".format(emp_id), '+w') as file:
        json.dump({'{}'.format(emp_id): todo_dic}, fp=file)


if __name__ == "__main__":
    '''entry point'''
    request(int(sys.argv[1]))
