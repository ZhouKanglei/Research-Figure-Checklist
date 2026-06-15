# 什么是好的科研图？

科研图不是简单地“把数据画出来”，而是把实验结果、方法设计和论文观点组织成读者可以快速理解的视觉证据。本文中的“科研图”泛指论文中的各类插图，包括实验数据图、方法框架图、流程图、模块示意图、可视化案例图和对比展示图等。

!!! note "本节导学"

    读完这一节，你应该能够完成几件事。

    - 区分常见科研图类型，明确不同图的主要任务；
    - 判断一张图是否真正服务于论文观点；
    - 用“结论、证据、表达、规范”四个维度检查自己的图；
    - 避免把“好看”误认为“好图”。

## 1. 科研图的本质

科研图的核心任务是**降低读者理解论文的成本**。正文用语言展开逻辑，图则把这条逻辑压缩成可见结构：读者应该能更快看到问题是什么、证据在哪里、结论如何成立。

```mermaid
flowchart LR
    A[论文观点] --> B[图的任务]
    B --> C[选择证据]
    B --> D[组织结构]
    B --> E[控制视觉表达]
    C --> F[读者理解]
    D --> F
    E --> F
    F --> G[支撑论文论证]
```

因此，科研图不是论文之外的装饰，而是论文论证的一部分。画图前先回答三个问题，可以避免后续只在配色、排版和美化上反复调整。

- **这张图想说明什么？**
- **图中的证据是否支持这个判断？**
- **读者能否快速读出主要信息？**

## 2. 科研图的常见类型

不同类型的科研图承担不同任务。画图前先判断图的类型，能避免把“示意图”“结果图”和“证据图”混在一起：示意图负责解释关系，结果图负责呈现实验证据，案例图负责补充直观现象。类型判断清楚以后，图中该保留什么、强调什么、删掉什么才有依据。

### 2.1 方法框架图

方法框架图用于展示模型结构、训练流程、模块关系和输入输出逻辑。它的核心目标不是证明方法更强，而是让读者快速理解方法是如何工作的。

<figure markdown>
  ![MAGR++ 方法框架图](fig/magrpp-framework.png)

  <figcaption>图 1. <a href="https://arxiv.org/abs/2510.06842">MAGR++ 方法框架图</a>。展示模型模块、信息流和输入输出关系。</figcaption>
</figure>

<figure markdown>
  ![PACE 方法框架图](fig/pace-framework.png)

  <figcaption>图 2. <a href="https://openreview.net/pdf?id=k5PgSlNc4E">PACE 方法框架图</a>。通过模块结构说明方法的整体流程。</figcaption>
</figure>

<figure markdown>
  ![FlyPrompt 方法框架图](fig/flyprompt-framework.png)

  <figcaption>图 3. <a href="https://openreview.net/pdf?id=8pi1rP71qv">FlyPrompt 方法框架图</a>。展示输入、提示机制和预测模块之间的关系。</figcaption>
</figure>

这类图最容易出问题的地方是信息流不清：模块太多、箭头混乱、主流程和辅助模块没有区分，或者颜色只起装饰作用而没有语义。

### 2.2 流程图和示意图

流程图和示意图通常用于解释任务设定、数据处理流程、问题动机或核心思想。它们不一定展示真实实验数据，但必须把概念关系讲清楚，让读者知道论文面对的场景、约束和关键差异。

<figure markdown>
  ![质量攻击方法示意图](fig/quality-attack-teaser.png)

  <figcaption>图 4. <a href="https://arxiv.org/pdf/2606.13022">质量攻击方法示意图</a>。通过流程对比说明新方法与已有攻击方法的差异。</figcaption>
</figure>

<figure markdown>
  ![MAGR++ 研究动机示意图](fig/magrpp-teaser.png)

  <figcaption>图 5. <a href="https://arxiv.org/abs/2510.06842">MAGR++ 研究动机示意图</a>。通过真实场景和任务差异引出方法需要解决的问题。</figcaption>
