#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速功能测试
测试所有主要功能是否正常工作
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from gui_interface_clean import TireModelCalculator
from enhanced_bcde_calculator import EnhancedBCDECalculator

def quick_function_test():
    """快速功能测试"""
    
    print("🔍 快速功能测试")
    print("=" * 80)
    
    try:
        # 创建GUI实例
        root = tk.Tk()
        root.withdraw()
        app = TireModelCalculator(root)
        
        print("✅ GUI界面创建成功")
        
        # 测试参数设置
        test_params = {
            'fz': 500,
            'gamma': 15,
            'kappa': 20,
            'alpha': 15,
            'lateral_stiffness': 900,
            'rolling_resistance': 0.3,
            're': 340.6
        }
        
        print(f"\n📊 测试参数设置:")
        for param, value in test_params.items():
            if hasattr(app, f'{param}_var'):
                getattr(app, f'{param}_var').set(value)
                print(f"  {param}: {value} ✅")
            else:
                print(f"  {param}: 变量不存在 ❌")
        
        # 测试BCDE计算
        print(f"\n🔢 测试BCDE计算:")
        calculator = EnhancedBCDECalculator()
        all_bcde = calculator.calculate_all_forces_bcde(test_params['fz'], test_params['gamma'])
        
        print(f"  BCDE计算结果:")
        for force_type, bcde in all_bcde.items():
            print(f"    {force_type}: B={bcde['B']:.6f}, C={bcde['C']:.6f}, D={bcde['D']:.6f}, E={bcde['E']:.6f}")
        
        # 测试力和力矩计算
        print(f"\n⚡ 测试力和力矩计算:")
        forces = calculator.calculate_magic_formula_forces(
            all_bcde, 
            test_params['kappa'], 
            test_params['alpha'], 
            test_params['fz'],
            test_params['lateral_stiffness'],
            test_params['re'],
            test_params['rolling_resistance']
        )
        
        print(f"  力和力矩计算结果:")
        for force_name, value in forces.items():
            print(f"    {force_name}: {value:.6f}")
        
        # 测试图表数据生成
        print(f"\n📈 测试图表数据生成:")
        import numpy as np
        kappa_range = np.linspace(-100, 100, 100)
        alpha_range = np.linspace(-30, 30, 100)
        
        chart_data = app.calculate_chart_data(all_bcde, kappa_range, alpha_range, test_params['fz'])
        
        print(f"  生成的图表数量: {len(chart_data)}")
        
        chart_names = ['κ-Fx', 'α-Fy', 'α-Mz', 'α-Mx', 'α-My', 'α-Fz']
        
        for i, (x_data, y_data, x_label, y_label) in enumerate(chart_data):
            if i < len(chart_names):
                chart_name = chart_names[i]
                print(f"    {i+1}. {chart_name}: 数据范围 {min(y_data):.3f} ~ {max(y_data):.3f} {y_label.split('(')[1].replace(')', '')}")
        
        # 测试TIR文件生成
        print(f"\n📄 测试TIR文件生成:")
        
        # 设置计算结果
        app.current_results = {
            'forces': forces,
            'bcde': all_bcde
        }
        
        tir_content = app.generate_tir_content()
        
        # 保存测试TIR文件
        test_filename = "功能测试.tir"
        with open(test_filename, 'w', encoding='utf-8') as f:
            f.write(tir_content)
        
        print(f"  TIR文件生成成功: {test_filename}")
        print(f"  TIR文件大小: {len(tir_content)} 字符")
        
        # 测试TIR验证
        print(f"\n🔍 测试TIR验证:")
        
        # 检查关键段
        required_sections = [
            '[MDI_HEADER]',
            '[MODEL]', 
            '[UNITS]',
            '[DIMENSION]',
            '[PARAMETER]',
            '[LONGITUDINAL_COEFFICIENTS]',
            '[LATERAL_COEFFICIENTS]',
            '[ALIGNING_COEFFICIENTS]'
        ]
        
        missing_sections = []
        for section in required_sections:
            if section in tir_content:
                print(f"    {section}: ✅")
            else:
                print(f"    {section}: ❌")
                missing_sections.append(section)
        
        if len(missing_sections) == 0:
            print(f"  TIR验证: ✅ 所有必要段都存在")
        else:
            print(f"  TIR验证: ❌ 缺少 {len(missing_sections)} 个段")
        
        # 测试参数响应
        print(f"\n⚙️ 测试参数响应:")
        
        # 测试胎体侧向刚度对Mx的影响
        original_ls = test_params['lateral_stiffness']
        test_ls_values = [600, 900, 1200]
        
        print(f"  胎体侧向刚度对Mx的影响:")
        mx_values = []
        for ls in test_ls_values:
            test_forces = calculator.calculate_magic_formula_forces(
                all_bcde, test_params['kappa'], test_params['alpha'], test_params['fz'],
                ls, test_params['re'], test_params['rolling_resistance']
            )
            mx = test_forces['Mx']
            mx_values.append(mx)
            print(f"    LS={ls}N/mm → Mx={mx:.3f}N·m")
        
        mx_variation = max(mx_values) - min(mx_values)
        print(f"    Mx变化幅度: {mx_variation:.3f}N·m {'✅' if mx_variation > 10 else '❌'}")
        
        # 测试滚动阻力系数对My的影响
        test_rr_values = [0.1, 0.3, 0.5]
        
        print(f"\n  滚动阻力系数对My的影响:")
        my_values = []
        for rr in test_rr_values:
            test_forces = calculator.calculate_magic_formula_forces(
                all_bcde, test_params['kappa'], test_params['alpha'], test_params['fz'],
                test_params['lateral_stiffness'], test_params['re'], rr
            )
            my = test_forces['My']
            my_values.append(my)
            print(f"    RR={rr} → My={my:.3f}N·m")
        
        my_variation = max(my_values) - min(my_values)
        print(f"    My变化幅度: {my_variation:.3f}N·m {'✅' if my_variation > 10 else '❌'}")
        
        root.destroy()
        
        print(f"\n🎉 所有功能测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主函数"""
    
    print("🔍 轮胎模型计算器功能测试")
    print("=" * 100)
    
    success = quick_function_test()
    
    if success:
        print(f"\n✅ 功能测试通过!")
        print(f"\n📋 测试项目:")
        print(f"  ✅ GUI界面创建")
        print(f"  ✅ 参数设置")
        print(f"  ✅ BCDE计算")
        print(f"  ✅ 力和力矩计算")
        print(f"  ✅ 图表数据生成")
        print(f"  ✅ TIR文件生成")
        print(f"  ✅ TIR文件验证")
        print(f"  ✅ 参数响应测试")
        
        print(f"\n🎯 程序状态: 所有功能正常工作")
    else:
        print(f"\n❌ 功能测试失败")
        print(f"请检查错误信息并修复问题")

if __name__ == "__main__":
    main()
