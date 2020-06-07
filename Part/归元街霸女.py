from PublicReference.base import *

class 归元街霸女技能0(主动技能):
    名称 = '抛沙'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 409.1 *1.088
    成长 = 52.6 *1.088
    CD = 3.0
    TP成长 = 0.08
    TP上限 = 7

class 归元街霸女技能1(主动技能):
    名称 = '擒月炎'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2390.0 *1.123
    成长 = 220.5 *1.123
    CD = 5.5
    TP成长 = 0.10
    TP上限 = 7

class 归元街霸女技能2(主动技能):
    名称 = '毒影针'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2897.7
    成长 = 227.3
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7

class 归元街霸女技能3(主动技能):
    名称 = '双重投掷'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    是否有伤害 = 0
    关联技能 = ['抛沙']
    关联技能2 = ['街头风暴']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.60 + 0.04* self.等级, 5)
    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.98 + 0.02* self.等级, 5)

class 归元街霸女技能4(被动技能):
    名称 = '爪精通'
    所在等级 = 25
    等级上限 = 30
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.01* self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.01* self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.01* self.等级, 5)

class 归元街霸女技能5(主动技能):
    名称 = '砖袭'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 2094.6 *1.116
    成长 = 236.9 *1.116
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7

class 归元街霸女技能6(主动技能):
    名称 = '挑衅'
    所在等级 = 35
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.15 + 0.01* self.等级, 5)

class 归元街霸女技能7(主动技能):
    名称 = '伏虎霸王拳'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 6060.0 *1.05
    成长 = 680.5 *1.05
    CD = 15.0
    TP上限 = 7
    TP成长 = 0.089

class 归元街霸女技能8(被动技能):
    名称 = '狂霸王拳'
    所在等级 = 40
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['伏虎霸王拳']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.03* self.等级, 5)

class 归元街霸女技能9(主动技能):
    名称 = '裂地飞沙'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 10339.8 *1.121
    成长 = 799.8 *1.121
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.27
        self.CD *= 1.00

class 归元街霸女技能10(主动技能):
    名称 = '毒雷引爆'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 1729.89 *1.09
    成长 = 133.11 *1.09
    攻击次数 = 5
    CD = 24.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.07
        self.CD *= 0.90

class 归元街霸女技能11(主动技能):
    名称 = '街头风暴'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 8132.2 *1.108
    成长 = 1622.8 *1.108
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.227

class 归元街霸女技能12(被动技能):
    名称 = '猛毒之血'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.015 * self.等级, 5)

class 归元街霸女技能13(主动技能):
    名称 = '死亡毒雾'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 25214.0
    成长 = 7742.0
    CD = 145

class 归元街霸女技能14(主动技能):
    名称 = '猛毒擒月炎'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 14442.3 *1.163
    成长 = 1631.3 *1.163
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.219
        self.CD *= 0.80


class 归元街霸女技能15(主动技能):
    名称 = '爆碎砖袭'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 16047.5
    成长 = 1789.6
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.119
        self.CD *= 1.00

class 归元街霸女技能16(被动技能):
    名称 = '猛毒之伤'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)

class 归元街霸女技能17(主动技能):
    名称 = '连环毒爆弹'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 40368.8
    成长 = 4558.2
    CD = 40.0

class 归元街霸女技能18(主动技能):
    名称 = '毒龙轰天雷'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 39663.2 *1.072
    成长 = 4394.8 *1.072
    CD = 45.0

class 归元街霸女技能19(主动技能):
    名称 = '万毒噬心诀'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 47534.2 *1.148
    成长 = 14404.3 *1.148
    CD = 180.0
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)

class 归元街霸女技能20(主动技能):
    名称 = '万毒噬心诀x4'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 7179 *1.05
    成长 = 1258 *1.05
    CD = 1.0

class 归元街霸女技能21(主动技能):
    名称 = '万毒噬心诀x3'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 5029 *1.05
    成长 = 898 *1.05
    CD = 1.5