</figure>

<figure markdown>
  ![PACE 研究动机示意图](fig/pace-teaser.png)

  <figcaption>图 6. <a href="https://openreview.net/pdf?id=k5PgSlNc4E">PACE 研究动机示意图</a>。用应用场景和限制条件说明任务设定。</figcaption>
</figure>

<figure markdown>
  ![CVQA 应用场景示意图](fig/cvqa-teaser.png)

  <figcaption>图 7. <a href="https://arxiv.org/pdf/2502.19644E">CVQA 应用场景示意图。</a>展示虚拟现实视频质量评价中的用户场景、内容变化和设备约束。</figcaption>
</figure>

这类图常见的问题是概念过多、层级不清、图中文字太长，或者示意元素和正文表述不一致。读者如果需要反复对照正文才能理解图，说明图还没有完成解释任务。

### 2.3 实验结果图

实验结果图用于展示定量结果，例如柱状图、折线图、热力图、散点图、箱线图等。它的核心目标是让读者看出实验现象是否稳定、主要对比是否成立、方法优势是否有足够证据支撑。

<figure markdown>
  ![FlyPrompt 实验结果图](fig/flyprompt-res.png)

  <figcaption>图 8. <a href="https://openreview.net/pdf?id=8pi1rP71qv">FlyPrompt 实验结果图</a>。用于展示不同方法或设置之间的定量差异。</figcaption>
</figure>

<figure markdown>
  ![PACE 实验结果图](fig/pace-res.png)

  <figcaption>图 9. <a href="https://openreview.net/pdf?id=k5PgSlNc4E">PACE 实验结果图</a>。通过结果对比突出方法表现。</figcaption>
</figure>

这类图常见的问题是只展示数字、不突出结论、坐标轴范围不合理、配色混乱。结果图不应该只是表格的图形版本，而应该把最重要的比较关系组织出来。

### 2.4 消融分析图

消融分析图用于说明不同模块、损失函数、超参数或设计选择的贡献。它需要清楚回答“哪个设计有效，为什么有效”，并且让读者看出变量控制是否公平。

<figure markdown>
  ![PACE 消融对比图](fig/pace-ablation.png)

  <figcaption>图 10. <a href="https://openreview.net/pdf?id=k5PgSlNc4E">PACE 消融对比图</a>。用于说明不同模块或设置对结果的贡献。</figcaption>
</figure>

<figure markdown>
  ![BriMA 消融对比图](fig/brima-ablation.png)

  <figcaption>图 11. <a href="https://arxiv.org/pdf/2602.19170">BriMA 消融对比图</a>。直观展示检索增强策略相对于传统策略的有效性。</figcaption>
</figure>

这类图常见的问题是缺少基线方法、变量控制不清、不同设置之间不可比较。消融图如果没有明确控制变量，就很难支撑“某个设计确实有贡献”的判断。

### 2.5 可视化案例图

可视化案例图用于展示预测结果、重建结果、注意力图、失败案例或定性比较。它的价值在于把定量指标背后的行为差异展示出来，但不能用少数“最好看”的样例替代系统评估。

<figure markdown>
  ![MAGR++ 案例分析图](fig/magrpp-case.png)

  <figcaption>图 12. <a href="https://arxiv.org/pdf/2510.06842">MAGR++ 案例分析图</a>。通过具体样例展示方法输出或错误模式。</figcaption>
</figure>

<figure markdown>
  ![CaRF 案例分析图](fig/carf-case.png)

  <figcaption>图 13. <a href="https://arxiv.org/pdf/2511.03992">CaRF 案例分析图</a>。用于呈现定性结果和样例级差异。</figcaption>
</figure>

<figure markdown>
  ![GeoCGA 案例分析图](fig/GeoCGA-case.png)

  <figcaption>图 14. <a href="https://arxiv.org/pdf/2511.03992">GeoCGA 案例分析图</a>。用于展示可视化案例和局部现象。</figcaption>
</figure>

