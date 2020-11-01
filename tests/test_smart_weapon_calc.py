import pytest

from PublicReference.calc_core import *


class TestCalcCore:
    def test_get_specify_counts_weapon(self):
        有效智慧产物 = [['衣服1', '衣服2', '衣服3'], ['头肩1', '头肩2', '头肩3'], ['下装1', '下装2', '下装3']]
        挑选数量 = 2
        已挑选装备 = []
        装备组合 = 获取指定数量的智慧产物组合(有效智慧产物, 挑选数量, 已挑选装备)
        print(装备组合)
        assert len(装备组合) == 54  # A(3,2)*3*3

    def test_get_specify_counts_weapon(self):
        有效智慧产物 = [['衣服1', '衣服2', '衣服3'], ['头肩1', '头肩2', '头肩3'], ['下装1', '下装2', '下装3']]
        挑选数量 = 2
        已挑选装备 = []
        装备组合 = 获取指定数量的智慧产物组合_V2(有效智慧产物, 挑选数量, 已挑选装备, 0)
        print(装备组合)
        assert len(装备组合) == 27  # C(3,2)*3*3
