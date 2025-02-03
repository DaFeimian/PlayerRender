# -*- coding: utf-8 -*-
from mod.common.mod import Mod
import mod.server.extraServerApi as ServerApi
import mod.client.extraClientApi as ClientApi
from ModCommon import config

@Mod.Binding(name=config.ModName, version=config.ModVersion)
class ModDemo(object):
    def __init__(self):
        pass

    @Mod.InitServer()
    def ModServerInit(self):
        ServerApi.RegisterSystem(config.ModName, config.ServerSystemName, config.ServerSystemPath)

    @Mod.DestroyServer()
    def ModServerDestroy(self):
        pass

    @Mod.InitClient()
    def ModClientInit(self):
        ClientApi.RegisterSystem(config.ModName, config.ClientSystemName, config.ClientSystemPath)

    @Mod.DestroyClient()
    def ModClientDestroy(self):
        pass