这类图常见的问题是案例选择不公平、没有说明成功或失败原因、样例过少或排版过挤。好的案例图应该帮助读者理解方法的行为，而不是只展示几个视觉上讨喜的输出。

## 3. 好图的判断标准

主观感觉“好看”不是充分标准。科研图首先要服务于论文论证，其次才是视觉风格。为了让判断更具体，本节以 Nature Research Figure Guide 的图件规范[^nature-guide]为参照，把“好图”拆成几个可以直接检查的维度。

Nature 的规范并不是只在投稿前才有用。它真正提供的是一套面向读者的判断方式：图是否帮助读者快速理解结论，是否保留了数据和图像细节，是否在缩放、印刷、在线阅读和编辑过程中仍然可靠。因此，即使目标期刊不是 Nature，这些标准也可以作为科研绘图的通用底线。

!!! note "可迁移性"

    此处多以 Nature 为例，是为了让标准更具体，不是要求所有论文都使用同一套尺寸。不同期刊、会议论文、学位论文、技术报告和书籍的纸张大小、版心宽度、单栏/双栏设置、图注位置和在线展示方式都可能不同。实际投稿或排版时，应优先查看目标出版物的 author guidelines，并根据最终页面尺寸调整图宽、字号、线宽和面板密度。

!!! note "示例图来源说明"

    本节中的规范说明参考 Nature Research Figure Guide，但页面内的 Avoid/Recommended 图片已改为本站自绘示意图，用于教学说明和复现规范原则。引用 Nature 时应链接其原页面作为规范来源，避免直接复用原图。

### 3.1 结论明确

一张图应该服务于一个清晰的论文观点。读者看完后应该知道这张图想说明什么，而不是只看到一组元素、颜色或数值。图中的每个子图、标注、颜色和箭头，都应该把读者推向同一个结论。

Nature 科研图指南[^nature-guide]把图视为论文内容的重要组成部分，并强调编辑良好的图可以提高理解效率。这个观点可以转化为一个实用的检查问题：**这张图支撑的是论文中的哪一个结论？** 如果回答不出来，通常说明图还停留在“展示材料”的层面，而没有完成“组织证据”的任务。

不同类型的科研图适合支撑不同层次的结论。画图前可以先用下表反推：**这张图最应该让读者相信哪一句话？** 如果回答不出来，通常需要先重新明确图的任务，再考虑图形形式。

| 科研图类型 | 最应该回答的问题 | 结论重点 | 常见偏差 |
| --- | --- | --- | --- |
| 方法框架图 | 方法如何工作？ | **模块关系、信息流、关键设计** | 试图证明性能优势 |
| 流程图和示意图 | 问题、流程或任务设定是什么？ | **任务设定、输入输出、约束条件** | 画得像结果图，但没有证据 |
| 实验结果图 | 方法是否更好，趋势是否稳定？ | **性能差异、趋势、统计证据** | 只堆数字，不突出主对比 |
| 消融分析图 | 哪个设计真正有贡献？ | **模块有效性、变量控制、设计必要性** | 把消融画成另一张总结果图 |
| 可视化案例图 | 具体样例中发生了什么？ | **行为差异、局部现象、失败模式** | 用少数好看样例替代定量评估 |

### 3.2 信息清晰

图中的主趋势、关键对比和主要结论应该容易识别。不要让读者在过多颜色、文字、箭头和图例中寻找重点。清晰不是简单地减少信息，而是建立信息层级：先看到主结论，再看到支持它的局部证据。

Nature 图件规格[^nature-preparing]给了很多具体例子：数据图需要坐标轴、刻度和单位；文字不能重叠；标签不能压在复杂背景上；不必要的网格线、阴影、图标和装饰会干扰阅读。这些要求看似细碎，本质上都是为了减少读者的搜索成本。实际检查时，可以先看标题、坐标轴、图例、标注和高亮元素是否共同指向同一个重点。

