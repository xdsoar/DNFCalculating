from PublicReference.equipment.equ_list import *
from PublicReference.equipment.称号 import *
from PublicReference.equipment.宠物 import *
from PublicReference.equipment.辟邪玉 import *
from PublicReference.equipment.武器融合 import *
from PublicReference.choise.选项设置 import *
from PublicReference.choise.细节选项 import *
from PublicReference.common import *

class 技能:
    名称 = ''
    备注 = ''
    所在等级 = 0
    等级上限 = 0
    等级 = 0
    基础等级 = 0
    等级溢出 = 0
    自定义描述 = 0

    关联技能 = ['无']
    关联技能2 = ['无']
    关联技能3 = ['无']
    冷却关联技能 = ['无']
    冷却关联技能2 = ['无']
    冷却关联技能3 = ['无']

    def 等级加成(self, x):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
                if self.基础等级 != self.等级上限 and self.关联技能 != ['无']:
                    self.等级溢出 = 1
            else:
                self.等级 += x

class 主动技能(技能):
    #只扩展了技能的三条属性，第一条技能hit默认1,2、3条hit默认为0，需要手动赋值
    #如果需要继续扩展，可以在各自职业类内继承后自行扩展，同时需要重写下等效百分比函数
    #固伤在填写基础及成长的时候需要注意，技能面板/独立得到的成长及数值需要*100
    基础 = 0.0
    成长 = 0.0
    攻击次数 = 1.0
    基础2 = 0.0
    成长2 = 0.0
    攻击次数2 = 0.0
    基础3 = 0.0
    成长3 = 0.0
    攻击次数3 = 0.0
    CD = 0.0
    TP成长 = 0.0
    TP上限 = 0
    TP等级 = 0
    是否主动 = 1
    是否有伤害 = 1
    恢复 = 1.0
    倍率 = 1.0
    被动倍率 = 1.0
    基础释放次数 = 0
    演出时间 = 0
    是否有护石 = 0
    护石选项 = ['魔界']

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)
                        
    def 等效CD(self, 武器类型):
        # Will修改
        return round(self.CD  / self.恢复, 1)

class 被动技能(技能):
    是否主动 = 0
    是否有伤害 = 0
    关联技能 = ['所有']

符文效果选项 = ['无', '攻击+5%,CD+3%', 'CD-4%', '攻击+3%', '攻击-3%,CD-6%', '攻击+3%,CD+2%', 'CD-3%', '攻击+2%', '攻击-2%,CD-4%',
    '攻击+2%,CD+1%', 'CD-2%', '攻击+1%', '攻击-1%,CD-3%', '攻击+6%,CD+4%', 'CD-5%', '攻击+4%', '攻击-4%,CD-7%']

刀魂之卡赞数据 = [0, 31, 40, 48, 58, 67, 79, 90, 103, 116, 131, 145, 161, 178, 194, 212, 230, 250, 270, 292, 313]

class 角色属性(属性):
    职业分类 = '输出'
    主BUFF = 1.0
    系统奶 = False
    年宠技能 = False
    白兔子技能 = False
    斗神之吼秘药 = False
    称号触发 = False
    战术技能BUFF = False
    兵法技攻BUFF = False
    希洛克BUFF = False

    物理攻击力 = 65
    魔法攻击力 = 65
    独立攻击力 = 1045
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    
    进图物理攻击力 = 0
    进图魔法攻击力 = 0
    进图独立攻击力 = 0
    进图属强 = 0

    #红阵，远古记忆 -1表示没有该技能
    远古记忆 = -1
    刀魂之卡赞 = -1

    百分比力智 = 0.0
    百分比三攻 = 0.0
    伤害增加 = 0.0
    黄字 = 0.0 #冲突属性
    附加伤害 = 0.0
    属性附加 = 0.0
    暴击伤害 = 0.0
    爆伤 = 0.0 #冲突属性
    最终伤害 = 0.0
    技能攻击力 = 1.0
    持续伤害 = 0.0
    加算冷却缩减 = 0.0
    百分比减防 = 0.0
    固定减防 = 0
    词条提升率 = [0] * 6
    词条选择 = []

    #队友增幅系数
    队友增幅系数 = 1.0

    防御输入 = 0
    火抗输入 = 0
    冰抗输入 = 0
    光抗输入 = 0
    暗抗输入 = 0

    攻击速度 = 0.00
    移动速度 = 0.00
    释放速度 = 0.00
    命中率 = 0.0
    回避率 = 0.0
    物理暴击率 = 0.00
    魔法暴击率 = 0.00

    自适应选项 = [0] * 2
    自适应描述 = ['无'] * 2

    时间输入 = 0
    次数输入 = []
    宠物次数 = []
    技能切装 = []
    装备切装 = []
    开启切装 = 0
    切装修正 = []

    转甲选项 = 0

    希洛克武器词条 = 0
    武器词条触发 = 0
    
    #0英雄 1传说
    角色熟练度 = 0
    #0 1 2 3 4 5 6
    技能栏空位 = 6
    #0数学期望 1黄字+35% 2爆伤+35% 3白字+35% 4终伤+35% 5三攻+35%
    命运的抉择 = 0
    #0数学期望 123456
    天命无常 = 0
    #0数学期望 1 HP高于70% 2 HP在70~30% 3 HP低于30%
    悲剧的残骸 = 0
    #0数学期望 1 5%属性附加 2 10%技能攻击力 3 15%技能攻击力
    先知者的预言 = 0
    #0无霸体状态 1 霸体状态 2 无伤状态 
    贫瘠沙漠的遗产 = 1
    #0数学期望 1 7效果 2 77效果 3 777效果
    幸运三角 = 0
    #0过充电状态 1过负荷状态
    擎天战甲 = 0
    #0.00~1.00
    持续伤害计算比例 = 0
    #0 120+ 1 120-100 2 100-80 3 80-60 4 60-40 5 40-
    军神的隐秘遗产 = 0
    #0太极天帝剑：阳  1太极天帝剑：阴  
    太极天帝剑 = 0
    #0绿色生命的面容：无  1绿色生命的面容：阴暗面
    绿色生命的面容 = 1

    攻击属性 = 0
    
    #是否为图内状态
    状态 = 0
    # 是否为输出装备描述
    装备描述 = 0
 
    #辟邪玉属性
    附加伤害增加增幅 = 1.0
    属性附加伤害增加增幅 = 1.0
    技能伤害增加增幅 = 1.0
    暴击伤害增加增幅 = 1.0
    伤害增加增幅 = 1.0
    最终伤害增加增幅 = 1.0
    力量智力增加增幅 = 1.0
    物理魔法攻击力增加增幅 = 1.0
    所有属性强化增加 = 1.0

    def 附加伤害加成(self, x ):
        if self.装备描述 == 1:
            return '附加伤害 +{}%<br>'.format(round(x*100,0))
        else:
             self.附加伤害 += self.附加伤害增加增幅 * x 
        return ''

    def 三攻固定加成(self, x=0, y=0,z=0):
        if self.装备描述 == 1:
            return '物攻/魔攻/独立 +{}<br>'.format(x)
        else:
            self.物理攻击力 += x
            self.魔法攻击力 += x
            self.独立攻击力 += x
        return ''

    def 力智固定加成(self, x=0, y=0):
        if self.装备描述 == 1:
            return '力量、智力 +{}<br>'.format(x)
        else:
             self.力量 += x 
             self.智力 += x
        return ''

    def 持续伤害加成(self, x ):
        if self.装备描述 == 1:
            return '持续伤害 +{}%<br>'.format(round(x*100,0))
        else:
             self.持续伤害 += x 
        return ''

    def 属性附加加成(self, x ):
        if self.装备描述 == 1:
            return '附加伤害 +{}%<br>'.format(round(x*100,0))
        else:
            self.属性附加 += self.属性附加伤害增加增幅 * x 
        return ''

    def 技能攻击力加成(self, x):
        if self.装备描述 ==1:
            return '技能攻击力 +{}%<br>'.format(round(x*100,0))
        else:
            self.技能攻击力 *= 1 + self.技能伤害增加增幅 * x 
        return ''
        
    def 暴击伤害加成(self, x):
        if self.装备描述 ==1:
            return '暴击伤害 +{}%<br>'.format(round(x*100,0))
        else:
            self.暴击伤害 += self.暴击伤害增加增幅 * x 
        return ''
        
    def 伤害增加加成(self, x):
        if self.装备描述 ==1:
            return '伤害增加 +{}%<br>'.format(round(x*100,0))
        else:
            self.伤害增加 += self.伤害增加增幅 * x 
        return ''
        
    def 最终伤害加成(self, x):
        if self.装备描述 ==1:
            return '最终伤害 +{}%<br>'.format(round(x*100,0))
        else:
            self.最终伤害 += self.最终伤害增加增幅 * x 
        return ''
        
    def 百分比力智加成(self, x):
        if self.装备描述 ==1:
            return '力量、智力 +{}%<br>'.format(round(x*100,0))
        else:
            self.百分比力智 += self.力量智力增加增幅 * x 
        return ''
        
    def 百分比三攻加成(self, x):
        if self.装备描述 ==1:
            return '百分比三攻 {}%<br>'.format(('+' if x>0 else '')+str(round(x*100,0)))
        else:
            self.百分比三攻 += self.物理魔法攻击力增加增幅 * x 
        return ''
        
    def 火属性强化加成(self, x):
        if self.装备描述 ==1:
            return '火属性强化 +{}<br>'.format(x)
        else:
            if self.状态 == 0:
                self.火属性强化 += self.所有属性强化增加 * x 
            else:
                self.火属性强化 += int(self.所有属性强化增加 * x)             
        return ''

    def 冰属性强化加成(self, x):
        if self.装备描述 ==1:
            return '冰属性强化 +{}<br>'.format(x)
        else:
            if self.状态 == 0:
                self.冰属性强化 += self.所有属性强化增加 * x 
            else:
                self.冰属性强化 += int(self.所有属性强化增加 * x) 
        return ''


    def 光属性强化加成(self, x):
        if self.装备描述 ==1:
            return '光属性强化 +{}<br>'.format(x)
        else:
            if self.状态 == 0:
                self.光属性强化 += self.所有属性强化增加 * x 
            else:
                self.光属性强化 += int(self.所有属性强化增加 * x)             
        return ''


    def 暗属性强化加成(self, x):
        if self.装备描述 ==1:
            return '暗属性强化 +{}<br>'.format(x)
        else:
            if self.状态 == 0:
                self.暗属性强化 += self.所有属性强化增加 * x 
            else:
                self.暗属性强化 += int(self.所有属性强化增加 * x) 
        return ''

    def 所有属性强化加成(self, x):
        if self.装备描述 ==1:
            return '所有属性强化 +{}<br>'.format(x)
        else:
            if self.状态 == 0:
                temp = self.所有属性强化增加 * x 
            else:
                temp = int(self.所有属性强化增加 * x)
            self.所有属性强化(temp)
        return ''

    def 攻击速度增加(self,x):
        if self.装备描述 ==1:
            return '攻击速度 {}%<br>'.format(("+" if x > 0 else '')+str(round(x*100,2)))
        else:
            self.攻击速度 += x
        return ''

    def 移动速度增加(self,x):
        if self.装备描述 ==1:
            return '移动速度 {}%<br>'.format(("+" if x > 0 else '')+str(round(x*100,2)))
        else:
            self.移动速度 += x
        return ''

    def 释放速度增加(self,x):
        if self.装备描述 ==1:
            return '释放速度 {}%<br>'.format(("+" if x > 0 else '')+str(round(x*100,2)))
        else:
            self.释放速度 += x
        return ''

    def 命中率增加(self,x):
        if self.装备描述 ==1:
            return '命中率 {}%<br>'.format(("+" if x > 0 else '')+str(int(x*100)))
        else:
            self.命中率 +=x
        return ''

    def 物理暴击率增加(self,x):
        if self.装备描述 ==1:
            return '物理暴击率 +{}%<br>'.format(int(x*100))
        else:
            self.物理暴击率 += x
        return ''

    def 魔法暴击率增加(self,x):
        if self.装备描述 ==1:
            return '魔法暴击率 +{}%<br>'.format(int(x*100))
        else:
            self.魔法暴击率 +=x
        return ''


    def 防具精通计算(self, i):
        temp = 装备列表[装备序号[self.装备栏[i]]]
        if temp.等级 == 100:
            if temp.所属套装 != '智慧产物':
                return 精通计算(temp.等级,temp.品质,self.强化等级[i],部位列表[i])
            else:
                return 精通计算(temp.等级,temp.品质,0,部位列表[i])
        elif temp.等级 > 85:
            计算等级 = temp.等级
            if temp.所属套装 == '兵法之神':
                if self.装备检查('过往时光的轮回'): 计算等级 = 100 
            return 精通计算(计算等级,temp.品质,self.强化等级[i],部位列表[i])
        else:
            计算等级 = temp.等级
            if temp.所属套装 == '战术之王的御敌':
                if self.装备检查('战术之王的战术指挥棒'): 计算等级 = 100
            elif temp.所属套装 == '魔战无双':   
                if self.装备检查('聚魔漩涡'): 计算等级 = 100
            x = 精通计算(计算等级,temp.品质,self.强化等级[i],部位列表[i])
            if self.转甲选项 == 1:
                return round(x, 2)
            else:
                return round(0.4 * x, 2)



    def 装备检查(self, 装备名称):
        for i in self.装备栏:
            if i == 装备名称:
                return True
        return False

    def 所有属性强化(self, x):
        self.火属性强化 += x
        self.冰属性强化 += x
        self.光属性强化 += x
        self.暗属性强化 += x

    def 技能等级加成(self, 加成类型, minLv, maxLv, lv):
        lv = int(lv)
        if self.装备描述 ==1:
            if 加成类型=="所有":
                if minLv == maxLv:
                    return "Lv{} 技能等级+{}<br>".format(minLv,lv)
                else:
                    return "Lv{}-{} 技能等级+{}<br>".format(minLv,maxLv,lv)
            else:
                if minLv == maxLv:
                    return "Lv{} 主动技能等级+{}<br>".format(minLv,lv)
                else:
                    return "Lv{}-{} 主动技能等级+{}<br>".format(minLv,maxLv,lv)            
        else:
            if self.远古记忆 > 0:
                if minLv <= 15 and maxLv >= 15:
                    self.远古记忆 = min(20, self.远古记忆 + lv)

            if self.刀魂之卡赞 > 0:
                if minLv <= 5 and maxLv >= 5:
                    self.刀魂之卡赞 = min(20, self.刀魂之卡赞 + lv)

            for i in self.技能栏:
                if i.所在等级 >= minLv and i.所在等级 <= maxLv:
                    if 加成类型 == '所有':
                        i.等级加成(lv)
                    else:
                        if i.是否主动 == 1:
                            i.等级加成(lv)            
        return ''
        
    def 技能冷却缩减(self, min, max, x):
        if self.装备描述 ==1:
            if min == max:
                return "Lv{} 技能CD-{}%<br>".format(min,int(x*100))
            else:
                return "Lv{}-{} 技能CD-{}%<br>".format(min,max,int(x*100))
        else:
            for i in self.技能栏:
                if i.所在等级 >= min and i.所在等级 <= max:
                    if i.是否有伤害 == 1:
                        i.CD *= (1 - x)            
        return ''

    def 技能恢复加成(self, min, max, x):
        if self.装备描述 ==1:
            if min == max:
                return "Lv{} 技能恢复+{}%<br>".format(min,int(x*100))
            else:
                return "Lv{}-{} 技能恢复+{}%<br>".format(min,max,int(x*100))                  
        else:
            for i in self.技能栏:
                if i.所在等级 >= min and i.所在等级 <= max:
                    if i.是否有伤害 == 1:
                        i.恢复 += x      
        return ''


    def 技能倍率加成(self, lv, x):
        if self.装备描述 ==1:
            return "Lv{} 技能攻击力{}%<br>".format(lv,('+' if x > 0 else "") + str(int(x*100)))
        else:
            for i in self.技能栏:
                if i.所在等级 == lv:
                    if i.是否有伤害 == 1:
                        i.倍率 *= (1 + x * self.技能伤害增加增幅)        
        return ''
     
    def 单技能修改(self, 名称, 倍率, CD):
        if self.装备描述 ==1:
            tem = ""
            if 倍率 !=1 :
                tem+="[{}] 攻击力{}%<br>".format(名称,('+' if 倍率 > 1 else "")+str(int((倍率-1)*100)))
            if CD !=1 :
                tem+="[{}] CD{}%<br>".format(名称,('+' if CD > 1 else "")+str(int((CD-1)*100)))
            return tem            
        else:
            for i in self.技能栏:
                if i.是否有伤害 == 1:
                    if i.名称 == 名称:
                        i.倍率 *= 倍率
                        i.CD *= CD            
        return ''

    def 站街力量(self):
        return int(self.力量)

    def 站街智力(self):
        return int(self.智力)

    def 面板力量(self):
        if self.系统奶 == False:
            return int(int((self.力量 + self.进图力量)) * (1 + self.百分比力智))
        else:
            return int(int((self.力量 + int((self.力量 - self.基础力量) * 1.35 + 7664) +self.进图力量)) * (1 + self.百分比力智))

    def 面板智力(self):
        if self.系统奶 == False:
            return int(int((self.智力 + self.进图智力)) * (1 + self.百分比力智))
        else:
            return int(int((self.智力 + int((self.智力 - self.基础智力) * 1.35 + 7664) +self.进图智力)) * (1 + self.百分比力智))

    def 站街物理攻击力倍率(self):
        站街物理攻击倍率 =  1.0
        for i in self.技能栏:
            try : 站街物理攻击倍率 *= i.物理攻击力倍率(self.武器类型)
            except : pass
        return 站街物理攻击倍率

    def 站街魔法攻击力倍率(self):
        站街魔法攻击倍率 =  1.0
        for i in self.技能栏:
            try : 站街魔法攻击倍率 *= i.魔法攻击力倍率(self.武器类型)
            except : pass
        return 站街魔法攻击倍率

    def 站街独立攻击力倍率(self):
        站街独立攻击倍率 = 1.0
        for i in self.技能栏:
            try : 站街独立攻击倍率 *= i.独立攻击力倍率(self.武器类型)
            except : pass
        return 站街独立攻击倍率

    def 站街物理攻击力(self):
        return self.物理攻击力 * self.站街物理攻击力倍率()

    def 站街魔法攻击力(self):
        return self.魔法攻击力 * self.站街魔法攻击力倍率()

    def 站街独立攻击力(self):
        return self.独立攻击力 * self.站街独立攻击力倍率()

    def 面板物理攻击力(self):
        面板物理攻击 = (self.物理攻击力 + self.进图物理攻击力) * (1 + self.百分比三攻) * (1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        for i in self.技能栏:
            try : 面板物理攻击 *= i.物理攻击力倍率进图(self.武器类型)
            except : pass
        return 面板物理攻击 * self.站街物理攻击力倍率()


    def 面板魔法攻击力(self):
        面板魔法攻击 = (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻) * (1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        for i in self.技能栏:
            try : 面板魔法攻击 *= i.魔法攻击力倍率进图(self.武器类型)
            except : pass
        return 面板魔法攻击 * self.站街魔法攻击力倍率()

    def 面板独立攻击力(self):
        面板独立攻击 = (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻)
        for i in self.技能栏:
            try : 面板独立攻击 *= i.独立攻击力倍率进图(self.武器类型)
            except : pass
        return 面板独立攻击 * self.站街独立攻击力倍率()

    def 加算冷却计算(self):
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                i.CD *= (1 - self.加算冷却缩减)

    def CD倍率计算(self):
        for i in self.技能栏:
            if i.冷却关联技能 !=['无']:
                if i.冷却关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率(self.武器类型)
                else:
                    for k in i.冷却关联技能:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率(self.武器类型)
            if i.冷却关联技能2 !=['无']:
                if i.冷却关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率2(self.武器类型)
                else:
                    for k in i.冷却关联技能2:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率2(self.武器类型)
            if i.冷却关联技能3 !=['无']:
                if i.冷却关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率3(self.武器类型)
                else:
                    for k in i.冷却关联技能3:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率3(self.武器类型)

    def 被动倍率计算(self):
        if self.远古记忆 > 0:
            self.进图智力 += self.远古记忆 * 15
        if self.刀魂之卡赞 > 0:
            self.进图力量 += 刀魂之卡赞数据[self.刀魂之卡赞]
            self.进图智力 += 刀魂之卡赞数据[self.刀魂之卡赞]
        for i in self.技能栏:
            if i.关联技能 != ['无']:
                if i.关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率(self.武器类型)
                else :
                    for k in i.关联技能:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率(self.武器类型)
            
            if i.关联技能2 != ['无']:
                if i.关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率2(self.武器类型)
                else :
                    for k in i.关联技能2:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率2(self.武器类型)
            
            if i.关联技能3 != ['无']:
                if i.关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率3(self.武器类型)
                else :
                    for k in i.关联技能3:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率3(self.武器类型)

    def 面板系数计算(self):
        if self.类型 == '物理百分比':
            return int((self.面板力量() / 250 + 1) * (self.物理攻击力 + self.进图物理攻击力) * (1 + self.百分比三攻))
        elif self.类型 == '魔法百分比':
            return int((self.面板智力() / 250 + 1) * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻))
        elif self.类型 == '物理固伤':
            return int((self.面板力量() / 250 + 1) * (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻))
        elif self.类型 == '魔法固伤':
            return int((self.面板智力() / 250 + 1) * (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻))

    def 词条提升率计算(self, 词条范围, 词条数值, y = 0):

        词条提升率 = [0] * 6

        if 0 in 词条范围:
            #百分比力智
            x = self.面板系数计算()
            self.百分比力智加成(词条数值[0])
            词条提升率[0] = self.面板系数计算() / x - 1
            self.百分比力智加成(-词条数值[0])

        if 1 in 词条范围:
            #百分比三攻
            x = 1 + self.百分比三攻
            self.百分比三攻加成(词条数值[1])
            词条提升率[1] = (1 + self.百分比三攻) / x - 1
            self.百分比三攻加成(-词条数值[1])  
        
        if 2 in 词条范围:
            #伤害增加
            x = 1 + int(self.伤害增加 * 100) / 100
            self.伤害增加加成(词条数值[2])
            词条提升率[2] = (1 + int(self.伤害增加 * 100) / 100) / x - 1
            self.伤害增加加成(-词条数值[2])

        if 3 in 词条范围:    
            #附加伤害
            x = 1 + self.附加伤害 + self.属性附加 * self.属性倍率
            self.附加伤害加成(词条数值[3])
            词条提升率[3] = (1 + self.附加伤害 + self.属性附加 * self.属性倍率) / x - 1
            self.附加伤害加成(-词条数值[3])

        if 4 in 词条范围:    
            #暴击伤害
            x = 1 + self.暴击伤害
            self.暴击伤害加成(词条数值[4])
            词条提升率[4] = (1 + self.暴击伤害) / x - 1
            self.暴击伤害加成(-词条数值[4])        

        if 5 in 词条范围:    
            #最终伤害
            x = 1 + self.最终伤害
            self.最终伤害加成(词条数值[5])
            词条提升率[5] = (1 + self.最终伤害) / x - 1
            self.最终伤害加成(-词条数值[5])  
        
        if y == 1:
            self.词条提升率 = copy(词条提升率)

        for k in range(6):
            if 词条提升率[k] == max(词条提升率):
                词条属性列表[k].加成属性(self, 词条数值[k])
                return k

    def 自适应计算(self):
        if self.自适应选项[0] != 0: #宠物
            词条数值 = {0:0.07, 2:0.07, 3:0.08}
            index = self.词条提升率计算([0, 2, 3], 词条数值)
            self.自适应描述[0] = '{}%{}'.format(int(词条数值[index] * 100), 词条属性列表[index].描述)
        
        if self.自适应选项[1] != 0: #光环
            index = self.词条提升率计算([1, 2, 4], [0.05] * 6)
            self.自适应描述[1] = '{}%{}'.format(5, 词条属性列表[index].描述)

    def 自适应输出(self):
        temp = ''
        if self.自适应选项[0] != 0: #宠物
            temp += '宠物:' + self.自适应描述[0]
        if self.自适应选项[1] != 0: #光环
            if temp != '':
                temp += '|'
            temp += '光环:' + self.自适应描述[1]
        return temp

    def 希洛克武器提升(self):
        if self.希洛克武器词条 == 0:
            self.词条提升率 = [0] * 6
            return

        self.词条选择.clear()
        self.词条选择.append(self.词条提升率计算([0, 1, 2, 3, 4, 5], [0.10] * 6, 1))
        if self.武器词条触发 == 1:
            self.词条选择.append(self.词条提升率计算([0, 1, 2, 3, 4, 5], [0.05] * 6))

    def 属性倍率计算(self):
        # 火、冰、光、暗
        self.属性倍率组 = []
        self.属性倍率组.append(1.05 + 0.0045 * int(self.火属性强化 - self.火抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.冰属性强化 - self.冰抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.光属性强化 - self.光抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.暗属性强化 - self.暗抗输入))        
        if self.攻击属性 == 0:
            self.属性倍率 = max(self.属性倍率组)
        elif self.攻击属性 == 1:
            self.属性倍率 = self.属性倍率组[0]
        elif self.攻击属性 == 2:
            self.属性倍率 = self.属性倍率组[1]
        elif self.攻击属性 == 3:
            self.属性倍率 = self.属性倍率组[2]
        elif self.攻击属性 == 4:
            self.属性倍率 = self.属性倍率组[3]
        

    def 伤害指数计算(self):
        
        防御 = max(self.防御输入 - self.固定减防, 0) * (1 - self.百分比减防)
        基准倍率 = 1.5 * self.主BUFF * (1 - 防御 / (防御+ 20000))

        #避免出现浮点数取整BUG
        self.伤害增加 += 0.00000001
        
        self.属性倍率计算()
        
        if sum(self.自适应选项) != 0:
            self.自适应计算()

        self.希洛克武器提升()

        面板 = self.面板系数计算()

        增伤倍率 = 1 + int(self.伤害增加 * 100) / 100
        增伤倍率 *= 1 + self.暴击伤害
        增伤倍率 *= 1 + self.最终伤害
        增伤倍率 *= self.技能攻击力
        增伤倍率 *= 1 + self.持续伤害 * self.持续伤害计算比例
        增伤倍率 *= 1 + self.附加伤害 + self.属性附加 * self.属性倍率
        # 添加希洛克BUFF
        self.伤害指数 = 面板 * self.属性倍率 * 增伤倍率 * 基准倍率 / 100 * self.队友增幅系数 * (1 + self.希洛克BUFF * 0.15)
        

    def 切装判断(self):
        for i in self.装备切装:
            if i != '无':
                return True
        return False
        
    def 装备替换(self):
        Q = deepcopy(self)
        P = deepcopy(self)
        
        for i in range(12):
            if P.装备切装[i] != '无':
                P.装备栏[i] = P.装备切装[i]

        P.适用套装计算()

        P.武器类型 = 装备列表[装备序号[P.装备栏[11]]].类型
        P.力量 += P.切装修正[0]
        P.智力 += P.切装修正[1]
        P.物理攻击力 += P.切装修正[2]
        P.魔法攻击力 += P.切装修正[3]
        P.独立攻击力 += P.切装修正[4]
        P.所有属性强化加成(P.切装修正[5])

        return [Q, P]

    def 伤害计算(self, x = 0):
        if 切装模式 == 1 and self.切装判断():
            temp = self.装备替换()
            A = temp[0].数据计算(1, 1)  #身上装备计算
            B = temp[1].数据计算(1, 0)  #切装装备计算
            self.预处理()
            for i in range(len(self.技能栏)):
                self.技能栏[i] = deepcopy(temp[self.技能切装[i]].技能栏[i])
            C = []
            总伤害 = 0
            for i in range(len(A)):
                C.append(A[i] if (self.技能切装[int(i / 4)] == 0) else B[i])
                if i % 4 == 1:
                    总伤害 += C[i]
            if x == 0:
                return 总伤害
            else:
                for i in range(int(len(A) / 4)):
                    if 总伤害 != 0:
                        C[i * 4 + 3] = C[i * 4 + 1] / 总伤害 * 100
                    else:
                        C[i * 4 + 3] = 0  
                return C
        else:
            self.技能切装 = [0] * len(self.技能栏)
            return self.数据计算(x)
            
    def 预处理(self):
        self.装备属性计算()
        self.所有属性强化(self.进图属强)
        self.CD倍率计算()
        self.加算冷却计算()
        self.被动倍率计算()
        self.伤害指数计算()

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if self.次数输入[self.技能序号[i.名称]] == '/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间) / i.等效CD(self.武器类型) + 1 + i.基础释放次数))
                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)
        return 技能释放次数

    def 技能单次伤害计算(self, y):
        #y切装标记
        技能单次伤害 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1 and self.技能切装[self.技能序号[i.名称]] != y:
                技能单次伤害.append(i.等效百分比(self.武器类型) * self.伤害指数 * i.被动倍率)
            else:
                技能单次伤害.append(0)
        return 技能单次伤害

    def 技能总伤害计算(self, a, b):
        #a次数 b单次伤害
        技能总伤害 = []
        for i in self.技能栏:
            index = self.技能序号[i.名称]
            if i.是否有伤害 == 1 and a[index] != 0:
                技能总伤害.append(a[index] * b[index] * (1 
                    + self.白兔子技能 * 0.20 
                    + self.年宠技能 * 0.10 * self.宠物次数[index] / a[index]  #宠物技能占比 = 宠物次数 / 释放次数
                    + self.斗神之吼秘药 * 0.12))
            else:
                技能总伤害.append(0)
        return 技能总伤害

    def 数据返回(self, x, a, b):
        #a次数  b伤害
        总伤害 = sum(b)
        if x == 0:
            #伤害数据，用于排序
            return 总伤害
        elif x == 1:
            #详细数据，用于展示  四个数据一组  
            #0次数 1总伤害 2平均伤害 3占比
            data = []
            for i in range(0, len(self.技能栏)):
                data.append(a[i])
                data.append(b[i])
                if a[i] != 0:
                    data.append(b[i] / a[i])
                else:
                    data.append(b[i])
                if 总伤害 != 0:
                    data.append(b[i] / 总伤害 * 100)
                else:
                    data.append(0)
            return data

    def 数据计算(self, x = 0, y = -1):
        self.预处理()
        #初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算(y)
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        #返回结果
        return self.数据返回(x, 技能释放次数, 技能总伤害)
    
    def 装备词条计算(self):
        if 调试开关 == 0:
            for i in range(11):
                装备列表[装备序号[self.装备栏[i]]].城镇属性(self)

            if 武器序号 == -1:
                装备列表[装备序号[self.装备栏[11]]].城镇属性(self)
            else:
                装备列表[武器序号].城镇属性(self)

            for i in self.套装栏:
                套装列表[套装序号[i]].城镇属性(self)

            #进图触发属强向下取整
            self.状态 = 1
            for i in range(11):
                装备列表[装备序号[self.装备栏[i]]].进图属性(self)

            if 武器序号 == -1:
                装备列表[装备序号[self.装备栏[11]]].进图属性(self)
            else:
                装备列表[武器序号].进图属性(self)

            for i in self.套装栏:
                套装列表[套装序号[i]].进图属性(self)
            self.状态 = 0

        #冲突属性计算
        self.伤害增加加成(self.黄字)
        self.暴击伤害加成(self.爆伤)
        
        #光环属性计算
        if self.战术技能BUFF:
            self.技能等级加成('所有', 60, 80, 3)
        if self.兵法技攻BUFF:
            self.技能攻击力加成(0.10)

    def 装备属性计算(self):
        self.装备基础()
        self.装备词条计算()
    
    def 其它属性计算(self):
        for i in range(11):
            装备列表[装备序号[self.装备栏[i]]].其它属性(self)

        if 武器序号 == -1:
            装备列表[装备序号[self.装备栏[11]]].其它属性(self)
        else:
            装备列表[武器序号].其它属性(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].其它属性(self)

