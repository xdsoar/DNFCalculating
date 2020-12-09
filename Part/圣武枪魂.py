from PublicReference.base import *

class 职业主动技能(主动技能):

    data0 = []
    data1 = []
    data2 = []
    data3 = []

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.data0) >= self.等级 and len(self.data0) > 0:
            等效倍率 += self.data0[self.等级] * self.攻击次数
        if len(self.data1) >= self.等级 and len(self.data1) > 0:
            等效倍率 += self.data1[self.等级] * self.攻击次数2
        if len(self.data2) >= self.等级 and len(self.data2) > 0:
            等效倍率 += self.data2[self.等级] * self.攻击次数3
        if len(self.data3) >= self.等级 and len(self.data3) > 0:
            等效倍率 += self.data3[self.等级] * self.攻击次数4
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 等效CD(self, 武器类型):
        # 长枪+5%,长枪精通-13%
        if self.所在等级 == 100 or self.所在等级 == 85 or self.所在等级 == 50:
            return round(self.CD  / self.恢复 * 1.05, 1)
        else:
            return round(self.CD  / self.恢复 * 1.05 * 0.87, 1)

class 技能0(被动技能):	
    名称 = '长枪精通'	
    所在等级 = 15	
    等级上限 = 30	
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1 + 0.01 * self.等级, 5)
        else:
            return round(0.8 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)	

class 技能1(职业主动技能):	
    名称 = '双重刺击'	
    所在等级 = 20	
    等级上限 = 60	
    基础等级 = 43	
    # #第1击攻击力：<data0>%
    # data0 = [0, 1695, 1868, 2040, 2211, 2383, 2556, 2728, 2900, 3071, 3244, 3416, 3588, 3760, 3932, 4104, 4276, 4449, 4621, 4792, 4964, 5137, 5309, 5481, 5652, 5825, 5997, 6169, 6340, 6513, 6685, 6857, 7029, 7201, 7373, 7545, 7717, 7890, 8061, 8233, 8405, 8578, 8750, 8921, 9094, 9266, 9438, 9610, 9782, 9954, 10126, 10298, 10471, 10642, 10814, 10986, 11159, 11331, 11502, 11674, 11847, 12019, 12190, 12362, 12535, 12707, 12879, 13050, 13223, 13395, 13567]
    # #第1击枪尾攻击力：<data1>%
    # data1 = [0, 1860, 2050, 2239, 2427, 2616, 2805, 2993, 3183, 3372, 3561, 3749, 3937, 4126, 4315, 4504, 4693, 4882, 5070, 5259, 5449, 5638, 5826, 6015, 6204, 6392, 6582, 6770, 6959, 7147, 7336, 7525, 7715, 7903, 8092, 8281, 8469, 8658, 8848, 9037, 9225, 9414, 9602, 9790, 9980, 10169, 10358, 10546, 10735, 10924, 11114, 11302, 11491, 11680, 11868, 12057, 12247, 12435, 12623, 12812, 13001, 13189, 13379, 13568, 13757, 13945, 14134, 14323, 14513, 14701, 14890]
    
    # 近距离攻击和枪尾攻击不会同时命中一个敌人， 判定重叠时， 会优先判定为枪尾攻击
    #第2击攻击力：<data2>%
    data0 = [0, 1884, 2075, 2266, 2458, 2649, 2840, 3031, 3222, 3414, 3605, 3796, 3987, 4178, 4369, 4561, 4752, 4943, 5134, 5325, 5516, 5708, 5899, 6090, 6281, 6472, 6664, 6855, 7046, 7237, 7427, 7618, 7811, 8002, 8193, 8383, 8574, 8767, 8958, 9148, 9339, 9530, 9721, 9913, 10104, 10295, 10486, 10677, 10868, 11060, 11251, 11442, 11633, 11824, 12016, 12207, 12398, 12589, 12780, 12971, 13163, 13354, 13545, 13736, 13927, 14118, 14310, 14501, 14692, 14883, 15074]
    #第2击枪尾攻击力：<data3>%
    data1 = [0, 2252, 2480, 2710, 2939, 3167, 3396, 3624, 3852, 4080, 4310, 4538, 4767, 4996, 5224, 5452, 5681, 5910, 6138, 6366, 6596, 6824, 7052, 7282, 7510, 7738, 7967, 8196, 8424, 8652, 8882, 9110, 9338, 9567, 9795, 10024, 10252, 10482, 10710, 10938, 11167, 11395, 11623, 11854, 12082, 12310, 12538, 12767, 12995, 13223, 13454, 13682, 13910, 14139, 14367, 14595, 14823, 15053, 15282, 15510, 15739, 15967, 16195, 16425, 16653, 16881, 17110, 17339, 17567, 17795, 18025]
    攻击次数2 =1
    # 基础 = 3694.57142857143	
    # 成长 = 417.428571428571	
    CD = 7.0	
    TP成长 = 0.1	
    TP上限 = 5

