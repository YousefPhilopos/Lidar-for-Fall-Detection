import urllib.request

with urllib.request.urlopen('http://10.0.0.212:8000/') as response:
    html = response.read()
    text = html.decode('utf-8')
    start = text.find('<h3><a href="/new">Add New Task</a></h3>') + len('<h3><a href="/new">Add New Task</a></h3>')
    end = text.find('</body></html>', start)
    tasks = text[start:end].strip().replace('</br>', ', ')
    print(tasks)
