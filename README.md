# apparel-listing-images

服装商品套图规则（TK美区 / 亚马逊美国站）。角色：美区电商资深商品视觉设计总监。
主要用法：ChatGPT 项目（普通对话），也可作为插件 / 技能给 Hermes、OpenClaw 用。

## 流程
发商品图 → 识别商品、细节锁定表、卖点 → 选平台 → 选模板 → 确认清单 → 每次回复 1 出一张。

## 模板
① 白底卖点图解　② 3D立体展示　③ 真人模特展示　④ 差异化对比（测试中）　⑤ 3D卖点套图
①–④：TK 9 张、亚马逊 8 张；⑤：两个平台都是 5 张（3D 主图 + A/B/C 三张卖点图 + 尺码图）。
比例：TK 3:4、1800×2400；亚马逊 3:4、1600×2133。

## 文件
```
SKILL.md            角色、硬规则、持续学习、流程
lessons.md          经验库（只记踩过的坑；确认后增量更新，只改这个文件）
templates.md        五套模板、3D 立体填充标准
platforms.md        平台规格、加元素图、转TK尺寸
selling-points.md   卖点、三种卖点版式、措辞
extras.md           尺码图、组合装、多颜色、模特
prompts.md          英文提示词要点
```

## 安装
- ChatGPT 项目：项目设置里填项目指令，「来源」里上传合并后的规则文件和经验库
- 插件：Releases `skill-latest` 里的 `apparel-listing-images-plugin.zip`（每次 main 更新自动重打包）
- 自动任务只能增量更新 `lessons.md`，且只写用户确认过的经验

## 另一个项目：营销主图底图（icon-main/）
卖点小图标底图 + 反差图，纯色背景为主；单独一个 ChatGPT 项目使用，经验库和主项目共用 lessons.md。