class 技能2(职业主动技能):	
    名称 = '行云：风'	
    所在等级 = 15	
    等级上限 = 60	
    基础等级 = 46	
    # 稍稍对不上
    #刺击攻击力：<data0>%
    data0 = [0, 158, 174, 189, 206, 222, 238, 254, 270, 286, 302, 318, 335, 350, 366, 382, 398, 415, 431, 446, 462, 479, 495, 511, 526, 543, 559, 575, 591, 607, 623, 639, 655, 672, 687, 703, 719, 736, 752, 767, 783, 799, 816, 832, 848, 863, 880, 896, 912, 928, 944, 960, 976, 992, 1009, 1024, 1040, 1056, 1073, 1089, 1104, 1120, 1137, 1153, 1169, 1184, 1201, 1217, 1233, 1249, 1264]
    #旋风攻击力：<data1>%
    data1 = [0, 263, 289, 316, 343, 369, 396, 423, 449, 476, 502, 529, 556, 582, 609, 636, 662, 689, 716, 742, 769, 796, 822, 849, 876, 902, 929, 955, 982, 1009, 1035, 1062, 1089, 1115, 1142, 1169, 1195, 1222, 1249, 1275, 1302, 1329, 1355, 1382, 1409, 1435, 1462, 1488, 1515, 1542, 1568, 1595, 1622, 1648, 1675, 1702, 1728, 1755, 1782, 1808, 1835, 1862, 1888, 1915, 1942, 1968, 1995, 2021, 2048, 2075, 2101]
    攻击次数2 = 8
    # 基础 = 2094.93333333333	
    # 成长 = 236.066666666667	
    CD = 5	
    TP成长 = 0.1	
    TP上限 = 5

class 技能3(职业主动技能):	
    名称 = '行云：疾'	
    所在等级 = 20	
    等级上限 = 60	
    基础等级 = 43	
    #横扫攻击力：<data0>%
    data0 = [0, 2932, 3231, 3529, 3826, 4124, 4421, 4719, 5016, 5314, 5611, 5909, 6206, 6504, 6801, 7099, 7397, 7695, 7993, 8290, 8588, 8885, 9183, 9480, 9778, 10075, 10373, 10670, 10968, 11265, 11563, 11861, 12159, 12457, 12754, 13052, 13349, 13647, 13944, 14242, 14539, 14837, 15134, 15432, 15730, 16027, 16326, 16623, 16921, 17218, 17516, 17813, 18111, 18408, 18706, 19003, 19301, 19599, 19896, 20194, 20491, 20790, 21087, 21385, 21682, 21980, 22277, 22575, 22872, 23170, 23468]
    # 基础 = 2634.38095238095	
    # 成长 = 297.619047619048	
    CD = 6.0	
    TP成长 = 0.1	
    TP上限 = 5

class 技能4(职业主动技能):	
    名称 = '行云：落'	
    所在等级 = 25	
    等级上限 = 60	
    基础等级 = 41	
    # 基础 = 3784.675
    # 成长 = 427.325
    data0 = [0, 4212, 4639, 5067, 5494, 5921, 6348, 6776, 7203, 7631, 8058, 8485, 8912, 9339, 9768, 10195, 10622, 11049, 11476, 11903, 12332, 12759, 13186, 13613, 14040, 14468, 14896, 15323, 15750, 16177, 16604, 17032, 17459, 17887, 18314, 18741, 19169, 19596, 20023, 20451, 20878, 21305, 21733, 22160, 22587, 23014, 23442, 23870, 24297, 24724, 25151, 25578, 26006, 26434, 26861, 27288, 27715, 28142, 28571, 28998, 29425, 29852, 30279, 30707, 31135, 31562, 31989, 32416, 32843, 33271, 33698]
    CD = 8.0	
    TP成长 = 0.1	
    TP上限 = 5

class 技能5(被动技能):	
    名称 = '行云：沐'	
    所在等级 = 25	
    等级上限 = 20	
    基础等级 = 10	
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.05 + 0.01 * self.等级, 5)
        else:
            return round(0.95 + 0.02 * self.等级, 5)

class 技能6(职业主动技能):	
    名称 = '旋风枪'	
    所在等级 = 25	
    等级上限 = 60	
    基础等级 = 41	
    # 基础 = 4467.65	
    # 成长 = 504.35	
    CD = 9
    data0 = [0, 452, 498, 542, 589, 635, 681, 727, 772, 819, 864, 910, 956, 1001, 1048, 1094, 1139, 1185, 1231, 1277, 1322, 1368, 1415, 1461, 1505, 1552, 1598, 1643, 1690, 1735, 1782, 1827, 1873, 1920, 1964, 2010, 2057, 2103, 2148, 2194, 2240, 2286, 2331, 2378, 2424, 2469, 2515, 2561, 2606, 2653, 2698, 2745, 2790, 2836, 2883, 2927, 2973, 3020, 3066, 3111, 3157, 3203, 3249, 3294, 3340, 3387, 3432, 3479, 3524, 3569, 3616]
    攻击次数 =11
    TP成长 = 0.1	
    TP上限 = 5