class 归元街霸女技能22(被动技能):
    名称 = '毒门魔境'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 归元街霸女技能23(主动技能):
    名称 = '痛苦杀手'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 110633.4
    成长 = 12492.6
    CD = 60.0

class 归元街霸女技能24(主动技能):
    名称 = '黑死咒：毒牙吞天'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 273645
    成长 = 82609
    CD = 290.0

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

归元街霸女技能列表 = []
i = 0
while i >= 0:
    try:
        exec('归元街霸女技能列表.append(归元街霸女技能'+str(i)+'())')
        i += 1
    except:
        i = -1

归元街霸女技能序号 = dict()
for i in range(len(归元街霸女技能列表)):
    归元街霸女技能序号[归元街霸女技能列表[i].名称] = i

归元街霸女一觉序号 = 0
归元街霸女二觉序号 = 19
归元街霸女三觉序号 = 0
for i in 归元街霸女技能列表:
    if i.所在等级 == 50:
        归元街霸女一觉序号 = 归元街霸女技能序号[i.名称]
    if i.所在等级 == 100:
        归元街霸女三觉序号 = 归元街霸女技能序号[i.名称]

归元街霸女护石选项 = ['无']
for i in 归元街霸女技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        归元街霸女护石选项.append(i.名称)

归元街霸女符文选项 = ['无']
for i in 归元街霸女技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        归元街霸女符文选项.append(i.名称)

class 归元街霸女角色属性(角色属性):

    职业名称 = '归元街霸女'

    武器选项 = ['爪']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比']
    
    #默认
    伤害类型 = '魔法百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量','智力']

    主BUFF = 9.50
   
    #基础属性(含唤醒)
    基础力量 = 976.0
    基础智力 = 959.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13

    死亡毒雾力智开关 = 0
  
    def __init__(self):
        self.技能栏= copy.deepcopy(归元街霸女技能列表)
        self.技能序号= copy.deepcopy(归元街霸女技能序号)

    def 站街力量(self):
        return int(max(self.力量,self.智力))

    def 站街智力(self):
        return self.站街力量()

    def 面板力量(self):
        return max(super().面板力量(), super().面板智力())
      
    def 面板智力(self):
        return self.面板力量()

    def 装备基础(self):
        self.力量 += 防具力量[self.防具类型]
        self.智力 += 防具智力[self.防具类型]
        if 装备列表[装备序号[self.装备栏[0]]].品质 == '神话':
            self.力量 += 神话上衣额外力量[self.防具类型]
            self.智力 += 神话上衣额外智力[self.防具类型]

        for i in [0,1,2,3,4]:
            if 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 精通计算(100,装备列表[装备序号[self.装备栏[i]]].品质,self.强化等级[i],部位列表[i])
            else:
                x = 精通计算(100,装备列表[装备序号[self.装备栏[i]]].品质,0,部位列表[i])
            if '力量' in self.防具精通属性:
                self.力量 += x
            if '智力' in self.防具精通属性:
                self.智力 += x
  

        for i in [9,10]:
            if 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 左右计算(100,'史诗',self.强化等级[i])
                self.力量 += x
                self.智力 += x

        for i in range(0,12):
            if self.是否增幅[i] and 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 增幅计算(100,装备列表[装备序号[self.装备栏[i]]].品质,self.强化等级[i])
                self.力量 += x
                self.智力 += x

        if 装备列表[装备序号[self.装备栏[11]]].所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(100,'史诗',self.强化等级[11],self.武器类型,'物理')
            self.魔法攻击力 += 武器计算(100,'史诗',self.强化等级[11],self.武器类型,'魔法')
            self.独立攻击力 += 锻造计算(100,'史诗',self.武器锻造等级)
        
        if 装备列表[装备序号[self.装备栏[8]]].所属套装 != '智慧产物':
            x = 耳环计算(100,装备列表[装备序号[self.装备栏[8]]].品质,self.强化等级[8])
            self.物理攻击力 += x
            self.魔法攻击力 += x
            self.独立攻击力 += x

        for i in [5,6,7,8,9,10,11]:
            self.力量 += 装备列表[装备序号[self.装备栏[i]]].力量
            self.智力 += 装备列表[装备序号[self.装备栏[i]]].智力
            self.物理攻击力 += 装备列表[装备序号[self.装备栏[i]]].物理攻击力
            self.魔法攻击力 += 装备列表[装备序号[self.装备栏[i]]].魔法攻击力
            self.独立攻击力 += 装备列表[装备序号[self.装备栏[i]]].独立攻击力

    def 伤害指数计算(self):
        if self.死亡毒雾力智开关 == 1:
            self.力量+= self.技能栏[self.技能序号['死亡毒雾']].等级 * 6.5 + 91
            self.智力+= self.技能栏[self.技能序号['死亡毒雾']].等级 * 6.5 + 91

        基准倍率 = 1.5 * (0.9 + self.主BUFF/10) * (1 - 443215 / (443215 + 20000))

        if self.伤害类型 == '物理百分比':
            面板 = (self.面板力量()/250+1) * (self.物理攻击力 + self.进图物理攻击力) * (1 + self.百分比三攻)
        if self.伤害类型 == '魔法百分比':
            面板 = (self.面板智力()/250+1) * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻)
        if self.伤害类型 == '物理固伤':
            面板 = (self.面板力量()/250+1) * (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻)
        if self.伤害类型 == '魔法固伤':
            面板 = (self.面板智力()/250+1) * (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻)

        属性倍率=1.05+0.0045*max(self.火属性强化,self.冰属性强化,self.光属性强化,self.暗属性强化)
        增伤倍率=1+self.伤害增加
        增伤倍率*=1+self.暴击伤害
        增伤倍率*=1+self.最终伤害
        增伤倍率*=self.技能攻击力
        增伤倍率*=1+self.持续伤害*(1-0.1*self.持续伤害计算比例)
        增伤倍率*=1+self.附加伤害+self.属性附加*属性倍率
        self.伤害指数=面板*属性倍率*增伤倍率*基准倍率/100

