# -*- coding:utf-8 -*-

from ServerEventList import EventList

def ClientEvent(EventName):
    # type: (str) -> any
    """监听客户端事件，若为服务端调用，则默认监听客户端NotifyToServer事件
    :param EventName: 事件名称
    """
    def Run(Func):
        EventDict = {
            "EventName": EventName,
            "EventType": "Client",
            "EventFunc": Func
        }
        # 说明是第一次要注册，啊不对，我的世界里这种双端，只会调用一次装饰器，如果用其他方式调用执行这个函数，则不会走装饰器
        if EventDict not in EventList:
            EventList.append(EventDict)
        # 说明是其他函数调用
        else:
            print EventName, Func
        return Func
    return Run

def ServerEvent(EventName):
    # type: (str) -> any
    """监听服务端事件，若为客户端调用，则默认监听服务端NotifyToClient等事件
    :param EventName: 事件名称
    """
    def Run(Func):
        EventDict = {
            "EventName": EventName,
            "EventType": "Server",
            "EventFunc": Func
        }
        EventList.append(EventDict)
        return Func
    return Run

def AIEvent(EventName):
    # type: (str) -> any
    """监听魔法指令
    :param EventName: 事件名称
    """
    def Run(Func):
        global func
        EventDict = {
            "EventName": EventName,
            "EventType": "AI",
            "EventFunc": Func
        }
        EventList.append(EventDict)
        return Func
    return Run