class 技能7(职业主动技能):	
    名称 = '无畏波动枪'
    # 其余部分能被撞出去的才有,固定怪物没有
    备注 = '突进+刺击'
    所在等级 = 30	
    等级上限 = 60	
    基础等级 = 38	
    # 固定怪物吃以下
    #普通突进攻击力：<data2>%
    data0 = [0, 1756, 1934, 2112, 2290, 2468, 2646, 2824, 3002, 3180, 3358, 3537, 3716, 3894, 4072, 4250, 4428, 4606, 4784, 4962, 5140, 5318, 5496, 5674, 5854, 6032, 6210, 6388, 6566, 6744, 6922, 7100, 7278, 7456, 7634, 7812, 7990, 8170, 8348, 8526, 8704, 8882, 9060, 9238, 9416, 9594, 9772, 9950, 10128, 10306, 10486, 10664, 10842, 11020, 11198, 11376, 11554, 11732, 11910, 12088, 12266, 12444, 12622, 12802, 12980, 13158, 13336, 13514, 13692, 13870, 14048]
    攻击次数 = 1
    #普通刺击攻击力：<data3>%
    data1 = [0, 4097, 4513, 4928, 5344, 5760, 6176, 6591, 7007, 7422, 7838, 8254, 8670, 9085, 9501, 9916, 10332, 10748, 11164, 11580, 11995, 12411, 12826, 13242, 13658, 14074, 14490, 14905, 15320, 15736, 16152, 16568, 16984, 17399, 17814, 18230, 18646, 19062, 19478, 19894, 20309, 20724, 21140, 21556, 21972, 22388, 22804, 23218, 23634, 24050, 24466, 24882, 25298, 25713, 26128, 26544, 26960, 27376, 27792, 28208, 28622, 29038, 29454, 29870, 30286, 30702, 31118, 31532, 31948, 32364, 32780]
    攻击次数2 = 1

    # 能推开的吃以下的
    #对被刺穿敌人的攻击力：<data0>%
    # data0 = [0, 1463, 1612, 1759, 1908, 2057, 2206, 2353, 2502, 2651, 2799, 2947, 3096, 3245, 3393, 3541, 3690, 3839, 3986, 4135, 4284, 4432, 4580, 4729, 4878, 5026, 5174, 5323, 5472, 5619, 5768, 5917, 6066, 6213, 6362, 6511, 6659, 6807, 6956, 7105, 7253, 7401, 7550, 7699, 7846, 7995, 8144, 8292, 8440, 8589, 8738, 8886, 9034, 9183, 9332, 9480, 9628, 9777, 9925, 10073, 10222, 10371, 10519, 10667, 10816, 10965, 11113, 11261, 11410, 11559, 11707]
    # 攻击次数 = 1
    #被刺穿后弹开时的攻击力：<data1>%
    # data1 = [0, 3512, 3868, 4224, 4580, 4937, 5294, 5650, 6006, 6362, 6718, 7074, 7431, 7788, 8144, 8500, 8856, 9212, 9569, 9925, 10282, 10638, 10994, 11350, 11707, 12063, 12420, 12776, 13132, 13488, 13844, 14201, 14557, 14914, 15270, 15626, 15982, 16339, 16695, 17052, 17408, 17764, 18120, 18476, 18833, 19189, 19546, 19902, 20258, 20614, 20971, 21327, 21683, 22040, 22396, 22752, 23109, 23465, 23821, 24178, 24534, 24890, 25246, 25603, 25959, 26315, 26672, 27028, 27384, 27741, 28097]
    #弹开的敌人撞到地面时的冲撞攻击力：<data4>%
    # data4 = [0, 878, 967, 1056, 1145, 1234, 1323, 1412, 1501, 1590, 1679, 1768, 1857, 1946, 2035, 2124, 2213, 2302, 2391, 2481, 2570, 2659, 2748, 2837, 2927, 3016, 3105, 3194, 3283, 3372, 3461, 3550, 3639, 3728, 3817, 3906, 3995, 4084, 4173, 4262, 4351, 4440, 4529, 4618, 4707, 4797, 4886, 4975, 5064, 5153, 5243, 5332, 5421, 5510, 5599, 5688, 5777, 5866, 5955, 6044, 6133, 6222, 6311, 6400, 6489, 6578, 6667, 6756, 6845, 6934, 7023]
    #弹开的敌人撞到墙壁时的冲撞攻击力：<data5>%
    # data5 = [0, 994, 1095, 1197, 1297, 1399, 1499, 1600, 1702, 1802, 1904, 2004, 2105, 2206, 2307, 2408, 2509, 2610, 2710, 2812, 2912, 3014, 3115, 3215, 3317, 3417, 3518, 3620, 3720, 3822, 3922, 4023, 4124, 4225, 4327, 4427, 4528, 4629, 4730, 4830, 4932, 5033, 5133, 5235, 5335, 5437, 5537, 5638, 5740, 5840, 5942, 6042, 6143, 6245, 6345, 6446, 6547, 6648, 6748, 6850, 6951, 7052, 7153, 7253, 7355, 7455, 7557, 7658, 7758, 7860, 7960]

    # 基础 = 5259.13513513513	
    # 成长 = 593.864864864865	
    CD = 9.0	
    TP成长 = 0.1	
    TP上限 = 5

