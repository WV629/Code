#-*- coding:utf-8 -*-
import frida
import sys


rdev = frida.get_remote_device()
# hook app的包名
session = rdev.attach("油联合伙人")
src = '''
Java.perform(function() {
        // 包名 + 类名
        var interceptors = Java.use("com.yltx.oil.partner.utils.Md5")

        // 类名点函数名，hook代码
        interceptors.md5.implementation = function (str) {
            console.log('加密前'+str)

            // 执行原来的代码，传入对应的参数
            var res = this.md5(str)
            console.log('加密后'+res)
        }
    }
)
'''
script = session.create_script(src)

# def on_messege(message, data):
#     print(message,data)
#
# script.on("messege",on_messege)
script.load()
sys.stdin.read()