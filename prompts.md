# 英文提示词要点

每条生图提示词 = 本张画面 + 英文商品描述 + 下面需要的句子，用通顺的英文写。

**第 1 张**（附用户参考图）：
`Use the attached photo only to identify the product, and create a new image in the style described below. Keep the product design exactly the same, with every part in its true proportion and position. Do not copy the photo's pose, placement, flat shape, wrinkles or angle.`

**第 2 张起**（附主参考图）：
`The attached image is the master reference. Keep the garment, colors, details and style exactly the same; only change what this image needs (angle, crop or layout).`

**加附细节图时**（做某个部位）：
`The second attached photo is a close-up of the <part>. Use it only to get this part exactly right; keep everything else, the style and the composition based on the master reference.`

**编辑第 1 张**（加元素图、卖点图、尺码图）：`Edit the attached image. Keep the garment exactly as it is, pixel for pixel; do not redraw it. Only add: …`
- 卖点图 B 需要空间时：`Extend the canvas to the right with the same white background and place the detail cards there; the garment stays unchanged.`

**局部修改**（配合框选）：`Only change <编号 + 位置，如 the main zipper pull at the center of the chest> inside the selected area, to match the attached close-up. Keep <其他五金，如 the two side pocket zipper pulls> and everything else exactly unchanged.`

**插兜**（在认可的垂手图上编辑）：`Edit the attached image. Move only the <right> hand into the <right front slanted pocket>; the pocket opening runs <diagonally from the waist down toward the side seam>. The hand goes inside the pocket, only the thumb visible, the fabric slightly stretched by the hand. Keep the garment, the model and everything else unchanged.`

**第 2 张**（编辑第 1 张）：`Edit the attached image. Keep the garment, position, size and angle unchanged. Only add these selling-point elements: …`

**风格**
- 白底隐形模特：`Invisible ghost mannequin product photo, pure white background.`
- 3D 立体：`3D ghost mannequin photo, straight front view, the main zipper closed to the collar. The garment is naturally filled as if worn by an invisible body: rounded shoulders, both sleeves evenly filled from shoulder to cuff, smooth fabric on the chest, back and sleeves, with only a few soft natural folds at the armpits, elbows and cuffs. Real fabric texture.`
- 真人模特：`A real American model actually wearing the garment, framed from the neck down (face not shown), arms relaxed at the sides. The garment fits and drapes naturally like a real fashion photo, not pasted on.`（裤子改成 `framed from the waist to the shoes`）

**视角**
- 背面：`Rear view; only the back of the garment is visible, no front-only details.`
- 3/4：`Three-quarter view at 45 degrees.`

**每张都加**：
`Photorealistic commercial product photography, true-to-life colors, natural fabric texture, no CGI or plastic look. This is a real product photo taken in one single camera shot; the frame is one continuous scene from edge to edge. Highest resolution.`

**画幅**：TK 和亚马逊都加 `Vertical 3:4 format.`

提示词只写想要的画面，不写 grid、collage 这类描述画面布局的否定词（会让模型往拼图方向联想）

**每张都写清关键部件**：从细节锁定表里把这张会出现的拉头、口袋、Logo 等写具体（形状、颜色、大小、位置），不要只写 "black zipper pull"

**深色商品加**：`Keep the fabric texture and folds clearly visible; no crushed blacks.`
