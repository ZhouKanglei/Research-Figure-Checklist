# 字体配置

科研图中的字体应优先保证 **论文 PDF 中缩小后仍然清楚、导出后不被替换、与正文和公式风格一致**。

这里讨论的是 **投稿阶段的图件规范**。不同出版物、不同出版社在最终出版时会有自己的字体和排版规范，论文接收后出版商也可能进一步调整版式。投稿时先把图中的字体处理好，主要目的是让审稿人更容易阅读图中的坐标轴、图例、标注和公式，减少因为字体混乱、过小或被替换造成的理解成本。

## 为什么建议使用无衬线字体

科研图中的文字通常很小，尤其是坐标轴数字、图例、子图编号和局部标注。**无衬线字体更适合这些小尺寸信息**，因为字形结构更简洁，缩小到单栏或双栏宽度后仍然比较清楚。

无衬线字体和有衬线字体的主要区别在于笔画末端：

- **无衬线字体** 没有额外的小装饰笔画，例如 Arial、Helvetica、DejaVu Sans。它们在坐标轴、图例和短标签中更干净，适合科研图内部文字。
- **有衬线字体** 在笔画末端有小装饰，例如 Times New Roman。它们常用于论文正文，但放在图内的小字号标注中，容易显得更密、更碎。

因此，本项目的建议是：**图内英文标注优先使用 Arial 或 Helvetica 一类无衬线字体**。这不是说所有出版物最终都会使用这些字体，而是为了在投稿 PDF 中提高审稿阶段的可读性和一致性。

若图中包含公式，或后期需要在 PowerPoint 中编辑数学符号，建议额外配置 Latin Modern Math，使公式风格更接近 LaTeX。

## 字体对比

下面的示例分成两部分：上半部分直接对比 **无衬线字体** 和 **有衬线字体** 在小尺寸柱状图标注、坐标轴和数字中的效果；下半部分对比几种常见字体在标题、普通标注、坐标轴数字和数学表达式中的表现。

**不要只看字体名称，要看系统实际匹配到了哪个字体。** 例如在某些 Linux 环境中，请求 Helvetica 或 Latin Modern Math 时，系统可能会回退到 Arial 或 DejaVu Sans。

![科研图字体对比](fig/font_comparison.png)

生成脚本见 [visualize_font_comparison.py](code/visualize_font_comparison.py)。如果要检查当前机器上的实际字体匹配结果，可以使用：

```bash
fc-match Arial
fc-match Helvetica
fc-match "Latin Modern Math"
```

## Linux 配置 Arial 字体

### 为什么需要

英文论文图常用 Arial 或 Helvetica 这类无衬线字体。Linux 默认可能没有 Arial，容易导致导出图片时字体被替换；如果图中包含中文，则需要显式设置中文字体。

需要注意的是，**字体配置服务于投稿稿件的清晰度**。正式出版时，出版商可能会根据期刊模板、生产流程和网页展示要求进一步调整字体。

### 怎么安装

```bash
sudo apt update
sudo apt install ttf-mscorefonts-installer
sudo fc-cache -f -v
```

### 怎么检查

```bash
fc-match Arial
```

### Matplotlib 推荐写法

Matplotlib 中推荐显式指定字体，并保留 fallback。英文绘图可以使用 Arial / Helvetica，中文绘图则把 `font.sans-serif` 改成系统中可用的中文字体。

```python
import matplotlib.pyplot as plt

plt.rcParams.update(
    {
        "font.family": "Arial",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
)
```

`pdf.fonttype = 42` 和 `ps.fonttype = 42` 可以让导出的矢量文件保留 TrueType 字体，减少后续在 Illustrator、PowerPoint 或投稿系统中出现字体替换问题。

## PowerPoint 配置 Latin Modern Math 字体

### 为什么需要

如果用 PowerPoint 画示意图或后期编辑公式，默认数学字体通常和 LaTeX 论文中的公式风格不一致。可以将公式字体设置为 `Latin Modern Math`，它和 LaTeX 常见的 Computer Modern / Latin Modern 风格更接近。

正文、坐标轴和普通标注仍可使用 Arial 或 Helvetica；数学符号、变量和公式建议使用 `Latin Modern Math`。

### 怎么安装

Linux 下可以安装 Latin Modern 字体包：

```bash
sudo apt update
sudo apt install fonts-lmodern
sudo fc-cache -f -v
```

如果已经安装完整 TeX Live，系统中通常也会包含 Latin Modern 相关字体。

### 怎么检查

```bash
fc-match "Latin Modern Math"
```

### 常见问题

PowerPoint 中插入公式后，可以选中公式内容，将数学字体改为 `Latin Modern Math`。如果字体列表中找不到该字体，通常是系统字体没有安装或 PowerPoint 尚未重新加载字体缓存。