<div class="example-pair" markdown>
<figure markdown>
  ![缺少刻度和轴标签的错误坐标轴示例](fig/nature-preparing-figures/axis-avoid-missing-ticks.png)

  <figcaption><strong>避免：</strong>缺少刻度、轴标签和单位，读者无法判断数值含义。</figcaption>
</figure>

<figure markdown>
  ![包含刻度和轴标签的推荐坐标轴示例](fig/nature-preparing-figures/axis-recommended-labels.png)

  <figcaption><strong>推荐：</strong>保留坐标轴、刻度和单位，让数据含义可以被直接读取。</figcaption>
</figure>
</div>

<div class="example-pair" markdown>
<figure markdown>
  ![标注密集且互相重叠的错误示例](fig/nature-preparing-figures/labels-avoid-overlap.png)

  <figcaption><strong>避免：</strong>小字、密集标注和互相重叠的标签会遮挡数据。</figcaption>
</figure>

<figure markdown>
  ![重新排列标签后更清晰的推荐示例](fig/nature-preparing-figures/labels-recommended-rearranged.png)

  <figcaption><strong>推荐：</strong>减少不必要标签，并重新排布标注位置，先保证读者能读懂。</figcaption>
</figure>
</div>

清晰还包括可访问性。Nature 图件排版说明[^nature-export]强调，颜色组合要能被色觉差异读者区分，文字与背景之间要有足够对比，不必要的装饰图标应改为明确文字标签。换句话说，清晰度不仅取决于图上“有没有信息”，也取决于读者是否能无歧义地读出信息。

<div class="example-pair" markdown>
<figure markdown>
  ![红绿配色在色盲模拟下难以区分的示例](fig/nature-preparing-figures/colourblind-avoid-red-green.png)

  <figcaption><strong>避免：</strong>只依赖容易混淆的颜色组合区分类别。</figcaption>
</figure>

<figure markdown>
  ![色盲模拟下仍有足够对比度的推荐配色示例](fig/nature-preparing-figures/colourblind-recommended-contrast.png)

  <figcaption><strong>推荐：</strong>使用在色觉差异下仍能区分的颜色和对比关系。</figcaption>
</figure>
</div>

<div class="example-pair" markdown>
<figure markdown>
  ![用彩色文字说明图例的错误示例](fig/nature-preparing-figures-extra/legend-avoid-coloured-text.png)

  <figcaption><strong>避免：</strong>用彩色文字充当图例，颜色和文本含义绑定不够稳妥。</figcaption>
</figure>

<figure markdown>
  ![用色块和黑色文字说明图例的推荐示例](fig/nature-preparing-figures-extra/legend-recommended-colour-boxes.png)

  <figcaption><strong>推荐：</strong>用色块、线型或引线对应类别，文字保持黑色并清晰可读。</figcaption>
</figure>
</div>

<div class="example-pair" markdown>
<figure markdown>
  ![用图案填充分隔饼图扇区的错误示例](fig/nature-preparing-figures-extra/patterns-avoid-pie.png)

  <figcaption><strong>避免：</strong>用密集图案区分类别，缩小后容易形成视觉噪声。</figcaption>
</figure>

<figure markdown>
  ![用实色区分饼图扇区的推荐示例](fig/nature-preparing-figures-extra/patterns-recommended-solid.png)

  <figcaption><strong>推荐：</strong>用稳定、简洁的实色区分类别，并保证相邻区域可区分。</figcaption>
</figure>
</div>

<div class="example-pair" markdown>
<figure markdown>
  ![低对比度彩色文字示例](fig/nature-preparing-figures/contrast-avoid-low.png)

  <figcaption><strong>避免：</strong>彩色文字与背景对比不足，读者需要额外辨认。</figcaption>
</figure>

<figure markdown>
  ![高对比度文字示例](fig/nature-preparing-figures/contrast-recommended-high.png)

  <figcaption><strong>推荐：</strong>使用黑色或白色等高对比文字，让标签在不同背景上都清楚。</figcaption>
</figure>
</div>

