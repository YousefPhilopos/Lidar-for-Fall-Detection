import urllib.request

with urllib.request.urlopen('http://10.0.0.212:8000/') as response:
    html = response.read()
    text = html.decode('utf-8')
    start = text.find('<h3><a href="/new">Add New Task</a></h3>') + len('<h3><a href="/new">Add New Task</a></h3>')
    end = text.find('</body></html>', start)
    tasks = text[start:end].strip().split('</br>')
    ip_54_tasks = []
    ip_231_tasks = []
    for task in tasks:
        if '(10.0.0.54)' in task:
            ip_54_tasks.append(task)
        elif '(10.0.0.231)' in task:
            ip_231_tasks.append(task)
    print("Tasks from 10.0.0.54:")
    print(ip_54_tasks)
    print("Tasks from 10.0.0.231:")
    print(ip_231_tasks)