class 归元街霸女(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 归元街霸女角色属性()
        self.角色属性A = 归元街霸女角色属性()
        self.角色属性B = 归元街霸女角色属性()
        self.一觉序号 = 归元街霸女一觉序号
        self.二觉序号 = 归元街霸女二觉序号
        self.三觉序号 = 归元街霸女三觉序号
        self.护石选项 = copy.deepcopy(归元街霸女护石选项)
        self.符文选项 = copy.deepcopy(归元街霸女符文选项)

    def 界面(self):
        super().界面()
        self.死亡毒雾力智开关=QCheckBox('死亡毒雾力智',self.main_frame2)
        self.死亡毒雾力智开关.resize(100,20)
        self.死亡毒雾力智开关.move(325,420)
        self.死亡毒雾力智开关.setStyleSheet(复选框样式)

        self.毒雷个数数选择=QComboBox(self.main_frame2)
        self.毒雷个数数选择.addItem('毒雷引爆：0颗')
        self.毒雷个数数选择.addItem('毒雷引爆：1颗')
        self.毒雷个数数选择.addItem('毒雷引爆：2颗')
        self.毒雷个数数选择.addItem('毒雷引爆：3颗')
        self.毒雷个数数选择.addItem('毒雷引爆：4颗')
        self.毒雷个数数选择.addItem('毒雷引爆：5颗')
        self.毒雷个数数选择.addItem('毒雷引爆：6颗')
        self.毒雷个数数选择.addItem('毒雷引爆：7颗')
        self.毒雷个数数选择.addItem('毒雷引爆：8颗')
        self.毒雷个数数选择.setCurrentIndex(5)
        self.毒雷个数数选择.resize(120,20)
        self.毒雷个数数选择.move(315,460)
        self.毒雷个数数选择.setStyleSheet(下拉框样式)

    def 输入属性(self, 属性):
        super().输入属性(属性)
        if self.死亡毒雾力智开关.isChecked():
            属性.死亡毒雾力智开关 = 1
        属性.技能栏[属性.技能序号['毒雷引爆']].攻击次数 = self.毒雷个数数选择.currentIndex()