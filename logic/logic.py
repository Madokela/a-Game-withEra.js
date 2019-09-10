import erajs.api as a  # 虽然在logic包里面，但也可以用这个语句来调用API哟！

def g_save():
    # 保存游戏界面
    a.page()
    a.h('保存游戏')
    a.t()
    a.show_save_to_save()  # 显示当前存档以供保存
    a.b('返回', a.back)


def g_load():
    a.page()
    a.h('读取游戏')
    a.t()
    a.show_save_to_load(g_main)  # 显示当前存档以供加载（参数为加载之后进入哪个界面（最好是根界面））
    a.b('返回', a.back)



def initiate():
    a.page()
    a.h('开始游戏')
    a.t()
    a.divider()
    a.b('开始新游戏',a.goto,g_story)
    a.b('读取存档',a.goto,g_load)
    a.b('透出游戏', a.exit)


def g_main():
    a.page()
    a.h('主菜单')
    a.data['db']['pos'] = '嗨森林'
    a.shake(100)
    a.t()
    a.t('当前位置 {}'.format(a.data['db']['pos']))
    a.t()
    a.t('现在主菜单里什么都没有，你只能：')
    a.b('保存游戏',a.goto,g_save)
    a.t('或者')
    a.b('读取游戏',a.goto,g_load)
    a.divider()
    a.t()
    a.t('也可以干脆的')
    a.b('透出游戏', a.exit)



def g_story():
    a.page()
    a.t()
    a.t('首先，欢迎你来到，我的世界',True)
    a.t()
    a.t('我的世界？',True)
    a.t('开什么玩笑',True)
    a.t(' 这里是狐狸的世界',True)
    a.t()
    a.t('今年下半年或者明年上半年',True)
    a.t()
    a.t('中美合拍的......',True)
    a.t('闭嘴，该死的家伙',True)
    a.t()
    a.t('现在什么都没有你要让玩家玩什么？',True)
    a.t()
    a.t('总会有的啦~',True)
    a.t()
    a.t('那么~ 开始实验吧',True)
    a.b('进入主菜单',a.goto,g_main)