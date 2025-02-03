# -*- coding:utf-8 -*-
import EventApi as Event
import mod.server.extraServerApi as serverApi

class ServerLingmienAether(object):
    def GetLASys(self, ApiKey):
        """获取灵免以太接口系统，后续将废除传统获取接口系统的方式
        :param ApiKey: 密钥
        :return: 接口系统
        """
        ProxySys = serverApi.GetSystem('LingmienAether', 'LingmienAetherProxyServerSystem')
        return ProxySys.GetServerSystemByApiKey(ApiKey) or ServerLingmienAether()

    def AddObjectFunction(self, Manifest):
        # type: (list) -> None
        """给实例添加函数库
        :param Manifest: 函数库清单
        """
        for FunctionName, Function, IsDecorator, DecoratorModule, DecoratorName in Manifest:
            if IsDecorator:  # 如果函数带有装饰器
                Decorator = getattr(Event, DecoratorModule.split('.')[-1])
                DecoratedFunc = Decorator(DecoratorName)(Function.__get__(self))
                setattr(self, FunctionName, DecoratedFunc)
            else:  # 如果函数不带装饰器
                setattr(self, FunctionName, Function.__get__(self))

    def ServerMsg(self, PlayerId, Msg):
        # type: (str, str) -> None
        """发送消息
        :param PlayerId: 玩家id
        :param Msg: 消息内容
        :return: None
        """
        pass

    def PlaySound(self, PlayerId, SoundName, ClearStop=False):
        # type: (str, str, bool) -> None
        """播放音效(全局)
        :param PlayerId: 玩家id
        :param SoundName: 音效名称
        :param ClearStop: 是否清除同名播放音效，防止音效重叠，默认为False
        :return:
        """
        pass

    def PlayUISound(self, PlayerId, SoundName, ClearStop=False):
        # type: (str, str, bool) -> None
        """播放音效(个人)
        :param PlayerId: 玩家id
        :param SoundName: 音效名称
        :param ClearStop: 是否清除同名播放音效，防止音效重叠，默认为False
        :return:
        """
        pass

    def GetAndAttackRadiusEntities(self, AttackId, Radius, IsCanSee, IsAttack=False, Damage=0, BetweenAngle=0.0):
        # type: (str, float, bool, bool, int, float) -> dict
        """获取实体Id周围的实体列表且是否直接执行攻击
        :param AttackId: 攻击者实体Id
        :param Radius: 攻击范围
        :param IsCanSee: 是否需要可视才能攻击
        :param IsAttack: 是否直接执行攻击，默认不执行攻击
        :param Damage: 伤害，默认为0
        :param BetweenAngle: 攻击角度范围，默认为0.0
        :return: 处理完毕后的实体id字典
        """
        pass

    def SummonEntityByName(self, EntityName, EntityPos, EntityRot=(0, 0), DimensionId=0):
        # type: (str, tuple, tuple, int) -> str
        """根据实体名生成实体
        :param EntityName: 实体IdStr名称，例如"minecraft:zombie"
        :param EntityPos: 实体生成的三维坐标
        :param EntityRot: 实体生成的二维朝向默认为(0, 0)
        :param DimensionId: 实体生成的维度，默认为0，即主世界
        :return: 生成的实体Id
        """
        pass

    def SetModRenderAttrByKey(self, EntityId, DataKey, Value):
        # type: (str, str, dict) -> None
        """设置存储于实体数据新的值(仅限于本存档)
        :param EntityId: 实体id
        :param DataKey: 数据Key
        :param Value: 数据值
        """
        pass

    def GetModRenderAttrByKey(self, EntityId, DataKey):
        # type: (str, str) -> dict
        """获取存储于实体数据的值
        :param EntityId: 实体id
        :param DataKey: 数据Key
        """
        pass

    def GetEntityPos(self, EntityId):
        # type: (str) -> tuple
        """获取实体三维坐标
        :param EntityId: 实体id
        :return: 实体三维坐标
        """
        pass

    def GetAttrMaxValue(self, EntityId, AttrKey):
        # type: (str, int) -> float
        """获取实体属性最大值
        :param EntityId: 实体id
        :param AttrKey: 实体属性Key
        :return: 该属性最大值
        """
        pass

    def GetAttrValue(self, EntityId, AttrKey):
        # type: (str, int) -> float
        """获取实体属性当前值
        :param EntityId: 实体id
        :param AttrKey: 实体属性Key
        :return: 该属性当前值
        """
        pass

    def SetAttrValue(self, EntityId, AttrKey, NewValue=None, MaxValue=None):
        # type: (str, int, float, float) -> None
        """修改实体属性当前值或最大值
        :param EntityId: 实体id
        :param AttrKey: 实体属性Key
        :param NewValue: 该属性新的当前值，默认为None，不执行
        :param MaxValue: 该属性新的最大值，默认为None，不执行
        :return: 该属性当前值
        """
        pass

    def InitLingmienAetherMod(self, ModData):
        # type: (dict) -> None
        """[必用]注册灵免以太模组信息
        :param ModData: 模组信息
        """
        pass

    def SetImmuneDamage(self, EntityId, Bool, Timer=None):
        # type: (str, bool, float) -> None
        """设置实体无敌
        :param EntityId: 实体id
        :param Bool: 是否无敌
        :param Timer: 结束无敌时长，默认为None
        """
        pass

    def UseClientApi(self, ApiName, ArgsList, PlayerId=None):
        # type: (str, list, str) -> None
        """使用客户端接口，但无法获得返回值
        :param ApiName: 客户端接口名称
        :param ArgsList: 客户端接口参数列表
        :param PlayerId: 指定客户端玩家Id，默认为None，则广播所有客户端使用该接口
        :return: None
        """
        pass

    def GetOneBlockMaxPos(self, PosX, PosZ, DimensionId=0, Times=8):
        # type: (float, float, int, int) -> tuple
        """根据XZ来获取顶部方块坐标
        :param PosX: X坐标
        :param PosZ: Z坐标
        :param DimensionId: 实体生成的维度，默认为0，即主世界
        :param Times: 计算次数，即精细程度，默认为8，精度为1.2格
        :return: 顶部方块坐标
        """
        pass

    def CheckChunkAndSummonEntity(self, Pos, EntityStr, SummonMobPosList=[]):
        # type: (tuple, str, list) -> bool
        """检测区块是否加载并生成实体，区块未加载则无法生成生物，因此需要使用SummonMobPosList
        :param Pos: 需要生成实体的三维坐标
        :param EntityStr: 实体id名称，如"minecraft:zombie"
        :param SummonMobPosList: 生成实体坐标列表，用于防止重复生成生物。如果坐标在此列表内，则不生成，默认为[]
        :return: 是否生成成功
        """
        pass

    def GetRecentlyTargetId(self, EntityId, Radius):
        # type: (str, int) -> str
        """获取某实体(客户端为本玩家)最近的实体Id
        :param EntityId: 实体Id
        :param Radius: 检索距离
        :return: 最近的实体Id，没有则返回None
        """
        pass

    def GetBlockDictByPos(self, BlockPos, DimensionId=0):
        # type: (tuple, int) -> dict
        """根据坐标获取方块数据
        :param BlockPos: 方块三维坐标
        :param DimensionId: 方块所在的维度，默认为0，即主世界
        :return: 方块数据
        """
        pass

    def CheckAndSetBlockByPos(self, BlockPos, BlockName, BlockAux=0, DimensionId=0, Type=0, IsLegacy=True, UpdateNeighbors=False, SetBlockPosList=[]):
        # type: (tuple, str, int, int, int, bool, bool, list) -> bool
        """根据坐标放置方块，区块未加载则无法放置方块，因此需要使用SetBlockPosList
        :param BlockPos: 方块三维坐标
        :param BlockName: 方块id，例如"minecraft:diamond_block"
        :param BlockAux: 方块特殊值，默认为0
        :param DimensionId: 方块所在的维度，默认为0，即主世界
        :param Type: 方块防止类型，0：替换，1：销毁，2：保留，默认为0
        :param IsLegacy: 是否设置为传统的aux，建议设置为True，即aux对应的state不随着版本迭代而变化。默认为False
        :param UpdateNeighbors: 是否给相邻的方块触发方块更新 (opens new window)以及BlockNeighborChangedServerEvent事件。默认为True触发。若选择不触发可节省约30%的性能消耗。
        :param SetBlockPosList: 生成方块坐标列表，用于防止重复放置方块。如果坐标在此列表内，则不生成，默认为[]
        :return: 是否防止成功
        """
        pass

    def SetChestReward(self, BlockPos, LootTablePath, DimensionId=0, IsSpilt=True):
        # type: (tuple, str, int, bool) -> bool
        """设置奖励箱内容。

        仅支持未打开过的箱子，若箱子已经打开过，则设置失败。维度需要已经加载。如有玩家在相应维度上，则算维度已加载，若完全没玩家在对应维度上，则维度未加载
        :param BlockPos: 方块三维坐标
        :param LootTablePath: 战利品json文件路径，例如"loot_tables/entities/zombie.json"
        :param DimensionId: 方块所在的维度，默认为0，即主世界
        :param IsSpilt: 是否随机分类堆叠
        :return: 是否设置成功
        """
        pass

    def BindCustomBlockInteractFunction(self, BlockName, FunctionInstance, IsAdd=True):
        # type: (str, any, bool) -> None
        """绑定自定义方块交互事件函数，值得注意的是，键鼠、手柄的交互可以长按将会一直执行事件！
        :param BlockName: 自定义方块id，例如"dfm:fengche"
        :param FunctionInstance: 函数(一个dict参数)，例如self.CreateMsg，不要填写成self.CreateMsg()样式
        :param IsAdd: 是否是添加绑定，默认为True，则为添加类型反之为删除
        :return: 无
        """
        pass

    def GetEntityNameByEntityId(self, EntityId):
        # type: (str) -> str
        """根据实体id获取实体名称
        :param EntityId: 实体id
        :return: 实体名称，如"minecraft:zombie"
        """
        pass

    def BindOnStandOnBlockFunction(self, BlockName, FunctionInstance, IsAdd=True):
        # type: (str, any, bool) -> None
        """绑定实体踩上方块事件函数，触发后会持续Tick执行
        :param BlockName: 自定义方块id，例如"dfm:fengche"
        :param FunctionInstance: 函数(一个dict参数)，例如self.CreateMsg，不要填写成self.CreateMsg()样式
        :param IsAdd: 是否是添加绑定，默认为True，则为添加类型反之为删除
        :return: 无
        """
        pass

    def BindStepOnBlockFunction(self, BlockName, FunctionInstance, IsAdd=True):
        # type: (str, any, bool) -> None
        """绑定实体刚刚踩上方块事件函数
        :param BlockName: 自定义方块id，例如"dfm:fengche"
        :param FunctionInstance: 函数(一个dict参数)，例如self.CreateMsg，不要填写成self.CreateMsg()样式
        :param IsAdd: 是否是添加绑定，默认为True，则为添加类型反之为删除
        :return: 无
        """
        pass

    def SetEntityOnFire(self, EntityId, Timer=0, Damage=0):
        # type: (str, int, int) -> bool
        """获取或设置实体当前着火状态
        :param EntityId: 实体id
        :param Timer: 着火时间，默认为0，则不着火，返回获取实体当前着火状态
        :param Damage: 着火伤害，默认为0，则不着火，返回获取实体当前着火状态
        :return: 实体是否着火
        """
        pass

    def SetPlayerGameMode(self, PlayerId, GameMode=None):
        # type: (str, int) -> int
        """获取或设置玩家游戏模式
        :param PlayerId: 玩家id
        :param GameMode: 游戏模式，默认为None，则不设置，返回当前玩家游戏模式
        :return: 当前玩家游戏模式
        """
        pass

    def GetPlayerName(self, PlayerId):
        # type: (str) -> str
        """获取玩家名称
        :param PlayerId: 玩家id
        :return: 玩家名称
        """
        pass

    def GetEntityChineseName(self, EntityName):
        # type: (str) -> str
        """获取实体中文名称
        :param EntityName: 实体IdStr名称，例如"minecraft:zombie"
        :return: 实体名称
        """
        pass

    def BindPlayerOnHandItemFunction(self, ItemName, FunctionInstance, ButtonText='', IsAdd=True):
        # type: (str, any, str, bool) -> None
        """绑定玩家手持某物品的事件函数，首次需要切换物品后才会触发
        :param ItemName: 物品名称，例如'minecraft:stick'
        :param FunctionInstance: 函数(一个dict参数)，例如self.CreateMsg，不要填写成self.CreateMsg()样式
        :param IsAdd: 是否是添加绑定，默认为True，则为添加类型反之为删除
        :param ButtonText: 按钮文字，默认为''，用按钮点击方式来触发绑定的函数
        :return: 无
        """
        pass

    def GetTwoPosLength(self, FirstPos, TargetPos):
        # type: (tuple, tuple) -> float
        """获取目标坐标与第一坐标之间的距离
        :param FirstPos: 第一三维坐标
        :param TargetPos: 目标三维坐标
        :return: 距离
        """
        pass

    def GetLingmienAetherMod(self):
        # type: () -> dict
        """获取已注册的灵免以太模组数据
        :return: 灵免以太模组数据
        """
        pass

    def GetAllLoadItems(self, Flag=True):
        # type: (bool) -> list
        """获取已经加载的物品id
        :param Flag: True获取所有物品，False仅获取注册到创造栏的物品，默认为True
        :return: 已经加载的物品id列表
        """
        pass

    def CreateLootItem(self, ItemName, ItemPos, Count, ItemAuxValue=0, ShowInHand=True, EnChantData=[], ModEnchantData=[], CustomTips=None, ExtraId=None, UserData={}, Durability=None, DimensionId=0):
        # type: (str, tuple, int, int, bool, list, list, str, str, dict, int, int) -> str
        """生成掉落物
        :param ItemName: 物品名称，例如'minecraft:stick'
        :param ItemPos: 物品生成三维坐标
        :param Count: 物品生成数量
        :param ItemAuxValue: 物品特殊值，默认为0(选填)
        :param ShowInHand: 物品是否可以显示在手上，默认为True(选填)
        :param EnChantData: 物品原版附魔信息list(tuple(EnchantType, int))，默认为[](选填)
        :param ModEnchantData: 物品自定义附魔信息list(tuple(CustomEnchantType, int))，默认为[](选填)
        :param CustomTips: 物品自定义提示信息，默认为None(选填)
        :param ExtraId: 物品自定义标识符，用于保存数据区分物品，默认为None(选填)
        :param UserData: 用户数据，用于区分旗帜物品，默认为{}(选填)
        :param Durability: 物品耐久度，默认为None(选填)
        :param DimensionId: 掉落物生成维度，默认为0，即主世界
        :return: 掉落物实体Id
        """
        pass

    def ExchangePlayerInv(self, PlayerId, FirstInv, SecondInv):
        # type: (str, int, int) -> bool
        """交换玩家背包物品位置
        :param PlayerId: 玩家id
        :param FirstInv: 一号物品槽位
        :param SecondInv: 二号物品槽位
        :return: 是否成功
        """
        pass

    def GetPlayerSelectInv(self, PlayerId):
        # type: (str) -> int
        """获取玩家当前所选择的槽位
        :param PlayerId: 玩家id
        :return: 槽位
        """
        pass

    def GetItemDictByInv(self, PlayerId, Type, TypeInv):
        # type: (str, int, int) -> dict
        """根据背包类型、槽位来获取物品数据信息
        :param PlayerId: 玩家id
        :param Type: 背包类型0:物品栏及背包, 1:副手, 2:主手, 3:盔甲栏
        :param TypeInv: 对应类型的槽位
        :return: 物品数据信息
        """
        pass

    def GetEntitySize(self, EntityId):
        # type: (str) -> tuple
        """获取实体碰撞箱大小
        :param EntityId: 实体id
        :return: 宽、高的二维元组
        """
        pass

    def DeltaDateTime(self, FirstDate, SecondDate):
        # type: (str, str) -> any
        """计算日期差值,FirstDate-SecondDate
        :param FirstDate: 格式为%Y-%m-%d %H:%M:%S
        :param SecondDate: 格式为%Y-%m-%d %H:%M:%S
        :return: 差值(datetime), <type 'datetime.timedelta'>
        """
        pass

    def SplitListByQuantity(self, List, Number):
        # type: (list, int) -> list
        """ 按数量拆分list
        :param List: 需要拆分的List
        :param Number: 拆分结果：几个元素为一个新变量
        :return: 处理完毕之后的list
        """
        pass

    def SortListByNumberMagnitude(self, List, Key, IsPositiveSequence):
        # type: (list, str, bool) -> list
        """ 根据数字排序由Dict元素组成的List--[{}, {}, ...]
        :param List: 需要排序的List
        :param Key: 按List内的哪个Key排序，没有则填None
        :param IsPositiveSequence: 是否为正序
        :return: ResultList(list) 处理完毕之后的list
        """
        pass

    def SortDictByNumberMagnitude(self, Dict, Key, IsPositiveSequence, Num):
        # type: (dict, str, bool, int) -> list
        """ 据数字排序由Dict元素组成的Dict--{'x':{}, 'y':{}, ...}
        :param Dict: 需要排序的Dict
        :param Key: 需要排序的Dict中的Dict的Key
        :param IsPositiveSequence: 是否为正序
        :param Num: 排出多少个
        :return: KeyList
        """
        pass

    def GetPlayerDimension(self, PlayerId):
        # type: (str) -> int
        """获取玩家所在维度
        :param PlayerId: 玩家id
        :return: 维度id
        """
        pass

    def SetPlayerSelectItem(self, PlayerId, NewInv):
        # type: (str, int) -> bool
        """设置玩家选中的物品槽位
        :param PlayerId: 玩家id
        :param NewInv: 新的槽位
        :return: 是否成功
        """
        pass

    def ClearPlayerOnHandItem(self, PlayerId):
        # type: (str) -> bool
        """清除玩家主手物品
        :param PlayerId: 玩家id
        :return: 是否成功
        """
        pass

    def GetPlayerPing(self, PlayerId):
        # type: (str) -> int
        """获取玩家延迟
        :param PlayerId: 玩家id
        :return: 玩家当前延迟(单位:ms)
        """
        pass

    def GetAllItemDict(self, PlayerId, Type):
        # type: (str, int) -> list
        """获取类型所有物品数据
        :param PlayerId: 玩家id
        :param Type: 类型0:背包物品栏，1副手，2主手，3盔甲栏
        :return: 物品信息列表 dictlist
        """
        pass

    def SetIsDisable(self, Type, Bool=None):
        # type: (str, bool) -> bool
        """服务端设置，需要在服务端初始化后直接调用
        :param Type: 设置类型
        :param Bool: 是否启用，默认为None
        :return: 该设置的布尔值
        """
        pass

    def GetPlatForm(self):
        # type: () -> int
        """获取服务端运行环境
        :return: 运行环境 0：Windows平台；1：IOS；2：Android；-1：其他，例如联机大厅，阿波罗等linux服务器
        """
        pass

    # 留意json跟dict的区分，例如json的key一定要是字符串，json没有tuple等
    # 该接口有调用频率限流，同一个组件所有联机大厅房间的请求频率最多为每秒50次。如果请求超过该频率会导致阻塞，请求的相应时间变长。
    # int/float/str
    def SetPlayerDataInLobby(self, PlayerData, PlayerId=None, FunctionInstance=None):
        # type: (dict, str, any) -> None
        """设置联机大厅玩家/服务器存储数据(对应Key进行覆盖)
        :param PlayerId: 玩家id，默认为None，则获取服务器存储数据
        :param PlayerData: 玩家需要存储的数据，可进行部分覆盖
        :param FunctionInstance: 指定CallBack返回函数(一个dict参数)，例如self.CreateMsg，不要填写成self.CreateMsg()，默认为None
        :return: None
        """
        pass

    # 该接口有调用频率限流，同一个组件所有联机大厅房间的请求频率最多为每秒200次。如果请求超过该频率会导致阻塞，请求的相应时间变长。
    # 因此玩家初始化设置的时候会出现伪“回档”现象，需要进行逻辑规避
    def GetPlayerDataInLobby(self, PlayerDataKeyList, PlayerId=None, DataKey='LobbyData', FunctionInstance=None):
        # type: (list, str, str, any) -> dict
        """获取联机大厅玩家/服务器存储数据(可部分获取)，如果返回值为空，可以GetModRenderAttrByKey获取Key为'LobbyData'
        :param PlayerId: 玩家id，默认为None，则获取服务器存储数据
        :param PlayerDataKeyList: 玩家存储的数据Key列表，可部分获取
        :param DataKey: 指定获取返回值GetModRenderAttrByKey接口的Key，默认为'LobbyData'
        :param FunctionInstance: 指定CallBack返回函数(一个dict参数)，例如self.CreateMsg，不要填写成self.CreateMsg()，默认为None
        :return: 根据Key列表的Dict玩家数据
        """
        pass

    def GetPlayerLobbyUID(self, PlayerId):
        # type: (str) -> int
        """获取玩家联机大厅UID
        :param PlayerId: 玩家id
        :return: 玩家联机大厅UID
        """
        pass

    def BindPlayerBuyItemFunction(self, ItemCmd, FunctionInstance):
        # type: (str, any) -> None
        """绑定联机大厅玩家购买商品事件函数，为防止作弊无法解绑
        :param ItemCmd: 商品指令
        :param FunctionInstance: 函数(一个dict参数)，例如self.CreateMsg，不要填写成self.CreateMsg()
        :return: None
        """
        pass

    def GetCustomFeatureRulesPos(self, CustomFeatureRuleId, DimensionId=0):
        # type: (str, int) -> tuple
        """获取特征规则坐标
        :param CustomFeatureRuleId: 自定义特征规则Id
        :param DimensionId: 所在的维度，默认为0，即主世界
        :return: 该特征规则坐标
        """
        pass

    def GetCustomFeatureRulesByPos(self, Pos, OneCustomFeatureRuleId, DimensionId=0):
        # type: (tuple, str, int) -> str
        """根据当前坐标获取离自己最近的多结构自定义特征Id
        :param Pos: 三维坐标
        :param OneCustomFeatureRuleId: 任一多结构自定义特征规则Id Feature_Num_UUID
        :param DimensionId: 所在的维度，默认为0，即主世界
        :return: 该特征规则Id
        """
        pass

    def GetDictExtremeValueKey(self, Dict, Key, FindMax=True):
        # type: (dict, any, bool) -> any
        """获取Dict中指定Key的极值对应的键--{'x':float, 'y':float, ...}
        :param Dict: 需要获取的Dict
        :param Key: 用于比较的目标Key，字典中该Key的值用于比较
        :param FindMax: 是否寻找最大值，默认为True
        :return: 极值对应的键
        """
        pass

    def SetPlayerRender(self, JsonId, PlayerId):
        # type: (str, str) -> None
        """设置玩家自定义渲染，自动广播给所有玩家
        :param PlayerId: 渲染的玩家id
        :param JsonId: 配置组件JsonId
        :return: 无
        """
        pass

    def ResetPlayerRender(self, JsonId, PlayerId):
        # type: (str, str) -> None
        """重置玩家自定义渲染，自动广播给所有玩家
        :param PlayerId: 渲染的玩家id
        :param JsonId: 需要重置的配置组件JsonId
        :return: 无
        """
        pass

    # 也可以进入正式服使用联机大厅后台控制中心获取服务器存储数据Key为CloudLobbyNotice来进行实时调整，需要设置务器数据根Key,默认为ServerStorage，所有的服务器数据将会放在该Key目录下
    # 推荐先给联机大厅后台控制中心添加服务器存储数据Key为CloudLobbyNotice且Title为demo（不会显示在游戏内）的数据来进行存储，方便在游戏内复制粘贴实时调整
    # 类型：
    # Text: 文本，使用$imagepath$添加图片，格式为textures/ui/...
    def RegisterCustomLobbyNotice(self, Title, Icon, Type, Data, StartDate=None, EndDate=None):
        #type: (str, str, str, dict, tuple, tuple) -> None
        """注册自定义联机大厅公告
        :param Title: 公告列表标题
        :param Icon: 图标路径，例如textures/ui/LA/button
        :param Type: 类型，仅限指定类型
        :param Data: 所需参数数据
        :param StartDate: 活动开始时间
        :param EndDate: 活动结束时间
        :return: 无
        """
        pass

    def RegisterCustomLobbyPriceType(self, BindDataKey, Icon, IsCharged=True, IsLobby=True):
        # type: (str, str, bool, bool) -> None
        """[服务端初始化时调用]注册自定义联机大厅货币类型，自动绑定购买指令及发放函数，购买指令为BindDataKey_Num，固定为600,1200,4000,6800,12800,32800,64800档位
        :param BindDataKey: 价格类型名称与绑定存储数据Key
        :param Icon: 货币类型图标路径，例如textures/ui/LA/button
        :param IsCharged: 是否为联机大厅充值货币
        :param IsLobby: 是否为联机大厅数据存储Key
        :return: 无
        """
        pass

    def AddPlayerCoinInLobby(self, PlayerId, CoinKey, AddCoinNum, IsVisible=True):
        # type: (str, str, int, bool) -> None
        """为已注册的货币进行添加或减少
        :param PlayerId: 玩家id
        :param CoinKey: 货币Key
        :param AddCoinNum: 添加的数量(负数为减少)
        :param IsVisible: 是否显示加载界面，默认为True
        :return: None
        """
        pass

    def RegisterCustomLobbyStore(self, Title, Icon, Tag, PriceType, Price, Info, ModName, ServerSystemName, FunctionName, OtherData={}):
        # type: (str, str, str, str, int, str, str, str, str, dict) -> None
        """[服务端初始化时调用]注册自定义联机大厅商品，需要提前注册货币
        :param Title: 商品名称
        :param Icon: 商品图标路径，例如textures/ui/LA/button
        :param Tag: 商品分类标签
        :param PriceType: 价格类型
        :param Price: 价格数量
        :param Info: 富文本商品介绍
        :param ModName: 购买成功后发货触发函数(接受一个参数,会返回PlayerId)所在的模组名称
        :param ServerSystemName: 购买成功后发货触发函数(接受一个参数,会返回PlayerId)所在的服务端名称
        :param FunctionName: 购买成功后发货触发函数(接受一个参数,会返回PlayerId)所在的服务端函数名称
        :param OtherData: 其他数据，用于自定义标记商品数据，如售卖数量、售卖的物品id，注意key不要和之前的参数冲突
        :return: 无
        """
        pass

    def BindPlayerChargedFunctionInLobby(self, FunctionInstance):
        """绑定联机大厅玩家充值后调用的函数
        :param FunctionInstance: 指定CallBack返回函数(一个dict参数)，例如self.CreateMsg，不要填写成self.CreateMsg()
        :return: 无
        """
        pass

    def RegisterCustomLobbyRank(self, BindDataKey, Name, Icon, InfoText='', IsPositiveSequence=False):
        # type: (str, str, str, str, bool) -> None
        """[服务端初始化时调用]注册联机大厅排行榜，使用GetModRenderAttrByKey接口Key为RankListBy{BindDataKey}获取排行榜list数据
        :param BindDataKey: 排行榜绑定的服务器ChargedRank下的数据Key,Value为dictlist，且dict必须包含Value,PlayerUID,PlayerName
        :param Name: 该排行榜显示的名字
        :param InfoText: 该排行榜提示文字信息，默认为''
        :param IsPositiveSequence: 排序是否为正序，默认为False
        :param Icon: 图标路径，例如textures/ui/LA/button
        :return: 无
        """
        pass

    def RegisterOPPlayerUIDInLobby(self, PlayerUID):
        # type: (int) -> None
        """[玩家进入前调用]注册联机大厅管理员UID
        :param PlayerUID: 玩家UID
        :return: 无
        """
        pass

    def RegisterEntityChat(self, EntityName, JsonId):
        # type: (str, str) -> None
        """[服务端初始化时调用]注册实体自定义聊天
        :param EntityName: 实体IdStr名称，例如"minecraft:zombie"
        :param JsonId: 配置组件JsonId
        :return: 无
        """
        pass

    def RegisterEntityAbility(self, EntityName, JsonId):
        # type: (str, str) -> None
        """[服务端初始化时调用]注册自定义功能实体
        :param EntityName: 实体IdStr名称，例如"minecraft:zombie"
        :param JsonId: 配置组件JsonId
        :return: 无
        """
        pass

    def SetItemLayer(self, PlayerId, ItemDict, Level, TextureKey, ExtraData=None):
        # type: (str, dict, int, str, dict) -> dict
        """设置物品层级贴图，仍需要手动将物品数据生成给玩家，因此使用该接口前需要清除传入的ItemDict物品
        :param PlayerId: 玩家id
        :param ItemDict: 物品数据信息
        :param Level: 层级：可选-2，-1，1，2，3
        :param TextureKey: 贴图Key，需要在item_texture.json中注册
        :param ExtraData: 需要给物品携带的数据信息，根据Key进行部分覆盖，默认为None
        :return: 带有自定义物品数据的物品数据信息
        """
        pass

    def RemovePlayerItemByInvPos(self, PlayerId, InvType, InvPos):
        # type: (str, int, int) -> None
        """根据背包槽位删除玩家物品
        :param PlayerId: 玩家id
        :param InvType: 背包类型(0:背包物品栏, 1:副手, 2:主手, 3:盔甲栏)
        :param InvPos: 槽位坐标
        :return: 无
        """
        pass

    def SetPlayerItemByInvPos(self, PlayerId, InvType, InvPos, ItemDict):
        # type: (str, int, int, dict) -> None
        """根据背包槽位设置玩家物品，会覆盖原有位置物品
        :param PlayerId: 玩家id
        :param InvType: 背包类型(0:背包物品栏, 1:副手, 2:主手, 3:盔甲栏)
        :param InvPos: 槽位坐标
        :param ItemDict: 物品数据信息
        :return: 无
        """
        pass