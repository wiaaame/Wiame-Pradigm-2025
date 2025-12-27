import json
import sys
from field import field
from gen_random import gen_random
from unique import Unique
from sort import sort
from print_result import print_result
from cm_timer import cm_timer_1
import random

from typing import List, Dict, Any

with open("data.json", 'r', encoding='utf-8') as file:
    json_data = json.load(file)


def unique(data):
    unique_data = set()
    for dct in data:
        job = dct.get("job-name")
        if job and job not in unique_data:
            yield job
            unique_data.add(job)

def get_jobs(data: List[Dict]) -> List:
    return list(unique(data))

def unique_reverse_sort(data: List):
    res = sorted(data, key = lambda s: s.lower(), reverse=True)
    return res

def get_all_programmists(data: List):
    return list(filter(lambda s: "программист" in s.lower(), data))

def add_python_expirience(data):
    return list(map(lambda job: job + " с опытом Python", data))

def add_salary(data):
    return list(zip(data, [random.randint(100_000, 200_000) for sal in range(len(data))]))

def executor(data : Any, actions: List[callable]):
    res = data
    for a in actions:
        res = a(res)
    return res

print("\nЗадание 7")

if __name__ == "__main__":
    action = [
        get_jobs,
        unique_reverse_sort,
        get_all_programmists,
        add_python_expirience,
        add_salary]
    print('\n'.join(f'{i[0]}, {i[1]}' for i in executor(json_data, action)))
