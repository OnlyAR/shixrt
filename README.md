# 士信融天大赛代码仓库

## 目录结构

```
.
├── data
│   └── problem1
│       ├── 赛题1-时间序列数据预测.pdf
│       ├── datax-x.csv
│       ├── goldx-x.csv
│       ├── outx-x.csv
│       └── resultx-x.csv
├── README.md
├── requirements.txt
├── src
│   ├── fourier
│   │   ├── eval.py
│   │   ├── filter.py
│   │   ├── fourier.py
│   │   ├── __init__.py
│   │   ├── offset.py
│   │   ├── output.py
│   │   ├── window.py
│   │   └── workflow.py
│   ├── generate.py
│   ├── main.py
│   └── utils
│       ├── dataloader.py
│       ├── evaluate.py
│       ├── __init__.py
│       └── plot.py
└── submit
```

- `data` 大赛要求的使用的数据
- `src` 代码目录
  - `fourier` 傅里叶展开相关代码
  - `utils` 工具函数
  - `generate.py` 生成自定义数据
  - `main.py` 预测算法入口

---

$\mathcal{Team}$: 恭喜以上获奖队伍
