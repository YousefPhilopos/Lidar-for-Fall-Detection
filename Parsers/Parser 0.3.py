import urllib.request
import time

def Average(lst):
    return sum(lst) / len(lst)

while True:
    with urllib.request.urlopen('http://192.168.4.36:8000/') as response:
        html = response.read()
        text = html.decode('utf-8')
        start = text.find('<h3><a href="/new">Add New Task</a></h3>') + len('<h3><a href="/new">Add New Task</a></h3>')
        end = text.find('</body></html>', start)
        tasks = text[start:end].strip().split('</br>')
        ip_54_tasks = []
        ip_231_tasks = []
        for task in tasks:
            if ' (192.168.4.46)' in task:
                ip_54_tasks.append(task)
            elif '(192.168.4.46)' in task:
                ip_231_tasks.append(task)
        #print("Tasks from 10.0.0.231:")
        #print(ip_54_tasks)
        
        cm_data_points = []
        for task in ip_54_tasks:
            if ' cm / ' in task:
                cm_end = task.index(' cm / ')
                cm_data_point = task[0:cm_end]
                cm_data_point = int(float(cm_data_point))
                cm_data_points.append(cm_data_point)
        #print("Centimeter data points from 10.0.0.231:")
        base = 250
        if Average(cm_data_points) < 200:
            print("Detected")
            
        #print(cm_data_points)

        #print("Tasks from 192.168.4.46:")
        #print(ip_231_tasks)
    time.sleep(0.05)