<div class="example-pair" markdown>
<figure markdown>
  ![用装饰性图标替代文字标签的错误示例](fig/nature-preparing-figures/icons-avoid-decorative.png)

  <figcaption><strong>避免：</strong>用容易误读的图标代替文字标签，图标含义可能不唯一。</figcaption>
</figure>

<figure markdown>
  ![用明确文字标签替代装饰图标的推荐示例](fig/nature-preparing-figures/icons-recommended-text-labels.png)

  <figcaption><strong>推荐：</strong>用直接文字标签说明类别，只保留真正帮助理解的视觉元素。</figcaption>
</figure>
</div>

<div class="example-pair" markdown>
<figure markdown>
  ![蛋白图中使用浅色文字标签的错误示例](fig/nature-preparing-figures-extra/protein-avoid-coloured-labels.png)

  <figcaption><strong>避免：</strong>把彩色文字直接压在复杂结构上，标签和背景容易混在一起。</figcaption>
</figure>

<figure markdown>
  ![蛋白图中用黑色文字和引线标注的推荐示例](fig/nature-preparing-figures-extra/protein-recommended-keylines.png)

  <figcaption><strong>推荐：</strong>用黑色文字配合引线标注，让标签与结构关系清楚。</figcaption>
</figure>
</div>

### 3.3 视觉统一

同一篇论文中的字体、字号、线宽、颜色、图例、子图编号和排版风格应该尽量一致。统一不是为了形式整齐，而是为了降低读者在不同图之间切换的认知成本。读者不应该每看一张图都重新学习一套视觉规则。

期刊规范会把统一性写得很具体。Nature 终稿说明[^nature-final]建议图中文字使用无衬线字体，优先 Helvetica 或 Arial，并在所有图中保持一致；Nature 图件规格[^nature-preparing]还要求使用标准字体，子图标注采用统一格式，文字保持可读并可编辑。由此可以得到一个实用标准：**同一篇论文不要让字体、字号、颜色规则和子图标注各自为政**。

版面组织也是统一性的一部分。Nature 图件排版说明[^nature-export]强调面板排列要整洁、节省空间，并尽量按字母顺序组织。多子图不是把若干小图拼在一起，而是要让读者顺着版面自然阅读。

<div class="example-pair" markdown>
<figure markdown>
  ![面板随机排列且空间利用差的错误示例](fig/nature-preparing-figures/panels-avoid-random.png)

  <figcaption><strong>避免：</strong>面板顺序混乱、空白分布不均，读者难以按逻辑阅读。</figcaption>
</figure>

<figure markdown>
  ![面板有序排列且空间利用好的推荐示例](fig/nature-preparing-figures/panels-recommended-ordered.png)

  <figcaption><strong>推荐：</strong>按内容重要性和阅读顺序安排面板，让版面紧凑但不拥挤。</figcaption>
</figure>
</div>

<div class="example-pair" markdown>
<figure markdown>
  ![使用非标准窄字体的错误示例](fig/nature-preparing-figures/font-avoid-nonstandard.png)

  <figcaption><strong>避免：</strong>使用变形、过窄或风格化字体，降低跨图一致性和可读性。</figcaption>
</figure>

<figure markdown>
  ![使用标准字体的推荐示例](fig/nature-preparing-figures/font-recommended-standard.png)

  <figcaption><strong>推荐：</strong>全图使用标准无衬线字体，并保持字号和标注风格一致。</figcaption>
</figure>
</div>

<div class="example-grid" markdown>
<figure markdown>
  ![自绘示意图中的无衬线正文字体](fig/nature-preparing-figures-extra/font-sans-serif-body.png)

  <figcaption>无衬线字体用于常规标签。</figcaption>
</figure>

<figure markdown>
  ![自绘示意图中的粗体子图标签](fig/nature-preparing-figures-extra/font-bold-labels.png)

  <figcaption>粗体用于子图编号等层级标记。</figcaption>
</figure>

