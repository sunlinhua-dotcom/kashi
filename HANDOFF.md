# 接手文档 · 卡诗 GLOSS Wave 2 项目
*— 给接手的程序员 / 视觉 / 文案 —*

---

## 一、项目基础信息

| 项 | 值 |
|---|---|
| **GitHub 仓库** | https://github.com/sunlinhua-dotcom/kashi.git |
| **当前分支** | `main` |
| **最新 commit** | 见 `git log --oneline -1` |
| **部署平台** | Zeabur · `https://kashi.zeabur.app` |
| **Zeabur 项目入口** | https://zeabur.com/projects/69faf9e15749ae9f51253f5a |
| **开发主机本地路径** | `/Volumes/ProjectEXF/kashi/output/` |
| **主页文件** | `web/index.html`（21 章节单页 web） |
| **主图目录** | `images/` 下 42 张 WebP（已优化） |
| **主创意文档** | `creative_v2_master.md` |
| **调研文档** | `research/00 ~ 07.md` 共 8 份 |

---

## 二、目录结构（接手后看这个就够）

```
kashi/  (即 output/)
├── README.md                          # 项目说明
├── HANDOFF.md                         # 本文件
├── PRD.md                             # 项目需求文档
├── creative_v2_master.md              # 创意主文档（最重要）
├── creative_v2_delta.md               # v1 → v2 修改说明
├── big_idea_v2.md                     # Big Idea 三选一
├── final_creative_direction.md        # v1 创意（已淘汰但保留）
├── research_findings.md               # v1 调研（已淘汰但保留）
│
├── research/                          # ⭐ 7 份核心调研
│   ├── 00_executive_summary.md
│   ├── 01_overseas_consumer_reviews.md
│   ├── 02_shanghai_partner_shops.md
│   ├── 03_budget_roi_calculation.md
│   ├── 04_bd_intel_3shops.md
│   ├── 05_overseas_reviews_52quotes.md
│   ├── 06_competitor_scan.md
│   └── 07_domestic_ugc_honest.md
│
├── web/
│   └── index.html                     # ⭐ 21 章节主页（核心交付物）
│
├── images/                            # 42 张 WebP（不要直接改，按下方流程改）
│   ├── kv01-master-hero.webp
│   ├── kv02-wave1-opening-scene.webp
│   ├── ... (40 more)
│   ├── _generation_log.json           # v1 图生成记录
│   └── _generation_v2_log.json        # v2 图生成记录
│
├── index.html                         # 根目录重定向（zeabur 用）
├── zbpack.json                        # Zeabur 部署配置
├── .gitignore                         # 已配置好，不要乱删
│
├── image_prompts.json                 # v1 32 张图 prompt 清单
├── image_prompts_v2.json              # v2 8 张图 prompt 清单
├── generate_images.py                 # v1 批量生图脚本
└── generate_v2_images.py              # v2 批量生图脚本
```

---

## 三、环境准备（首次接手 1 次性）

### 3.1 安装基础工具

**macOS**：
```bash
# Git（系统自带或装 Xcode Command Line Tools）
xcode-select --install

# Python 3.10+
brew install python@3.11

# Pillow（用于图像优化）
pip3 install --user --break-system-packages Pillow
```

**Windows**：
```powershell
# 安装 Git for Windows: https://git-scm.com/download/win
# 安装 Python 3.10+: https://www.python.org/downloads/
pip install Pillow
```

**Linux**：
```bash
sudo apt install git python3 python3-pip
pip3 install Pillow
```

### 3.2 配置 Git 身份

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

### 3.3 配置 GitHub 推送权限

**方法 A · HTTPS + Personal Access Token（推荐）：**
1. 打开 https://github.com/settings/tokens?type=beta
2. 点击 "Generate new token"
3. Repository access 选 `sunlinhua-dotcom/kashi`
4. Permissions → Repository permissions → Contents 选 **Read and write**
5. 保存后复制 token（`ghp_xxxxxxxxxxx`）