class 技能8(职业主动技能):	
    名称 = '升龙破空枪'	
    所在等级 = 35	
    等级上限 = 60	
    基础等级 = 36	
    # 数据对不上
    # 基础 = 8384.54285714286	
    # 成长 = 1091.45714285714	
    #横扫攻击力：<data0>%
    data0 = [0, 2305, 2538, 2772, 3006, 3240, 3473, 3708, 3941, 4176, 4409, 4643, 4877, 5111, 5344, 5578, 5812, 6045, 6280, 6513, 6747, 6981, 7215, 7448, 7683, 7916, 8150, 8384, 8618, 8851, 9086, 9319, 9554, 9787, 10021, 10255, 10489, 10722, 10957, 11190, 11424, 11658, 11892, 12125, 12360, 12593, 12828, 13061, 13294, 13529, 13762, 13996, 14230, 14464, 14697, 14932, 15165, 15399, 15633, 15867, 16100, 16335, 16568, 16802, 17036, 17270, 17503, 17738, 17971, 18206, 18439]
    #上挑攻击力：<data1>%
    data1 = [0, 3457, 3808, 4159, 4509, 4860, 5210, 5562, 5912, 6263, 6613, 6965, 7315, 7666, 8016, 8367, 8718, 9069, 9419, 9770, 10122, 10472, 10823, 11173, 11525, 11875, 12226, 12576, 12927, 13278, 13629, 13979, 14330, 14681, 15032, 15382, 15733, 16083, 16435, 16786, 17136, 17487, 17838, 18189, 18539, 18890, 19241, 19592, 19942, 20293, 20643, 20995, 21345, 21696, 22046, 22398, 22748, 23099, 23449, 23800, 24152, 24502, 24853, 25203, 25555, 25905, 26256, 26606, 26957, 27308, 27659]
    攻击次数2 =1
    #最后一击攻击力：<data2>%
    data2 = [0, 4714, 5192, 5671, 6149, 6627, 7106, 7584, 8063, 8540, 9018, 9497, 9975, 10454, 10932, 11410, 11889, 12367, 12846, 13323, 13801, 14280, 14758, 15237, 15715, 16193, 16672, 17150, 17629, 18106, 18584, 19063, 19541, 20020, 20498, 20976, 21455, 21933, 22412, 22889, 23367, 23846, 24324, 24803, 25281, 25759, 26238, 26716, 27195, 27672, 28150, 28629, 29107, 29586, 30064, 30542, 31021, 31499, 31977, 32455, 32933, 33412, 33890, 34369, 34847, 35325, 35804, 36282, 36760, 37238, 37716]
    攻击次数3 = 1
    CD = 20
    TP成长 = 0.1	
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.10
            self.CD *= 0.88
        if x == 1:
            self.倍率 *= 1.19
            self.CD *= 0.88

class 技能9(职业主动技能):	
    名称 = '狂龙怒啸'	
    所在等级 = 40	
    等级上限 = 60	
    基础等级 = 33	
    #旋转攻击力：<data0>%
    data0 = [0, 635, 700, 765, 829, 894, 958, 1022, 1088, 1152, 1216, 1281, 1346, 1410, 1475, 1539, 1603, 1668, 1733, 1797, 1861, 1927, 1991, 2055, 2120, 2184, 2249, 2314, 2378, 2442, 2508, 2572, 2636, 2701, 2765, 2830, 2894, 2959, 3023, 3087, 3153, 3217, 3281, 3346, 3411, 3475, 3540, 3604, 3669, 3734, 3798, 3862, 3926, 3992, 4056, 4120, 4185, 4250, 4314, 4379, 4443, 4507, 4573, 4637, 4701, 4766, 4831, 4895, 4959, 5024, 5088]
    攻击次数 = 15
    # 基础 = 8556.5625	
    # 成长 = 968.4375
    CD = 20
    TP成长 = 0.1	
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.1
            self.CD *= 0.76
        if x == 1:
            self.倍率 *= 1.188
            self.CD *= 0.76

class 技能10(职业主动技能):	
    名称 = '夺命雷霆枪'	
    所在等级 = 45	
    等级上限 = 60	
    基础等级 = 31	
    #近距离刺击攻击力：<data0>%
    data0 = [0, 850, 937, 1023, 1110, 1196, 1281, 1368, 1454, 1541, 1627, 1713, 1800, 1886, 1972, 2059, 2145, 2232, 2318, 2404, 2491, 2576, 2663, 2749, 2835, 2922, 3008, 3095, 3181, 3267, 3354, 3440, 3526, 3613, 3698, 3786, 3871, 3957, 4044, 4130, 4217, 4303, 4389, 4476, 4562, 4648, 4735, 4821, 4908, 4993, 5079, 5166, 5252, 5339, 5425, 5511, 5598, 5684, 5771, 5857, 5943, 6030, 6116, 6201, 6288, 6374, 6461, 6547, 6633, 6720, 6806]
    攻击次数 = 15
    # 引起受创效果的刺击攻击力：<data1>%
    # data1 = [0, 850, 937, 1023, 1110, 1196, 1281, 1368, 1454, 1541, 1627, 1713, 1800, 1886, 1972, 2059, 2145, 2232, 2318, 2404, 2491, 2576, 2663, 2749, 2835, 2922, 3008, 3095, 3181, 3267, 3354, 3440, 3526, 3613, 3698, 3786, 3871, 3957, 4044, 4130, 4217, 4303, 4389, 4476, 4562, 4648, 4735, 4821, 4908, 4993, 5079, 5166, 5252, 5339, 5425, 5511, 5598, 5684, 5771, 5857, 5943, 6030, 6116, 6201, 6288, 6374, 6461, 6547, 6633, 6720, 6806]
    # #每1次刺击对应的横斩攻击力：<data2>%
    data1 = [0, 154, 170, 185, 201, 217, 233, 249, 264, 280, 295, 311, 327, 342, 358, 374, 390, 406, 421, 436, 452, 468, 484, 499, 515, 531, 547, 563, 577, 593, 609, 625, 641, 657, 672, 688, 704, 719, 735, 750, 766, 782, 798, 814, 829, 844, 860, 876, 892, 907, 923, 939, 955, 971, 985, 1001, 1017, 1033, 1049, 1064, 1080, 1096, 1112, 1127, 1142, 1158, 1174, 1190, 1206, 1222, 1237]
    攻击次数2 = 15
    #最后横斩攻击力：<data3>%
    data2 = [0, 9282, 10223, 11164, 12107, 13048, 13989, 14931, 15873, 16814, 17756, 18698, 19639, 20581, 21523, 22464, 23406, 24348, 25289, 26231, 27173, 28114, 29056, 29997, 30939, 31881, 32822, 33764, 34706, 35647, 36589, 37531, 38472, 39414, 40356, 41297, 42239, 43181, 44122, 45063, 46006, 46947, 47888, 48831, 49772, 50713, 51656, 52597, 53538, 54481, 55422, 56363, 57305, 58247, 59188, 60130, 61072, 62013, 62955, 63897, 64838, 65780, 66722, 67663, 68605, 69547, 70488, 71430, 72371, 73313, 74255]
    攻击次数3 = 1
    # 基础 = 21869.8666666667	
    # 成长 = 2472.13333333333	
    CD = 47	
    TP成长 = 0.1	
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.data2 = [(i * 1.65) for i in self.data2]
        if x == 1:
            self.data2 = [(i * 1.86) for i in self.data2]

