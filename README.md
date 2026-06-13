![](teaser.svg)


# Research Figure Checklist

科研绘图不是简单地“把数据画出来”，而是将实验结果转化为论文论证的一部分。

本仓库整理了笔者在论文写作、科研绘图与学生指导中的实践经验，涵盖绘图原则、检查清单、配色方案、代码模板与案例分析，帮助科研新手绘制更清晰、规范、统一且可复现的论文插图，更有效地展示实验结果、方法优势与论文创新点。

示例主要来自计算机科学领域，尤其是机器学习与计算机视觉方向，并以 `LaTeX`、`Matplotlib` 和 `PowerPoint` 为主要工具；相关绘图原则也可为其他学科提供参考。

## 环境配置

`requirements.txt` 只记录 Python 依赖。系统字体、`pdfcrop` 和 LaTeX 工具链属于系统依赖，需要单独安装。

### Python 依赖

#### 为什么需要

案例中的绘图脚本主要依赖 `Matplotlib` 和 `NumPy`。当前 base 环境中用于生成案例图的主要版本是：

```text
matplotlib==3.9.2
numpy==1.26.4
```

#### 怎么安装

```bash
pip install -r requirements.txt
```

### 字体配置

英文论文图建议配置 Arial 或 Helvetica；如果用 PowerPoint 编辑公式，建议额外配置 `Latin Modern Math`。详细安装、检查和 Matplotlib 设置见 [字体配置](fonts/README.md)。

### 用 `pdfcrop` 自动裁剪 Matplotlib 导出的 PDF

#### 为什么需要

Matplotlib 导出的 PDF 有时会带白边。即使在 `savefig` 中使用 `bbox_inches="tight"` 或 tight layout，仍可能残留少量空白。

一种处理方式是在 LaTeX 中手动裁剪：

```latex
\includegraphics[width=\linewidth, trim=10pt 20pt 10pt 20pt, clip]{figures/example.pdf}
```

其中 `trim=left bottom right top`，四个值分别表示从左、下、右、上裁掉多少空白。这适合临时微调单张图，但需要反复试参数，不适合批量生成。

#### 怎么使用

更推荐的做法是在 Matplotlib 脚本导出 PDF 后，直接调用 `pdfcrop` 自动裁剪：

```python
os.system(f"pdfcrop {output_pdf} {output_pdf}")
```

这样可以把裁剪步骤固定在绘图脚本里，减少手工后处理，也更容易保证多张图的裁剪方式一致。裁剪后的 PDF 插入 LaTeX 时通常只需要：

```latex
\includegraphics[width=\linewidth]{figures/example.pdf}
```

#### 怎么安装

`pdfcrop` 通常来自 TeX Live：

```bash
sudo apt update
sudo apt install texlive-extra-utils
```

#### 怎么检查

```bash
which pdfcrop
pdfcrop --version
```

当前环境中 `pdfcrop` 路径为：

```text
/usr/bin/pdfcrop
```
