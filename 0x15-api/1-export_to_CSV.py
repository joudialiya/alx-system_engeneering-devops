#!/usr/bin/python3
'''This module fetch employes data'''
import requests
import sys


def request(emp_id):
    '''helper function'''
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    user = requests.get(BASE_URL + '/users/{:d}'.format(emp_id)).json()
    todos = requests.get(BASE_URL + '/users/{:d}/todos'.format(emp_id)).json()

    with open("{}.csv".format(emp_id), '+w') as file:
        for todo in todos:
            entry = ",".join([
                '\"' + str(user['id']) + '\"',
                '\"' + user['username'] + '\"',
                '\"' + str(todo['completed']) + '\"',
                '\"' + todo['title'] + '\"'
            ])
            file.write(entry + '\n')


if __name__ == "__main__":
    '''entry point'''
    request(int(sys.argv[1]))