class 技能11(被动技能):	
    名称 = '行云：启'	
    所在等级 = 48	
    等级上限 = 40	
    基础等级 = 20	
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.06 + 0.015 * self.等级, 5)

class 技能12(职业主动技能):	
    名称 = '流云幻灭'	
    所在等级 = 50	
    等级上限 = 40	
    基础等级 = 12	
    # 基础 = 43306.1
    # 成长 = 13091
    # 原数据是游戏数据的1.1倍,需要确认
    #第一击攻击力：<data0>%
    data0 = [0, 964, 1188, 1411, 1635, 1858, 2081, 2305, 2529, 2752, 2976, 3200, 3424, 3647, 3871, 4094, 4317, 4541, 4765, 4988, 5212, 5436, 5660, 5883, 6106, 6330, 6553, 6777, 7001, 7224, 7448, 7672, 7896, 8119, 8342, 8566, 8789, 9013, 9237, 9461, 9684, 9908, 10132, 10355, 10578, 10802, 11025, 11249, 11473, 11697, 11920, 12144, 12368, 12590, 12814, 13038, 13261, 13485, 13709, 13933, 14156, 14380, 14604, 14826, 15050, 15274, 15497, 15721, 15945, 16169, 16392]
    攻击次数 = 1
    #第2击攻击力：<data1>%
    data1 = [0, 2739, 3375, 4010, 4645, 5281, 5916, 6552, 7187, 7821, 8458, 9092, 9728, 10363, 10999, 11633, 12270, 12904, 13540, 14175, 14811, 15445, 16082, 16716, 17353, 17987, 18622, 19258, 19893, 20528, 21164, 21799, 22434, 23070, 23705, 24340, 24976, 25611, 26247, 26882, 27517, 28153, 28788, 29423, 30059, 30694, 31329, 31964, 32600, 33234, 33871, 34505, 35142, 35776, 36412, 37047, 37683, 38317, 38954, 39588, 40224, 40859, 41495, 42129, 42766, 43400, 44035, 44671, 45306, 45942, 46577]
    攻击次数2 = 1
    #第3击攻击力：<data2>%
    data2 = [0, 3288, 4049, 4811, 5574, 6337, 7100, 7861, 8624, 9387, 10149, 10911, 11673, 12437, 13199, 13960, 14723, 15485, 16249, 17011, 17772, 18535, 19298, 20061, 20822, 21584, 22348, 23110, 23872, 24634, 25396, 26160, 26921, 27684, 28446, 29210, 29972, 30733, 31496, 32259, 33022, 33783, 34545, 35308, 36071, 36833, 37595, 38357, 39121, 39883, 40645, 41407, 42170, 42933, 43694, 44457, 45219, 45982, 46744, 47506, 48269, 49032, 49795, 50556, 51318, 52082, 52844, 53605, 54368, 55130, 55894]
    攻击次数3 = 1
    #第4击攻击力：<data3>%
    data3 = [0, 3835, 4725, 5614, 6503, 7394, 8283, 9172, 10062, 10951, 11840, 12729, 13619, 14508, 15397, 16289, 17178, 18067, 18957, 19846, 20735, 21624, 22514, 23403, 24293, 25183, 26072, 26961, 27851, 28740, 29629, 30518, 31409, 32299, 33189, 34078, 34967, 35856, 36746, 37635, 38524, 39414, 40304, 41193, 42083, 42972, 43861, 44752, 45641, 46530, 47419, 48310, 49199, 50088, 50978, 51867, 52756, 53645, 54535, 55424, 56314, 57204, 58094, 58983, 59873, 60762, 61651, 62541, 63430, 64320, 65210]
    攻击次数4 = 1
    #第5击攻击力：<data4>%
    data4 = [0, 4384, 5400, 6416, 7433, 8449, 9465, 10482, 11498, 12515, 13532, 14548, 15564, 16581, 17598, 18615, 19631, 20647, 21665, 22681, 23697, 24714, 25730, 26747, 27764, 28780, 29797, 30813, 31828, 32845, 33862, 34878, 35895, 36912, 37928, 38945, 39961, 40977, 41995, 43011, 44027, 45044, 46060, 47078, 48094, 49110, 50127, 51143, 52160, 53177, 54193, 55209, 56227, 57243, 58258, 59275, 60291, 61307, 62325, 63341, 64358, 65374, 66390, 67408, 68424, 69440, 70457, 71474, 72490, 73507, 74523]
    攻击次数5 = 1
    #第6击攻击力：<data5>%
    data5 = [0, 1644, 2025, 2406, 2786, 3168, 3549, 3930, 4312, 4694, 5074, 5456, 5835, 6217, 6599, 6980, 7361, 7742, 8124, 8506, 8886, 9267, 9647, 10029, 10411, 10792, 11173, 11555, 11936, 12318, 12697, 13079, 13461, 13841, 14223, 14604, 14985, 15367, 15747, 16128, 16509, 16891, 17273, 17653, 18035, 18416, 18797, 19178, 19559, 19941, 20322, 20703, 21085, 21465, 21847, 22229, 22608, 22990, 23371, 23753, 24134, 24515, 24897, 25276, 25658, 26040, 26420, 26802, 27184, 27565, 27946]
    攻击次数6 = 3
    #第7击攻击力：<data6>%
    data6 = [0, 4932, 6075, 7219, 8361, 9505, 10649, 11792, 12936, 14081, 15224, 16367, 17511, 18654, 19798, 20942, 22085, 23228, 24372, 25516, 26660, 27804, 28947, 30090, 31233, 32377, 33521, 34665, 35809, 36952, 38095, 39239, 40383, 41526, 42670, 43813, 44956, 46100, 47245, 48388, 49532, 50676, 51818, 52962, 54106, 55249, 56393, 57538, 58680, 59824, 60967, 62111, 63255, 64398, 65541, 66685, 67828, 68973, 70117, 71260, 72403, 73547, 74690, 75834, 76978, 78121, 79265, 80408, 81552, 82696, 83839]
    攻击次数7 = 1
    #第8击攻击力：<data7>%
    data7 = [0, 5478, 6749, 8020, 9290, 10561, 11832, 13103, 14373, 15644, 16915, 18185, 19456, 20727, 21998, 23268, 24539, 25810, 27080, 28351, 29621, 30892, 32162, 33433, 34704, 35974, 37245, 38516, 39788, 41057, 42329, 43600, 44869, 46141, 47412, 48683, 49953, 51224, 52495, 53763, 55035, 56306, 57577, 58847, 60118, 61389, 62659, 63930, 65201, 66472, 67742, 69013, 70284, 71555, 72825, 74096, 75367, 76636, 77907, 79178, 80449, 81719, 82990, 84261, 85531, 86802, 88073, 89344, 90614, 91885, 93156]
    攻击次数8 = 1
    #斗气长枪攻击力：<data8>%
    data8 = [0, 24110, 29702, 38820, 44971, 51121, 57271, 63421, 69571, 75721, 81871, 88022, 94171, 100321, 106472, 112621, 118773, 124922, 131070, 137222, 143371, 149520, 155672, 161821, 167971, 174122, 180271, 186422, 192572, 198722, 204872, 211023, 217172, 223322, 229473, 235622, 241773, 247923, 254072, 260223, 266373, 272524, 278673, 284823, 290974, 297123, 303272, 309424, 315572, 321723, 327873, 334022, 340173, 346323, 352473, 358624, 364774, 370923, 377074, 383224, 389373, 395525, 401674, 407823, 413975, 420124, 426273, 432425, 438574, 444725, 450875]
    攻击次数9 = 1
    CD = 145
    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        等效倍率 += self.data0[self.等级] * self.攻击次数
        等效倍率 += self.data1[self.等级] * self.攻击次数2
        等效倍率 += self.data2[self.等级] * self.攻击次数3
        等效倍率 += self.data3[self.等级] * self.攻击次数4
        等效倍率 += self.data4[self.等级] * self.攻击次数5
        等效倍率 += self.data5[self.等级] * self.攻击次数6
        等效倍率 += self.data6[self.等级] * self.攻击次数7
        等效倍率 += self.data7[self.等级] * self.攻击次数8
        等效倍率 += self.data8[self.等级] * self.攻击次数9
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能13(职业主动技能):	
    名称 = '风火燎原'	
    所在等级 = 60	
    等级上限 = 40	
    基础等级 = 23	
    data0 = [0, 1222, 1346, 1471, 1595, 1719, 1843, 1967, 2091, 2215, 2339, 2462, 2586, 2710, 2834, 2958, 3082, 3206, 3331, 3455, 3579, 3703, 3827, 3951, 4075, 4199, 4323, 4447, 4571, 4695, 4819, 4943, 5067, 5191, 5316, 5440, 5564, 5688, 5812, 5936, 6060, 6184, 6308, 6432, 6556, 6680, 6804, 6928, 7052, 7176, 7301, 7425, 7549, 7673, 7797, 7921, 8045, 8168, 8292, 8416, 8540, 8664, 8788, 8912, 9036, 9161, 9285, 9409, 9533, 9657, 9781]
    攻击次数 = 20
    # 基础 = 21959.0909090909	
    # 成长 = 2480.90909090909	
    CD = 32.0	
    TP成长 = 0.1	
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.275
        if x == 1:
            self.倍率 *= 1.365