**第一次 push 时**：
```bash
git push origin main
# Username: sunlinhua-dotcom
# Password: 粘贴上面的 ghp_xxx token（不是 GitHub 密码）
```

**保存凭据**（之后不再问）：
```bash
# macOS
git config --global credential.helper osxkeychain
# Windows
git config --global credential.helper manager
# Linux
git config --global credential.helper store
```

**方法 B · SSH（更安全）：**
```bash
# 1. 生成 SSH key
ssh-keygen -t ed25519 -C "你的邮箱"

# 2. 拷贝公钥
cat ~/.ssh/id_ed25519.pub

# 3. 打开 https://github.com/settings/keys → New SSH key → 粘贴
# 4. 修改远程仓库为 SSH 协议
cd 项目目录
git remote set-url origin git@github.com:sunlinhua-dotcom/kashi.git
```

---

## 四、克隆代码到本地

```bash
# 选个工作目录
cd ~/Documents

# Clone 仓库
git clone https://github.com/sunlinhua-dotcom/kashi.git
cd kashi
```

---

## 五、本地预览 web

```bash
cd kashi
python3 -m http.server 8080
# 浏览器打开 http://127.0.0.1:8080/web/index.html
```

或者直接在浏览器拖入 `web/index.html` 也可以（部分图可能因 file:// 协议不显示，建议用 http.server）。

---

## 六、常见修改场景 + 完整命令

### 场景 A · 改文字 / 改 Slogan / 调颜色

1. **编辑文件**：`web/index.html`
2. **本地预览**：刷新浏览器
3. **推送**：

```bash
cd kashi
git status                                       # 看改了什么
git add web/index.html
git commit -m "改 Wave 1 slogan 为新版本"
git push origin main
```

Zeabur 会自动检测推送并重新部署（约 1-2 分钟）。

### 场景 B · 替换某张图（不需要 API）

如果你已经有现成的新图（PSD/PNG/JPG）：

1. **命名规则**：保持原文件名（例如要替换 `kv01-master-hero.webp`，就把新图也命名成这个）
2. **转换为 WebP**（必须）：

```bash
# 安装 webp 工具
brew install webp        # macOS
# 或
sudo apt install webp    # Linux

# 转换（保留宽高比，最大宽 1280px，质量 82）
cwebp -q 82 -resize 1280 0 input.png -o images/kv01-master-hero.webp
```

或用 Python：
```python
from PIL import Image
img = Image.open("input.png").convert("RGB")
w, h = img.size
if max(w, h) > 1280:
    s = 1280 / max(w, h)
    img = img.resize((int(w*s), int(h*s)), Image.LANCZOS)
img.save("images/kv01-master-hero.webp", "WEBP", quality=82, method=6)
```

3. **推送**：

```bash
git add images/kv01-master-hero.webp
git commit -m "替换 master hero KV"
git push origin main
```

### 场景 C · 用 AI 生成新图（需要 API key）

1. **环境变量配置**（每次 shell 都要设，或写进 `~/.bashrc` / `~/.zshrc`）：

```bash
export IMAGE_API_KEY="你的_API_KEY"
export IMAGE_API_URL="https://api.apiyi.com/v1/images/generations"
export IMAGE_MODEL="gpt-image-2-all"
```

> ⚠️ **API Key 在哪拿**：原项目使用了 apiyi.com 的 GPT-Image-2 中转服务。如需获取，问项目主理人 Linhua（sunlinhua@gmail.com）。**绝不能 commit 到 git**。

2. **加新图**：

   a. 在 `image_prompts_v2.json` 添加新条目：
   ```json
   {
     "id": "V2-09",
     "filename": "v2-09-new-image.webp",
     "section": "新章节描述",
     "title": "图标题",
     "size": "1024x1024",
     "prompt": "Editorial luxury beauty photography ... (你的 prompt)"
   }
   ```

   b. 运行生图脚本：
   ```bash
   python3 generate_v2_images.py
   # 默认会跳过已存在的图，只生成新的
   ```

   c. **重要**：脚本默认输出 `.png`。生成后必须转 WebP：
   ```bash
   # 用 macOS 的脚本（如果你没有，参考下方"图像优化脚本"章节自己写）
   python3 -c "
   from PIL import Image
   p = 'images/v2-09-new-image.png'
   img = Image.open(p).convert('RGB')
   w,h = img.size
   if max(w,h)>1280:
       s = 1280/max(w,h); img=img.resize((int(w*s),int(h*s)),Image.LANCZOS)
   img.save(p.replace('.png','.webp'),'WEBP',quality=82,method=6)
   import os; os.remove(p)
   "
   ```

