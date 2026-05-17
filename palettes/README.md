# 科研图配色方案

本目录整理适合论文图、汇报图和 multi-panel figure 的期刊风格配色。这里的 Nature、Science、Cell 指的是对应期刊常见视觉风格的 palette，不是投稿强制标准。实际使用时应优先保证可读性、色盲友好和灰度打印可区分。

## 使用原则

- 同一篇论文中尽量固定一套主 palette。
- 颜色要承担语义，而不是只做装饰。
- 类别数少时优先使用高区分度颜色；类别数多时降低饱和度。
- 柱状图、面积图、散点背景点可以使用半透明色。
- 文字、坐标轴和误差线不要使用过浅颜色。

## Nature 风格

Nature 风格适合大多数机器学习、生物医学和综合科研图。特点是蓝、青、绿、红区分明显，适合多方法对比和多 panel figure。

### Hex

```python
NATURE_HEX = [
    "#E64B35",  # vermilion red
    "#4DBBD5",  # cyan blue
    "#00A087",  # green
    "#3C5488",  # dark blue
    "#F39B7F",  # salmon
    "#8491B4",  # muted purple blue
    "#91D1C2",  # mint
    "#DC0000",  # strong red
    "#7E6148",  # brown
    "#B09C85",  # taupe
]
```

### RGB

```python
NATURE_RGB = [
    (230, 75, 53),
    (77, 187, 213),
    (0, 160, 135),
    (60, 84, 136),
    (243, 155, 127),
    (132, 145, 180),
    (145, 209, 194),
    (220, 0, 0),
    (126, 97, 72),
    (176, 156, 133),
]
```

### Matplotlib 半透明写法

```python
from matplotlib.colors import to_rgba

NATURE_RGBA_032 = [to_rgba(color, alpha=0.32) for color in NATURE_HEX]
NATURE_RGBA_060 = [to_rgba(color, alpha=0.60) for color in NATURE_HEX]
```

常用语义映射：

```python
NATURE_SEMANTIC = {
    "risk": to_rgba("#E64B35", alpha=0.32),
    "baseline": to_rgba("#3C5488", alpha=0.32),
    "method": to_rgba("#4DBBD5", alpha=0.32),
    "improvement": to_rgba("#00A087", alpha=0.45),
    "background": to_rgba("#D0D0D0", alpha=0.32),
    "text": "#1A1A1A",
    "grid": "#E6E6E6",
}
```

## Science 风格

Science 风格适合对比强、结论明确的结果图。特点是深蓝、正红、绿色和紫色对比强，适合方法比较、分类结果和关键实验组。

### Hex

```python
SCIENCE_HEX = [
    "#3B4992",  # deep blue
    "#EE0000",  # red
    "#008B45",  # green
    "#631879",  # purple
    "#008280",  # teal
    "#BB0021",  # dark red
    "#5F559B",  # violet blue
    "#A20056",  # magenta
    "#808180",  # gray
    "#1B1919",  # near black
]
```

### RGB

```python
SCIENCE_RGB = [
    (59, 73, 146),
    (238, 0, 0),
    (0, 139, 69),
    (99, 24, 121),
    (0, 130, 128),
    (187, 0, 33),
    (95, 85, 155),
    (162, 0, 86),
    (128, 129, 128),
    (27, 25, 25),
]
```

### Matplotlib 半透明写法

```python
from matplotlib.colors import to_rgba

SCIENCE_RGBA_032 = [to_rgba(color, alpha=0.32) for color in SCIENCE_HEX]
SCIENCE_RGBA_060 = [to_rgba(color, alpha=0.60) for color in SCIENCE_HEX]
```

常用语义映射：

```python
SCIENCE_SEMANTIC = {
    "control": to_rgba("#3B4992", alpha=0.32),
    "treatment": to_rgba("#EE0000", alpha=0.32),
    "secondary": to_rgba("#008B45", alpha=0.32),
    "ablation": to_rgba("#631879", alpha=0.32),
    "background": to_rgba("#808180", alpha=0.24),
    "text": "#1B1919",
    "grid": "#E6E6E6",
}
```

## Cell 风格

Cell 风格适合机制图、组学图和多类别实验图。这里采用 Cell Press 风格的高区分度色组：蓝、橙、绿、红、紫、棕、粉、灰组合，适合同时展示多个类别或条件。

### Hex

```python
CELL_HEX = [
    "#1F77B4",  # blue
    "#FF7F0E",  # orange
    "#2CA02C",  # green
    "#D62728",  # red
    "#9467BD",  # purple
    "#8C564B",  # brown
    "#E377C2",  # pink
    "#7F7F7F",  # gray
    "#BCBD22",  # olive
    "#17BECF",  # cyan
]
```

### RGB

```python
CELL_RGB = [
    (31, 119, 180),
    (255, 127, 14),
    (44, 160, 44),
    (214, 39, 40),
    (148, 103, 189),
    (140, 86, 75),
    (227, 119, 194),
    (127, 127, 127),
    (188, 189, 34),
    (23, 190, 207),
]
```

### Matplotlib 半透明写法

```python
from matplotlib.colors import to_rgba

CELL_RGBA_032 = [to_rgba(color, alpha=0.32) for color in CELL_HEX]
CELL_RGBA_060 = [to_rgba(color, alpha=0.60) for color in CELL_HEX]
```

常用语义映射：

```python
CELL_SEMANTIC = {
    "group_a": to_rgba("#1F77B4", alpha=0.32),
    "group_b": to_rgba("#FF7F0E", alpha=0.32),
    "group_c": to_rgba("#2CA02C", alpha=0.32),
    "negative": to_rgba("#7F7F7F", alpha=0.24),
    "positive": to_rgba("#D62728", alpha=0.32),
    "text": "#1A1A1A",
    "grid": "#E6E6E6",
}
```

## 快速复制模板

如果只需要在一张图里使用半透明期刊风格颜色，可以直接复制下面这段：

```python
from matplotlib.colors import to_rgba

NATURE = {
    "red": "#E64B35",
    "cyan": "#4DBBD5",
    "green": "#00A087",
    "blue": "#3C5488",
    "gray": "#D0D0D0",
}

COLORS = {
    "main": to_rgba(NATURE["blue"], alpha=0.32),
    "compare": to_rgba(NATURE["cyan"], alpha=0.32),
    "gain": to_rgba(NATURE["red"], alpha=0.32),
    "highlight": to_rgba(NATURE["green"], alpha=0.60),
    "background": to_rgba(NATURE["gray"], alpha=0.24),
    "text": "#1A1A1A",
    "grid": "#E6E6E6",
}
```

## 透明度建议

| 场景 | 推荐 alpha |
| --- | --- |
| 主柱状图填充 | `0.32` - `0.45` |
| 散点主类别 | `0.55` - `0.75` |
| 背景散点 | `0.18` - `0.32` |
| inset 或辅助区域 | `0.24` - `0.45` |
| 高亮边框、文字、误差线 | 不建议透明 |

注意：透明色适合降低视觉压力，但不适合用于细线、文字和误差线。导出 PDF 时也要检查透明叠加是否符合期刊投稿系统要求。
