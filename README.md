<div align="center">

# ADAMS 轮胎模型计算器 | ADAMS-Tire-Model-Calculator

### Pacejka magic-formula tire mechanics calculator.

Tire six-force computation, real-time charts, ADAMS TIR file generation and parameter-response analysis.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pacejka](https://img.shields.io/badge/Pacejka-Magic%20Formula-2EA44F)](https://www.sciencedirect.com/topics/engineering/magic-formula)

</div>

---

**ADAMS-Tire-Model-Calculator** is a professional **tire-mechanics calculator** built on the **Pacejka magic formula**. It computes the tire six forces, plots results in real time, generates **ADAMS TIR** files and supports parameter-response analysis — a reliable helper for ADAMS multi-body dynamics simulation.

> [!NOTE]
> 中文项目：基于 Pacejka 魔术公式的 ADAMS 轮胎模型计算器——六分力计算、实时图表、TIR 文件生成、参数响应分析。

---

## Features

- **Six-force computation** — Pacejka magic-formula tire model.
- **ADAMS TIR generation** — export tire files for simulation (100% success).
- **Real-time charts** — visualize force characteristics.
- **High precision** — 20-decimal computation, error ≤ 0.1%.
- **Batch / parallel** — 1000+ operating-condition cases.

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/ADAMS-Tire-Model-Calculator.git
cd ADAMS-Tire-Model-Calculator

pip install -r requirements.txt

python src/main.py          # open the calculator UI
```

---

## Project Structure

```
ADAMS-Tire-Model-Calculator/
├── src/                    # Pacejka model + computation + charts
├── ui/                     # Chinese-friendly interface
├── output/                 # generated TIR files & plots
└── docs/                   # usage, blog
```

---

## License

MIT — free to use, modify and distribute.
