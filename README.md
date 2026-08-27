<div align="center">

# 🛞 ADAMS-Tire-Model-Calculator

### Pacejka magic-formula tire model calculator.

Compute Fy / Fx / Mz tire forces with the Pacejka magic formula — GUI, Excel parameters, ADAMS integration.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-2EA44F)](https://docs.python.org/3/library/tkinter.html)

</div>

---

**ADAMS-Tire-Model-Calculator** computes tire forces (Fy, Fx, Mz) using the **Pacejka magic formula**, with a desktop GUI, Excel-driven parameters, and ADAMS integration for vehicle dynamics workflows.

> [!NOTE]
> 中文项目：基于 Pacejka 魔术公式的轮胎模型计算器——Fy/Fx/Mz 力，GUI，Excel 参数，ADAMS 集成。

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/ADAMS-Tire-Model-Calculator.git
cd ADAMS-Tire-Model-Calculator

pip install -r requirements.txt

# Launch the GUI
python "01_核心程序/gui_interface_clean.py"

# Headless calculator
python "01_核心程序/enhanced_bcde_calculator.py"
```

There is also a Windows `.bat` launcher in `01_核心程序/`.

---

## Features

- **Magic formula** — Pacejka Fy / Fx / Mz force calculation.
- **GUI** — interactive desktop interface.
- **Excel parameters** — load/save coefficient tables (`.xlsx` in `02_数据文件`).
- **ADAMS integration** — export ready for ADAMS vehicle dynamics.

---

## Project Structure

```
ADAMS-Tire-Model-Calculator/
├── 01_核心程序/            # gui_interface_clean.py, enhanced_bcde_calculator.py, .bat launcher
├── 02_数据文件/            # Pacejka coefficient Excel files
├── 04_文档说明/            # user guide, quick start
├── 05_测试验证/            # functional tests
└── requirements.txt
```

---

## License

MIT — free to use, modify and distribute.
