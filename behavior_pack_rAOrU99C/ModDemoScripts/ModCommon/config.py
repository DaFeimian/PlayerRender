# -*- coding: utf-8 -*-

ModName = "Demo"
AuthorName = "Mod"
ScriptsName = AuthorName + ModName + "Scripts"

Version = [1, 0, 0]

ModVersion = "{0}.{1}.{2}".format(Version[0], Version[1], Version[2])

ServerSystemName = ModName + "ServerSystem"
ServerSystemPath = ScriptsName + ".ModServer" + ".GlobalServerSystem.{0}ServerSystem".format(ModName)

ClientSystemName = ModName + "ClientSystem"
ClientSystemPath = ScriptsName + ".ModClient" + ".GlobalClientSystem.{0}ClientSystem".format(ModName)
