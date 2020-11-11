from PublicReference.base import *

class 屠戮之魂技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['猎杀枪']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

class 屠戮之魂技能1(被动技能):
    名称 = '光枪精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.02 * self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.02 * self.等级, 5)

class 屠戮之魂技能2(被动技能):
    名称 = '狩猎本能'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)

class 屠戮之魂技能3(被动技能):
    名称 = '枪魂感知'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)

class 屠戮之魂技能4(被动技能):
    名称 = '狩猎之心'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 屠戮之魂技能5(主动技能):
    名称 = '猎杀枪'
    所在等级 = 15
    等级上限 = 5
    基础等级 = 1
    基础 = 222.0
    成长 = 26.0
    CD = 0.85
    TP成长 = 0.10
    TP上限 = 3
    基础释放次数 = 5
    def 等效CD(self, 武器类型):
        return 0.85

class 屠戮之魂技能6(主动技能):
    名称 = '隐鼠袭杀'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1856.40
    成长 = 209.60
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 5

class 屠戮之魂技能7(主动技能):
    名称 = '光焰飞枪'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2309.05
    成长 = 260.95
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5

class 屠戮之魂技能8(主动技能):
    名称 = '蛮横冲撞'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3719.00
    成长 = 420.00
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5

class 屠戮之魂技能9(主动技能):
    名称 = '猎杀枪掠食'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3266.26
    成长 = 368.74
    CD = 9.0
    TP成长 = 0.10
    TP上限 = 5

class 屠戮之魂技能10(主动技能):
    名称 = '光焰枪'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4720.03
    成长 = 532.97
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5

class 屠戮之魂技能11(主动技能):
    名称 = '猎杀枪穿心'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 3629.97
    成长 = 410.03
    CD = 10.0
    TP成长 = 0.10
    TP上限 = 5

class 屠戮之魂技能12(主动技能):
    名称 = '光焰囚杀'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7051.80
    成长 = 796.20
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

class 屠戮之魂技能13(主动技能):
    名称 = '利刃收割'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6394.43
    成长 = 721.57
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.1
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.19
            self.CD *= 0.9

class 屠戮之魂技能14(主动技能):
    名称 = '鹰坠'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 10325.19
    成长 = 1165.81
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
  
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.1
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.1 + 0.09
            self.CD *= 0.9

class 屠戮之魂技能15(主动技能):
    名称 = '龙鳞碎割'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 16415.52
    成长 = 1855.48
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.23 + 0.08
            self.CD *= 0.9

class 屠戮之魂技能16(主动技能):
    名称 = '逐云灭龙杀'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 37586.91
    成长 = 11389.97
    CD = 145.0

class 屠戮之魂技能17(主动技能):
    名称 = '天龙破'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 13676.65
    成长 = 1544.35
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.26
        elif x == 1:
            self.倍率 *= 1.348

class 屠戮之魂技能18(主动技能):
    名称 = '地龙狩'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 20315.33
    成长 = 2293.67
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.17
        elif x == 1:
            self.倍率 *= 1.17 + 0.08
            

class 屠戮之魂技能19(主动技能):
    名称 = '地龙封魔杀'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 32961.50
    成长 = 3721.50
    CD = 40.0
    是否有护石 = 1

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.33

class 屠戮之魂技能20(主动技能):
    名称 = '无尽杀戮'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 42988.14
    成长 = 4853.86
    CD = 45.0
    是否有护石 = 1

    护石选项 = ['圣痕']#CPhit：16+2
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.3680134248

class 屠戮之魂技能21(主动技能):
    名称 = '绝命猎杀死亡穿刺'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 88483.00
    成长 = 26712.00
    CD = 180

class 屠戮之魂技能22(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 屠戮之魂技能23(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 屠戮之魂技能24(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

屠戮之魂技能列表 = []
i = 0
while i >= 0:
    try:
        exec('屠戮之魂技能列表.append(屠戮之魂技能'+str(i)+'())')
        i += 1
    except:
        i = -1

屠戮之魂技能序号 = dict()
for i in range(len(屠戮之魂技能列表)):
    屠戮之魂技能序号[屠戮之魂技能列表[i].名称] = i

屠戮之魂一觉序号 = 0
屠戮之魂二觉序号 = 0
屠戮之魂三觉序号 = 0
for i in 屠戮之魂技能列表:
    if i.所在等级 == 50:
        屠戮之魂一觉序号 = 屠戮之魂技能序号[i.名称]
    if i.所在等级 == 85:
        屠戮之魂二觉序号 = 屠戮之魂技能序号[i.名称]
    if i.所在等级 == 100:
        屠戮之魂三觉序号 = 屠戮之魂技能序号[i.名称]

屠戮之魂护石选项 = ['无']
for i in 屠戮之魂技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        屠戮之魂护石选项.append(i.名称)

屠戮之魂符文选项 = ['无']
for i in 屠戮之魂技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        屠戮之魂符文选项.append(i.名称)

class 屠戮之魂角色属性(角色属性):

    实际名称 = '屠戮之魂'
    角色 = '魔枪士'
    职业 = '狩猎者'

    武器选项 = ['光枪']
    
    类型选择 = ['魔法百分比']
    
    类型 = '魔法百分比'
    防具类型 = '重甲'
    防具精通属性 = ['智力']

    主BUFF = 1.85
   
    远古记忆 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(屠戮之魂技能列表)
        self.技能序号= deepcopy(屠戮之魂技能序号)

class 屠戮之魂(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 屠戮之魂角色属性()
        self.角色属性A = 屠戮之魂角色属性()
        self.角色属性B = 屠戮之魂角色属性()
        self.一觉序号 = 屠戮之魂一觉序号
        self.二觉序号 = 屠戮之魂二觉序号
        self.三觉序号 = 屠戮之魂三觉序号
        self.护石选项 = deepcopy(屠戮之魂护石选项)
        self.符文选项 = deepcopy(屠戮之魂符文选项)
