# -*- coding:utf-8 -*-
import EventApi as Event
import mod.client.extraClientApi as clientApi

playerId = clientApi.GetLocalPlayerId()

class ClientLingmienAether(object):
    def GetLASys(self, ApiKey):
        """获取灵免以太接口系统，后续将废除传统获取接口系统的方式
        :param ApiKey: 密钥
        :return: 接口系统
        """
        ProxySys = clientApi.GetSystem('LingmienAether', 'LingmienAetherProxyClientSystem')
        return ProxySys.GetClientSystemByApiKey(ApiKey) or ClientLingmienAether()

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

    def QueryGet(self, QueryName):
        # type: (str) -> float
        """获取自定义Molang函数的值
        :param QueryName: 函数名，自动补全为query.mod.QueryName
        """
        pass

    def QueryMolangGet(self, QueryName):
        # type: (str) -> float
        """获取原版Molang函数的值
        :param QueryName: 函数名，自动补全为query.QueryName
        """
        pass

    def QuerySet(self, QueryName, Value):
        # type: (str, float) -> float
        """设置自定义Molang函数的值
        :param QueryName: 函数名，自动补全为query.mod.QueryName
        :param Value: 对应函数的值
        """
        pass

    def Msg(self, Msg):
        # type: (str) -> float
        """发送消息
        :param Msg: 消息内容
        """
        pass

    def ModelAnimationControllerInit(self, dfmJsonDict):
        # type: (dict) -> list
        """骨骼模型动画控制器系统初始化，目前一个骨骼模型只支持一个动画控制器和单个动画. 但是很卡很烂！！！！
        \n将会使用自定义Attr存储于玩家身上，key为ModelAnimationController
        \n服务端需要有名为ModelAnimationControllerInitEvent的监听客户端事件
        \n将传参args中的PLayerId AttrValue 以key为ModelAnimationController存入
        :param dfmJsonDict: jsondict
        :return: 返回初始动画名
        """
        pass

    def ModelAnimationControllerTick(self, *args):
        """骨骼模型动画控制器逻辑运行，需要Tick化，当动画存在translation变化的时候，才会进行广播通信
        \n服务端需要有名为ModelAnimationControllerTranslateStateEvent的监听客户端事件用于修改Attr和广播
        \n事件参数：PlayerId，ModAttrKey，NewState，StateDict
        \n根据PlayerId， ModAttrKey修改NewState和StateDict为Key的值
        """
        pass

    def ModelAnimationControllerTranslateState(self, PlayerId):
        # type: (str) -> None
        """骨骼模型动画控制器转化新状态并播放动画等, 需要进行服务端广播后客户端接收调用
        :param PlayerId: 玩家id
        """
        pass

    def GetModelAnimationControllerStateDictByStateName(self, StateName, StateList):
        # type: (str, list) -> dict
        """获取骨骼模型动画控制器的状态dict
        :param StateName: 状态名称
        :param StateList: 状态dict列表
        :return: 返回该状态dict
        """
        pass

    def PlayModelAnimation(self, PlayerId, AnimationName):
        # type: (str, str) -> None
        """播放骨骼模型动画
        :param PlayerId: 玩家id
        :param AnimationName: 动画名称
        """
        pass

    def GetModelAnimationControllerStateTransitionResult(self, DictList):
        # type: (list) -> dict
        """获取骨骼模型动画控制器状态转化结果dict，目前只适合简单的动画控制器，不能使用简写，必须使用标准表达式
        :param DictList: 动画控制器transitions的dictlist条件
        :return: 返回所有条件结果dict。for state, result in results.items():
        """
        pass

    def EvaluateMolangExpression(self, expression):
        # type: (str) -> bool
        """获取骨骼模型动画控制器状态的条件转化结果
        :param expression: 动画控制器transitions的每一个key的value，也就是转化条件
        :return: 该条件结果
        """
        pass

    def GetRecentlyTargetId(self, Radius):
        # type: (int) -> str
        """获取某实体(客户端为本玩家)最近的实体Id
        :param Radius: 检索距离
        :return: 实体id
        """
        pass

    def CreateDefaultUI(self, ModName, UiName, ScriptsName, AllValue):
        # type: (str, str, str, bool) -> bool
        """常规UI注册并创建
        :param ModName: 模组名称
        :param UiName: UI界面名称
        :param ScriptsName: 脚本文件夹名称
        :param AllValue: '/all'界面的value
        :return: 是否成功
        """
        pass

    def CreateUIByEntity(self, ModName, UiName, EntityId, Scale, Offset):
        # type: (str, str, str, int, tuple) -> object
        """常规实体UI创建，需要使用RegisterUI注册UI才能创建
        :param ModName: 模组名称
        :param UiName: Ui界面名称
        :param EntityId: 绑定实体
        :param Scale: 值为( 0 / 1 ) ，意为绑定实体的UI是否会自动根据实体与本地玩家的距离动态缩放大小，默认值为1，即会动态缩放头顶UI的大小。
        :param Offset: xyz偏移
        :return: 该实体UI实例，注意：GetUIObject无法获取实体UI类型
        """
        pass

    def RegisterUI(self, ModName, UiName, ScriptsName):
        # type: (str, str, str) -> None
        """注册UI，不要重复注册损耗性能！
        :param ModName: 模组名称
        :param UiName: Ui界面名称
        :param ScriptsName: 脚本文件夹名称
        :return:
        """
        pass

    def QueryInit(self, PlayerId, QueryName, InitValue):
        # type: (str, str, float) -> None
        """自定义Molang注册并创建，需要在客户端事件'OnLocalPlayerStopLoading'下使用
        :param PlayerId: 玩家id
        :param QueryName: 函数名称，会自动补全为query.mod.xxx
        :param InitValue: 函数初始数值
        :return None
        """
        pass

    def CameraMotionRun(self, FloatingCoefficient, ResetCoefficient, MotionLimit, LinearCoefficient, AppressLimit, FloatingSppedLimit):
        # type: (float, float, float, float, float, float) -> tuple
        """普通视角摇晃运行，使用客户端Tick直接调用
        :param FloatingCoefficient: 浮动系数，系数越大，晃动幅度越小
        :param ResetCoefficient: 重置系数，系数越大，恢复正常视角越快
        :param MotionLimit: 跟随限度(角度)
        :param LinearCoefficient: 线性系数(0~1)，1表示完全线性，数字越小，晃动幅度越小
        :param AppressLimit: 趋近限度(0~1)，当非线性运动时，趋近限度将限制最小的趋近斜率
        :param FloatingSppedLimit: 速度限度，防止因过快的晃动屏幕而高速度使动画产生撕裂感
        :return: DefaultCameraRot_z, MotionBlurRot_y 正为左 负为右 用于调用自定义Molang,MotionBlurRot_y为动态模糊所用
        """
        pass

    def ResetCameraMotion(self):
        # type: () -> bool
        """ 重置镜头跟随
        :return: 是否设置成功
        """
        pass

    def HighCameraMotionRun(self, FloatingCoefficient, MotionLimit, LinearCoefficient, AppressLimit):
        # type: (float, float, float, float) -> None
        """高处视角摇晃运行，使用客户端Tick直接调用！
        :param FloatingCoefficient: 浮动系数，系数越大，晃动幅度越小
        :param MotionLimit: 跟随限度(角度)
        :param LinearCoefficient: 线性系数(0~1)，1表示完全线性，数字越小，晃动幅度越小
        :param AppressLimit: 趋近限度(0~1)，当非线性运动时，趋近限度将限制最小的趋近斜率
        :return: None
        """
        pass

    def GetDeltaCameraMotion(self, IsAbs):
        # type: (bool) -> tuple
        """获取玩家摄像机运动单位差值(后面这里再给返回的值加其他的参数调整)
        :param IsAbs: 是否返回绝对值
        :return: DeltaRot_x, DeltaRot_y, DeltaRot_z
        """
        pass

    def GetFrictionAllData(self):
        # type: () -> None
        """获取本接口的所有参数
        :return: {
            "MoveTime": MoveTime,
            "StartMove": StartMove,
            "LastMotionData": LastMotionData,
            "PlayerMotion": PlayerMotion
        }
        """
        pass

    def SetPlayerFriction(self, Bool):
        # type: (bool) -> None
        """设置玩家是否有摩擦力
        :param Bool: 是否有摩擦力
        :return: None
        """
        pass

    def FrictionMath(self, IsStartMove):
        # type: (bool) -> None
        """摩擦力计算，过一段时间后(0.01s)，使用AddTimer调用ResetFriction,注意，需要在客户端Tick调用FrictionPlay
        :param IsStartMove: 是否正在移动
        :return: None
        """
        pass

    def FrictionPlay(self):
        # type: () -> None
        """在客户端Tick调用，用于实现摩擦力效果
        :return: None
        """
        pass

    def ResetFriction(self, IsOccupy):
        # type: (bool) -> bool
        """重置摩擦力
        :param IsOccupy: 是否有其他优先级内容占用
        :return: Bool, None 是否需要再次Reset
        """
        pass

    def RealPlaySfx(self, PlayerId, SfxId, FaceCamara, Offset, Rot, Scale, DestroyTimer=None, IsJson=False, IsParticle=False):
        # type: (str, str, bool, tuple, tuple, tuple, float, bool, bool) -> None
        """真正的特效播放，不广播则只能自己看到
        :param PlayerId: 特效绑定的实体Id，现在将不再局限于玩家Id
        :param SfxId: 特效Id
        :param FaceCamara: 是否面向摄像机
        :param Offset: 特效偏移三维相对坐标
        :param Rot: 特效旋转三维坐标
        :param Scale: 特效大小倍数三维坐标
        :param DestroyTimer: 特效销毁时间，默认为None
        :param IsJson: 是否为json预设特效，默认为False
        :param IsParticle: 是否为中国版粒子特效，默认为False
        """
        pass

    def PlaySfxToEveryBody(self, SfxList):
        # type: (list) -> None
        """播放特效(自动广播)
        :param SfxList: dictlist. 特效列表
        特效dict数据示例： {
                            'Id': str,  # 特效Id
                            'EntityId': str # 特效绑定的实体Id
                            'FaceCamara': bool, # 是否面向摄像机
                            'Offset': tuple(float, float, float),    # 特效偏移
                            'Rot': tuple(float, float, float),   # 特效旋转
                            'Scale': tuple(float, float, float),    # 特效大小
                            'DestroyTimerTime': float,     # 特效销毁时间
                            'IsJson': bool,  # 是否为json预设特效
                            'IsParticle': bool    # 是否为中国版粒子特效
                        }
        """
        pass

    def GetLingmienAetherManifest(self):
        # type: () -> list
        """获取灵免以太函数库清单
        :return: 灵免以太函数库清单
        """
        pass

    def UseServerApi(self, ApiName, ArgsList):
        # type: (str, list) -> str
        """使用服务端接口，但无法获得返回值
        :param ApiName: 服务端接口名称
        :param ArgsList: 服务端接口参数列表
        :return: ApiId，用于获取本次返回值
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

    def OpenTips(self, Object, Title, Content, LeftButtonText=None, LeftButton=None, RightButtonText=None, RightButton=None, CloseButton='Left'):
        # type: (object, str, str, str, str, str, str, str) -> None
        """打开提示弹窗
        :param Title: 标题
        :param Content: 内容
        :param LeftButtonText: 左边按钮显示的文字
        :param LeftButton: 左边按钮触发事件所返回的函数名称，默认为None，则不显示按钮
        :param RightButtonText: 右边按钮显示的文字
        :param RightButton: 右边触发事件所返回的函数名称，默认为None，则不显示按钮
        :param CloseButton: 默认关闭按钮，默认为Left，可选Right,None，表示左边的按钮是关闭，无
        :param Object: 触发事件所返回的函数所在的实例，传入示例：clientApi.GetSystem(config.ModName, config.ClientSystemName)
        """
        pass

    def SetPerspective(self, NewPerspective=None):
        # type: (int) -> int
        """获取或设置玩家人称视角
        :param NewPerspective: 设置新的人称，默认为None，则效果为Get
        :return: 返回最新的人称结果
        """
        pass

    def CloseTips(self):
        # type: () -> None
        """关闭提示窗口
        :return: None
        """
        pass

    def GetLingmienAetherUIObject(self):
        # type: () -> object
        """获取灵免以太主界面UI实例
        :return: 返回灵免以太主界面UI实例
        """
        pass

    def GetUIObject(self, ModName, UIName):
        # type: (str, str) -> object
        """获取UI实例
        :param ModName: 模组名称
        :param UIName: UI名称
        :return: 返回对应UI实例
        """
        pass

    def GetIsStart(self):
        # type: () -> bool
        """获取玩家是否处于进入游戏状态(这里指进入灵免以太主界面后是否点击了"单人游戏")
        :return: 玩家是否处于进入游戏状态
        """
        pass

    def SetButtonUpEvent(self, UIObject, ButtonPath, FuncName=None, FuncObject=None, FunctionInstance=None):
        # type: (object, str, str, object, any) -> bool
        """设置按钮弹起回调事件
        :param UIObject: UI实例
        :param ButtonPath: 按钮类型控件路径
        :param FuncName: 回调函数名称，需要有一个参数接收事件返回的dict参数
        :param FuncObject: 回调函数所在的实例，默认为None，则调用UI实例中的函数
        :param FunctionInstance: 用函数实例进行绑定按钮事件
        :return: 是否成功
        """
        pass

    def SetButtonDownEvent(self, UIObject, ButtonPath, FuncName, FuncObject=None, FunctionInstance=None):
        # type: (object, str, str, object, any) -> bool
        """设置按钮按下回调事件
        :param UIObject: UI实例
        :param ButtonPath: 按钮类型控件路径
        :param FuncName: 回调函数名称，需要有一个参数接收事件返回的dict参数
        :param FuncObject: 回调函数所在的实例，默认为None，则调用UI实例中的函数
        :param FunctionInstance: 用函数实例进行绑定按钮事件
        :return: 是否成功
        """
        pass

    def CloseVisibleAndOpenVisible(self, UIObject, ClosedPath, OpenedPath):
        # type: (object, str, str) -> None
        """关闭一个控件显示和显示另一个控件
        :param UIObject: UI实例
        :param ClosedPath: 关闭显示的控件路径
        :param OpenedPath: 开启显示的控件路径
        :return: None
        """
        pass

    def ResetAnimation(self, UIObject, Path):
        # type: (object, str) -> None
        """重制UI动画
        :param UIObject: UI实例
        :param Path: 控件路径
        :return: None
        """
        pass

    def BindKeyPress(self, Key, IsDown, Object=None, FunctionName=None, ScreenName=None, IsAdd=True, FunctionInstance=None):
        # type: (str, bool, object, str, str, bool, any) -> bool
        """ 绑定或取消绑定键盘按键
        :param Key: 绑定的按键编号
        :param IsDown: 是否按下时触发，取消绑定时，该参数无意义
        :param FunctionInstance: 函数(无参数)，例如self.CreateMsg，不要填写成self.CreateMsg()样式，默认为None
        :param Object: [可用，但现已不推荐]该函数所在的客户端实例，取消绑定时，该参数无意义
        :param FunctionName: [可用，但现已不推荐]触发的函数名称(无参数)，取消绑定时，该参数无意义
        :param ScreenName: 只在该界面名称下触发，默认为None，则不根据界面情况执行，取消绑定时，该参数无意义
        :param IsAdd: 是否是添加绑定，默认为True，则为添加类型反之为删除
        :return: 是否成功
        """
        pass

    def ResetAutoCtrl(self, *args):
        """重置到自动控制模式
        :return: 无
        """
        pass

    def GetPlayerCtrl(self):
        # type: () -> int
        """获取玩家的操控模式
        :return: 操作模式(0键鼠,1触控,2手柄)
        """
        pass

    def BindGamepadTriggerPress(self, GamepadTriggerKey, Object=None, FunctionName=None, Type='Down', FunctionInstance=None):
        # type: (int, object, str, str, any) -> None
        """绑定手柄扳机，右扳机将会屏蔽原版攻击逻辑
        :param GamepadTriggerKey: 0: 左扳机, 1: 右扳机
        :param Object: [可用，但现已不推荐]客户端实例，传入None则为取消绑定
        :param FunctionName: [可用，但现已不推荐]触发的函数名称(1参数'Up','Down',表示扳机类型)，传入None则为取消绑定
        :param FunctionInstance: 函数(1参数'Up','Down',表示按键类型)，例如self.CreateMsg，不要填写成self.CreateMsg()样式，默认为None
        :param Type: 绑定类型'Up'扳机抬起，扳机按下'Down'，默认为'Down'，'Up'部分手柄不兼容！
        :return: 无
        """
        pass

    def RunGamepadTriggerPress(self, args):
        pass

    def RunGamepadKeyPress(self, args):
        pass

    def BindGamepadKeyPress(self, GamepadKey, Object=None, FunctionName=None, FunctionInstance=None):
        # type: (int, object, str, any) -> None
        """绑定手柄按键
        :param FunctionInstance: 函数(1参数'Up','Down',表示按键类型)，例如self.CreateMsg，不要填写成self.CreateMsg()样式，默认为None
        :param GamepadKey: 仅支持以下4个，其他的控制存在冲突 2: B, 3: X, 4: Y, 9: LS, 10: RS, 11: LB, 12: RB, 13: VIEW
        :param Object: [可用，但现已不推荐]客户端实例，传入None则为取消绑定
        :param FunctionName: [可用，但现已不推荐]触发的函数名称(1参数'Up','Down',表示按键类型)，传入None则为取消绑定
        :return: None
        """
        pass

    def GetEntityNameByEntityId(self, EntityId):
        # type: (str) -> str
        """根据实体id获取实体名称
        :param EntityId: 实体id
        :return: 实体名称，如"minecraft:zombie"
        """
        pass

    def LocalConfigData(self, Key, Dict=None, IsGlobal=False):
        # type: (str, dict, bool) -> dict
        """存储或获取本地存储数据
        :param Key: 数据的名称，用于区别不同的本地数据
        :param Dict: 数据内容，默认为None则为获取并返回该Key的数据，反之不为None则是存储数据
        :param IsGlobal: 为True时是全局配置，否则为存档配置，默认为False
        :return: 当Dict为None时，返回所存储的数据
        """
        pass

    def BindGameHighTickFunction(self, FunctionInstance, IsAdd=True):
        # type: (any, bool) -> None
        """绑定游戏高Tick函数

        原版MC每秒20Tick，网易MC脚本每秒30Tick，该Tick的基准以玩家当前Fps为准
        :param FunctionInstance: 函数(无参数)，例如self.CreateMsg，不要填写成self.CreateMsg()样式
        :param IsAdd: 是否是添加绑定，默认为True，则为添加类型反之为删除
        :return: 无
        """
        pass

    def ComputePitchYaw(self, MainPos, TargetPos):
        # type: (tuple, tuple) -> tuple
        """根据两个坐标，计算目标坐标相对于主坐标的俯仰角，偏航角
        :param MainPos: 主坐标
        :param TargetPos: 目标坐标
        :return: 俯仰角，偏航角
        """
        pass

    def SLerp(self, Start, End, Factor):
        # type: (float, float, float) -> float
        """角度形非线性计算
        :param Start: 开始角度
        :param End: 结束角度
        :param Factor: 非线性系数
        :return: 线性插值后的结果
        """
        pass

    def Lerp(self, Start, End, Factor):
        # type: (float, float, float) -> float
        """常规非线性计算
        :param Start: 开始数值
        :param End: 结束数值
        :param Factor: 非线性系数
        :return: 线性插值后的结果
        """
        pass

    def CameraLookAtTargetRun(self, TargetPos, SmoothingFactor=0.1, OffsetPitch=0, OffsetYaw=0):
        # type: (tuple, float, float, float) -> None
        """玩家看向目标坐标视角运动器，使用客户端Tick直接调用
        :param TargetPos: 目标三维坐标
        :param SmoothingFactor: 非线性系数
        :param OffsetPitch: 俯仰角偏移角度(选填)
        :param OffsetYaw: 偏航角偏移角度(选填)
        :return: 无
        """
        pass

    def GetPlayerName(self):
        # type: () -> str
        """获取玩家名称
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

    def SetLabelText(self, UIObject, LabelPath, Text=None):
        # type: (object, str, str) -> str
        """获取或设置文本控件文字
        :param UIObject: UI实例
        :param LabelPath: 文本类型控件路径
        :param Text: 需要设置的文字，默认为None，则不设置，返回当前文本控件的文字
        :return: 当前文本控件的文字
        """
        pass

    def SetProgressBarValue(self, UIObject, ProgressPath, Percent):
        # type: (object, str, float) -> None
        """设置进度条控件的比例
        :param UIObject: UI实例
        :param ProgressPath: 进度条类型控件路径
        :param Percent: 需要设置进度条的比例，1为100%
        :return: 无
        """
        pass

    def SetImagePath(self, UIObject, ImagePath, TexturePath):
        # type: (object, str, str) -> None
        """设置图像控件显示的图片路径
        :param UIObject: UI实例
        :param ImagePath: 图像类型控件路径
        :param TexturePath: 需要设置图像所显示的图片路径，例如'textures/ui/LingmienAether'
        :return: 无
        """
        pass

    def SetUIVisible(self, UIObject, ControlPath, IsVisible=None):
        # type: (object, str, str) -> bool
        """获取或设置UI控件的显示
        :param UIObject: UI实例
        :param ControlPath: 控件路径
        :param IsVisible: 是否显示，默认为None，则不设置，返回当前UI控件是否显示
        :return: 当前UI控件是否显示
        """
        pass

    def GetPlayerFps(self):
        # type: () -> float
        """获取玩家当前FPS
        :return: 玩家当前FPS
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

    def GetEntitySize(self, EntityId):
        # type: (str) -> tuple
        """获取实体碰撞箱大小
        :param EntityId:
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

    def GetPlayerDimension(self):
        # type: () -> int
        """获取玩家所在维度
        :return: 维度id
        """
        pass

    def OpenLA(self):
        # type: () -> None
        """模拟打开灵免以太主界面
        :return: 无
        """
        pass

    def GetPlayerPing(self, PlayerId):
        # type: (str) -> int
        """获取玩家延迟
        :param PlayerId: 玩家id
        :return: 玩家当前延迟(单位:ms)
        """
        pass

    def GetAllItemDict(self, Type):
        # type: (int) -> list
        """获取类型所有物品数据
        :param Type: 类型0:背包物品栏，1副手，2主手，3盔甲栏
        :return: 物品信息列表 dictlist
        """
        pass

    def GetItemDictByInv(self, Type, TypeInv):
        # type: (int, int) -> dict
        """根据背包类型、槽位来获取物品数据信息
        :param Type: 背包类型0:物品栏及背包, 1:副手, 2:主手, 3:盔甲栏
        :param TypeInv: 对应类型的槽位
        :return: 物品数据信息
        """
        pass

    def SetItemRender(self, UIObject, ItemRenderPath, ItemName, AuxValue=0):
        # type: (object, str, str, int) -> bool
        """设置物品渲染控件显示的物品内容
        :param UIObject: UI实例
        :param ItemRenderPath: 物品渲染类型控件路径
        :param ItemName: 物品名称，例如'minecraft:stick'
        :param AuxValue: 物品特殊值，默认为0(选填)
        :return: 是否成功
        """
        pass

    def SetImageAndTextColor(self, UIObject, UIPath, Color):
        # type: (object, str, tuple) -> None
        """设置图像控件或文本控件的颜色
        :param UIObject: UI实例
        :param UIPath: 图像控件或文本控件的路径
        :param Color: 颜色RGB(r, g, b)，取值[0, 1]表示各色泽的百分比，及1=255
        :return: 无
        """
        pass

    def GetScrollViewChildPath(self, UIObject, ScrollViewPath):
        # type: (object, str) -> str
        """获取滚动列表控件的子控件路径(无法通过绝对路径获取，只能使用该接口，然后使用相对路径获取其绑定的子控件内容)
        :param UIObject: UI实例
        :param ScrollViewPath: 滚动列表控件类型的路径
        :return: 子控件路径
        """
        pass

    def GetCloneListByDemoPath(self, DemoPath):
        # type: (str) -> list
        """根据复制的UI路径获取该Demo复制后的结果列表
        :param DemoPath: 复制的UI路径
        :return: 复制的ResultName列表
        """
        pass

    def CloneUIControl(self, UIObject, DemoPath, ResultPath, ResultNameList, IsClear=True):
        # type: (object, str, str, list, bool) -> dict
        """复制并粘贴UI到指定路径并指定名字
        :param UIObject: UI实例
        :param DemoPath: 复制的UI路径
        :param ResultNameList: 粘贴后重命名的名字列表(不能重复)
        :param ResultPath: 粘贴的UI路径，会粘贴在该目录下
        :param IsClear: 是否清理之前所Clone的同Demo的内容，默认为True
        :return: 粘贴后的UI路径数据，key为粘贴后重命名的名字
        """
        pass

    def DeleteUIControl(self, UIObject, DeletePath):
        # type: (object, str) -> None
        """删除UI控件
        :param UIObject: UI实例
        :param DeletePath: 删除的UI路径
        :return: 无
        """
        pass

    def SetEditText(self, UIObject, EditPath, Text=None):
        # type: (object, str, str) -> str
        """获取或设置输入框控件文字
        :param UIObject: UI实例
        :param EditPath: 输入框类型控件路径
        :param Text: 需要设置的文字，默认为None，则不设置，返回当前文本控件的文字
        :return: 当前文本控件的文字
        """
        pass

    def BindPlayerStartFunction(self, FunctionInstance, IsAdd=True):
        """绑定玩家点击灵免以太主界面进入游戏后的函数
        :param FunctionInstance: 函数(无参数)，例如self.CreateMsg，不要填写成self.CreateMsg()样式
        :param IsAdd: 是否是添加绑定，默认为True，则为添加类型反之为删除
        :return: 无
        """
        pass

    def GetServerIsDisable(self, Type):
        """获取服务端设置信息
        :param Type: 设置类型
        :return: 该设置的布尔值
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

    def SetPlayerRender(self, JsonId, PlayerId=playerId, IsKeep=False):
        # type: (str, str, bool) -> None
        """设置玩家自定义渲染，自动广播给所有玩家
        :param PlayerId: 渲染的玩家id，默认为该客户端玩家id
        :param JsonId: 配置组件JsonId
        :param IsKeep: 是否保留原版模型
        :return: 无
        """
        pass

    def ResetPlayerRender(self, JsonId, PlayerId=playerId):
        # type: (str, str) -> None
        """重置玩家自定义渲染，自动广播给所有玩家
        :param PlayerId: 渲染的玩家id，默认为该客户端玩家id
        :param JsonId: 需要重置的配置组件JsonId
        :return: 无
        """
        pass

    def RegisterLobbyMenuButton(self, Icon, FunctionInstance, IsMust=False):
        # type: (str, any, bool) -> None
        """注册自定义联机大厅菜单按钮
        :param Icon: 图标路径，例如textures/ui/LA/button
        :param FunctionInstance: 该按钮按下触发的函数(一个dict参数)，例如self.CreateMsg，不要填写成self.CreateMsg()
        :param IsMust: 是否为必显菜单列表的按钮
        :return: 无
        """
        pass

    def RebindMenuButtonFunction(self, MenuType, FunctionInstance=None):
        # type: (str, any) -> None
        """重新绑定菜单按钮触发函数
        :param MenuType: 菜单类型
        :param FunctionInstance: 该按钮按下的函数(一个dict参数)，例如self.CreateMsg，不要填写成self.CreateMsg()。默认为None，则隐藏该按钮
        :return: 无
        """
        pass

    def SelectNotice(self, Title):
        # type: (str) -> None
        """打开指定标题公告活动界面
        :param Title: 公告列表标题
        :return: 无
        """
        pass

    def OpenStoreInLobby(self):
        # type: () -> None
        """打开联机大厅商店界面
        :return: None
        """
        pass

    def OpenAndSelectStoreTagInLobby(self, Tag):
        """打开指定标签分类的联机大厅商店界面
        :param Tag: 标签分类名称
        :return: None
        """
        pass

    def SetLobbyMenuVisible(self, Visible):
        # type: (bool) -> None
        """设置联机大厅菜单是否显示
        :param Visible: 是否显示
        :return: 无
        """
        pass

    def RegisterDebugTool(self, Name, IconPath, Info, Plat, Version, ToolMenu):
        # type: (str, str, str, str, str, list) -> None
        """注册自定义调试工具
        :param Name: 工具名称
        :param IconPath: 工具图标路径
        :param Info: 工具介绍信息，支持富文本
        :param Plat: 适用平台
        :param Version: 版本号
        :param ToolMenu: 工具菜单列表
        :return: 无
        """
        pass

    def CreateFormByJsonId(self, JsonId, ExtraData=None):
        # type: (str, dict) -> None
        """根据配置文件创建自定义表单
        :param JsonId: 配置组件JsonId
        :param ExtraData: 额外参数、用于继承该配置表单加以修改，默认为None
        :return: 无
        """
        pass

    def AreaSfx(self, FirstPos, SecondPos, EffectJson='debug_line', SaveKey='BuildingAreaSfxList'):
        # type: (tuple, tuple, str, str) -> None
        """创建区域包围盒特效
        :param FirstPos: 起始三维坐标
        :param SecondPos: 终点三维坐标
        :param EffectJson: 序列帧特效JsonId，必须为16x16贴图序列帧特效，贴图总缩放系数为(1, 1, 1)
        :param SaveKey: 包围盒特效存储Key，唯一
        :return: 无
        """
        pass

    def ClearAreaSfx(self, SaveKey):
        # type: (str) -> None
        """销毁区域包围盒特效
        :param SaveKey: 包围盒特效存储Key，唯一
        :return: 无
        """
        pass

    def PlaceBuildingByJsonId(self, StartPos, JsonId, Timer=0, DimensionId=0, IsDestroy=False, ItemDataList=None, ModName=None, ServerSystemName=None, CallBackFunctionName=None):
        # type: (tuple, str, float, int, bool, list, str, str, str) -> str
        """根据配置组件放置建筑
        :param StartPos: 起始坐标
        :param JsonId: 配置组件JsonId
        :param Timer: 放置速度
        :param ItemDataList: 【废弃】已有物品数据信息列表，如果填写，则放置建筑依赖材料，需要通过返回函数来删除对应物品，默认为None
        :param ModName: 函数所在脚本模组名称
        :param ServerSystemName: 函数所在脚本模组服务端名称
        :param CallBackFunctionName: 完成后的服务端返回函数，用于删除库存，默认为None。返回一个dict参数(key包含：PlayerId, PlaceBuildingId, JsonId, StartPos, DimensionId, BuildingData)
        :return: 建造数据存档Id(PlaceBuildingId)，暂停后通过GetModRenderAttrByKey接口获取该玩家 建造数据存档Id的存储值即可获得实时情况
        """
        pass

    def PausePlaceBuilding(self, PlaceBuildingId):
        # type: (str) -> None
        """暂停建筑建造
        :param PlaceBuildingId: PlaceBuildingByJsonId返回的建造数据存档Id
        :return: 无
        """
        pass

    def ContinuePlaceBuilding(self, PlaceBuildingId):
        # type: (str) -> None
        """继续建筑建造
        :param PlaceBuildingId: PlaceBuildingByJsonId返回的建造数据存档Id
        :return: 无
        """
        pass

    def DebugPlaceBuildingList(self):
        # type: () -> None
        """打开建筑建造列表管理界面
        :return: 无
        """
        pass

    def CreateTipsTitle(self, Content, SoundName='random.levelup'):
        # type: (str, str) -> None
        """创建并显示一个提示标题
        :param Content: 提示标题显示内容
        :param SoundName: 提示标题显示时播放的音效，默认为random.levelup
        :return: 无
        """
        pass

    def OpenDebugToolMenu(self, DebugDict):
        # type: (dict) -> None
        """打开指定调试工具的菜单
        :param DebugDict: 该调试工具的数据
        :return: 无
        """
        pass

    def CloseDebugToolMenu(self):
        # type: () -> None
        """关闭已打开的调试工具的菜单
        :return: 无
        """
        pass

    def CreateEntityChatUI(self, EntityId, Content, StopTimer=3, SoundName=None, Scale=1, Offset=(0, 1, 0)):
        # type: (str, str, int, str, int, tuple) -> object
        """创建实体自言自语UI
        :param EntityId: 实体id
        :param Content: 说话的文字内容
        :param StopTimer: 关闭延时，默认为3
        :param SoundName: 播放音效名称，默认为None
        :param Scale: 大小类型，可选0, 1，默认为1
        :param Offset: 偏移坐标，默认为(0, 1, 0)
        :return: 实体UI Object
        """
        pass