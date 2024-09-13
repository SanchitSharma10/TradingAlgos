import json
import time
from datetime import datetime, timedelta
from termcolor import cprint
import random


#function for loading task

def load_task():
    with open('C:/Users/sanch/Desktop/AlgoProductivity/tasks.json', 'r') as f:
        tasks = json.load(f)
    return tasks

def get_taks_schedule(tasks):
    task_start_time = datetime.now()
    schedule = []
    for task, minutes in tasks.items():
        end_time = task_start_time + timedelta(minutes=minutes)
        schedule.append((task, task_start_time, end_time))
        task_start_time = end_time 
    return schedule 


def main():
    #call function
    tasks = load_task()
    schedule = get_taks_schedule(tasks)
    current_index = 0 # track index

    while True:
        now = datetime.now()
        current_task, start_time, end_time = schedule[current_index]
        remaining_time = end_time - now
        remaining_minutes = int(remaining_time.total_seconds() // 60)

        print('')

        for index, (task, s_time, e_time) in enumerate(schedule):
            if index < current_index:
                # task is 
                print(f'{task}: done: {e_time.strftime("%H:%M")}')
            elif index == current_index:
                #current task
                if remaining_minutes < 2:
                    cprint(f'{task} < 2m left!', 'white', 'on_red', attrs=['blink'])
                elif remaining_minutes < 5:
                    cprint(f'{task} - {remaining_minutes} mins', 'white', 'on_red')
                else:
                    cprint(f'{task} - {remaining_minutes} mins', 'white', 'on_blue')
            else:
                print(f'{task} @ {s_time.strftime("%H:%M")}')

        list_of_reminders = [
            "I have a 1000 percent algo",
            "time is irrelevant, keep swimin",
            "every day improve",
            "gonna makes me a robot",
        ]
        random_reminder = random.choice(list_of_reminders)
        print('✨' + random_reminder)
        if now >= end_time:
            current_index += 1
            if current_index >= len(schedule):
                cprint("all tasks are completed","white", 'on_green')
                break
        time.sleep(15)

main()
        

