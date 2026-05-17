![](teaser.svg)


# Research Figure Checklist

科研绘图不是简单地“把数据画出来”，而是将实验结果转化为论文论证的一部分。

本仓库整理了笔者在论文写作、科研绘图与学生指导中的实践经验，涵盖绘图原则、检查清单、配色方案、代码模板与案例分析，帮助科研新手绘制更清晰、规范、统一且可复现的论文插图，更有效地展示实验结果、方法优势与论文创新点。

示例主要来自计算机科学领域，尤其是机器学习与计算机视觉方向，并以 `LaTeX`、`Matplotlib` 和 `PowerPoint` 为主要工具；相关绘图原则也可为其他学科提供参考。

## 环境配置

`requirements.txt` 只记录 Python 依赖。`pdfcrop`、系统字体和 LaTeX 工具链属于系统依赖，需要单独安装。

### Python 依赖

当前 base 环境中用于生成案例图的主要版本是：

```text
matplotlib==3.9.2
numpy==1.26.4
```

安装方式：

```bash
pip install -r requirements.txt
```

如果在 Linux 或受限环境中看到 Matplotlib cache 目录不可写的提示，可以设置一个可写缓存目录：

```bash
export MPLCONFIGDIR=/tmp/matplotlib
```

### `pdfcrop`

部分绘图脚本会在导出 PDF 后调用 `pdfcrop` 裁剪空白边距。`pdfcrop` 通常来自 TeX Live：

```bash
sudo apt update
sudo apt install texlive-extra-utils
```

检查是否安装成功：

```bash
which pdfcrop
pdfcrop --version
```

当前环境中 `pdfcrop` 路径为：

```text
/usr/bin/pdfcrop
```

如果没有安装 `pdfcrop`，绘图脚本仍可先导出 PDF，但自动裁剪步骤会失败；可以手动注释掉脚本中的 `pdfcrop` 调用。

### Linux 配置 Arial 字体

论文图常用 Arial 或 Helvetica。Linux 默认可能没有 Arial，需要安装 Microsoft core fonts：

```bash
sudo apt update
sudo apt install ttf-mscorefonts-installer
sudo fc-cache -f -v
```

检查 Arial 是否可用：

```bash
fc-match Arial
```

Matplotlib 中推荐显式指定字体，并保留 fallback：

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

其中 `pdf.fonttype = 42` 和 `ps.fonttype = 42` 可以让导出的矢量文件保留 TrueType 字体，减少后续在 Illustrator、PowerPoint 或投稿系统中出现字体替换问题。
