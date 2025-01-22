import os
import subprocess

current_directory = os.getcwd()
print('当前目录', current_directory)

items = os.listdir(current_directory)
print('当前目录全部文件', items)

items = [item for item in items if item.endswith('.deb')]
print('当前目录deb文件', items)

queue = []
while True:
    for item in items:
        result = subprocess.run(
            ['sudo', 'dpkg', '-i', item], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            print(item, '安装成功')
        else:
            queue.append(item)

    if len(queue) > 0:
        items = queue
        queue = []
    else:
        break

print('安装完成')
