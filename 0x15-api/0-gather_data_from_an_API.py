#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys

def api_data():
    url = 'https://jsonplaceholder.typicode.com/todos'
    tots_task = 0
    task_comp = 0
    tasks = []

    if len(sys.argv) < 2:
        print("Enusre passing user_id")
        sys.exit()

    user_id = int(sys.argv[1])
    data = requests.get(url)
    j_data = data.json()
    #print(j_data)

    for dic in j_data:
        #print(dic)
        if int(dic['userId']) == user_id:
            tots_task += 1
            if dic['completed']:
                tasks.append(dic['title'])
                task_comp += 1
        else:
            print("User id not found...")
            sys.exit()

    print("Employee Patricia is done with tasks({}/{}):".format(task_comp, tots_task))
    for task in tasks:
        print("\t {}".format(task))

    #print(data.json())

if __name__ == '__main__':
    api_data()
    