<figure markdown>
  ![自绘示意图中的 Courier 等宽字体](fig/nature-preparing-figures-extra/font-courier-code.png)

  <figcaption>等宽字体适合序列或代码式内容。</figcaption>
</figure>

<figure markdown>
  ![自绘示意图中的希腊字母符号字体](fig/nature-preparing-figures-extra/font-symbol-greek.png)

  <figcaption>希腊字母等符号应保持标准字形。</figcaption>
</figure>
</div>

### 3.4 表达准确

图不能通过不合理的坐标轴范围、选择性展示、夸张配色或过度处理误导读者。美观不能牺牲准确性。科研图的可信度来自图与数据之间的稳定关系，而不是来自视觉冲击力。

Cleveland 和 McGill 的图形感知研究[^cleveland1984]说明，不同视觉编码会影响读者提取数量信息的准确性；Nature 图像完整性说明[^nature-integrity]也要求最终图像正确代表原始数据。检查数据图时，不只看图是否漂亮，还要看坐标轴、刻度、误差线、归一化方式和样例选择是否让读者得到与数据一致的结论。检查图像类结果时，则要特别注意裁剪、对比度、伪彩色和局部增强是否改变了读者对原始现象的判断。

坐标轴范围是最常见的准确性问题之一。截断坐标轴不一定永远错误，但如果没有明确说明，就容易把很小的差异画成巨大的视觉差异。下面的例子使用同一组数据，左图让差异显得非常夸张，右图则让读者看到差异在完整尺度中的实际大小。

<div class="example-pair" markdown>
<figure markdown>
  ![截断 y 轴导致差异被夸大的柱状图](fig/nature-preparing-figures/axis-avoid-truncated.png)

  <figcaption><strong>避免：</strong>用截断 y 轴放大视觉差异，却没有说明尺度变化。</figcaption>
</figure>

<figure markdown>
  ![完整 y 轴尺度下展示真实差异的柱状图](fig/nature-preparing-figures/axis-recommended-full-scale.png)

  <figcaption><strong>推荐：</strong>使用更完整的尺度，或在必须截断时清楚标注截断方式。</figcaption>
</figure>
</div>

一个简单原则是：图可以帮助读者更快看出结论，但不能让读者看出数据本身并不支持的结论。

### 3.5 可读可复现

图在缩小到论文单栏或双栏宽度后仍应清晰可读。对于数据图，代码、数据和输出结果应尽量可复现；对于图片类插图，原始图像、标注层和导出文件也应该能被追溯和重新编辑。

可读性有明确的投稿约束。Nature 图件排版说明[^nature-export]给出了单栏和双栏图宽，并要求缩小后文字仍然清楚、可编辑；Nature 图件规格[^nature-preparing]进一步要求图片分辨率、字体嵌入、比例尺和文字标注满足编辑与出版需要。可复现性则来自工具链控制，例如 Matplotlib 字体文档[^matplotlib-fonts]说明了导出时字体处理方式会影响后续编辑和跨平台显示。实际投稿前应同时检查两件事：**缩小后能不能读，换环境后能不能稳定导出**。

因此，Nature 的 89 mm 单栏、183 mm 双栏和高度限制可以作为理解“按版面设计”的例子，但不应机械套用到所有出版物。其他模板可能采用 A4、Letter、不同版心宽度或不同栏目数量；同一张图在单栏、双栏、横版页面或在线补充材料中，合适的字号、线宽和子图数量也会不同。

<div class="example-pair" markdown>
<figure markdown>
  ![Nature 单栏图宽示意](fig/nature-preparing-figures/sizing-single-column.png)

  <figcaption><strong>单栏：</strong>按单栏宽度设计时，所有文字和关键标注仍要能读清。</figcaption>
</figure>

<figure markdown>
  ![Nature 双栏图宽示意](fig/nature-preparing-figures/sizing-double-column.png)

  <figcaption><strong>双栏：</strong>信息量更大的多面板图可以使用双栏，但高度和图注空间也要一起考虑。</figcaption>
