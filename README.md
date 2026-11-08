# apparel-listing-images

服装商品套图生成 skill（ChatGPT 插件 / 技能、Hermes、OpenClaw）。角色：美区电商资深商品视觉设计总监。

## 用法
```
TK美区 白底卖点图解
亚马逊 3D立体展示 加字
TK美区 真人模特展示 组合装 黑+灰+蓝
TK SKU 灰色
```
流程：传商品图 → 确认档案和卖点 → 确认清单 → 每次回复 1 出一张。

## 模板与张数
四套模板：白底卖点图解、3D立体展示、真人模特展示、差异化对比（测试中）。
两个平台都是第 1 张纯白、第 2 张在纯白图上加卖点元素；TK 9 张（尺码图第 9 张），亚马逊 8 张（尺码图第 7 张）。TK 1:1、1600×1600；亚马逊 3:4、1600×2133。

## 文件
```
SKILL.md            角色、硬规则、持续学习、流程
lessons.md          经验库（开工前必读，做完一套追加新经验）
templates.md        四套模板
platforms.md        平台规格、加元素图
selling-points.md   卖点、差异化、措辞
extras.md           尺码图、组合装、多颜色、模特
prompts.md          英文提示词要点
```

## TK 美区最新版 Skill

新增独立 [tk-apparel-visuals](tk-apparel-visuals/SKILL.md) 子技能，按用户在2026-11确认的2–3张卖点图、原实拍细节优先、真人不露脸、组合装、真实拉链开口、图片转尺寸与换背景等规则执行。亚马逊老工作流保留。

- 最新可安装ZIP：GitHub Releases 标签 `skill-latest` 的 `skill.zip`（每次main更新覆盖旧资产）
- 每日增量：由 ChatGPT 的定时自动任务检查已确认反馈后提交，不靠GitHub Action自动理解聊天；Action只自动重打包已提交的规则。
