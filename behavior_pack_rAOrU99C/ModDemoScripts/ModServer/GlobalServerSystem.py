# -*- coding:utf-8 -*-
import logging
import mod.server.extraServerApi as serverApi
from ServerEventList import EventList
import ModDemoScripts.ModCommon.config as config
import EventApi as Event
from ServerLingmienAether import ServerLingmienAether

compFactory = serverApi.GetEngineCompFactory()
ServerSystem = serverApi.GetServerSystemCls()
levelId = serverApi.GetLevelId()
compTimer = serverApi.GetEngineCompFactory().CreateGame(levelId)
compCmd = serverApi.GetEngineCompFactory().CreateCommand(levelId)

class DemoServerSystem(ServerSystem, ServerLingmienAether):

    def __init__(self, namespace, systemName):
        super(DemoServerSystem, self).__init__(namespace, systemName)
        print '================GlobalServerSystemInit================'
        for Event in EventList:
            try:
                Func = getattr(self, Event['EventFunc'])
            except:
                logging.debug('EventApi ListenEvent')
                Func = Event['EventFunc']
            logging.debug('ServerListenEvent: {0}   {1}'.format(Event['EventType'], Event['EventName']))
            if Event['EventType'] == 'Server':
                self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), Event['EventName'], self, Func)
            elif Event['EventType'] == 'Client':
                self.ListenForEvent(config.ModName, config.ClientSystemName, Event['EventName'], self, Func)
            else:
                self.ListenForEvent("Minecraft", "aiCommand", Event["EventName"], self, Func)
        self.LA = self.GetLASys('')


    def Timer(self):
        pass

