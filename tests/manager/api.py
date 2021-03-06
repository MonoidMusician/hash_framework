#!/usr/bin/env python3

import hash_framework as hf
import requests
import time

api = 'http://localhost:8000'

def tc_api_create_task():
    r = requests.post(api + '/tasks/', json=[{'name': 'test-1', 'algo': 'md4'}, {'name': 'test-2', 'algo': 'md5'}])
    assert(r.status_code == 200)

    return True


def tc_api_create_host():
    r = requests.post(api + '/hosts/', json={'ip': '127.0.0.1', 'hostname': 'localhost', 'cores': 4, 'memory': 16288468, 'disk': 419343296, 'version': 'faa6a5d87eb63465d0628ac8f264e478aedc5352', 'in_use': True})
    assert(r.status_code == 200)

    return True

def tc_api_assign_benchmark():
    count=20000
    task_id = 1

    data = []
    for i in range(0, count):
        obj = {
            'task': task_id,
            'kernel': 'benchmark',
            'algo': 'md4',
            'args': str(i),
            'result_table': 'results'
        }
        data.append(obj)

    print(len(data))

    t1 = time.time()
    r = requests.post(api + '/task/' + str(task_id) + '/jobs/', json=data)
    print(r.status_code)
    t2 = time.time()

    print(t2 - t1)

    return True

def __main__():
    #tests = [tc_api_create_task, tc_api_create_host]
    tests = [tc_api_assign_benchmark]

    for test in tests:
        ret = test()
        if ret:
            print(test.__name__ + "... OK")
        else:
            print(test.__name__ + "... Failed")
            break

if __name__ == "__main__":
    __main__()
