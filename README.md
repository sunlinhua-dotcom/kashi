# 主角光环 ✦ MAIN CHARACTER AURA

> 卡诗 GLOSS ABSOLU Wave 2 · IMC 比稿方案 · 2026.05  
> Kérastase × Glossy Girls · Wave 2 IMC Pitch · v 2.0

---

## 一句话项目背景

巴黎卡诗 GLOSS ABSOLU 系列 2026 年 7-8 月双 Wave 上市（**釉光奶皮子发膜**+**釉光小香雾**+**Bestie Gifting** 礼盒）。本仓库是**4A 级整合营销创意方案** + **可直接演示的网页 deck** + **34 张 GPT-Image-2 生成的视觉资产**。

---

## 🎯 核心创意主张

> # **主角光环 ✦ MAIN CHARACTER AURA**
> ### **「主角的光，从一抹釉光开始。」**
> ### **THE GLOSS OF THE MAIN CHARACTER.**

**双 Wave 拆解：**
- **Wave 1 · 第 1 集 · 开机仪式** — 发膜 = 主角上场前的"开机"
- **Wave 2 · 第 2 集 · 双女主同框** — 香水 = 闺蜜出门那一秒的镜头共享
- **Bestie Gifting · 共光胶囊** — 4 Tier 礼盒 = 高光时刻的可分享容器
- **IP Pop-Up · The AURA CAFÉ × 13 de Marzo** — 武康-安福片场化空间

---

## 🔥 这个 Big Idea 凭什么世界级

1. **挖到中文「高光」三关合一** ——hair gloss × main character aura × life moment——这是英语广告人做不到的语义独占
2. **占领 2026 小红书最炽热的自我赋权词**——「主角光环」32 万贴 / 4.2 亿阅读，至今无品牌占领
3. **完美兼容 brief 全部 10 条硬约束**（详见 web 第 1 章）
4. **直接对位 Cannes 2024-25 美妆获奖法则**——Hair = Identity, not surface

---

## 📂 仓库内容

```
output/
├── web/
│   └── index.html                  # 14 章节 4A 级演示网页（单文件）
├── images/                         # 34 张 GPT-Image-2 生成的视觉资产
│   ├── kv01-master-hero.png        # 主 KV
│   ├── kv02-wave1-opening-scene.png  # Wave 1 KV
│   ├── kv03-wave2-co-stars.png     # Wave 2 KV
│   ├── kv04-aura-cafe-exterior.png # Pop-Up Café 外立面
│   ├── prd01~06.png                # 产品图（发膜/香水/礼盒/小粉珠）
│   ├── ta01~04.png                 # 4 个 TA 生活切片
│   ├── nn01~10.png                 # 10 个昵称概念图
│   ├── ip01~04.png                 # IP 联名（Café 内部 / 小熊 / 甜品 / 周边）
│   ├── bes01~02.png                # Bestie Gifting + 主角徽章
│   └── cmp01~04.png                # 代言 KV / OOH / 地铁 / 社交
├── PRD.md                          # 项目产品需求文档
├── research_findings.md            # 8 维深度调研备忘
├── big_idea_v2.md                  # Big Idea 三选一对比矩阵
├── final_creative_direction.md     # 主角光环完整创意方向（11 章节）
├── image_prompts.json              # 34 张图的完整 prompt
└── generate_images.py              # 批量生图脚本（OpenAI 兼容 API）
```

---

## 🌐 如何查看演示

### 方法 1 · 本地直开
```bash
open output/web/index.html
```

### 方法 2 · 本地 HTTP 服务（推荐，避免跨域）
```bash
cd output
python3 -m http.server 8765
# 然后浏览器访问 http://127.0.0.1:8765/web/index.html
```

### 方法 3 · GitHub Pages
进入 GitHub repo Settings → Pages → 选择分支 main → 路径 `/output` → 保存。  
访问 `https://sunlinhua-dotcom.github.io/kashi/web/index.html`

---

## 🎨 重新生成图像

```bash
export IMAGE_API_KEY="your-openai-compatible-api-key"
export IMAGE_API_URL="https://api.openai.com/v1/images/generations"  # 可选
export IMAGE_MODEL="gpt-image-2-all"  # 或 dall-e-3 / gpt-image-1
python3 output/generate_images.py
```

需要 OpenAI 或兼容服务的 API Key（已支持 `apiyi.com` 等中转）。

---

## 📊 关键数据复盘

### Wave 1 战绩（2025.7-8）
- 销售额 **3,700 万元**
- 小粉珠售出 **5.8 万瓶**
- 全渠道 NO.1（天猫/京东/抖音/丝芙兰）
- 社交聆听 PSR **94.1%**

### Wave 2 销售目标
| 单品 | 上市 | 售价 | 目标 |
|---|---|---|---|
| 釉光奶皮子发膜 | 2026.7 | ¥390 | 第二大发膜 SKU |
| 釉光小香雾 | 2026.8 | ¥360 | 15K 支首期 |
| 小粉珠精油 | 涨价至 6 月 | ¥320 | 销售翻倍 |

### Wave 2 预测影响力
- 系列销售额 **6,800 万 +84%**
- 小红书 UGC **15K+ +166%**
- 微博话题 **#主角光环上线# 5 亿+**
- 客群年龄下沉至 **27.5 岁**（vs 现状 29.8）

---

## 🛠 技术方案

| 层 | 选型 |
|---|---|
| 网页 | 单文件 HTML + Tailwind CSS（CDN） |
| 字体 | Playfair Display + Inter + Noto Serif/Sans SC |
| 动效 | IntersectionObserver + CSS Transitions |
| 图像生成 | GPT-Image-2 (via apiyi.com OpenAI 兼容协议) |
| 视觉调研 | Xiaomi MiMo-v2-omni（多模态视觉） |

---

## 📜 版权与免责

- 本仓库为**比稿创意方案**，未经客户确认前为内部交付物
- 所有视觉为 **AI 生成**（GPT-Image-2），非真实拍摄；最终上市方案需替换为正式拍摄
- "杨幂代言 KV" 为**风格意象图**，非真实代言人肖像（规避肖像权）
- 13 de Marzo / 卡诗 / Kérastase 商标版权归原品牌所有
- Cannes Lions / Sol de Janeiro / Dove 等案例引用仅供创意参考

---

## 📅 时间线

- **2026.05.06 上午**：BRIEF + 录音 + Excel 全量解读 + PPT 视觉分析（小米 MiMo）
- **2026.05.06 下午**：8 维深度调研 + Big Idea v2 推导 + 网页搭建 + 34 图生成
- **2026.05.06 晚**：Push to GitHub（本次）

---

*— "主角的光，从一抹釉光开始。" —*
