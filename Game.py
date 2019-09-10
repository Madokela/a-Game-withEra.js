import erajs.api as a 
import logic.logic as t 
version = '0.0.0a'
def cover():
    a.title('测试用狐狸程序 v{} with Era.js v{}'.format(version, a.version))
    a.page()
    a.h("测试用狐狸程序 v{}".format(version))
    a.t(" withEra.js v{}".format(a.version))
    a.t()
    a.divider()
    a.t()
    a.b('开始游戏',a.goto,t.initiate)
a.init()
a.goto(cover)