3. **在 web 中引用**：编辑 `web/index.html`，找到要插入的位置，加：
   ```html
   <img loading="lazy" decoding="async" src="../images/v2-09-new-image.webp" class="w-full h-full object-cover">
   ```

4. **推送**：

```bash
git add image_prompts_v2.json images/v2-09-new-image.webp web/index.html
git commit -m "加 V2-09 新图：xxx"
git push origin main
```

### 场景 D · 修改 research 内容

```bash
# 编辑 research/01_overseas_consumer_reviews.md
git add research/01_overseas_consumer_reviews.md
git commit -m "research: 更新海外评论的某条数据"
git push origin main
```

如果 research 内容也在 web/index.html 显示，记得同步改 HTML。

### 场景 E · 一次性优化全部图（已优化过，但万一有人手动加了 PNG）

```bash
# 用项目内置的脚本
python3 generate_v2_images.py  # 生成新 PNG（如果有新条目）

# 然后用我之前写的优化脚本（保存到 /tmp/optimize_images.py 或 scripts/ 目录）
# 见下方"图像优化脚本"章节
python3 /tmp/optimize_images.py

# 删除所有 PNG（因为已经有 WebP）
rm images/*.png
git add -A
git commit -m "perf: 重新优化图像"
git push origin main
```

### 图像优化脚本（保存为 `scripts/optimize_images.py`）

```python
#!/usr/bin/env python3
"""把 images/ 下所有 PNG 转 WebP（max 1280px, q82）"""
from pathlib import Path
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

SRC = Path("images")
MAX_DIM, Q = 1280, 82

def opt(p):
    out = p.with_suffix(".webp")
    if out.exists(): return f"SKIP {p.name}"
    img = Image.open(p).convert("RGB")
    w, h = img.size
    if max(w, h) > MAX_DIM:
        s = MAX_DIM / max(w, h)
        img = img.resize((int(w*s), int(h*s)), Image.LANCZOS)
    img.save(out, "WEBP", quality=Q, method=6)
    return f"OK {p.name}: {p.stat().st_size//1024}KB → {out.stat().st_size//1024}KB"

with ThreadPoolExecutor(8) as pool:
    for r in pool.map(opt, SRC.glob("*.png")):
        print(r)
```

---

## 七、Git 常用命令速查

```bash
# 看本地状态
git status

# 看修改的具体内容
git diff
git diff web/index.html

# 看历史
git log --oneline -10

# 撤销未 commit 的修改
git restore web/index.html        # 单文件
git restore .                      # 全部

# 撤销已 commit 但未 push 的（保留改动到工作区）
git reset HEAD~1

# 撤销已 commit 但未 push 的（彻底丢弃）⚠️ 危险
git reset --hard HEAD~1

# 拉远程最新（推送前先拉）
git pull origin main --rebase

# 处理冲突
# 编辑冲突文件 → git add → git rebase --continue

# 推送
git push origin main

# 强制推送（重写历史时用）⚠️ 仅在自己的分支
git push --force-with-lease origin main
```

---

## 八、Zeabur 部署 · 完整说明

### 8.1 自动部署
- **每次 `git push` 到 main 分支，Zeabur 自动检测并重新部署**
- 部署时间 1-3 分钟（看图像数量）
- 可在 Zeabur 控制台 → 服务状态 看实时日志

### 8.2 关键配置（已设定好，别动）