class 技能14(职业主动技能):	
    名称 = '三一斩月'	
    所在等级 = 70	
    等级上限 = 40	
    基础等级 = 18
    #枪身攻击力：<data0>%
    data0 = [0, 635, 699, 763, 827, 891, 956, 1021, 1085, 1150, 1214, 1278, 1342, 1406, 1472, 1536, 1600, 1665, 1729, 1793, 1857, 1922, 1987, 2051, 2115, 2180, 2244, 2308, 2372, 2438, 2502, 2566, 2630, 2695, 2759, 2823, 2889, 2953, 3017, 3081, 3145, 3210, 3274, 3339, 3404, 3468, 3532, 3596, 3660, 3725, 3790, 3854, 3919, 3983, 4047, 4111, 4176, 4240, 4305, 4369, 4434, 4498, 4562, 4626, 4691, 4756, 4820, 4884, 4949, 5013, 5077]
    #[三一斩月]攻击力：<data1>%
    data1 = [0, 3887, 4281, 4676, 5070, 5465, 5859, 6254, 6648, 7043, 7437, 7832, 8226, 8620, 9015, 9409, 9804, 10198, 10593, 10987, 11382, 11776, 12170, 12565, 12959, 13354, 13748, 14143, 14537, 14930, 15325, 15719, 16114, 16508, 16903, 17297, 17692, 18086, 18481, 18875, 19269, 19664, 20058, 20453, 20847, 21242, 21636, 22031, 22425, 22819, 23214, 23608, 24003, 24397, 24792, 25186, 25581, 25975, 26370, 26764, 27158, 27553, 27947, 28342, 28736, 29131, 29525, 29918, 30313, 30707, 31102]
    攻击次数2 = 8
    # 基础 = 28510.88235	
    # 成长 = 3220.117647
    CD = 52.0	
    TP成长 = 0.1	
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        if x == 1:
            self.倍率 *= 1.31