class 角色窗口(窗口):
    def __init__(self):
        super().__init__()

    def 界面(self):
        count = 0
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                count += 1
        self.窗口高度 = max(55 + 30 * count, 680)
        self.setFixedSize(1120, self.窗口高度)
        self.输出背景图片 = QPixmap('./ResourceFiles/img/输出背景.png')
        super().界面()

    def 界面1(self):
        super().界面1()

        for i in 称号列表:
            self.称号.addItem(i.名称)
        
        for i in 宠物列表:
            self.宠物.addItem(i.名称)  

        标签 = QLabel('装备条件设置', self.main_frame1)
        标签.move(940, 5)
        标签.resize(170,20)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        self.装备条件选择.clear()
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['角色熟练度：英雄', '角色熟练度：传说'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['技能栏空位：0', '技能栏空位：1', '技能栏空位：2', '技能栏空位：3', '技能栏空位：4', '技能栏空位：5', '技能栏空位：6'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['命运的抉择：数学期望', '命运的抉择：黄字+35%', '命运的抉择：爆伤+35%', '命运的抉择：白字+35%', '命运的抉择：终伤+35%', '命运的抉择：三攻+35%'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['骰子：数学期望', '骰子：1点', '骰子：2点', '骰子：3点', '骰子：4点', '骰子：5点', '骰子：6点'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['悲剧的残骸：数学期望', '悲剧的残骸：HP高于70%', '悲剧的残骸：HP70-30%', '悲剧的残骸：HP低于30%'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['先知者预言：数学期望', '先知者预言：属白+5%', '先知者预言：技攻+10%', '先知者预言：技攻+15%'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['贫瘠沙漠的遗产：无', '贫瘠沙漠的遗产：霸体', '贫瘠沙漠的遗产：无伤'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['幸运三角：数学期望', '幸运三角：7效果', '幸运三角：77效果', '幸运三角：777效果'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['擎天战甲：过充电状态', '擎天战甲：过负荷状态'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        for i in range(101):
            self.装备条件选择[-1].addItem('持续伤害适用：' + str(100 - i) + '%')
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['军神的隐秘遗产：120%以上', '军神的隐秘遗产：120-100%', '军神的隐秘遗产：100-80%', '军神的隐秘遗产：80-60%', '军神的隐秘遗产：60-40%', '军神的隐秘遗产：40%以下'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['太极天帝剑：阳', '太极天帝剑：阴'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['绿色生命的面容：无', '绿色生命的面容：阴暗面'])
        for i in range(0, len(self.装备条件选择)):
            self.装备条件选择[i].resize(170, 20)
            self.装备条件选择[i].move(940, 30 + 28 * i)

        self.百变怪选项 = QCheckBox('百变怪   ', self.main_frame1)
        self.百变怪选项.move(660, 613)
        self.百变怪选项.resize(80, 24)
        self.百变怪选项.setToolTip('<font size="3" face="宋体">仅在极速模式和套装模式下生效</font>')
        self.百变怪选项.setStyleSheet(复选框样式)

        self.计算模式选择 = MyQComboBox(self.main_frame1)
        self.计算模式选择.addItems(['计算模式：极速模式', '计算模式：套装模式', '计算模式：单件模式'])
        self.计算模式选择.move(750, 613)
        self.计算模式选择.resize(235, 24)
        self.计算模式选择.setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QComboBox:hover{background-color:rgba(65,105,225,0.8)}")
        self.计算模式选择.setToolTip('<font size="3" face="宋体">极速模式：533和3332(散搭) (不含智慧产物)<br><br>套装模式：533、3332(散搭)和3233(双防具) (不含智慧产物)<br><br>单件模式：所有组合 (不含百变怪)</font>')
        
        self.最大使用线程数 = thread_num

        #一键修正按钮添加
        一键站街修正名称 = ['站街力智', '站街三攻', '站街属强']
        for i in range(0, len(一键站街修正名称)):
            名称 = QLabel(一键站街修正名称[i], self.main_frame1)
            名称.setAlignment(Qt.AlignCenter)
            名称.move(940 + i*57, 394)
            名称.resize(52, 25)
            名称.setStyleSheet(白色字体标签)
            self.一键站街设置输入.append(QLineEdit(self.main_frame1))
            self.一键站街设置输入[i].setAlignment(Qt.AlignCenter)
            self.一键站街设置输入[i].setStyleSheet(文本框样式白)
            self.一键站街设置输入[i].resize(52, 22)
            self.一键站街设置输入[i].move(940 + i*57, 424)

        一键修正按钮 = QPushButton('一键修正面板细节', self.main_frame1)
        一键修正按钮.clicked.connect(lambda state: self.一键修正())
        一键修正按钮.move(940, 450)
        一键修正按钮.resize(166, 25)
        一键修正按钮.setStyleSheet(按钮样式)
        
        x = 1006; y = 485; 宽度 = 100; 高度 = 20; 间隔 = 4
        self.红色宠物装备 = QCheckBox('宠物装备择优', self.main_frame1)
        self.红色宠物装备.move(x, y)
        self.红色宠物装备.resize(宽度, 高度)
        self.红色宠物装备.setStyleSheet(复选框样式)
        self.红色宠物装备.setToolTip('<font size="3" face="宋体">7%黄字，7%力智，8%白字取最高值<br><br>需配合修改第三页相关选项</font>')
        self.红色宠物装备.stateChanged.connect(lambda state: self.下拉框禁用(self.红色宠物装备, self.细节选项输入[0][11]))

        self.光环自适应 = QCheckBox('光环词条择优', self.main_frame1)
        self.光环自适应.move(x, y + (高度 + 间隔) * 1)
        self.光环自适应.resize(宽度, 高度)
        self.光环自适应.setStyleSheet(复选框样式)
        self.光环自适应.setToolTip('<font size="3" face="宋体">5%黄字，5%爆伤，5%三攻取最高值<br><br>需配合修改第三页相关选项</font>')
        self.光环自适应.stateChanged.connect(lambda state: self.下拉框禁用(self.光环自适应, self.细节选项输入[1][13]))

        self.禁用存档 = QCheckBox('禁用自动存档', self.main_frame1)
        self.禁用存档.move(x, y + (高度 + 间隔) * 2)
        self.禁用存档.resize(宽度, 高度)
        self.禁用存档.setStyleSheet(复选框样式)

        self.神话排名选项 = QCheckBox('神话排名模式', self.main_frame1)
        self.神话排名选项.move(x, y + (高度 + 间隔) * 3)
        self.神话排名选项.resize(宽度, 高度)
        self.神话排名选项.setToolTip('<font size="3" face="宋体">仅显示有神话的组合，且每件神话装备只会出现一次</font>')
        self.神话排名选项.setStyleSheet(复选框样式)

        self.显示选项 = QCheckBox('亿为单位显示', self.main_frame1)
        self.显示选项.move(x, y + (高度 + 间隔) * 4)
        self.显示选项.resize(宽度, 高度)
        self.显示选项.setStyleSheet(复选框样式)

        x = 910; y = 485; 宽度 = 90; 高度 = 20; 间隔 = 4
        重置按钮 = QPushButton('全局重置', self.main_frame1)
        重置按钮.clicked.connect(lambda state: self.全局重置())
        重置按钮.move(x, y)
        重置按钮.resize(宽度, 高度)
        重置按钮.setStyleSheet(按钮样式)
        
        self.线程数选择 = MyQComboBox(self.main_frame1)
        self.线程数选择.move(x, y + (高度 + 间隔) * 1)
        self.线程数选择.resize(宽度, 高度)
        for i in range(thread_num, 0, -1):
            self.线程数选择.addItem('进程:' + str(i))

        self.存档选择 = MyQComboBox(self.main_frame1)
        self.存档选择.move(x, y + (高度 + 间隔) * 2)
        self.存档选择.resize(宽度, 高度)
        self.存档选择.currentIndexChanged.connect(lambda state :self.存档更换())

        self.智慧产物限制 = MyQComboBox(self.main_frame1)
        self.智慧产物限制.move(x, y + (高度 + 间隔) * 3)
        self.智慧产物限制.resize(宽度, 高度)
        for i in range(1, 12):
            self.智慧产物限制.addItem('改造≤{}件'.format(i))
        self.智慧产物限制.setCurrentIndex(2)
        self.智慧产物限制.setToolTip('<font size="3" face="宋体">不计智慧产物武器以及轮回SS</font>')

        self.攻击属性选项 = MyQComboBox(self.main_frame1)
        self.攻击属性选项.move(x, y + (高度 + 间隔) * 4)
        self.攻击属性选项.resize(宽度, 高度)
        self.攻击属性选项.addItem('攻击属性:全')
        self.攻击属性选项.addItem('攻击属性:火')
        self.攻击属性选项.addItem('攻击属性:冰')
        self.攻击属性选项.addItem('攻击属性:光')
        self.攻击属性选项.addItem('攻击属性:暗')

    def 界面2(self):
        # 第二个布局界面
        
        #技能等级、TP、次数输入、宠物次数
        self.BUFF输入 = QLineEdit(self.main_frame2)
        self.时间输入 = MyQComboBox(self.main_frame2)
        self.护石栏 = []
        for i in range(3):
            self.护石栏.append(MyQComboBox(self.main_frame2))
        self.符文 = []
        self.符文效果 = []

        self.觉醒选择状态 = 2
        
        self.等级调整 = []
        self.TP输入 = []
        self.次数输入 = []
        self.宠物次数 = []

        if 切装模式 == 1:
            self.技能切装 = []
        
        count = 0
        for i in self.角色属性A.技能栏:
            i.等级 = i.基础等级
            self.等级调整.append(MyQComboBox(self.main_frame2))
            self.等级调整[count].currentIndexChanged.connect(lambda state, index = count:self.等级调整标注(index))
            count += 1
            if i.是否有伤害 == 1 and i.TP上限 != 0:
                self.TP输入.append(MyQComboBox(self.main_frame2))
            else:
                self.TP输入.append('')
            if i.是否有伤害 == 1:
                self.次数输入.append(MyQComboBox(self.main_frame2))
                self.宠物次数.append(MyQComboBox(self.main_frame2))
                if 切装模式 == 1:self.技能切装.append(QCheckBox(self.main_frame2))
            else:
                self.次数输入.append('')
                self.宠物次数.append('')
                if 切装模式 == 1:self.技能切装.append('')
        
        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            if i.所在等级 == 50 or i.所在等级 == 85:
                for j in range(0, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
            else:
                for j in range(- i.基础等级, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
        
            if i.是否有伤害 == 1 and i.TP上限 != 0:
                for j in range(0, i.TP上限+1):
                    self.TP输入[序号].addItem(str(j))
        
            if i.是否有伤害 == 1:
                self.次数输入[序号].addItem('/CD')
                for j in range(0, 100):
                    self.次数输入[序号].addItem(str(j))
                    self.宠物次数[序号].addItem(str(j))
        
        #三觉强化选择
        self.一觉遮罩透明度 = QGraphicsOpacityEffect()
        self.一觉遮罩透明度.setOpacity(0.5)
        self.二觉遮罩透明度 = QGraphicsOpacityEffect()
        self.二觉遮罩透明度.setOpacity(0.0)

        横坐标=10
        纵坐标=0
        横坐标偏移量=60
        纵坐标偏移量=30
        词条框宽度=48
        行高 = 20
        
        counter=0
        for i in ["契约满级","等级调整"," TP等级","释放次数","宠物次数"]:
            x=QLabel(i, self.main_frame2)
            x.move(横坐标+横坐标偏移量-30+50*counter,纵坐标)
            x.setStyleSheet(标签样式)
            counter+=1
        
        纵坐标+=20
        
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                x=QLabel(self.main_frame2)
                x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
                x.resize(28,28)
                tempstr='<font face="宋体"><font color="#FF6666">'+i.名称 +i.备注 +'</font><br>'
                tempstr+='所在等级：'+str(i.所在等级) + '<br>'
                tempstr+='等级上限：'+str(i.等级上限)
                if i.是否主动 == 1:
                    tempstr+='<br>百分比：'+str(int(i.等效百分比(self.角色属性A.武器类型))) + '%'
                    if i.TP上限 !=0:
                        tempstr+='<br>TP成长：'+str(int(i.TP成长*100)) + '%'
                        tempstr+='<br>TP上限：'+str(i.TP上限)
                tempstr += '</font>'
                x.setToolTip(tempstr)
                x.move(横坐标,纵坐标+7)
                横坐标+=40
                x=QLabel('Lv'+str(i.基础等级), self.main_frame2)
                x.resize(40,28)
                x.move(横坐标,纵坐标+7)
                x.setStyleSheet(标签样式)
                横坐标+=40
                self.等级调整[self.角色属性A.技能序号[i.名称]].resize(词条框宽度,行高)
                self.等级调整[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标+10)
                横坐标-=80
                纵坐标+=纵坐标偏移量
        
        横坐标=横坐标+80+50
        纵坐标=30
        
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                if i.TP上限!=0:
                    self.TP输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                    self.TP输入[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标)
                纵坐标+=纵坐标偏移量
        
        横坐标=横坐标+50
        纵坐标=30
        
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                self.次数输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                self.次数输入[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标)
                self.宠物次数[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                self.宠物次数[self.角色属性A.技能序号[i.名称]].move(横坐标+50,纵坐标)
                if 切装模式 == 1:self.技能切装[self.角色属性A.技能序号[i.名称]].move(横坐标+55+词条框宽度,纵坐标 - 5)
                纵坐标+=纵坐标偏移量

        横坐标=横坐标+130
        纵坐标=20
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 0:
                x=QLabel(self.main_frame2)
                x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
                x.resize(28,28)
                tempstr='<font face="宋体"><font color="#FF6666">'+i.名称 +i.备注 +'</font><br>'
                tempstr+='所在等级：'+str(i.所在等级) + '<br>'
                tempstr+='等级上限：'+str(i.等级上限)
                tempstr += '</font>'
                x.setToolTip(tempstr)
                x.move(横坐标,纵坐标+7)
                横坐标+=40
                x=QLabel('Lv'+str(i.基础等级), self.main_frame2)
                x.resize(40,28)
                x.move(横坐标,纵坐标+7)
                x.setStyleSheet(标签样式)
                横坐标+=40
                self.等级调整[self.角色属性A.技能序号[i.名称]].resize(词条框宽度,行高)
                self.等级调整[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标+10)
                横坐标-=80
                纵坐标+=纵坐标偏移量
        
        x=横坐标+20;y=纵坐标+60
        self.觉醒选择=QLabel(self.main_frame2)
        self.觉醒选择.setPixmap(QPixmap('./ResourceFiles/img/觉醒选择.png'))
        self.觉醒选择.resize(120,100)
        self.觉醒选择.move(x,y-20)
        
        self.BUFF=QLabel(self.main_frame2)
        self.BUFF.setPixmap(QPixmap('./ResourceFiles/'+self.角色属性A.实际名称 + "/技能/BUFF.png"))
        self.BUFF.resize(28,28)
        self.BUFF.move(x-2,y-40)
        self.BUFF.setToolTip('<font size="3" face="宋体">最高值参考：' + str('%.1f' % ((self.角色属性A.主BUFF - 1) * 100)) + '</font>')
        
        self.BUFF输入.setText(str('%.1f' % ((self.角色属性A.主BUFF - 1) * 100)))
        self.BUFF输入.resize(50, 25)
        self.BUFF输入.move(x+38,y-38)
        self.BUFF输入.setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QLineEdit:hover{background-color:rgba(65,105,225,0.8)}")
        self.BUFF输入.setAlignment(Qt.AlignCenter)
        
        self.一觉图片=QLabel(self.main_frame2)
        self.一觉图片.setPixmap(self.技能图片[self.一觉序号])
        self.一觉图片.resize(28,28)
        self.一觉图片.move(x+7,y+8)
        self.二觉图片=QLabel(self.main_frame2)
        self.二觉图片.setPixmap(self.技能图片[self.二觉序号])
        self.二觉图片.resize(28,28)
        self.二觉图片.move(x+52,y+8)
        self.一觉遮罩=QPushButton(self.main_frame2)
        self.一觉遮罩.resize(38,50)
        self.一觉遮罩.move(x+2,y+5)
        self.一觉遮罩.setStyleSheet("QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}")
        self.一觉遮罩.setGraphicsEffect(self.一觉遮罩透明度)
        self.一觉遮罩.clicked.connect(lambda state, index = 1:self.强化觉醒选择(index))
        self.二觉遮罩=QPushButton(self.main_frame2)
        self.二觉遮罩.resize(38,50)
        self.二觉遮罩.move(x+47,y+5)
        self.二觉遮罩.setStyleSheet("QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}")
        self.二觉遮罩.setGraphicsEffect(self.二觉遮罩透明度)
        self.二觉遮罩.clicked.connect(lambda state, index = 2:self.强化觉醒选择(index))

        for i in range(3):
            self.护石栏[i].addItems(self.护石选项)
        self.护石类型选项 = []

        for i in range(0,9):
            self.符文.append(MyQComboBox(self.main_frame2))
            self.符文[i].addItems(self.符文选项)
            self.符文效果.append(MyQComboBox(self.main_frame2))
            self.符文效果[i].addItems(符文效果选项)
        
        横坐标=480;纵坐标=20;行高=18
        x=QLabel("护石1 (上)", self.main_frame2)
        x.move(横坐标,纵坐标 - 6)
        x.setStyleSheet(标签样式)
        y = MyQComboBox(self.main_frame2)
        y.move(横坐标 + 65,纵坐标)
        y.resize(65, 行高)
        self.护石类型选项.append(y)     
        纵坐标+=21
        self.护石栏[0].move(横坐标,纵坐标)
        self.护石栏[0].resize(130, 行高)
        self.护石栏[0].currentIndexChanged.connect(lambda state, index = 0:self.护石类型选项更新(index))
        纵坐标+=25
        for i in range(0,3):
            tempstr='符文'+str(i+1) + '选择: '
            x=QLabel(tempstr, self.main_frame2)
            x.move(横坐标,纵坐标-5)
            x.setStyleSheet(标签样式)
            纵坐标+=21
            self.符文[i].move(横坐标,纵坐标)
            self.符文[i].resize(130, 行高)
            self.符文[i].activated.connect(lambda state, index = i :self.符文技能更改(index))
            纵坐标+=21
            self.符文效果[i].move(横坐标,纵坐标)
            self.符文效果[i].resize(130,行高)
            self.符文效果[i].activated.connect(lambda state, index = i :self.符文效果更改(index))
            纵坐标+=25
        
        横坐标=650;纵坐标=20
        x=QLabel("护石2 (下)", self.main_frame2)
        x.move(横坐标,纵坐标 - 6)
        x.setStyleSheet(标签样式)
        y = MyQComboBox(self.main_frame2)
        y.move(横坐标 + 65,纵坐标)
        y.resize(65, 行高)
        self.护石类型选项.append(y)  
        纵坐标+=21
        self.护石栏[1].move(横坐标,纵坐标)
        self.护石栏[1].resize(130, 行高)
        self.护石栏[1].currentIndexChanged.connect(lambda state, index = 1:self.护石类型选项更新(index))
        纵坐标+=25
        for i in range(3,6):
            tempstr='符文'+str(i+1) + '选择: '
            x=QLabel(tempstr, self.main_frame2)
            x.move(横坐标,纵坐标-5)
            x.setStyleSheet(标签样式)
            纵坐标+=21
            self.符文[i].move(横坐标,纵坐标)
            self.符文[i].resize(130, 行高)
            纵坐标+=21
            self.符文效果[i].move(横坐标,纵坐标)
            self.符文效果[i].resize(130,行高)
            纵坐标+=25

        横坐标=820;纵坐标=20
        x=QLabel("护石3 (韩)", self.main_frame2)
        x.move(横坐标,纵坐标 - 6)
        x.setStyleSheet(标签样式)
        y = MyQComboBox(self.main_frame2)
        y.move(横坐标 + 65,纵坐标)
        y.resize(65, 行高)
        self.护石类型选项.append(y)  
        纵坐标+=21
        self.护石栏[2].move(横坐标,纵坐标)
        self.护石栏[2].resize(130, 行高)
        self.护石栏[2].currentIndexChanged.connect(lambda state, index = 2:self.护石类型选项更新(index))
        纵坐标+=25
        for i in range(6,9):
            tempstr='符文'+str(i+1) + '选择: '
            x=QLabel(tempstr, self.main_frame2)
            x.move(横坐标,纵坐标-5)
            x.setStyleSheet(标签样式)
            纵坐标+=21
            self.符文[i].move(横坐标,纵坐标)
            self.符文[i].resize(130, 行高)
            纵坐标+=21
            self.符文效果[i].move(横坐标,纵坐标)
            self.符文效果[i].resize(130,行高)
            纵坐标+=25
        
        for i in range(3):
            self.护石类型选项[i].addItem('魔界')
            self.护石类型选项[i].currentIndexChanged.connect(lambda state, index = i:self.护石描述更新(index))

        标签 = QLabel('辟邪玉计算 （鼠标悬停查看算法）',self.main_frame2)
        标签.setStyleSheet(标签样式 + 'QLabel{font-size:13px;}')
        标签.resize(300,20)
        标签.move(480,275)
        标签.setAlignment(Qt.AlignCenter)

        temp = '<font face="宋体">假定基础伤害为100，词条1=50%，词条2=50%：<br><br>'
        temp += '5%黄字增幅，佩戴前：200，佩戴后：205<br>'
        temp += '爆伤终伤白字属白力智三攻同上，黄字向下取整<br>'
        temp += '技攻辟邪玉加成等级技攻(歧路腰类)<br>不加成具体技能技攻(歧路鞋类)<br><br>'
        temp += '3%技攻增幅，佩戴前：100*1.5*1.5=225<br>佩戴后：100*1.515*1.515=229.5225<br><br>'
        temp += '属强增幅：唤醒(13)婚房(8)药剂和技能属强不享受加成<br>'
        temp += '进图触发属强单独计算向下取整<br><br>'
        temp += '<font color="#B99460">属白增幅分对应属性，计算器未作区分<br>双属性附加(星之海)需手动计算并在第三页修正<br><br>计算方式仅供参考，请以实际游戏为准！</font></font>'

        标签.setToolTip(temp)

        self.辟邪玉选择 = []
        self.辟邪玉数值 = []
        for i in range(4):
            x = MyQComboBox(self.main_frame2) 
            for j in 辟邪玉列表:
                x.addItem(j.名称)
            x.resize(200,20)
            x.move(480,300 + i * 25)
            x.currentIndexChanged.connect(lambda state, index = i:self.辟邪玉数值选项更新(index))
            self.辟邪玉选择.append(x)
            y = MyQComboBox(self.main_frame2) 
            y.resize(80,20)
            y.move(700,300 + i * 25)
            self.辟邪玉数值.append(y)

        横坐标=805;纵坐标=275
        名称 = ['奈克斯', '暗杀者', '卢克西', '守门人', '洛多斯']
        self.希洛克套装按钮 = []
        self.希洛克单件按钮 = []
        self.希洛克遮罩透明度 = []
        self.希洛克装备图标 = []
        self.希洛克选择状态 = [0] * 15 
        count = 0
        for i in 名称:
            self.希洛克套装按钮.append(QPushButton(i, self.main_frame2))
            self.希洛克套装按钮[count].setStyleSheet(按钮样式)
            self.希洛克套装按钮[count].resize(50,22)
            self.希洛克套装按钮[count].move(横坐标, 纵坐标 + 4 + count * 32)
            self.希洛克套装按钮[count].clicked.connect(lambda state, index = (count + 1) * 100:self.希洛克选择(index))
            for j in range(3):
                序号 = count * 3 + j
                图片 = QLabel(self.main_frame2)
                图片.setPixmap(QPixmap('./ResourceFiles/img/希洛克/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标+ 60 + j * 30, 纵坐标 + count * 32)
                self.希洛克装备图标.append(图片)
                self.希洛克遮罩透明度.append(QGraphicsOpacityEffect())
                self.希洛克遮罩透明度[序号].setOpacity(0.5)
                self.希洛克单件按钮.append(QPushButton(self.main_frame2))
                self.希洛克单件按钮[序号].setStyleSheet("background-color: rgb(0, 0, 0)")
                self.希洛克单件按钮[序号].resize(28, 28)
                self.希洛克单件按钮[序号].move(横坐标+ 60 + j * 30, 纵坐标 + count * 32)
                self.希洛克单件按钮[序号].setGraphicsEffect(self.希洛克遮罩透明度[序号])
                self.希洛克单件按钮[序号].clicked.connect(lambda state, index = 序号:self.希洛克选择(index))
            count += 1

        self.守门人属强 = MyQComboBox(self.main_frame2)
        for i in range(7):
            self.守门人属强.addItem('守门人属强：' + str(15 + i * 5))
        self.守门人属强.resize(120,20)
        self.守门人属强.setCurrentIndex(3)
        self.守门人属强.move(横坐标 + 12, 纵坐标 + 3 + count * 32)
    
        self.希洛克武器词条 = []
        count += 1
        self.希洛克武器词条.append(MyQComboBox(self.main_frame2))
        self.希洛克武器词条[0].addItems(['武器词条：无', '自适应最高值', '自选词条数值'])
        self.希洛克武器词条[0].resize(120,20)
        self.希洛克武器词条[0].move(横坐标 + 12, 纵坐标 + 3 + count * 32)
        self.希洛克武器词条[0].currentIndexChanged.connect(lambda state: self.希洛克武器词条更新())


        for i in range(1, 3):
            count += 1
            self.希洛克武器词条.append(MyQComboBox(self.main_frame2))
            for k in 词条属性列表:
                self.希洛克武器词条[i].addItem(k.描述)
            self.希洛克武器词条[i].resize(72,20)
            self.希洛克武器词条[i].move(横坐标 + 12, 纵坐标 + 3 + count * 32)
        
        count -= 2
        for i in range(3, 5):
            count += 1
            self.希洛克武器词条.append(MyQComboBox(self.main_frame2))
            for k in [3, 4, 5]:
                self.希洛克武器词条[i].addItem(str(k * (5 - i)) + '%')
            self.希洛克武器词条[i].resize(43,20)
            self.希洛克武器词条[i].move(横坐标 + 89, 纵坐标 + 3 + count * 32)

        for i in range(1, 5):
            self.希洛克武器词条[i].setEnabled(False)
            self.希洛克武器词条[i].setStyleSheet(不可选择下拉框样式)

        self.复选框列表 = []
        
        for i in 选项设置列表:
            # 已三觉职业移除希洛克未三觉buff属性
            if i.名称 == '未三觉希洛克buff' and "·" in self.初始属性.实际名称:
                pass
            else:
                self.复选框列表.append(QCheckBox(i.名称, self.main_frame2))
            
        counter=0

        for i in self.复选框列表:
            i.setStyleSheet(复选框样式)
            i.resize(125,20)
            i.move(980,10 + counter * 24)
            if counter < 7 and 调试开关 == 0:
                i.setChecked(True)
            counter+=1
        
        sign = 0
        if self.初始属性.远古记忆 != -1:
            i = QLabel(self.main_frame2)
            i.setPixmap(QPixmap('./ResourceFiles/img/远古记忆.png'))
            i.resize(28,28)
            i.move(1000, 15 + counter * 24)
            self.远古记忆 = MyQComboBox(self.main_frame2)
            self.远古记忆.currentIndexChanged.connect(lambda state, index = 100:self.等级调整标注(index))
            for i in range(12):
                self.远古记忆.addItem(str(i))
            self.远古记忆.resize(50,20)
            self.远古记忆.move(1035, 19 + counter * 24)
            sign = 30

        if self.初始属性.刀魂之卡赞 != -1:
            i = QLabel(self.main_frame2)
            i.setPixmap(QPixmap('./ResourceFiles/img/刀魂之卡赞.png'))
            i.resize(28,28)
            i.move(1000, 15 + sign + counter * 24)
            self.刀魂之卡赞 = MyQComboBox(self.main_frame2)
            self.刀魂之卡赞.currentIndexChanged.connect(lambda state, index = 200:self.等级调整标注(index))
            for i in range(12):
                self.刀魂之卡赞.addItem(str(i))
            self.刀魂之卡赞.resize(50,20)
            self.刀魂之卡赞.move(1035, 19 + sign + counter * 24)
        
        x=QLabel("攻击目标：", self.main_frame2)
        x.move(660, self.height() - 62)
        x.resize(70, 20)
        x.setStyleSheet(标签样式)
        self.攻击目标 = MyQComboBox(self.main_frame2)
        for i in 攻击目标:
            self.攻击目标.addItem(i[0])
        self.攻击目标.move(730, self.height() - 63)
        self.攻击目标.resize(110, 20)
        x=QLabel("时间输入：", self.main_frame2)
        x.move(850, self.height() - 62)
        x.resize(70, 20)
        x.setStyleSheet(标签样式)
        self.时间输入.addItems(['1', '10', '15', '20', '25', '30', '60'])
        self.时间输入.move(920, self.height() - 63)
        self.时间输入.resize(50, 20)

        self.计算按钮2 = QPushButton('开始计算', self.main_frame2)
        self.计算按钮2.clicked.connect(lambda state: self.计算())
        self.计算按钮2.move(990, self.height() - 70)
        self.计算按钮2.resize(100, 30)
        self.计算按钮2.setStyleSheet(按钮样式)

    def 界面3(self):
        # 第三个布局界面
        self.属性设置输入 = []
        self.细节选项输入 = []

        self.列名称 = []
        self.行名称 = []

        名称 = QLabel(表头名称1, self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(白色字体标签)
        名称.resize(80, 25)
        名称.move(10, 文本框间隔)
       
        m = -1
        for i in 列名称1:
            m += 1
            名称 = QLabel(i, self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(白色字体标签)
            if i == "选项":
                名称.resize(文本框宽度 * 2 + 5, 25)
            else:
                名称.resize(文本框宽度, 25)
            名称.move(95 + m * (文本框宽度 + 5), 文本框间隔)
            self.列名称.append(i)
    
        n = -1
        for j in 行名称1.keys():
            n += 1
            名称 = QLabel(j, self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            if 行名称1[j] == 1:
                名称.setStyleSheet(黄色字体标签)
            else:
                名称.setStyleSheet(白色字体标签)
            名称.resize(80, 25)
            名称.move(10, 文本框间隔 + 30 + n * 30)
            self.行名称.append(j)

        m = -1
        for i in 列名称1:
            m += 1
            templist = []
            n = -1
            for j in 行名称1.keys():
                n += 1
                if i == "选项":
                    templist.append(MyQComboBox(self.main_frame3))
                    templist[n].resize(文本框宽度 * 2 + 5, 22)
                    if 行1选项[j][0] != -1: 
                        templist[n].addItem('无') 
                        for s_id in 行1选项[j]:
                            templist[n].addItem(细节选项列表[s_id].描述)
                else:
                    templist.append(QLineEdit(self.main_frame3))
                    if 行名称1[j] == 1:
                        templist[n].setStyleSheet(文本框样式黄)
                    else:
                        templist[n].setStyleSheet(文本框样式白)
                    templist[n].resize(文本框宽度, 22)
                    templist[n].setAlignment(Qt.AlignCenter)
                templist[n].move(95 + m * (文本框宽度 + 5), 文本框间隔 + 30 + n * 30)
            if i == "选项":
                self.细节选项输入.append(templist)
            else:
                self.属性设置输入.append(templist)

        名称 = QLabel(表头名称2, self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(白色字体标签)
        名称.resize(80, 25)
        名称.move(160 + (len(列名称1) + 1) * 文本框宽度, 文本框间隔)

        m = -1
        for i in 列名称2:
            m += 1
            名称 = QLabel(i, self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(白色字体标签)
            if i == "技能":
                名称.resize(155, 25)
            elif i == "选项":
                名称.resize(文本框宽度 * 2 + 5, 25)
            else:
                名称.resize(文本框宽度, 25)
            名称.move(245 + (len(列名称1) + 1) * 文本框宽度 + m * (文本框宽度 + 5),  文本框间隔)
            self.列名称.append(i)
            if i == "选项":
                m += 1
    
        n = -1
        for j in 行名称2.keys():
            n += 1
            名称 = QLabel(j, self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            if 行名称2[j] == 1:
                名称.setStyleSheet(黄色字体标签)
            else:
                名称.setStyleSheet(白色字体标签)
            名称.resize(80, 25)
            名称.move(160 + (len(列名称1) + 1) * 文本框宽度, 文本框间隔 + 30 + n * 30)
            self.行名称.append(j)

        m = -1
        for i in 列名称2:
            m += 1
            templist = []
            n = -1
            for j in 行名称2.keys():
                n += 1
                if i == "选项":
                    templist.append(MyQComboBox(self.main_frame3))
                    templist[n].resize(文本框宽度 * 2 + 5, 22)
                    if 行2选项[j][0] != -1: 
                        templist[n].addItem('无') 
                        for s_id in 行2选项[j]:
                            templist[n].addItem(细节选项列表[s_id].描述)
                elif i == "技能":
                    templist.append(MyQComboBox(self.main_frame3))
                    templist[n].resize(155, 22)
                    if 行2技能[j][0] == -1: 
                        pass
                    elif 行2技能[j][0] == 999:
                        templist[n].addItem('无')  
                        for skill in self.角色属性A.技能栏:
                            templist[n].addItem(skill.名称 + 'Lv+1')
                    else:
                        templist[n].addItem('无') 
                        for s_id in 行2技能[j]:
                            templist[n].addItem(细节选项列表[s_id].描述)
                else:
                    templist.append(QLineEdit(self.main_frame3))
                    if 行名称2[j] == 1:
                        templist[n].setStyleSheet(文本框样式黄)
                    else:
                        templist[n].setStyleSheet(文本框样式白)
                    templist[n].resize(文本框宽度, 22)
                    templist[n].setAlignment(Qt.AlignCenter)
                templist[n].move(245 + (len(列名称1) + 1) * 文本框宽度 + m * (文本框宽度 + 5), 文本框间隔 + 30 + n * 30)
            if i in ["选项", "技能"]:
                self.细节选项输入.append(templist)
                m += 1
            else:
                self.属性设置输入.append(templist)

        self.修正列表名称 = ['力智%', '三攻%', '黄字', '白字', '属白', '爆伤', '终伤', '技攻']
        
        距离 = 30
        templist = []
        
        for i in range(0, len(self.修正列表名称)):
            名称 = QLabel(self.修正列表名称[i],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(白色字体标签)
            名称.resize(50, 25)
            名称.move(距离 + i*55, 570)
            templist.append(QLineEdit(self.main_frame3))
            templist[i].setAlignment(Qt.AlignCenter)
            templist[i].setStyleSheet(文本框样式白)
            templist[i].resize(50, 22)
            templist[i].move(距离 + i*55, 610)
        self.属性设置输入.append(templist)
        
        count = 0
        self.时装选项 = []
        for i in ['头部', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋']:
            名称 = QLabel(i,self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(白色字体标签)
            名称.resize(50, 25)
            名称.move(520 + count*55, 570)
            self.时装选项.append(MyQComboBox(self.main_frame3))
            self.时装选项[count].addItems(['高级', '节日', '稀有', '神器'])
            self.时装选项[count].resize(50, 22)
            self.时装选项[count].move(520 + count*55, 610)
            self.时装选项[count].currentIndexChanged.connect(lambda state, index = count:self.时装选项更新(index))
            count += 1

        self.时装选项.append(MyQComboBox(self.main_frame3))
        self.时装选项[8].addItems(['高级套装[8]', '节日套装[8]', '稀有套装[8]', '神器套装[8]'])
        self.时装选项[8].resize(100, 22)
        self.时装选项[8].move(990, 570)
        self.时装选项[8].currentIndexChanged.connect(lambda state, index = 8:self.时装选项更新(index))

        self.计算按钮3 = QPushButton('开始计算', self.main_frame3)
        self.计算按钮3.clicked.connect(lambda state: self.计算())
        self.计算按钮3.move(990, 610)
        self.计算按钮3.resize(100, 30)
        self.计算按钮3.setStyleSheet(按钮样式)
        
    def 界面5(self):
        #第五个布局
        标签 = QLabel('单件选择', self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(240, 25)
        标签.move(70, 20)

        标签 = QLabel('锁定', self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(70, 25)
        标签.move(10, 20)

        self.图片显示 = []
        self.图片列表 = []

        count = 0
        self.自选装备 = []
        if 切装模式 == 1:
            self.装备切装 = []
            self.切装修正属性 = []
        self.装备锁定 = []
        for i in 部位列表:
            锁定选择 = QCheckBox(i, self.main_frame5)
            锁定选择.setStyleSheet(复选框样式)
            锁定选择.resize(70, 22)
            锁定选择.move(10, 50 + 30 * count)
            self.装备锁定.append(锁定选择)
            self.自选装备.append(MyQComboBox(self.main_frame5))
            self.自选装备[count].resize(220, 22)
            self.自选装备[count].move(90, 50 + 30 * count)
            self.自选装备[count].currentIndexChanged.connect(lambda state, index = count:self.自选装备更改(index))
            if 切装模式 == 1:
                self.装备切装.append(QCheckBox(self.main_frame5))
                self.装备切装[count].move(320, 45 + 30 * count)
            for j in 装备列表:
                if j.部位 == i:
                    if i == '武器':
                        if j.类型 in self.角色属性A.武器选项:
                            self.自选装备[count].addItem(j.名称)
                    else:
                        self.自选装备[count].addItem(j.名称)
            count += 1
        
        if 切装模式 == 1:
            num = 0
            for i in ['力量', '智力', '物攻', '魔攻', '独立', '属强']:
                标签 = QLabel(i, self.main_frame5)
                标签.setAlignment(Qt.AlignCenter)
                标签.setStyleSheet(标签样式)
                标签.resize(45, 25)
                标签.move(30 + 50 * num, 60 + 30 * count)
                self.切装修正属性.append(QLineEdit(self.main_frame5))
                self.切装修正属性[num].setAlignment(Qt.AlignCenter)
                self.切装修正属性[num].setStyleSheet(文本框样式白)
                self.切装修正属性[num].resize(45, 22)
                self.切装修正属性[num].move(30 + 50 * num, 85 + 30 * count)
                num += 1

        self.计算标识 = 1
        
        横坐标 = 355
        标签 = QLabel('批量选择', self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(160, 25)
        标签.move(横坐标, 20)

        套装类型 = ['防具', '首饰', '特殊', '上链左', '镯下右', '环鞋指']
        count = 0
        self.自选套装 = []
        for i in 套装类型:
            self.自选套装.append(MyQComboBox(self.main_frame5))
            套装名称 = []
            for j in 套装列表:
                if j.名称 not in 套装名称 and j.类型 == i:
                    套装名称.append(j.名称)
            self.自选套装[count].addItems(套装名称)
            self.自选套装[count].resize(160, 22)
            self.自选套装[count].move(横坐标, 50 + 30 * count)
            self.自选套装[count].activated.connect(lambda state, index = count:self.自选套装更改(index))
            count += 1
      
        self.神话部位选项 = MyQComboBox(self.main_frame5)
        self.神话部位选项.addItems(['神话部位：无', '神话部位：上衣', '神话部位：手镯', '神话部位：耳环'])
        self.神话部位选项.resize(160, 22)
        self.神话部位选项.move(横坐标, 50 + 30 * count)
        self.神话部位选项.activated.connect(lambda state:self.神话部位更改())
        
        count += 1
        self.改造套装 = MyQComboBox(self.main_frame5)
        for n in 装备列表:
            try:
                self.改造套装.addItem(n.关联套装)
            except:
                pass
        self.改造套装.resize(160, 22)
        self.改造套装.move(横坐标, 50 + 30 * count)
        self.改造套装.activated.connect(lambda state:self.改造套装更改())

        count += 1   
        self.转甲选项 = QCheckBox('85SS转甲',self.main_frame5)
        self.转甲选项.resize(80, 22)
        self.转甲选项.move(横坐标 + 40, 50 + 30 * count)
        self.转甲选项.setChecked(True)
        self.转甲选项.setStyleSheet(复选框样式)
        self.转甲选项.stateChanged.connect(lambda state: self.自选计算(1))

        count += 1
        #一键修正按钮添加
        一键站街修正名称 = ['站街力智', '站街三攻', '站街属强']
        for i in range(0, len(一键站街修正名称)):
            名称 = QLabel(一键站街修正名称[i], self.main_frame5)
            名称.setAlignment(Qt.AlignCenter)
            名称.move(横坐标 - 5 + i*57, 50 + 30 * count)
            名称.resize(52, 25)
            名称.setStyleSheet(白色字体标签)
            self.一键站街设置输入.append(QLineEdit(self.main_frame5))
            self.一键站街设置输入[i + 3].setAlignment(Qt.AlignCenter)
            self.一键站街设置输入[i + 3].setStyleSheet(文本框样式白)
            self.一键站街设置输入[i + 3].resize(52, 22)
            self.一键站街设置输入[i + 3].move(横坐标 - 5 + i*57, 80 + 30 * count)
        
        count += 2
        一键修正按钮 = QPushButton('一键修正面板细节', self.main_frame5)
        一键修正按钮.clicked.connect(lambda state: self.一键修正(1))
        一键修正按钮.move(横坐标 - 5 , 50 + 30 * count)
        一键修正按钮.resize(165, 25)
        一键修正按钮.setStyleSheet(按钮样式)

        标签 = QLabel('辟邪玉提升率(理论值仅供参考)', self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(200, 25)
        标签.move(525, 20)

        self.辟邪玉提升率1 = []
        self.辟邪玉提升率2 = []
        count = 0
        for i in 辟邪玉列表:
            if i.名称 != '无':
                if i.最大值 != 1:
                    temp = i.名称 + '+' + str(i.最大值) + '%'
                else:
                    temp = i.名称 + '+' + str(i.最大值)
                self.辟邪玉提升率1.append(QLabel(temp, self.main_frame5))
                self.辟邪玉提升率1[count].setAlignment(Qt.AlignCenter)
                self.辟邪玉提升率1[count].setStyleSheet(标签样式)
                self.辟邪玉提升率1[count].resize(180, 25)
                self.辟邪玉提升率1[count].move(520, 50 + 30 * count)
                self.辟邪玉提升率2.append(QLabel('0.00%', self.main_frame5))
                self.辟邪玉提升率2[count].setAlignment(Qt.AlignCenter)
                self.辟邪玉提升率2[count].setStyleSheet(标签样式)
                self.辟邪玉提升率2[count].resize(30, 25)
                self.辟邪玉提升率2[count].move(710, 50 + 30 * count)
                count += 1

        初始x = 805
        初始y = 20
        图片显示 = QLabel(self.main_frame5)
        图片显示.setPixmap(self.输出背景图片)
        图片显示.setAlignment(Qt.AlignTop)
        图片显示.resize(268, 564)
        图片显示.move(初始x, 初始y)
        人物 = QLabel(self.main_frame5)
        图片 = QPixmap('./ResourceFiles/'+self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(初始x + 90 + int(45 - 图片.width() / 2), 初始y + 40)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)

        偏移量=187
        x坐标=[32,0,0,32,0,偏移量,偏移量+32,偏移量+32,偏移量,偏移量,偏移量+32,32]
        y坐标=[0,0,32,32,64,0,0,32,64,32,64,64]
        
        for i in range(12):
            self.图片列表.append(self.装备图片[装备序号[self.自选装备[i].currentText()]])
            self.图片显示.append(QLabel(self.main_frame5))
            self.图片显示[i].setMovie(self.图片列表[i])
            self.图片列表[i].start()
            self.图片显示[i].resize(26,26)
            self.图片显示[i].move(初始x + 10 + x坐标[i], 初始y + 31 + y坐标[i])
            self.图片显示[i].setAlignment(Qt.AlignCenter) 


        self.面板显示=[]
        for i in range(0,17):
            self.面板显示.append(QLabel(self.main_frame5)) 

        const = 139 + 初始y
        count = 0
        for i in  [9,10,0,1]:
            self.面板显示[i].move(20 + 初始x,const + count * 18)
            count += 1
        count = 0
        for i in  [11,12,2,3]:
            self.面板显示[i].move(150 + 初始x,const + count * 18)
            count += 1
        self.面板显示[4].move(150 + 初始x,const + count * 18)
        count = 5
        for i in  [5,6,7,8]:
            self.面板显示[i].move(150 + 初始x,const + count * 18)
            count += 1
        count = 5
        for i in  [13,14,15,16]:
            self.面板显示[i].move(20 + 初始x,const + count * 18)
            count += 1
        for i in range(0,len(self.面板显示)):
            if i >= 9:
                self.面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            else:
                self.面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(150,255,30)}")
            self.面板显示[i].resize(100,18)
            self.面板显示[i].setAlignment(Qt.AlignRight)  

        self.词条显示=[]
        for i in range(0,12):
            self.词条显示.append(QLabel(self.main_frame5))     

        j = 312 + 初始y
        for i in self.词条显示:
            i.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            i.move(5 + 初始x, j)
            i.resize(180,17)
            i.setAlignment(Qt.AlignLeft)
            j+=17

        self.总伤害=QLabel(self.main_frame5)
        self.总伤害.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        self.总伤害.resize(250,36)
        self.总伤害.move(10 + 初始x, 520 + 初始y)
        self.总伤害.setAlignment(Qt.AlignCenter) 

        self.套装名称显示=[]
        for i in range(0,10):
            self.套装名称显示.append(QLabel(self.main_frame5))
            self.套装名称显示[i].move(114 + 初始x, 133 + 180 + 20 * i + 初始y)
            self.套装名称显示[i].resize(150,18)
            self.套装名称显示[i].setAlignment(Qt.AlignCenter)   

        自选计算按钮 = QPushButton('查看详情', self.main_frame5)
        自选计算按钮.clicked.connect(lambda state: self.自选计算())
        自选计算按钮.move(995, 610)
        自选计算按钮.resize(80, 28)
        自选计算按钮.setStyleSheet(按钮样式)
        
        self.基准值 = []

        设置基准值 = QPushButton('设为基准', self.main_frame5)
        设置基准值.clicked.connect(lambda state: self.基准值设置())
        设置基准值.move(900, 610)
        设置基准值.resize(80, 28)
        设置基准值.setStyleSheet(按钮样式)

        清空基准值 = QPushButton('清空基准', self.main_frame5)
        清空基准值.clicked.connect(lambda state: self.基准值设置(1))
        清空基准值.move(805, 610)
        清空基准值.resize(80, 28)
        清空基准值.setStyleSheet(按钮样式)

        self.对比格式 = QCheckBox('数值对比', self.main_frame5)
        self.对比格式.stateChanged.connect(lambda state: self.自选计算(1))
        self.对比格式.move(720, 612)
        self.对比格式.resize(70, 24)
        self.对比格式.setStyleSheet(复选框样式)
    

    def 下拉框禁用(self, a, b):
        if a.isChecked():
            b.setEnabled(False)
            b.setStyleSheet(不可选择下拉框样式)
        else:
            b.setEnabled(True)
            b.setStyleSheet(下拉框样式)            

    def 希洛克武器词条更新(self):
        if self.希洛克武器词条[0].currentIndex() != 2:
            for i in range(1, 5):
                self.希洛克武器词条[i].setEnabled(False)
                self.希洛克武器词条[i].setStyleSheet(不可选择下拉框样式)
        else:
            for i in range(1, 5):
                self.希洛克武器词条[i].setEnabled(True)
                self.希洛克武器词条[i].setStyleSheet(下拉框样式)

    def 护石描述更新(self, x):
        try:
            self.护石栏[x].setToolTip('<font face="宋体">' + self.初始属性.技能栏[self.初始属性.技能序号[self.护石栏[x].currentText()]].护石描述(self.护石类型选项[x].currentIndex()) + '</font></font>')
        except:
            self.护石栏[x].setToolTip('<font face="宋体">暂缺</font>')
                    
    def 护石类型选项更新(self, x):
        self.护石类型选项[x].clear()
        if self.护石栏[x].currentText() != '无':
            try:
                self.护石类型选项[x].addItems(self.初始属性.技能栏[self.初始属性.技能序号[self.护石栏[x].currentText()]].护石选项)
            except:
                self.护石类型选项[x].addItem('魔界')
                self.护石栏[x].setCurrentIndex(0)
        else:
            self.护石类型选项[x].addItem('魔界')

    def 符文技能更改(self, i):
        if i == 0:
            for i in range(1, 9):
                self.符文[i].setCurrentIndex(self.符文[0].currentIndex())
        else:
            self.符文[i + 3].setCurrentIndex(self.符文[i].currentIndex())
            self.符文[i + 6].setCurrentIndex(self.符文[i].currentIndex())

    def 符文效果更改(self, i):
        self.符文效果[i + 3].setCurrentIndex(self.符文效果[i].currentIndex())
        self.符文效果[i + 6].setCurrentIndex(self.符文效果[i].currentIndex())

    def 等级调整标注(self, index):
        低等级 = "QComboBox{font-size:12px;color:white;background-color:rgba(34,157,70,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(5,185,65,0.8)} QComboBox QAbstractItemView::item {height: 18px;}"
        未调整 = "QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(65,105,225,0.8)} QComboBox QAbstractItemView::item {height: 18px;}"
        高等级 = "QComboBox{font-size:12px;color:white;background-color:rgba(197,34,70,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(225,5,65,0.8)} QComboBox QAbstractItemView::item {height: 18px;}"
        警告 = "技能等级调整指调整<font color='#FF0000'>学习等级</font>(非实际等级)<br>一般用于修正天空下装技能，一二觉时装切装<br>其余等级加成会自动计算，请勿手动调整"
        if index < 100:
            try:
                x = int(self.等级调整[index].currentText())
            except:
                x = 1
            if x > 0:
                self.等级调整[index].setStyleSheet(高等级)
            if x > 1:
                QMessageBox.information(self,"警告",  警告) 
            if x < 0:
                self.等级调整[index].setStyleSheet(低等级)
            if x == 0:
                self.等级调整[index].setStyleSheet(未调整)
        elif index == 100:
            try:
                x = int(self.远古记忆.currentText())
            except:
                x = 11
            if x == 11:
                self.远古记忆.setStyleSheet(高等级)
            if x < 10:
                self.远古记忆.setStyleSheet(低等级)
            if x == 10:
                self.远古记忆.setStyleSheet(未调整)
        elif index == 200:
            try:
                x = int(self.刀魂之卡赞.currentText())
            except:
                x = 11
            if x == 11:
                self.刀魂之卡赞.setStyleSheet(高等级)
            if x < 10:
                self.刀魂之卡赞.setStyleSheet(低等级)
            if x == 10:
                self.刀魂之卡赞.setStyleSheet(未调整)      
            
    def 时装选项更新(self, index):
        if index == 8:
            count = 0
            for i in self.时装选项:
                if count != 8:
                    i.setCurrentIndex(self.时装选项[8].currentIndex())
                count += 1
            return
        else:
            力量, 智力, 属强 = 0, 0, 0
            套装字典 = {'高级':0, '节日':0, '稀有':0, '神器':0}
            for i in range(8):
                套装字典[self.时装选项[i].currentText()] = 套装字典.get(self.时装选项[i].currentText(), 0) + 1
            #套装属性
            神器 = 套装字典['神器']
            稀有 = 套装字典['稀有'] + 神器
            if 套装字典['高级'] >= 3:
                力量 += 10; 智力 += 10
            if 稀有 >= 3 and 神器 < 3:
                力量 += 40; 智力 += 40
            if 套装字典['神器'] >= 3:
                力量 += 50; 智力 += 50
            if 套装字典['高级'] >= 8:
                力量 += 10; 智力 += 10
            if 套装字典['节日'] >= 8:
                力量 += 25; 智力 += 25
            if 稀有 >= 8 and 神器 < 8:
                力量 += 40; 智力 += 40; 属强 += 6
            if 套装字典['神器'] >= 8:
                力量 += 50; 智力 += 50; 属强 += 10
            数据 = [45, 45, 55, 65]
            智力 += 数据[self.时装选项[0].currentIndex()] #头部
            智力 += 数据[self.时装选项[1].currentIndex()] #帽子
            力量 += 数据[self.时装选项[7].currentIndex()] #鞋子
            数据 = [45, 45, 55, 65]
            力量 += 数据[self.时装选项[5].currentIndex()] #腰带
            数据 = [0, 6, 0, 0]
            属强 += 数据[self.时装选项[4].currentIndex()] #上衣

            数据 = [0, 20, 0, 0]
            智力 += 数据[self.时装选项[6].currentIndex()] #下装
            力量 += 数据[self.时装选项[6].currentIndex()] #下装

            self.属性设置输入[6][16].setText(str(max(力量, 智力)))
            self.属性设置输入[8][16].setText(str(属强 if 属强 != 0 else ''))
 

    def 载入配置(self, path = 'set'):
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ3.ini', 'r', encoding='utf-8').readlines()
            self.称号.setCurrentIndex(int(setfile[0].replace('\n', '')))
            self.宠物.setCurrentIndex(int(setfile[1].replace('\n', '')))
            self.计算模式选择.setCurrentIndex(int(setfile[2].replace('\n', '')))
            # 百变怪 && 神话排名 && 显示选项 && 时装选项
            if int(setfile[3].replace('\n', '')):
                self.百变怪选项.setChecked(True)
            if int(setfile[4].replace('\n', '')):
                self.神话排名选项.setChecked(True)
            if int(setfile[5].replace('\n', '')):
                self.显示选项.setChecked(True)
            for i in range(0,len(self.时装选项)):
                self.时装选项[i].setCurrentIndex(int(setfile[i + 6].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/attr.ini', 'r', encoding='utf-8').readlines()
            for i in range(0, len(self.列名称) - 2):
                for j in range(0, len(self.属性设置输入[i])):
                    self.属性设置输入[i][j].setText(setfile[i].replace('\n', '').split(',')[j])
            for i in range(3):
                for j in range(0, 17):
                    self.细节选项输入[i][j].setCurrentIndex(int(setfile[len(self.列名称) - 2 + i].replace('\n', '').split(',')[j]))
        except:
            pass

        try:
            self.批量选择(0)#先清空
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ.ini', 'r', encoding='utf-8').readlines()
            for i in range(0, len(装备列表)):
                if setfile[i].replace('\n', '') == '1':
                    self.装备图标点击事件(i, 1)
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ1.ini', 'r', encoding='utf-8').readlines()
            for i in range(0,len(self.装备打造选项)):
                self.装备打造选项[i].setCurrentIndex(int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ2.ini', 'r', encoding='utf-8').readlines()
            for i in range(0,len(self.装备条件选择)):
                self.装备条件选择[i].setCurrentIndex(int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill1.ini', 'r', encoding='utf-8').readlines()
            num = 0
            self.BUFF输入.setText(setfile[num].replace('\n', '')); num += 1
            self.时间输入.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.护石栏[0].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.护石栏[1].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            for i in range(0,6):
                self.符文[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.符文效果[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.强化觉醒选择(int(setfile[num].replace('\n', ''))); num += 1
            if self.初始属性.远古记忆 != -1:
                self.远古记忆.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            if self.初始属性.刀魂之卡赞 != -1:
                self.刀魂之卡赞.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.护石栏[2].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            for i in range(6,9):
                self.符文[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.符文效果[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            for i in range(3):
                self.护石类型选项[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            for i in range(5):
                self.希洛克武器词条[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill2.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in self.角色属性A.技能栏:
                序号 = self.角色属性A.技能序号[i.名称]
                self.等级调整[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                if i.是否有伤害 == 1 and i.TP上限 != 0:
                    self.TP输入[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                if i.是否有伤害 == 1:
                    self.次数输入[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                    self.宠物次数[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill3.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(4):
                self.辟邪玉选择[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.辟邪玉数值[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.希洛克选择(0, 1)
            for i in range(15):
                if setfile[num].replace('\n', '') == '1':
                    self.希洛克选择(i)
                num += 1
            self.守门人属强.setCurrentIndex(int(setfile[num].replace('\n', '')));num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill0.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(len(self.复选框列表)):
                if int(setfile[num].replace('\n', '')) == 1:
                    self.复选框列表[i].setChecked(True)
                else:
                    self.复选框列表[i].setChecked(False)
                num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ4.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(4 * 35):
                self.神话属性选项[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ5.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(12):
                self.自选装备[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            for i in range(12):
                if int(setfile[num].replace('\n', '')) == 1:
                    self.装备锁定[i].setChecked(True)
                else:
                    self.装备锁定[i].setChecked(False)
                num += 1
        except:
            pass
        
        if 切装模式 == 1:
            try:
                setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ6.ini', 'r', encoding='utf-8').readlines()
                num = 0
                for i in range(12):
                    if setfile[num].replace('\n', '') == '1': self.装备切装[i].setChecked(True)
                    num += 1
                for i in self.角色属性A.技能栏:
                    序号 = self.角色属性A.技能序号[i.名称]
                    if i.是否有伤害 == 1:
                        if setfile[num].replace('\n', '') == '1': self.技能切装[序号].setChecked(True)
                        num += 1
            except:
                pass

    def 保存配置(self, path = 'set'):
        if self.禁用存档.isChecked():
            return
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ3.ini', 'w', encoding='utf-8')
            setfile.write(str(self.称号.currentIndex()) + '\n')
            setfile.write(str(self.宠物.currentIndex()) + '\n')
            setfile.write(str(self.计算模式选择.currentIndex()) + '\n')
            # 百变怪 && 神话排名 && 显示选项 && 时装选择
            setfile.write(str(int(self.百变怪选项.isChecked())) + '\n')
            setfile.write(str(int(self.神话排名选项.isChecked())) + '\n')
            setfile.write(str(int(self.显示选项.isChecked())) + '\n')
            for i in range(0, len(self.时装选项)):
                setfile.write(str(self.时装选项[i].currentIndex()) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/attr.ini', 'w', encoding='utf-8')
            for i in range(0, len(self.列名称) - 2):
                for j in range(0, len(self.属性设置输入[i])):
                    setfile.write(self.属性设置输入[i][j].text() + ',')
                setfile.write('\n')
            for i in range(3):
                for j in range(0, 17):
                    setfile.write(str(self.细节选项输入[i][j].currentIndex()) + ',')
                setfile.write('\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ.ini', 'w', encoding='utf-8')
            for i in range(0, len(装备列表)):
                setfile.write(str(self.装备选择状态[i]) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ1.ini', 'w', encoding='utf-8')
            for i in range(0,len(self.装备打造选项)):
                setfile.write(str(self.装备打造选项[i].currentIndex()) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ2.ini', 'w', encoding='utf-8')
            for i in range(0,len(self.装备条件选择)):
                setfile.write(str(self.装备条件选择[i].currentIndex()) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill1.ini', 'w', encoding='utf-8')
            setfile.write(self.BUFF输入.text() + '\n')
            setfile.write(str(self.时间输入.currentIndex()) + '\n')
            setfile.write(str(self.护石栏[0].currentIndex()) + '\n')
            setfile.write(str(self.护石栏[1].currentIndex()) + '\n')
            for i in range(0,6):
                setfile.write(str(self.符文[i].currentIndex()) + '\n')
                setfile.write(str(self.符文效果[i].currentIndex()) + '\n')
            setfile.write(str(self.觉醒选择状态) + '\n')
            if self.初始属性.远古记忆 != -1:
                setfile.write(str(self.远古记忆.currentIndex()) + '\n')
            if self.初始属性.刀魂之卡赞 != -1:
                setfile.write(str(self.刀魂之卡赞.currentIndex()) + '\n')
            setfile.write(str(self.护石栏[2].currentIndex()) + '\n')
            for i in range(6,9):
                setfile.write(str(self.符文[i].currentIndex()) + '\n')
                setfile.write(str(self.符文效果[i].currentIndex()) + '\n')
            for i in range(3):
                setfile.write(str(self.护石类型选项[i].currentIndex()) + '\n')
            for i in range(5):
                setfile.write(str(self.希洛克武器词条[i].currentIndex()) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill2.ini', 'w', encoding='utf-8')
            for i in self.角色属性A.技能栏:
                序号 = self.角色属性A.技能序号[i.名称]
                setfile.write(str(self.等级调整[序号].currentIndex()) + '\n')
                if i.是否有伤害 == 1 and i.TP上限 != 0:
                    setfile.write(str(self.TP输入[序号].currentIndex()) + '\n')
                if i.是否有伤害 == 1:
                    setfile.write(str(self.次数输入[序号].currentIndex()) + '\n')
                    setfile.write(str(self.宠物次数[序号].currentIndex()) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill3.ini', 'w', encoding='utf-8')
            for i in range(4):
                setfile.write(str(self.辟邪玉选择[i].currentIndex()) + '\n')
                setfile.write(str(self.辟邪玉数值[i].currentIndex()) + '\n')
            for i in range(15):
                setfile.write(str(self.希洛克选择状态[i]) + '\n')
            setfile.write(str(self.守门人属强.currentIndex()) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill0.ini', 'w', encoding='utf-8')
            for i in range(len(self.复选框列表)):
                if self.复选框列表[i].isChecked():
                    setfile.write('1\n')
                else:
                    setfile.write('0\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ4.ini', 'w', encoding='utf-8')
            for i in range(4 * 35):
                setfile.write(str(self.神话属性选项[i].currentIndex()) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ5.ini', 'w', encoding='utf-8')
            for i in range(12):
                setfile.write(str(self.自选装备[i].currentIndex()) + '\n')
            for i in range(12):
                setfile.write(str(1 if self.装备锁定[i].isChecked() else 0) + '\n')
        except:
            pass
        
        if 切装模式 == 1:
            try:
                setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ6.ini', 'w', encoding='utf-8')
                for i in self.装备切装:
                    if i.isChecked():
                        setfile.write('1\n')
                    else:
                        setfile.write('0\n')
    
                for i in self.角色属性A.技能栏:
                    序号 = self.角色属性A.技能序号[i.名称]
                    if i.是否有伤害 == 1:
                        if self.技能切装[序号].isChecked():
                            setfile.write('1\n')
                        else:
                            setfile.write('0\n')
            except:
                pass
    
    #一键修正计算
    def 一键修正(self, x = 0):
        if x == 0:
            if self.组合计算(2) == 0:
                QMessageBox.information(self,"错误",  "请勾选齐全身上穿戴的装备")
                return
            if self.组合计算(2) > 1:
                QMessageBox.information(self,"错误",  "请勿勾选身上未穿戴的装备")
                return
        self.修正套装计算(x)
        self.角色属性B = deepcopy(self.初始属性)
        self.角色属性B.技能栏 = deepcopy(self.初始属性.技能栏)
        self.输入属性(self.角色属性B)
        self.角色属性B.穿戴装备计算套装(self.有效穿戴组合[0])
        for i in self.角色属性B.装备栏:
            装备列表[装备序号[i]].城镇属性(self.角色属性B)
        for i in self.角色属性B.套装栏:
            套装列表[套装序号[i]].城镇属性(self.角色属性B)
        self.角色属性B.装备基础()
        self.角色属性B.被动倍率计算()
        self.面板修正(self.角色属性B.类型, x * 3)

    def 面板修正(self, 类型, x):
        数据 = []
        原始数据 = []
        名称 = ['力智', '三攻', '属强']
        for i in range(3):
            try:
                if self.一键站街设置输入[i + x].text() != '':
                    数据.append(int(self.一键站街设置输入[i + x].text()))
                else:
                    数据.append(0)
            except:
                QMessageBox.information(self, "错误", 名称[i] + "输入格式错误，已重置为空")
                self.一键站街设置输入[i + x].setText('')
                数据.append(0)
        
        if sum(数据) == 0:
            return

        if 数据[0] != 0 and 数据[1] == 0:
            QMessageBox.information(self,"错误",  "请输入三攻")
            return
            
        for i in range(5):
            if self.属性设置输入[i][15].text() != '':
                原始数据.append(int(self.属性设置输入[i][15].text()))
            else:
                原始数据.append(0)
        if 数据[1] != 0:
            if 类型 == '物理百分比': self.物理百分比修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街力量()), 数据[1], 原始数据[0], 原始数据[2])
            elif 类型 == '魔法百分比': self.魔法百分比修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街智力()), 数据[1], 原始数据[1], 原始数据[3])
            elif 类型 == '物理固伤': self.物理固伤修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街力量()), 数据[1], 原始数据[0], 原始数据[4])
            elif 类型 == '魔法固伤': self.魔法固伤修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街智力()), 数据[1], 原始数据[1], 原始数据[4])

        if 数据[2] != 0:
            self.属强修正(数据[2])
        self.click_window(2)
        QMessageBox.information(self,"自动修正计算完毕",  "仅对站街修正进行了修改，使面板与输入一致<br>请自行核对其它页面 非力智三攻属强 条目")

    def 力量一键修正(self, 输入力智, 修正力量2):
        修正前力量 = self.角色属性B.力量
        if self.初始属性.实际名称 == '黑暗武士':
            self.角色属性B.力量 = 输入力智 / self.角色属性B.技能栏[38].力智倍率()
            修正力量 = int(输入力智 / self.角色属性B.技能栏[38].力智倍率() + 1) - int(修正前力量)
        else:
            self.角色属性B.力量 = 输入力智
            修正力量 = 输入力智- int(修正前力量)
        self.属性设置输入[0][15].setText(str(int(修正力量 + 修正力量2)))

    def 智力一键修正(self, 输入力智, 修正智力2):
        修正前智力 = self.角色属性B.智力
        if self.初始属性.实际名称 == '黑暗武士':
            self.角色属性B.智力 = 输入力智 / self.角色属性B.技能栏[38].力智倍率()
            修正智力 = int(输入力智 / self.角色属性B.技能栏[38].力智倍率() + 1) - int(修正前智力)
        else:
            self.角色属性B.智力 = 输入力智
            修正智力 = 输入力智- int(修正前智力)
        self.属性设置输入[1][15].setText(str(int(修正智力 + 修正智力2)))        

    def 物攻一键修正(self, 输入力智, 输入三攻, 修正物理攻击力2):
        修正前物理攻击力 =self.角色属性B.物理攻击力
        站街物理攻击倍率 = self.角色属性B.站街物理攻击力倍率()
        j = round(输入三攻/站街物理攻击倍率,0)
        站街实际三攻 = int(j)
        for k in range(int(j) - 2, int(j) + 3):
            self.角色属性B.物理攻击力 = float(k)
            验证物理攻击力1 = int(self.角色属性B.站街物理攻击力())
            self.角色属性B.物理攻击力 = float(k + 1)
            验证物理攻击力2 = int(self.角色属性B.站街物理攻击力())
            if 验证物理攻击力1 <= 输入三攻 and 验证物理攻击力2 > 输入三攻:
                站街实际三攻 = float(k)
        修正物理攻击力 = 站街实际三攻 - 修正前物理攻击力
        self.属性设置输入[2][15].setText(str(int(修正物理攻击力 + 修正物理攻击力2)))

    def 魔攻一键修正(self, 输入力智, 输入三攻, 修正魔法攻击力2):
        修正前魔法攻击力 =self.角色属性B.魔法攻击力
        站街魔法攻击倍率 = self.角色属性B.站街魔法攻击力倍率()
        j = round(输入三攻/站街魔法攻击倍率,0)
        站街实际三攻 = int(j)
        for k in range(int(j) - 2, int(j) + 3):
            self.角色属性B.魔法攻击力 = float(k)
            验证魔法攻击力1 = int(self.角色属性B.站街魔法攻击力())
            self.角色属性B.魔法攻击力 = float(k+1)
            验证魔法攻击力2 = int(self.角色属性B.站街魔法攻击力())
            if 验证魔法攻击力1 <= 输入三攻 and 验证魔法攻击力2 > 输入三攻:
                站街实际三攻 = float(k)
        修正魔法攻击力 = 站街实际三攻 - 修正前魔法攻击力
        self.属性设置输入[3][15].setText(str(int(修正魔法攻击力 + 修正魔法攻击力2)))

    def 独立一键修正(self, 输入力智, 输入三攻, 修正独立攻击力2):
        修正前独立攻击力 = self.角色属性B.独立攻击力
        站街独立攻击倍率 = self.角色属性B.站街独立攻击力倍率()
        j = round(输入三攻 / 站街独立攻击倍率, 0)
        站街实际三攻 = int(j)
        for k in range(int(j) - 2, int(j) + 3):
            self.角色属性B.独立攻击力 = float(k)
            验证独立攻击力1 = int(self.角色属性B.站街独立攻击力())
            self.角色属性B.独立攻击力 = float(k + 1)
            验证独立攻击力2 = int(self.角色属性B.站街独立攻击力())
            if 验证独立攻击力1 <= 输入三攻 and 验证独立攻击力2 > 输入三攻:
                站街实际三攻 = float(k)
        修正独立攻击力 = 站街实际三攻 - 修正前独立攻击力
        self.属性设置输入[4][15].setText(str(int(修正独立攻击力 + 修正独立攻击力2)))

    def 物理百分比修正(self, 输入力智, 输入三攻, 修正力量2, 修正物理攻击力2):
        self.力量一键修正(输入力智, 修正力量2)
        self.物攻一键修正(输入力智, 输入三攻, 修正物理攻击力2)

    def 魔法百分比修正(self, 输入力智, 输入三攻, 修正智力2, 修正魔法攻击力2):
        self.智力一键修正(输入力智, 修正智力2)
        self.魔攻一键修正(输入力智, 输入三攻, 修正魔法攻击力2)

    def 物理固伤修正(self, 输入力智, 输入三攻, 修正力量2, 修正独立攻击力2):
        self.力量一键修正(输入力智, 修正力量2)
        self.独立一键修正(输入力智, 输入三攻, 修正独立攻击力2)

    def 魔法固伤修正(self, 输入力智, 输入三攻, 修正智力2, 修正独立攻击力2):
        self.智力一键修正(输入力智, 修正智力2)
        self.独立一键修正(输入力智, 输入三攻, 修正独立攻击力2)        

    def 属强修正(self, 输入属强):
        try:
            站街火强 = self.角色属性B.火属性强化加成() + self.角色属性B.火属性强化
        except:
            站街火强 = self.角色属性B.火属性强化
        try:
            站街冰强 = self.角色属性B.冰属性强化加成() + self.角色属性B.冰属性强化
        except:
            站街冰强 = self.角色属性B.冰属性强化
        try:
            站街光强 = self.角色属性B.光属性强化加成() + self.角色属性B.光属性强化
        except:
            站街光强 = self.角色属性B.光属性强化
        try:
            站街暗强 = self.角色属性B.暗属性强化加成() + self.角色属性B.暗属性强化
        except:
            站街暗强 = self.角色属性B.暗属性强化

        if self.属性设置输入[5][15].text() != '':
            修改前 = float(self.属性设置输入[5][15].text())
        else:
            修改前 = 0

        修正前属强 = int(max(站街火强, 站街冰强, 站街光强, 站街暗强))
        
        for k in range(-2,3):
            temp = int((输入属强 + k - 修正前属强) / self.角色属性B.所有属性强化增加)
            y = 修正前属强 + temp * self.角色属性B.所有属性强化增加
            if int(y) == 输入属强:
                break

        修改后 = temp + 修改前
        self.属性设置输入[5][15].setText(str(int(修改后)))

    def 提升率颜色显示(self, 属性, k):
        if k in 属性.词条选择:
            if len(属性.词条选择) == 1:
                颜色 = '<font color="#CC00CC">'
            elif k == 属性.词条选择[0]:
                if k == 属性.词条选择[1]:
                    颜色 = '<font color="#FF00FF">'
                else:
                    颜色 = '<font color="#CC00CC">'
            elif k == 属性.词条选择[1]:
                颜色 = '<font color="#990099">'
            return 颜色 + ' %.2f' % (属性.词条提升率[k] * 100) + ' </font>'
        else:
            return '<font color="#96FF1E"> %.2f' % (属性.词条提升率[k] * 100) + ' </font>'

    def 希洛克武器词条提升率显示(self, 属性):
        tempstr = []
        if sum(属性.词条提升率) > 0:
            tempstr.append(self.提升率颜色显示(属性, 0)) 
            tempstr.append(self.提升率颜色显示(属性, 1))  
            tempstr.append(self.提升率颜色显示(属性, 2)) 
            tempstr.append(self.提升率颜色显示(属性, 3)) 
            tempstr.append('·· ')
            tempstr.append(self.提升率颜色显示(属性, 4)) 
            tempstr.append(self.提升率颜色显示(属性, 5)) 
            tempstr.append('·· ')
            tempstr.append('·· ') 
            tempstr.append('·· ') 
            tempstr.append('·· ') 
            tempstr.append('·· ')
        else:
            for i in range(12):
                tempstr.append('· ')
        return tempstr

    def 词条显示计算(self, 属性):
        词条提升率 = self.希洛克武器词条提升率显示(属性)

        属白换算 = 属性.属性倍率 * 属性.属性附加

        tempstr = []

        tempstr.append(词条提升率[0] + '力智:' + str(int(round(属性.百分比力智 * 100, 0))) + '%') 
        tempstr.append(词条提升率[1] + '三攻:' + str(int(round(属性.百分比三攻 * 100, 0))) + '%') 
        tempstr.append(词条提升率[2] + '黄字:' + str(int(round(属性.伤害增加 * 100, 0))) + '%')

        temp = 词条提升率[3] + '白字:' + str(int(round(属性.附加伤害 * 100, 0))) + '%'
        if 属白换算 != 0: temp += ' (' + str(int(round(属白换算 * 100 + 属性.附加伤害 * 100, 0))) + '%)'
        tempstr.append(temp)

        temp = 词条提升率[4] + '属白:'+str(int(round(属性.属性附加 * 100, 0))) + '%'
        if 属白换算 != 0: temp += ' (' + str(int(round(属白换算*100,0))) + '%)'
        tempstr.append(temp)

        tempstr.append(词条提升率[5] + '爆伤:'+str(int(round(属性.暴击伤害 * 100, 0))) + '%')
        tempstr.append(词条提升率[6] + '终伤:'+str(int(round(属性.最终伤害 * 100, 0))) + '%')
        tempstr.append(词条提升率[7] + '技攻:'+str(int(round(属性.技能攻击力 * 100 - 100, 0))) + '%')
        tempstr.append(词条提升率[8] + '持续:'+str(int(round(属性.持续伤害 * 100, 0))) + '%') 
        tempstr.append(词条提升率[9] + '攻速:'+str(int(round(属性.攻击速度 * 100, 0))) + '%') 
        tempstr.append(词条提升率[10] + '释放:'+str(int(round(属性.释放速度 * 100, 0))) + '%') 
        tempstr.append(词条提升率[11] + '移速:'+str(int(round(属性.移动速度 * 100, 0))) + '%')

        return tempstr
        
    def 自选计算(self, x = 0):
        if x == 0:
            self.保存配置(self.存档位置)
            self.排行窗口列表.clear()
            self.排行数据.clear()

        self.角色属性A = deepcopy(self.初始属性)
        if x == 0:
            self.输入属性(self.角色属性A)
        else:
            self.输入属性(self.角色属性A, 1)
        
        装备 = []
        for i in self.自选装备:
            装备.append(i.currentText())
        
        temp = deepcopy(self.初始属性)
        temp.穿戴装备计算套装(装备)
        套装 = temp.套装栏
                
        if x != 0:
            伤害列表 = []
            for i in range(len(辟邪玉列表)):
                temp = deepcopy(self.初始属性)
                self.输入属性(temp, 100 + i)
                temp.穿戴装备(装备,套装)
                伤害列表.append(temp.伤害计算(0))

            提升率 = []
            for i in range(1, len(伤害列表)):
                if 伤害列表[0] != 0:
                    提升率.append(伤害列表[i] / 伤害列表[0] - 1)
                else:
                    提升率.append(0)

            提升率排序 = copy(提升率)
            提升率排序.sort(reverse=True)

            for i in range(0, len(提升率)):
                temp = str('%.2f' % (提升率[i] * 100)) + '%'
                self.辟邪玉提升率2[i].setText(temp)
                x = 提升率排序.index(提升率[i]) / len(提升率) * 10 - 2
                y = 1 / (1 + math.exp(-x))
                颜色 = (int(255 - 80 * y), int(245 - 100 * y), int(0 + 150 * y))
                self.辟邪玉提升率1[i].setStyleSheet('QLabel{font-size:12px;color:rgb'+ str(颜色) + '}')
                self.辟邪玉提升率2[i].setStyleSheet('QLabel{font-size:12px;color:rgb'+ str(颜色) + '}')

            self.角色属性A = deepcopy(self.初始属性)
            self.输入属性(self.角色属性A)
            C = self.站街计算(装备, 套装)
            B = deepcopy(self.角色属性A)
            B.穿戴装备(装备,套装)
            B.其它属性计算()

            总伤害数值 = B.伤害计算(0)
            if len(self.基准值) != 0:
                self.总伤害.setText(self.百分比输出(总伤害数值, self.基准值[0]))
            else:
                self.总伤害.setText(self.格式化输出(str(int(总伤害数值))))


            tempstr = self.装备描述计算(B)
            for l in range(12):
                self.图片显示[l].setToolTip(tempstr[l])

            self.面板显示[0].setText(str(int(B.面板力量())))
            self.面板显示[1].setText(str(int(B.面板物理攻击力())))
            self.面板显示[2].setText(str(int(B.面板智力())))
            self.面板显示[3].setText(str(int(B.面板魔法攻击力())))

            self.面板显示[5].setText(str(int(B.火属性强化)))
            self.面板显示[6].setText(str(int(B.冰属性强化)))
            self.面板显示[7].setText(str(int(B.光属性强化)))
            self.面板显示[8].setText(str(int(B.暗属性强化)))

            tempstr = '<font color="#FFFFFF">'+str(int(C.站街独立攻击力())) + '</font>   '
            tempstr += '<font color="#96FF32">'+str(int(B.面板独立攻击力())) + '</font>'
            self.面板显示[4].setText(tempstr)

            self.面板显示[9].setText(str(int(C.站街力量())))
            self.面板显示[10].setText(str(int(C.站街物理攻击力())))
            self.面板显示[11].setText(str(int(C.站街智力())))
            self.面板显示[12].setText(str(int(C.站街魔法攻击力())))

            self.面板显示[13].setText(str(int(C.火属性强化)))
            self.面板显示[14].setText(str(int(C.冰属性强化)))
            self.面板显示[15].setText(str(int(C.光属性强化)))
            self.面板显示[16].setText(str(int(C.暗属性强化)))

            count = 0
            for i in self.词条显示计算(B):
                self.词条显示[count].setText(i)
                count += 1

            for i in self.套装名称显示:
                i.setText('')
            count = 0

            self.套装名称显示[count].setText(self.称号.currentText())
            self.套装名称显示[count].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            self.套装名称显示[count].setToolTip('<font size="3" face="宋体"><font color="#78FF1E">' + self.称号.currentText() + '</font><br>' + 称号列表[self.称号.currentIndex()].装备描述(B)[:-4] + '</font>')
            count += 1

            self.套装名称显示[count].setText(self.宠物.currentText())
            self.套装名称显示[count].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            self.套装名称显示[count].setToolTip('<font size="3" face="宋体"><font color="#78FF1E">' + self.宠物.currentText() + '</font><br>' + 宠物列表[self.宠物.currentIndex()].装备描述(B)[:-4] + '</font>')
            count += 1


            self.套装名称显示[count].setText(装备[11])
            self.套装名称显示[count].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            count += 1

            神话所在套装 = []
            for i in range(0,11):
                if 装备列表[装备序号[装备[i]]].品质 == '神话':
                    神话所在套装.append(装备列表[装备序号[装备[i]]].所属套装)
            for i in range(0,len(套装)):
                self.套装名称显示[count].setText(套装[i])
                if 套装[i].split('[')[0] in 神话所在套装:
                    self.套装名称显示[count].setStyleSheet("QLabel{font-size:12px;color:rgb(226,150,146)}")   
                else:
                    self.套装名称显示[count].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")  
                self.套装名称显示[count].setToolTip('<font size="3" face="宋体"><font color="#78FF1E">'+套装[i]+'</font><br>'+套装列表[套装序号[套装[i]]].装备描述(B)[:-4]+'</font>')
                count += 1

        if x == 0:
            self.排行数据.append(装备 + [0] + 套装 + ['无'])
            self.输出界面(0)
    
    def 格式化输出(self, 数字文本, x = 0):
        if x == 1:
            返回值 = str('%.2f' % round(int(数字文本)/100000000,2))
        elif self.显示选项.isChecked():
            返回值 = str('%.2f' % round(int(数字文本)/100000000,2)) + '亿'
        else:
            返回值=''
            for i in range(0,len(数字文本)):
                if len(数字文本)%3==2 and i%3==2:
                    返回值+=','
                if len(数字文本)%3==1 and i%3==1:
                    返回值+=','
                if len(数字文本)%3==0 and i%3==0:
                    if i!=0:
                        返回值+=','
                返回值+=str(数字文本[i])
        return 返回值

    def 站街计算(self,装备名称,套装名称):
        C = deepcopy(self.角色属性A)
        C.穿戴装备(装备名称,套装名称)
        if 调试开关 == 0:
            for i in C.装备栏:
                装备列表[装备序号[i]].城镇属性(C)
            for i in C.套装栏:
                套装列表[套装序号[i]].城镇属性(C)
            C.装备基础()
        C.被动倍率计算()

        return C

    def 装备描述计算(self, 属性):
        tempstr = []
        for i in range(0,12):
            装备 =  装备列表[装备序号[属性.装备栏[i]]]
            tempstr.append('<font size="3" face="宋体"><font color="' + 颜色[装备.品质] + '">' +装备.名称+'</font><br>')
            if 装备.所属套装 != '无':
                if 装备.所属套装 != '智慧产物':
                    y = ' ' + 装备.所属套装
                else:
                    try:
                        y = ' ' + 装备.所属套装2
                    except:
                        y = ' '
            else:
                y = ' '
            if i == 11:
                y += ' ' + 装备.类型
            tempstr[i] += 'Lv' + str(装备.等级) + ' ' + 装备.品质 + y

            if i < 5:
                x = 属性.防具精通计算(i)
                y = '<br>精通:'
                for n in 属性.防具精通属性:
                    y += n + ' '
                tempstr[i] += y + '+' + str(x)

            if 装备.所属套装 != '智慧产物':  
                if 属性.强化等级[i]!=0:
                    if i==8:
                        tempstr[i]+='<br><font color="#68D5ED">+'+str(属性.强化等级[i]) + ' 强化: '
                        tempstr[i]+='三攻 + '+str(耳环计算(装备.等级,装备.品质,属性.强化等级[i])) + '</font>'
                    if i in [9,10]:
                        tempstr[i]+='<br><font color="#68D5ED">+'+str(属性.强化等级[i]) + ' 强化: '
                        tempstr[i]+='四维 + '+str(左右计算(装备.等级,装备.品质,属性.强化等级[i])) +'</font>'
                    if i==11:
                        tempstr[i]+='<br><font color="#68D5ED">+'+str(属性.强化等级[i]) + ' 强化: '
                        tempstr[i]+='物理攻击力 + '+str(武器计算(装备.等级,装备.品质,属性.强化等级[i],装备.类型,'物理')) + '</font><br>'
                        tempstr[i]+='<font color="#68D5ED">+'+str(属性.强化等级[i]) + ' 强化: '
                        tempstr[i]+='魔法攻击力 + '+str(武器计算(装备.等级,装备.品质,属性.强化等级[i],装备.类型,'魔法')) + '</font>'

                if 属性.武器锻造等级!=0:
                    if i==11:
                        tempstr[i]+='<br><font color="#68D5ED">+'+str(属性.武器锻造等级) + '   锻造: '
                        tempstr[i]+='独立攻击力 + '+str(锻造计算(装备.等级,装备.品质,属性.武器锻造等级)) + '</font>'

                if 属性.是否增幅[i]==1:
                    if tempstr[i] !='':
                        tempstr[i]+='<br>'
                    tempstr[i]+='<font color="#FF00FF">+'+str(属性.强化等级[i]) + ' 增幅: '
                    if '物理' in 属性.类型 or '力量' in 属性.类型:
                        tempstr[i]+='异次元力量 + '+str(增幅计算(装备.等级,装备.品质,属性.强化等级[i])) + '</font>'
                    else:
                        tempstr[i]+='异次元智力 + '+str(增幅计算(装备.等级,装备.品质,属性.强化等级[i])) + '</font>'

            if tempstr[i] != '':
                tempstr[i] += '<br>'
            tempstr[i] += 装备.装备描述(属性)[:-4]
            tempstr[i] += '</font>'
        return tempstr
    
    def 百分比输出(self, A, B):
        if B == 0:
            return self.格式化输出(str(int(A)))
        temp1 = A - B
        temp2 = round((A / B - 1) * 100, 2)
        if self.对比格式.isChecked():
            if temp1 == 0:
                return '<font face="宋体">无变化</font>'
            elif temp1 > 0:
                return '<font face="宋体" color= "#96FF1E">+' + self.格式化输出(str(int(temp1)), 1) + ' (' + str('%.2f' % abs(temp2)) + '%)</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + self.格式化输出(str(int(temp1)), 1) + ' (' + str('%.2f' % abs(temp2)) + '%)</font>'
        else:
            if temp2 == 0:
                return '<font face="宋体">无变化</font>'
            elif temp2 > 0:
                return '<font face="宋体" color= "#96FF1E">+' + str('%.2f' % temp2) + '%</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + str('%.2f' % temp2) + '%</font>'

    def 输出界面(self, index, name = ''):
        #调试模式下 index为-1
        flag = 1
        if index < 0:
            flag = 0
            index = 0
            武器名称 = ''
            for i in 装备列表:
                if i.类型 == self.角色属性A.武器选项[0]:
                    武器名称 = i.名称
                    break
            self.排行数据.append(['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的心之所念', '军神的遗书', '军神的庇护宝石', 武器名称, 0, '噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]', '无'])

        装备名称 = []
        套装名称 = []
        百变怪 = self.排行数据[index][-1]
        for i in range(0, 12):
            装备名称.append(self.排行数据[index][i])
        for i in range(13,len(self.排行数据[index])-1):
            套装名称.append(self.排行数据[index][i])
        self.角色属性B = deepcopy(self.角色属性A)
        self.角色属性B.穿戴装备(装备名称,套装名称)

        if flag == 1:
            C = self.站街计算(装备名称,套装名称)
            self.角色属性B.其它属性计算()
        else:
            C = deepcopy(self.角色属性A)
            C.穿戴装备(装备名称,套装名称)
            C.被动倍率计算()

        统计详情 = self.角色属性B.伤害计算(1)

        #最大输出界面限制
        if len(self.输出窗口列表)>=10:
            del self.输出窗口列表[0]
    
        输出窗口 = QWidget()
        输出窗口.setStyleSheet('''QToolTip { 
           background-color: black; 
           color: white; 
           border: 0px
           }''')
        self.输出窗口列表.append(输出窗口)
        输出窗口.setFixedSize(788, 564)
        temp = ''
        if name == '':
            temp += '详细数据'
        else:
            temp += name
        temp += '（最多显示前18个技能）'
        输出窗口.setWindowTitle(temp)
        输出窗口.setWindowIcon(self.icon)  
        QLabel(输出窗口).setPixmap(self.输出背景图片)
        人物 = QLabel(输出窗口)
        图片 = QPixmap('./ResourceFiles/'+self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(90 + int(45 - 图片.width() / 2), 40)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)
      
        excel=[]
        for i in range(0,len(self.角色属性B.技能栏)):
            excel.append(统计详情[i*4+1])
        excel.sort()


        面板显示=[]
        for i in range(0,17):
            面板显示.append(QLabel(输出窗口))        
    
        面板显示[0].setText(str(int(self.角色属性B.面板力量())))
        面板显示[1].setText(str(int(self.角色属性B.面板物理攻击力())))
        面板显示[2].setText(str(int(self.角色属性B.面板智力())))
        面板显示[3].setText(str(int(self.角色属性B.面板魔法攻击力())))
        
        面板显示[5].setText(str(int(self.角色属性B.火属性强化)))
        面板显示[6].setText(str(int(self.角色属性B.冰属性强化)))
        面板显示[7].setText(str(int(self.角色属性B.光属性强化)))
        面板显示[8].setText(str(int(self.角色属性B.暗属性强化)))
        
        tempstr = '<font color="#FFFFFF">'+str(int(C.站街独立攻击力())) + '</font>   '
        tempstr += '<font color="#96FF1E">'+str(int(self.角色属性B.面板独立攻击力())) + '</font>'
        面板显示[4].setText(tempstr)

        面板显示[9].setText(str(int(C.站街力量())))
        面板显示[10].setText(str(int(C.站街物理攻击力())))
        面板显示[11].setText(str(int(C.站街智力())))
        面板显示[12].setText(str(int(C.站街魔法攻击力())))
        
        面板显示[13].setText(str(int(C.火属性强化)))
        面板显示[14].setText(str(int(C.冰属性强化)))
        面板显示[15].setText(str(int(C.光属性强化)))
        面板显示[16].setText(str(int(C.暗属性强化)))
        
        const = 139
        count = 0
        for i in  [9,10,0,1]:
            面板显示[i].move(20,const + count * 18)
            count += 1

        count = 0
        for i in  [11,12,2,3]:
            面板显示[i].move(150,const + count * 18)
            count += 1

        面板显示[4].move(150,const + count * 18)

        count = 5
        for i in  [5,6,7,8]:
            面板显示[i].move(150,const + count * 18)
            count += 1

        count = 5
        for i in  [13,14,15,16]:
            面板显示[i].move(20,const + count * 18)
            count += 1
      
        for i in range(0,len(面板显示)):
            if i >= 9:
                面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            else:
                面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(150,255,30)}")
            面板显示[i].resize(100,18)
            面板显示[i].setAlignment(Qt.AlignRight)

        j=312
        for i in self.词条显示计算(self.角色属性B):
            templab=QLabel(输出窗口)
            templab.setText(i)
            templab.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            templab.move(5,j)
            templab.resize(180,17)
            templab.setAlignment(Qt.AlignLeft)
            j+=17

        位置 = 313
        间隔 = 20
        if sum(self.角色属性B.自适应选项) != 0:
            套装名称.append(self.角色属性B.自适应输出())
            位置 -= 5
            间隔 -= 1
        
        适用称号名称=QLabel(self.称号.currentText(),输出窗口)
        适用称号名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用称号名称.move(114, 位置)
        适用称号名称.resize(150,18)
        适用称号名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔
        适用称号名称.setToolTip('<font size="3" face="宋体"><font color="#78FF1E">' + self.称号.currentText() + '</font><br>'+称号列表[self.称号.currentIndex()].装备描述(self.角色属性B)[:-4]+'</font>')

        适用宠物名称=QLabel(self.宠物.currentText(),输出窗口)
        适用宠物名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用宠物名称.move(114, 位置)
        适用宠物名称.resize(150,18)
        适用宠物名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔
        适用宠物名称.setToolTip('<font size="3" face="宋体"><font color="#78FF1E">' + self.宠物.currentText() + '</font><br>'+宠物列表[self.宠物.currentIndex()].装备描述(self.角色属性B)[:-4]+'</font>')

        适用武器名称=QLabel(装备名称[11],输出窗口)
        适用武器名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用武器名称.move(114, 位置)
        适用武器名称.resize(150,18)
        适用武器名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔

        神话所在套装 = []
        for i in range(0,11):
            if 装备列表[装备序号[装备名称[i]]].品质 == '神话':
                神话所在套装.append(装备列表[装备序号[装备名称[i]]].所属套装)
        for i in range(0,len(套装名称)):
            适用套装名称=QLabel(输出窗口)
            适用套装名称.setText(套装名称[i])
            适用套装名称.move(114,位置+i*间隔)
            适用套装名称.resize(150,18)
            适用套装名称.setAlignment(Qt.AlignCenter)  
            if 套装名称[i].split('[')[0] in 神话所在套装:
                适用套装名称.setStyleSheet("QLabel{font-size:12px;color:rgb(226,150,146)}")   
            else:
                适用套装名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            sign = 1
            if sum(self.角色属性B.自适应选项) != 0:
                if i == len(套装名称) - 1:
                    sign = 0
            if sign == 1:
                适用套装名称.setToolTip('<font size="3" face="宋体"><font color="#78FF1E">'+套装名称[i]+'</font><br>'+套装列表[套装序号[套装名称[i]]].装备描述(self.角色属性B)[:-4]+'</font>')
  
        实际技能等级=[]
        技能等效CD=[]
        for i in self.角色属性B.技能栏:
            实际技能等级.append(i.等级)
            if i.是否有伤害==1:
                技能等效CD.append(i.等效CD(self.角色属性B.武器类型))
            else:
                技能等效CD.append(0)
    
        总伤害数值=0

        count = 0
        for i in range(0,len(self.角色属性B.技能栏)):
            if 统计详情[i*4 + 1] != 0:
                count += 1
        count = min(18, count)
        self.行高 = min(int(440 / count),30)        
        
        伤害列表 = []
        for i in range(0,len(self.角色属性B.技能栏)):
            伤害列表.append(统计详情[i*4+1])
            总伤害数值 += 统计详情[i*4+1]
        伤害列表.sort(reverse = True)
        for i in range(0,len(self.角色属性B.技能栏)):
            if 伤害列表.index(统计详情[i * 4 + 1]) >= count:
                统计详情[i * 4 + 1] = 0

        if len(self.基准值) != 0:
            显示模式 = 1
        else:
            显示模式 = 0

        for i in range(0,len(self.角色属性B.技能栏)):
            j=len(self.角色属性B.技能栏)-1-excel.index(统计详情[i*4+1])
            if 统计详情[i*4 + 1] != 0:
                每行详情=[]
                for k in range(0,7):
                    每行详情.append(QLabel(输出窗口))
                #图片
                每行详情[0].setPixmap(self.技能图片[i])
                每行详情[0].resize(28,min(28,self.行高 - 2)) 
                try:
                    tempstr='<font face="宋体"><font color="#FF6666">'+self.角色属性B.技能栏[i].名称+self.角色属性B.技能栏[i].备注+ '</font><br>'
                    tempstr+='百分比：'+str(int(self.角色属性B.技能栏[i].等效百分比(self.角色属性B.武器类型) / self.角色属性B.技能栏[i].倍率)) + '%<br>'
                    tempstr+='被动倍率：'+str(round(self.角色属性B.技能栏[i].被动倍率*100,1)) + '%<br>'
                    if self.角色属性B.技能栏[i].倍率!=0:
                        tempstr+='其它倍率：'+str(round(self.角色属性B.技能栏[i].倍率*100,1)) + '%<br>'
                    tempstr+='CD显示：'+str(round(self.角色属性B.技能栏[i].等效CD(self.角色属性B.武器类型) * self.角色属性B.技能栏[i].恢复,2)) + 's<br>'
                    tempstr+='CD恢复：'+str(round(self.角色属性B.技能栏[i].恢复*100,1)) + '%</font>'
                    每行详情[0].setToolTip(tempstr)
                except:
                    pass
    
                每行详情[0].move(302, 50 + j * self.行高)
                #等级
                每行详情[1].setText('Lv.'+str(实际技能等级[i]))
                每行详情[1].move(337, 50 + j * self.行高)
                每行详情[1].resize(30,min(28,self.行高)) 
                #CD
                每行详情[2].setText(str(技能等效CD[i]) + 's')
                每行详情[2].move(380, 50 + j * self.行高)
                每行详情[2].resize(36,min(28,self.行高))
                #次数
                每行详情[3].setText(str(统计详情[i*4]))
                每行详情[3].move(418, 50 + j * self.行高)
                每行详情[3].resize(30,min(28,self.行高)) 
                #总伤害
                if 显示模式 == 1:
                    每行详情[4].setText(self.百分比输出(统计详情[i*4+1], self.基准值[1][i*4+1]))
                else:
                    每行详情[4].setText(self.格式化输出(str(int(统计详情[i*4+1]))))
                每行详情[4].move(448, 50 + j * self.行高)
                每行详情[4].resize(108,min(28,self.行高)) 
                #平均伤害
                if 显示模式 == 1:
                    每行详情[5].setText(self.百分比输出(统计详情[i*4+2], self.基准值[1][i*4+2]))
                else:
                    每行详情[5].setText(self.格式化输出(str(int(统计详情[i*4+2]))))
                每行详情[5].move(555, 50 + j * self.行高) 
                每行详情[5].resize(108,min(28,self.行高)) 
                #占比
                每行详情[6].setText(str(round(统计详情[i*4+3],1)) + '%')
                每行详情[6].move(660, 50 + j * self.行高)
                每行详情[6].resize(108,min(28,self.行高))
     
                for l in range(1,7):
                    每行详情[l].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
                    每行详情[l].setAlignment(Qt.AlignCenter) 
    
        #被动详情
        num=0
        for i in range(0,len(self.角色属性B.技能栏)):
            # Will修改
            tempstr = ''
            if self.角色属性B.技能栏[i].所在等级 != 100 or self.角色属性B.技能栏[i].是否主动 == 0:
                if self.角色属性B.技能栏[i].等级 > 0:
                    if self.角色属性B.技能栏[i].自定义描述 == 1:
                        tempstr+= '<font face="宋体"><font color="#FF6666">'+self.角色属性B.技能栏[i].名称+'</font><br>'
                        tempstr+= self.角色属性B.技能栏[i].技能描述(self.角色属性B.武器类型)            
                    else:
                        if self.角色属性B.技能栏[i].关联技能 != ['无'] and self.角色属性B.技能栏[i].加成倍率(self.角色属性B.武器类型) != 1:
                            tempstr+='<font face="宋体"><font color="#FF6666">'+self.角色属性B.技能栏[i].名称+'</font><br>'
                            tempstr+='加成倍率：'+str(round(self.角色属性B.技能栏[i].加成倍率(self.角色属性B.武器类型)*100-100,2)) + '%<br>'
                            tempstr+='关联技能：'
                            for j in self.角色属性B.技能栏[i].关联技能:
                                tempstr+=j
                                if j != self.角色属性B.技能栏[i].关联技能[-1]:
                                    tempstr+=','
                            if self.角色属性B.技能栏[i].关联技能2 != ['无']:
                                tempstr+='<br>加成倍率：'+str(round(self.角色属性B.技能栏[i].加成倍率2(self.角色属性B.武器类型)*100-100,2)) + '%<br>'
                                tempstr+='关联技能：'
                                for k in self.角色属性B.技能栏[i].关联技能2:
                                    tempstr+=k
                                    if k != self.角色属性B.技能栏[i].关联技能2[-1]:
                                        tempstr+=','
                            if self.角色属性B.技能栏[i].关联技能3 != ['无']:
                                tempstr+='<br>加成倍率：'+str(round(self.角色属性B.技能栏[i].加成倍率3(self.角色属性B.武器类型)*100-100,2)) + '%<br>'
                                tempstr+='关联技能：'
                                for l in self.角色属性B.技能栏[i].关联技能3:
                                    tempstr+=l
                                    if l != self.角色属性B.技能栏[i].关联技能3[-1]:
                                        tempstr+=','
                        if self.角色属性B.技能栏[i].冷却关联技能 != ['无'] and self.角色属性B.技能栏[i].CD缩减倍率(self.角色属性B.武器类型) != 1:
                            if tempstr == '':
                                tempstr+='<font face="宋体"><font color="#FF6666">'+self.角色属性B.技能栏[i].名称+'</font><br>'
                            else:
                                tempstr+='<br>'
                            tempstr+='冷却缩减：'+str(round(100 - self.角色属性B.技能栏[i].CD缩减倍率(self.角色属性B.武器类型)*100,2)) + '%<br>'
                            tempstr+='冷却关联技能：'
                            for j in self.角色属性B.技能栏[i].冷却关联技能:
                                tempstr+=j
                                if j != self.角色属性B.技能栏[i].冷却关联技能[-1]:
                                    tempstr+=','
                            if self.角色属性B.技能栏[i].冷却关联技能2 != ['无']:
                                tempstr+='<br>冷却缩减：'+str(round(100 - self.角色属性B.技能栏[i].CD缩减倍率2(self.角色属性B.武器类型)*100,2)) + '%<br>'
                                tempstr+='冷却关联技能：'
                                for j in self.角色属性B.技能栏[i].冷却关联技能2:
                                    tempstr+=j
                                    if j != self.角色属性B.技能栏[i].冷却关联技能2[-1]:
                                        tempstr+=','
                            if self.角色属性B.技能栏[i].冷却关联技能3 != ['无']:
                                tempstr+='<br>冷却缩减：'+str(round(100 - self.角色属性B.技能栏[i].CD缩减倍率3(self.角色属性B.武器类型)*100,2)) + '%<br>'
                                tempstr+='冷却关联技能：'
                                for j in self.角色属性B.技能栏[i].冷却关联技能3:
                                    tempstr+=j
                                    if j != self.角色属性B.技能栏[i].冷却关联技能3[-1]:
                                        tempstr+=','
                if tempstr != '':
                    tempstr += '</font>'
                    被动数据=QLabel(输出窗口)
                    被动数据.setPixmap(self.技能图片[i])
                    被动数据.setToolTip(tempstr)
                    被动数据.move(293+num*40, 500)
                    被动等级=QLabel(输出窗口)
                    被动等级.setText('Lv.'+str(实际技能等级[i]))
                    被动等级.move(293-6+num*40, 480)
                    被动等级.resize(40,28)
                    if 实际技能等级[i] != 0:
                        被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
                    else:
                        被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,0,0)}")
                    被动等级.setAlignment(Qt.AlignCenter)  
                    num+=1
        
        if self.角色属性B.远古记忆 > 0:
            被动数据=QLabel(输出窗口)
            被动数据.setPixmap((QPixmap('./ResourceFiles/img/远古记忆.png')))
            tempstr='<font face="宋体"><font color="#FF6666">'+'远古记忆'+'</font><br>'
            tempstr+='智力+'+str(self.角色属性B.远古记忆 * 15) + '</font>'
            被动数据.setToolTip(tempstr)
            被动数据.move(293+num*40, 500)
            被动等级=QLabel(输出窗口)
            被动等级.setText('Lv.'+str(self.角色属性B.远古记忆))
            被动等级.move(293-6+num*40, 480)
            被动等级.resize(40,28)
            被动等级.setAlignment(Qt.AlignCenter)
            被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")  
            num+=1

        if self.角色属性B.刀魂之卡赞 > 0:
            被动数据=QLabel(输出窗口)
            被动数据.setPixmap((QPixmap('./ResourceFiles/img/刀魂之卡赞.png')))
            tempstr='<font face="宋体"><font color="#FF6666">'+'刀魂之卡赞'+'</font><br>'
            tempstr+='力量/智力+'+str(刀魂之卡赞数据[self.角色属性B.刀魂之卡赞]) + '</font>'
            被动数据.setToolTip(tempstr)
            被动数据.move(293+num*40, 500)
            被动等级=QLabel(输出窗口)
            被动等级.setText('Lv.'+str(self.角色属性B.刀魂之卡赞))
            被动等级.move(293-6+num*40, 480)
            被动等级.resize(40,28)
            被动等级.setAlignment(Qt.AlignCenter)
            被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")  
            num+=1
    
        总伤害=QLabel(输出窗口)
        总伤害.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        if 显示模式 == 1:
            总伤害.setText(self.百分比输出(总伤害数值, self.基准值[0]))
        else:
            总伤害.setText(self.格式化输出(str(int(总伤害数值))))
        总伤害.resize(250,36)
        总伤害.move(10,520)
        总伤害.setAlignment(Qt.AlignCenter) 
    
        初始x=10;初始y=31
    
        图片列表 = []
    
        数量 = [0] * 3
        for i in range(15):
            数量[i % 3] += self.希洛克选择状态[i]

        # 0 上衣 1护肩 2护腿 3腰带 4鞋子 5 手镯 6 项链 7 戒指 8 耳环 9辅助 10魔法石 11 武器
        for i in range(0,12):
            # 下装
            if 数量[0] == 1 and i == 2:
                for item in range(5):
                    if self.希洛克选择状态[item*3+0] > 0:
                        图片列表.append(QMovie('./ResourceFiles/img/希洛克/'+str(item*3+0)+'.gif'))
            elif 数量[1] == 1 and i == 7:
                for item in range(5):
                    if self.希洛克选择状态[item*3+1] > 0:
                        图片列表.append(QMovie('./ResourceFiles/img/希洛克/'+str(item*3+1)+'.gif'))
            elif 数量[2] == 1 and i == 9:
                for item in range(5):
                    if self.希洛克选择状态[item*3+2] > 0:
                        图片列表.append(QMovie('./ResourceFiles/img/希洛克/'+str(item*3+2)+'.gif')) 
            elif self.希洛克武器词条[0].currentIndex() > 0 and i == 11:
                # 图片列表.append(QMovie('./ResourceFiles/img/希洛克/融-7.gif'))
                图片列表.append(QMovie('./ResourceFiles/img/希洛克/武器/'+ str(装备序号[self.排行数据[index][i]]) +'.gif'))    
            else:          
                图片列表.append(self.装备图片[装备序号[self.排行数据[index][i]]])
    
        偏移量=187
        x坐标=[32,0,0,32,0,偏移量,偏移量+32,偏移量+32,偏移量,偏移量,偏移量+32,32]
        y坐标=[0,0,32,32,64,0,0,32,64,32,64,64]
    
        tempstr = self.装备描述计算(self.角色属性B)

        for i in range(0,12):
            装备图标=QLabel(输出窗口)
            装备图标.setMovie(图片列表[i])
            图片列表[i].start()
            装备图标.resize(26,26)
            装备图标.move(初始x+x坐标[i],初始y+y坐标[i])
            装备图标.setAlignment(Qt.AlignCenter) 
            装备 =  装备列表[装备序号[self.角色属性B.装备栏[i]]]
            if self.角色属性B.装备栏[i] == 百变怪:
                图标遮罩=QLabel(输出窗口)
                图标遮罩.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.5)}")
                图标遮罩.resize(26,26)
                图标遮罩.move(初始x+x坐标[i],初始y+y坐标[i])
                图标遮罩.setToolTip(tempstr[i])
            else:
                装备图标.setToolTip(tempstr[i])

        for i in range(0,12):
            装备 =  装备列表[装备序号[self.角色属性B.装备栏[i]]]
            打造状态=QLabel(输出窗口)
            if 装备.所属套装 != '智慧产物':    
                打造状态.setText('+'+str(self.角色属性B.强化等级[i]))
                if self.角色属性B.是否增幅[i]==1:
                    打造状态.setStyleSheet("QLabel{color:rgb(228,88,169);font-size:12px;font-weight:Bold}")
                else:
                    打造状态.setStyleSheet("QLabel{color:rgb(25,199,234);font-size:12px;font-weight:Bold}")
                
            else:
                打造状态.setText('+'+str(self.角色属性B.改造等级[i]))
                打造状态.setStyleSheet("QLabel{color:rgb(249,141,62);font-size:12px;font-weight:Bold;}")
            
            打造状态.move(初始x+x坐标[i]+13,初始y+y坐标[i]-8)
        
        装备 =  装备列表[装备序号[self.角色属性B.装备栏[11]]]
        if 装备.所属套装 != '智慧产物' and self.角色属性B.武器锻造等级 != 0:
            打造状态=QLabel(输出窗口)
            打造状态.setText('+'+str(self.角色属性B.武器锻造等级))
            打造状态.setStyleSheet("QLabel{color:rgb(232,104,24);font-size:12px;font-weight:Bold}")
            打造状态.move(初始x+x坐标[11]+13,初始y+y坐标[11]+20)

        输出窗口.show()  

    def 希洛克属性计算(self, 属性):
        数量 = [0] * 3
        for i in range(15):
            数量[i % 3] += self.希洛克选择状态[i]
        
        #下装属性1
        if 数量[0] == 1:
            属性.最终伤害加成(0.05)

        #戒指属性1
        if 数量[1] == 1:
            属性.百分比三攻加成(0.05)

        #辅助装备属性1
        if 数量[2] == 1:
            属性.技能攻击力加成(0.05)
        
        i = 0 #奈克斯属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.伤害增加加成(0.05) #下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.暴击伤害加成(0.05) #戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.百分比力智加成(0.05) #辅助装备

        i = 1 #暗杀者属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.伤害增加加成(0.02)
            属性.技能冷却缩减(1,45,0.2) #下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.暴击伤害加成(0.03)
            属性.技能冷却缩减(60,70,0.2) #戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.百分比力智加成(0.03)
            属性.技能冷却缩减(75,80,0.17) #辅助装备

        i = 2 #卢克西属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.技能倍率加成(50,0.17)
            属性.技能倍率加成(85,0.17)
            属性.技能倍率加成(100,0.10) #下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.技能倍率加成(50,0.17)
            属性.技能倍率加成(85,0.17)
            属性.技能倍率加成(100,0.10) #戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.技能倍率加成(50,0.17)
            属性.技能倍率加成(85,0.17)
            属性.技能倍率加成(100,0.10)#辅助装备

        i = 3 #守门人属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.进图属强 += self.守门人属强.currentIndex() * 5 + 15 #下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.进图属强 += self.守门人属强.currentIndex() * 5 + 15 #戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.进图属强 += self.守门人属强.currentIndex() * 5 + 15 #辅助装备

        i = 4 #洛多斯属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.伤害增加加成(0.04) #下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.暴击伤害加成(0.04) #戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.百分比力智加成(0.04) #辅助装备

    def 输入属性(self, 属性, x = 0):

        i = self.攻击目标.currentIndex()
        属性.防御输入 = 攻击目标[i][1]
        属性.火抗输入 = 攻击目标[i][2]
        属性.冰抗输入 = 攻击目标[i][3]
        属性.光抗输入 = 攻击目标[i][4]
        属性.暗抗输入 = 攻击目标[i][5]

        if self.初始属性.远古记忆 != -1:
            属性.远古记忆 = self.远古记忆.currentIndex()
        if self.初始属性.刀魂之卡赞 != -1:
            属性.刀魂之卡赞 = self.刀魂之卡赞.currentIndex()

        属性.自适应选项 = copy([(1 if self.红色宠物装备.isChecked() else 0), (1 if self.光环自适应.isChecked() else 0)])

        if self.转甲选项.isChecked():
            属性.转甲选项 = 1
        else:
            属性.转甲选项 = 0

        if sum(self.希洛克选择状态) == 3:
            属性.武器词条触发 = 1

        if self.希洛克武器词条[0].currentIndex() == 1:
            属性.希洛克武器词条 = 1
        elif self.希洛克武器词条[0].currentIndex() == 2:
            词条属性列表[self.希洛克武器词条[1].currentIndex()].加成属性(属性, (self.希洛克武器词条[3].currentIndex() + 3) * 0.02)
            if 属性.武器词条触发 == 1:
                词条属性列表[self.希洛克武器词条[2].currentIndex()].加成属性(属性, (self.希洛克武器词条[4].currentIndex() + 3) * 0.01)

        for j in [self.等级调整, self.TP输入, self.次数输入, self.宠物次数]:
            for i in j:
                if i != '' and i.currentIndex() == -1:
                    i.setCurrentIndex(0)

        for i in 属性.技能栏:
            i.等级 = i.基础等级+int(self.等级调整[self.角色属性A.技能序号[i.名称]].currentText())
            if i.是否有伤害==1:
                if i.TP上限!=0:
                    i.TP等级=int(self.TP输入[self.角色属性A.技能序号[i.名称]].currentText())

        if x == 0:
            self.辟邪玉属性计算(属性)
        elif x >= 100:
            y = x - 100
            辟邪玉列表[y].当前值 = 辟邪玉列表[y].最大值
            辟邪玉列表[y].穿戴属性(属性)

        属性.时间输入 = int(self.时间输入.currentText())
        属性.次数输入.clear()
        属性.宠物次数.clear()
        属性.装备切装.clear()
        属性.技能切装.clear()
        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            if i.是否有伤害 == 1:
                属性.次数输入.append(self.次数输入[序号].currentText())
                if self.次数输入[序号].currentIndex() != 0:
                    self.宠物次数[序号].setCurrentIndex(min(self.宠物次数[序号].currentIndex(), self.次数输入[序号].currentIndex() - 1 + i.基础释放次数))
                属性.宠物次数.append(self.宠物次数[序号].currentIndex())
                if 切装模式 == 1:
                    if self.技能切装[序号].isChecked():
                        属性.技能切装.append(1)
                    else:
                        属性.技能切装.append(0)
            else:
                属性.次数输入.append('')
                属性.宠物次数.append(0)
                属性.技能切装.append(0)
        if 切装模式 == 1:
            for i in range(12):
                if self.装备切装[i].isChecked():
                    属性.装备切装.append(self.自选装备[i].currentText())
                else:
                    属性.装备切装.append('无')

        for i in range(len(self.复选框列表)):
            if self.复选框列表[i].isChecked():
                选项设置列表[i].适用效果(属性)
        
        count = 0
        for i in 装备列表:
            if i.品质 == '神话':
                i.属性1选择 = self.神话属性选项[count * 4 + 0].currentIndex()
                i.属性2选择 = self.神话属性选项[count * 4 + 1].currentIndex()
                i.属性3选择 = self.神话属性选项[count * 4 + 2].currentIndex()
                i.属性4选择 = self.神话属性选项[count * 4 + 3].currentIndex()
                count += 1
        
        属性.攻击属性 = self.攻击属性选项.currentIndex()

        称号列表[self.称号.currentIndex()].城镇属性(属性)
        if 属性.称号触发:
            称号列表[self.称号.currentIndex()].触发属性(属性)

        宠物列表[self.宠物.currentIndex()].城镇属性(属性)
        
        for k in range(3):
            if self.护石栏[k].currentText()!= '无':
                try:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石()
                except:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石(self.护石类型选项[k].currentIndex())
                    
        属性.护石第一栏 = self.护石栏[0].currentText()
        属性.护石第二栏 = self.护石栏[1].currentText()
        属性.护石第三栏 = self.护石栏[2].currentText()
    
        for i in range(0,9):
            if self.符文[i].currentText()!='无' and self.符文效果[i].currentText() != '无':
                for j in self.符文效果[i].currentText().split(','):
                    if '攻击' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率 *= 1 + int(j.replace('攻击','').replace('%',''))/100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD *= 1 + int(j.replace('CD','').replace('%',''))/100

        for i in range(0,12):
            属性.是否增幅[i] = self.装备打造选项[i].currentIndex()
            属性.强化等级[i] = self.装备打造选项[i + 12].currentIndex()
            属性.改造等级[i] = self.装备打造选项[i + 24].currentIndex()
        属性.武器锻造等级 = self.装备打造选项[36].currentIndex()
        属性.类型 = self.装备打造选项[37].currentText()

        try:
            属性.主BUFF = float(self.BUFF输入.text()) / 100 + 1
        except: 
            QMessageBox.information(self,"错误",  "BUFF数值输入错误,已设置为默认数值") 
            self.BUFF输入.setText(str('%.1f' % ((self.角色属性A.主BUFF - 1) * 100)))
        
        if self.角色属性A.技能栏[self.三觉序号].是否有伤害 == 1 and 属性.次数输入[self.三觉序号] == '0':
            属性.技能栏[self.三觉序号].关联技能 = ['无']
        else:
            if self.觉醒选择状态 == 1:
                属性.技能栏[self.三觉序号].关联技能 = [属性.技能栏[self.一觉序号].名称]
            if self.觉醒选择状态 == 2:
                属性.技能栏[self.三觉序号].关联技能 = [属性.技能栏[self.二觉序号].名称]
    
        属性.角色熟练度 = self.装备条件选择[0].currentIndex()
        属性.技能栏空位 = self.装备条件选择[1].currentIndex()
        属性.命运的抉择 = self.装备条件选择[2].currentIndex()
        属性.天命无常 = self.装备条件选择[3].currentIndex()
        属性.悲剧的残骸 = self.装备条件选择[4].currentIndex()
        属性.先知者的预言 = self.装备条件选择[5].currentIndex()
        属性.贫瘠沙漠的遗产 = self.装备条件选择[6].currentIndex()
        属性.幸运三角 = self.装备条件选择[7].currentIndex()
        属性.擎天战甲 = self.装备条件选择[8].currentIndex()
        属性.持续伤害计算比例 = 1 - 0.01 * self.装备条件选择[9].currentIndex()
        属性.军神的隐秘遗产 = self.装备条件选择[10].currentIndex()
        属性.太极天帝剑 = self.装备条件选择[11].currentIndex()
        属性.绿色生命的面容 = self.装备条件选择[12].currentIndex()
        
        self.希洛克属性计算(属性)
        self.基础属性(属性)
    
    def 基础属性(self, 属性):
        if 切装模式 == 1:
            属性.切装修正.clear()
            名称 = ['力量', '智力', '物攻', '魔攻', '独立', '属强']
            num = 0
            for i in self.切装修正属性:
                try:
                    if i.text() != '':
                        属性.切装修正.append(int(i.text()))
                    else:
                        属性.切装修正.append(0)
                except:
                    QMessageBox.information(self,"错误", 名称[num] + " 切装修正输入格式错误，已重置为空")
                    i.setText('')
                    属性.切装修正.append(0)
                num += 1
        
        for i in range(len(self.列名称) - 3):
            for j in range(len(行名称1)):
                if self.属性设置输入[i][j].text() != '':
                    try:
                        float(self.属性设置输入[i][j].text())
                    except:
                        QMessageBox.information(self,"错误", self.行名称[(j + len(行名称1)) if i >= len(列名称1) else j] + "：" + self.列名称[i] + "  输入格式错误，已重置为空")
                        self.属性设置输入[i][j].setText('')

        temp = []
        num = len(self.列名称) - 3
        for j in range(0, len(self.属性设置输入[num])):
            if self.属性设置输入[num][j].text() != '':
                try:
                    temp.append(float(self.属性设置输入[num][j].text())/100)
                    if temp[-1] > 1 or temp[-1] < -0.2:
                        QMessageBox.information(self,"错误", self.修正列表名称[j] + " 输入数值超出[-20,100]，已重置为空")
                        temp[-1] = 0.0
                        self.属性设置输入[num][j].setText('')
                except:
                    temp.append(0.0)
                    QMessageBox.information(self,"错误", self.修正列表名称[j] + " 输入格式错误，已重置为空")
                    self.属性设置输入[num][j].setText('')
            else:
                temp.append(0.0)

        属性.百分比力智加成(temp[0])
        属性.百分比三攻加成(temp[1])
        属性.伤害增加加成(temp[2])
        属性.附加伤害加成(temp[3])
        属性.属性附加加成(temp[4])
        属性.暴击伤害加成(temp[5])
        属性.最终伤害加成(temp[6])
        属性.技能攻击力加成(temp[7])

        for i in [0, 6, 9]:
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 0 and j in [1, 5, 10, 16]:
                        属性.进图力量 += float(self.属性设置输入[i][j].text())
                    else:
                        属性.力量 += float(self.属性设置输入[i][j].text())
        for i in [1, 6, 9]:
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 1 and j in [1, 5, 10, 16]:
                        属性.进图智力 += float(self.属性设置输入[i][j].text())
                    else:
                        属性.智力 += float(self.属性设置输入[i][j].text())

        for i in [2, 7, 10]:
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 2 and j in [1, 5, 10, 16]:
                        属性.进图物理攻击力 += float(self.属性设置输入[i][j].text())
                    else:
                        属性.物理攻击力 += float(self.属性设置输入[i][j].text())

        for i in [3, 7, 10]:
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 3 and j in [1, 5, 10, 16]:
                        属性.进图魔法攻击力 += float(self.属性设置输入[i][j].text())
                    else:
                        属性.魔法攻击力 += float(self.属性设置输入[i][j].text())

        for i in [4, 7, 10]:
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 4 and j in [1, 5, 10, 16]:
                        属性.进图独立攻击力 += float(self.属性设置输入[i][j].text())
                    else:
                        属性.独立攻击力 += float(self.属性设置输入[i][j].text())

        for i in [5, 8]:
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 5 and j in [1, 5, 10, 16]:
                        属性.进图属强 += float(self.属性设置输入[i][j].text())
                    elif i == 5 and j == 3: #3为婚房不吃辟邪玉
                        属性.所有属性强化(float(self.属性设置输入[i][j].text()))
                    else:
                        属性.所有属性强化加成(float(self.属性设置输入[i][j].text()))
                        
        for i in self.细节选项输入:
            for j in i:
                if j.isEnabled():
                    if j.currentText() not in ['', '无']:
                        try:
                            细节选项列表[细节选项序号[j.currentText()]].效果(属性)
                        except:
                            for k in 属性.技能栏:
                                if j.currentText() == k.名称 + 'Lv+1':
                                    k.等级加成(1)
                                    break