| 项 | 值 | 文件 |
|---|---|---|
| 部署类型 | 静态站点（Caddy 服务）| `zbpack.json` |
| 入口文件 | `web/index.html`（根 `index.html` 自动重定向） | `index.html` |
| 公网端口 | **8080**（不是 8765）| Zeabur 控制台 |

### 8.3 域名

- **主域名**：`https://kashi.zeabur.app`
- **直接访问主页**：`https://kashi.zeabur.app/web/index.html`
- **绑定自定义域名**：Zeabur 控制台 → 网络 → 自定义域名

### 8.4 502 错误排查
1. 检查公网访问端口是不是 **8080**（容器端口）
2. 查 Zeabur 服务状态日志
3. 看 GitHub 推送有没有触发部署（commit hash 是否匹配）
4. 实在不行：在 Zeabur 控制台手动点"重新部署"

---

## 九、不能 commit 到 git 的东西（绝对禁止）

```
.env
.env.*
*.key
secrets.json
*.pptx (原始 BRIEF 文件，机密)
*.m4a / *.mp3 (原始录音，机密)
*.xlsx / *.rtf (原始数据，机密)
__pycache__/
.venv/ venv/
.DS_Store
._*
*.swp
```

`.gitignore` 已经配好。**如果不小心提交了 API key**：

```bash
# 立刻撤销提交
git reset --soft HEAD~1
# 编辑文件移除 key
# 重新 commit
git push origin main

# 如果已经 push 了，必须撤销 GitHub 上的：
# 1. 立刻去 https://github.com/settings/tokens 撤销该 token
# 2. 联系项目主理人换 key
# 3. 用 git filter-repo 清理历史（高风险，不会就别动）
```

---

## 十、常见问题速查

### Q1: `git push` 卡住 / 报错 "Authentication failed"
A: GitHub 认证过期。重新生成 Personal Access Token，或参考第三章 SSH 配置。

### Q2: 推完 GitHub，Zeabur 没自动更新
A: 打开 Zeabur 控制台 → 服务 kashi → 点击右上角"重新部署"按钮。

### Q3: web 上传后图像不显示
A: 检查：
- 路径是不是 `../images/xxx.webp`（HTML 在 `web/` 子目录，所以用 `../images/`）
- 文件名是不是 `.webp`，不是 `.png`
- 浏览器开发者工具 Network Tab 看 404

### Q4: 我加了一张 PNG 图，但显示不出来
A: 必须转 WebP 才能用。参考场景 B 或场景 C 的"转 WebP"步骤。

### Q5: 中文乱码
A: HTML `<meta charset="UTF-8">` 已经设了。如果还乱码，检查你编辑器保存时的编码（必须 UTF-8 无 BOM）。

### Q6: 改完后部署版本和本地不一样
A: 浏览器缓存。Cmd/Ctrl + Shift + R 强制刷新。

---

## 十一、项目状态快照（截至本文档时间）

```
最新 commit:   见 git log
图像总数:      42 张 WebP
图像总大小:    ~4 MB（已从 89MB PNG 优化）
WEB 章节数:    21 章节
研究文档:      8 份 markdown
代码行数:      web/index.html ~1200 行
GitHub 推送数: 见 git log --oneline | wc -l
```

---

## 十二、联系方式

- **项目主理人**：Linhua Sun · sunlinhua@gmail.com
- **GitHub**：https://github.com/sunlinhua-dotcom
- **API key 持有人**：Linhua Sun

---

## 十三、推荐工作流（Daily ops）

```bash
# 早上开工
cd ~/Documents/kashi
git pull origin main --rebase

# 改东西
# ... 编辑 ...

# 本地测
python3 -m http.server 8080
# 浏览器打开 http://127.0.0.1:8080/web/index.html

# 满意后提交
git add -A
git status   # 二次确认没误加机密文件
git diff --cached   # 看 commit 内容
git commit -m "简短描述：改了什么"
git push origin main

# 等 1-2 分钟后检查 https://kashi.zeabur.app
```

---

*— 文档最后更新：2026-05-06 · 由 Claude AI 协助生成 —*
