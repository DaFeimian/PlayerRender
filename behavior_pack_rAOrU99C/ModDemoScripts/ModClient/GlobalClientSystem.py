# -*- coding:utf-8 -*-
import mod.client.extraClientApi as clientApi
import logging
from ClientEventList import EventList
import ModDemoScripts.ModCommon.config as config
import EventApi as Event
from ClientLingmienAether import ClientLingmienAether

ClientSystem = clientApi.GetClientSystemCls()
playerId = clientApi.GetLocalPlayerId()
levelId = clientApi.GetLevelId()
compFactory = clientApi.GetEngineCompFactory()
compTimer = compFactory.CreateGame(levelId)

class DemoClientSystem(ClientSystem, ClientLingmienAether):

    def __init__(self, namespace, systemName):
        super(DemoClientSystem, self).__init__(namespace, systemName)
        print "================GlobalClientSystemInit================"
        for Event in EventList:
            try:
                Func = getattr(self, Event['EventFunc'])
            except:
                logging.debug('EventApi ListenEvent')
                Func = Event['EventFunc']
            logging.debug("ClientListenEvent: {0}   {1}".format(Event["EventType"], Event["EventName"]))
            if Event["EventType"] == "Client":
                self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), Event["EventName"], self, Func)
            else:
                self.ListenForEvent(config.ModName, config.ServerSystemName, Event["EventName"], self, Func)
        self.LA = self.GetLASys('')

    def Timer(self):
        pass

    @Event.ClientEvent('ClientShapedRecipeTriggeredEvent')
    def PlayerStart(self, *args):
        # 在玩家合成物品后渲染为镜流
        self.LA.Msg('玩家{0}开始游戏变身'.format(self.LA.GetPlayerName()))
        self.LA.SetPlayerRender('jingliu', playerId)
