#!/usr/bin/python3
'''This module fetch employes data and export them as json'''
import json
import requests
import sys


def request():
    '''helper function'''
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    FILE_NAME = 'todo_all_employees.json'
    users = requests.get(BASE_URL + '/users').json()

    with open("{}.json".format(FILE_NAME), '+w') as file:
        global_dic = {}
        for user in users:
            todos = requests.get(
                BASE_URL +
                '/users/{}/todos'.format(user['id'])).json()
            todo_dic = [{
                'username': user['username'],
                'task': todo['title'],
                'completed': todo['completed'],
            } for todo in todos]
            global_dic['{}'.format(user['id'])] = todo_dic
        json.dump(global_dic, fp=file)


if __name__ == "__main__":
    '''entry point'''
    request()
