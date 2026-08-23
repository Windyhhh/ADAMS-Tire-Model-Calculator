# 🚗 ADAMS Tire Model Calculator | ADAMS 轮胎模型计算器

> **Full-stack tire dynamics calculator based on the Pacejka Magic Formula. Compute lateral (Fy), longitudinal (Fx), and aligning moment (Mz) forces with a GUI interface, Excel parameter files, and ADAMS integration.**
>
> 基于 Pacejka 魔术公式的全栈轮胎动力学计算器。通过 GUI 界面、Excel 参数文件和 ADAMS 集成，计算侧向力（Fy）、纵向力（Fx）和回正力矩（Mz）。

---

## 🌟 Features | 核心特性

- **Pacejka Magic Formula** — Industry-standard tire model (BCDE parameters)
- **Three Force Components** — Lateral Fy, Longitudinal Fx, Aligning Moment Mz
- **GUI Interface** — Tkinter-based interactive calculator (103KB)
- **Excel Parameters** — Load/save tire parameters in .xlsx format
- **ADAMS Integration** — Export-compatible format for MSC ADAMS
- **Batch Calculation** — Process multiple tire configurations at once
- **Test Suite** — Quick functional validation script

---

## 📁 Project Structure | 项目结构

```
ADAMS-Tire-Model-Calculator/
├── 01_核心程序/
│   ├── enhanced_bcde_calculator.py    # Core Pacejka calculator (26KB)
│   ├── gui_interface_clean.py          # Tkinter GUI (103KB)
│   └── 启动ADAMS轮胎模型计算器_最终版.bat
├── 02_数据文件/
│   ├── abcdef_BCDE_α-Fy.xlsx          # Lateral force parameters
│   ├── abcdef_BCDE_α-Mz.xlsx          # Aligning moment parameters
│   └── abcdef_BCDE_κ–Fx.xlsx          # Longitudinal force parameters
├── 04_文档说明/
│   ├── ADAMS轮胎模型计算器使用说明.md
│   ├── CSDN精品技术博文_ADAMS轮胎模型计算器.md
│   └── 快速上手指南.md
├── 05_测试验证/
│   └── 快速功能测试.py
├── CSDN_ADAMS轮胎模型计算器爆款博客.md
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start | 快速开始

```bash
pip install -r requirements.txt

# Launch GUI
python 01_核心程序/gui_interface_clean.py

# Or run calculator directly
python 01_核心程序/enhanced_bcde_calculator.py

# Run tests
python 05_测试验证/快速功能测试.py
```

---

## 🔬 Pacejka Magic Formula | Pacejka 魔术公式

The Magic Formula tire model computes forces as:

```
y(x) = D · sin(C · arctan(B·x - E·(B·x - arctan(B·x))))
```

Where:
- **B** = stiffness factor
- **C** = shape factor
- **D** = peak value
- **E** = curvature factor

Applied to lateral force (Fy vs slip angle α), longitudinal force (Fx vs slip ratio κ), and aligning moment (Mz).

---

## 📄 License | 许可证

MIT License.

---

<div align="center">

**Built with 🚗 for vehicle dynamics engineering**

[GitHub](https://github.com/Windyhhh/ADAMS-Tire-Model-Calculator)

</div>
