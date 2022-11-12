#-*- coding:utf-8 -*-
import frida


rdev = frida.get_remote_device()

# 获取所有进程的包名
processes = rdev.enumerate_processes()
for process in processes:
    print(process)

# 获取前台运行的app包名
front_app = rdev.get_frontmost_application()
print(front_app)