class 技能15(职业主动技能):	
    名称 = '无双突刺'	
    所在等级 = 75	
    等级上限 = 40	
    基础等级 = 16	
    #第1~2击攻击力：<data0>%
    data0 = [0, 3236, 3565, 3893, 4222, 4551, 4878, 5207, 5536, 5864, 6192, 6520, 6849, 7178, 7505, 7834, 8163, 8491, 8820, 9147, 9476, 9805, 10133, 10462, 10790, 11118, 11447, 11775, 12103, 12432, 12760, 13089, 13418, 13745, 14074, 14402, 14731, 15060, 15387, 15716, 16045, 16373, 16701, 17029, 17358, 17687, 18014, 18343, 18672, 19000, 19329, 19656, 19985, 20314, 20642, 20971, 21299, 21627, 21956, 22284, 22612, 22941, 23269, 23598, 23927, 24254, 24583, 24911, 25240, 25569, 25896]
    攻击次数 = 2
    #第3~4击攻击力：<data1>%
    # data1 = [0, 20418, 22489, 24562, 26633, 28704, 30776, 32847, 34918, 36991, 39062, 41133, 43204, 45276, 47347, 49419, 51491, 53562, 55633, 57705, 59776, 61848, 63920, 65991, 68062, 70133, 72205, 74277, 76348, 78420, 80491, 82562, 84634, 86706, 88777, 90849, 92920, 94991, 97062, 99135, 101206, 103277, 105349, 107420, 109491, 111564, 113635, 115706, 117778, 119849, 121920, 123993, 126064, 128135, 130207, 132278, 134349, 136422, 138493, 140564, 142635, 144707, 146778, 148850, 150922, 152993, 155064, 157136, 159207, 161279, 163351]
    #第3~4击枪尾攻击力：<data2>%
    data1 = [0, 22908, 25233, 27556, 29881, 32205, 34529, 36853, 39177, 41502, 43825, 46149, 48474, 50798, 53121, 55446, 57770, 60095, 62418, 64742, 67067, 69390, 71714, 74039, 76363, 78686, 81011, 83335, 85659, 87983, 90307, 92632, 94955, 97279, 99604, 101928, 104252, 106576, 108900, 111224, 113548, 115872, 118197, 120520, 122845, 125169, 127493, 129817, 132141, 134465, 136789, 139113, 141438, 143762, 146085, 148410, 150734, 153057, 155382, 157706, 160031, 162354, 164678, 167003, 169327, 171650, 173975, 176299, 178622, 180947, 183271]
    攻击次数2 = 2
    # 基础 = 46982.8	
    # 成长 = 5305.2	
    CD = 33.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            攻击次数 = 0
            self.data1 = [(i*1.45) for i in self.data1]
            # self.倍率 *= 1.27049

class 技能16(被动技能):	
    名称 = '行云：冥'	
    所在等级 = 75	
    等级上限 = 40	
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)	