</figure>
</div>

<div class="example-pair" markdown>
<figure markdown>
  ![文字被轮廓化后不可编辑的错误示例](fig/nature-preparing-figures/text-avoid-outlined.png)

  <figcaption><strong>避免：</strong>把文字转成轮廓形状，后续无法修改拼写、字体和字号。</figcaption>
</figure>

<figure markdown>
  ![文字作为可编辑文本层保留的推荐示例](fig/nature-preparing-figures/text-recommended-editable.png)

  <figcaption><strong>推荐：</strong>文字保持为可编辑文本层，并在导出时正确嵌入字体。</figcaption>
</figure>
</div>

对于以图片为主体的科研图，例如显微图、医学影像、遥感图像和可视化案例图，Nature 的例子尤其直观：RGB 图片通常比 CMYK 更适合保留荧光和高饱和颜色；低分辨率图片不能靠软件放大来恢复细节；比例尺、箭头和文字应作为可编辑元素叠加在图片上，而不是压平成模糊的背景像素。这些例子说明，可读性不只是“文字够大”，还包括**位图主体足够清晰，标注层仍可编辑，颜色空间不会主动损失信息**。对应的 Avoid/Recommended 图片示例可以在[通用科研绘图 Checklist](../checklists/general_figure_checklist.md#nature)中查看。

## 4. 常见误区

!!! warning "不要把“画得满”当成“信息充分”"

    科研图最常见的问题不是信息不够，而是信息没有层级。无关元素越多，读者越难判断什么才是重点。

常见误区主要有以下几类。它们表面上是设计问题，本质上通常是图的任务没有先想清楚。

- 把所有实验结果都塞进一张图，导致主结论被稀释；
- 用太多颜色表达类别，但颜色本身没有明确语义；
- 只强调视觉效果，却没有突出数据证据；
- 图注只描述“画了什么”，没有说明“说明了什么”；
- 多个子图的字体、坐标轴、图例和颜色规则不一致。

## 5. 一句话总结

好的科研图不是“更好看”的图，而是能更清楚、更准确、更有说服力地表达论文观点的图。实际画图时，可以按顺序检查四件事：先问结论是否明确，再看证据是否充分，然后检查表达是否清晰，最后确认导出和投稿规范是否可靠。

[^nature-guide]: Nature Research Figure Guide. 该指南说明科研图是论文内容的重要组成部分，编辑良好的图可以提高理解效率并扩大研究传播范围。<https://research-figure-guide.nature.com/>

[^nature-preparing]: Nature Research Figure Guide. *Preparing figures - our specifications*. 该规范列出数据图必须包含的坐标轴、刻度、单位、可读文字，也列出应避免的多余装饰、重叠文字和难读背景。<https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/>

[^nature-final]: Nature. *Final submission*. 该说明建议图中文字使用无衬线字体，优先 Helvetica 或 Arial，并在所有图中保持一致。<https://www.nature.com/nature/for-authors/final-submission>

[^cleveland1984]: Cleveland, W. S., & McGill, R. (1984). *Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods*. Journal of the American Statistical Association. 这篇文章讨论了位置、长度、角度、面积、颜色等视觉编码在人类图形感知中的差异。<https://www.jstor.org/stable/2288400>

[^nature-integrity]: Nature Research Figure Guide. *Image Integrity*. 该说明要求最终图像正确代表原始数据，并避免会遮蔽或改变数据含义的处理。<https://research-figure-guide.nature.com/figures/image-integrity/>

[^nature-export]: Nature Research Figure Guide. *Building and Exporting Figure Panels*. 该说明给出单栏和双栏图宽，并要求图中文字保持清楚、可编辑。<https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/>

[^matplotlib-fonts]: Matplotlib. *Fonts in Matplotlib*. 该文档说明 Matplotlib 在 PDF 和 PostScript 中的字体处理方式，相关设置会影响后续编辑和跨平台显示。<https://matplotlib.org/stable/users/explain/text/fonts.html>
