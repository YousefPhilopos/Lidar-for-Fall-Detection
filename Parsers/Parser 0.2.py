import urllib.request
import time


def Average(lst):
    return sum(lst) / len(lst)

while True:
    with urllib.request.urlopen('http://10.0.0.212:8000/') as response:
        html = response.read()
        text = html.decode('utf-8')
        start = text.find('<h3><a href="/new">Add New Task</a></h3>') + len('<h3><a href="/new">Add New Task</a></h3>')
        end = text.find('</body></html>', start)
        tasks = text[start:end].strip().split('</br>')
        ip_54_tasks = []
        ip_231_tasks = []
        for task in tasks:
            if ' (10.0.0.231)' in task:
                ip_54_tasks.append(task)
            elif '(192.168.4.46)' in task:
                ip_231_tasks.append(task)
        print("Tasks from 10.0.0.231:")
        print(ip_54_tasks)
        #av = Average(ip_54_tasks)
        #print(av)
        print("Tasks from 192.168.4.46:")
        print(ip_231_tasks)
    time.sleep(0.05)

    