class 技能17(职业主动技能):	
    名称 = '流光无影闪'	
    所在等级 = 80	
    等级上限 = 40	
    基础等级 = 13	
    # 基础 = 52609.8333333333	
    # 成长 = 5940.16666666667	
    #突进攻击力：<data0>%
    data0 = [0, 5269, 5804, 6338, 6872, 7408, 7942, 8476, 9011, 9546, 10081, 10615, 11149, 11685, 12219, 12753, 13288, 13823, 14357, 14892, 15426, 15962, 16496, 17030, 17565, 18100, 18634, 19169, 19703, 20238, 20773, 21307, 21841, 22377, 22911, 23446, 23980, 24515, 25050, 25584, 26118, 26654, 27188, 27722, 28257, 28791, 29327, 29861, 30395, 30931, 31465, 31999, 32534, 33068, 33603, 34138, 34672, 35207, 35742, 36276, 36811, 37345, 37880, 38415, 38949, 39483, 40019, 40553, 41087, 41622, 42157]
    攻击次数 = 1
    #终结攻击力：<data1>%
    data1 = [0, 53281, 58687, 64092, 69498, 74904, 80309, 85714, 91120, 96525, 101930, 107335, 112742, 118147, 123552, 128958, 134363, 139768, 145175, 150580, 155985, 161391, 166796, 172201, 177606, 183012, 188417, 193823, 199229, 204634, 210039, 215445, 220850, 226255, 231662, 237067, 242472, 247877, 253283, 258688, 264093, 269500, 274905, 280310, 285716, 291121, 296526, 301932, 307337, 312743, 318148, 323554, 328959, 334364, 339770, 345175, 350580, 355987, 361392, 366797, 372203, 377608, 383013, 388418, 393825, 399230, 404635, 410041, 415446, 420851, 426257]
    攻击次数2 = 1
    CD = 44
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            # 算法待定,加还是乘
            self.倍率 *= 1.2*1.14
            self.CD *= 0.88

class 技能18(职业主动技能):	
    名称 = '极影无形杀'	
    所在等级 = 85	
    等级上限 = 40	
    基础等级 = 5	
    #第1次刺击攻击力：<data0>%
    data0 = [0, 12630, 15559, 18487, 21416, 24345, 27275, 30204, 33133, 36061, 38990, 41919, 44848, 47777, 50705, 53634, 56563, 59492, 62421, 65349, 68278, 71207, 74136, 77065, 79994, 82922, 85851, 88781, 91710, 94639, 97567, 100496, 103425, 106354, 109283, 112211, 115140, 118069, 120998, 123927, 126855, 129784, 132713, 135642, 138571, 141500, 144428, 147358, 150287, 153216, 156145, 159073, 162002, 164931, 167860, 170789, 173717, 176646, 179575, 182504, 185433, 188362, 191290, 194219, 197148, 200077, 203007, 205934, 208864, 211793, 214722]
    #乱舞斩击攻击力：<data1>%
    data1 = [0, 7017, 8644, 10270, 11898, 13525, 15153, 16780, 18406, 20034, 21661, 23288, 24915, 26542, 28169, 29797, 31424, 33050, 34678, 36305, 37933, 39559, 41186, 42814, 44441, 46068, 47695, 49322, 50949, 52577, 54204, 55830, 57458, 59085, 60713, 62339, 63966, 65594, 67221, 68848, 70475, 72102, 73729, 75357, 76984, 78611, 80238, 81865, 83493, 85119, 86746, 88374, 90001, 91628, 93255, 94882, 96510, 98137, 99763, 101391, 103018, 104645, 106273, 107899, 109526, 111154, 112781, 114409, 116035, 117662, 119290]
    攻击次数2 = 7
    #乱舞刺击攻击力：<data2>%
    data2 = [0, 2806, 3458, 4108, 4759, 5410, 6061, 6711, 7363, 8013, 8664, 9315, 9966, 10616, 11268, 11918, 12569, 13220, 13871, 14521, 15173, 15823, 16474, 17125, 17776, 18426, 19078, 19728, 20380, 21030, 21681, 22332, 22983, 23633, 24285, 24935, 25586, 26238, 26888, 27539, 28190, 28841, 29491, 30143, 30793, 31444, 32095, 32746, 33396, 34048, 34698, 35349, 36000, 36651, 37301, 37953, 38603, 39255, 39905, 40556, 41207, 41858, 42508, 43160, 43810, 44461, 45112, 45763, 46413, 47065, 47715]
    攻击次数3 = 17
    #最后一击攻击力：<data3>%
    data3 = [0, 30874, 38034, 45194, 52353, 59512, 66672, 73831, 80991, 88149, 95309, 102469, 109628, 116788, 123947, 131106, 138266, 145426, 152585, 159744, 166904, 174063, 181223, 188383, 195541, 202701, 209860, 217020, 224179, 231338, 238498, 245658, 252817, 259976, 267136, 274295, 281455, 288615, 295773, 302933, 310093, 317252, 324411, 331570, 338730, 345890, 353049, 360208, 367368, 374527, 381687, 388847, 396005, 403165, 410325, 417484, 424643, 431803, 438962, 446122, 453282, 460440, 467600, 474759, 481919, 489079, 496237, 503397, 510557, 517716, 524875]
    攻击次数4 = 1

    # 基础 = 107737	
    # 成长 = 32553	
    CD = 180

class 技能19(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 技能20(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 技能21(被动技能):
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

技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能' + str(i) + '())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

一觉序号 = 0
二觉序号 = 0
三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        三觉序号 = 技能序号[i.名称]

护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        护石选项.append(i.名称)

符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        符文选项.append(i.名称)


class 职业属性(角色属性):
    实际名称 = '圣武枪魂'
    角色 = '魔枪士'
    职业 = '决战者'

    武器选项 = ['长枪']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 2.0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()

        x = self.技能栏[11].加成倍率(self.武器类型)
        self.技能栏[2].被动倍率 *= (0.025 + x) / x
        self.技能栏[3].被动倍率 *= (0.020 + x) / x
        self.技能栏[4].被动倍率 *= (0.015 + x) / x

        y = self.技能栏[16].加成倍率(self.武器类型)
        for i in [1, 2, 3, 4]:
            self.技能栏[i].被动倍率 *= (0.01 + y) / y
        
class 圣武枪魂(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)

