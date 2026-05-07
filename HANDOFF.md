# 接手文档 · GLOSSY GIRLS CLUB 2.0

## 一、项目基础信息

| 项 | 值 |
|---|---|
| GitHub 仓库 | https://github.com/sunlinhua-dotcom/kashi.git |
| 当前分支 | `main` |
| 部署平台 | Zeabur |
| Web 首页 | `web/index.html` |
| 静态资源目录 | `web/assets/` |
| PRD | `PRD.md` |
| 话题库 | `docs/platform-topic-library.md` |
| 推文 Demo 库 | `docs/post-demo-library.md` |

## 二、目录结构

```text
kashi/
├── index.html
├── web/
│   ├── index.html
│   └── assets/
├── PRD.md
├── README.md
├── HANDOFF.md
├── docs/
│   ├── client-proposal.md
│   ├── platform-topic-library.md
│   ├── post-demo-library.md
│   ├── kol-brief.md
│   └── ppt-outline.md
├── robots.txt
├── zbpack.json
└── .gitignore
```

## 三、本地预览

```bash
git clone https://github.com/sunlinhua-dotcom/kashi.git
cd kashi
python3 -m http.server 8765
```

浏览器打开：

```text
http://127.0.0.1:8765/web/index.html
```

## 四、修改规则

### 4.1 改页面文字

编辑：

```text
web/index.html
```

提交：

```bash
git add web/index.html
git commit -m "Update proposal copy"
git push origin main
```

### 4.2 新增或替换图片

必须转成 WebP 后再提交。不要提交 PNG / JPG。

Python / Pillow 示例：

```python
from PIL import Image

img = Image.open("input.png").convert("RGB")
w, h = img.size
if max(w, h) > 1280:
    scale = 1280 / max(w, h)
    img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
img.save("web/assets/example.webp", "WEBP", quality=82, method=6)
```

提交前检查：

```bash
find web/assets -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \)
```

该命令应该没有输出。

### 4.3 密钥安全

不要提交：

- `.env`
- API key
- GitHub token
- Zeabur token
- 任何私钥或客户内部资料

如果不慎泄漏 token：

1. 立刻打开 https://github.com/settings/tokens 撤销。
2. 联系 Linhua 更换 key。

### 4.4 Zeabur 端口

- 线上按 Zeabur /平台注入端口处理，排查时以 `8080` 规则为准。
- 本地 `8765` 只用于开发预览，不要写入线上配置。
- 当前 `zbpack.json` 为静态部署配置：

```json
{
  "build_command": "",
  "start_command": "",
  "output_dir": ".",
  "framework": "static"
}
```

## 五、上线流程

```bash
git status
git add .
git commit -m "Update glossy girls club proposal"
git push origin main
```

推送后 Zeabur 会自动触发重新部署。部署完成后检查：

- 根目录是否跳转到 `web/index.html`
- Web 页面是否显示 `GLOSSY GIRLS CLUB 2.0`
- 页面图片是否正常加载
- `web/assets` 下是否没有 PNG / JPG
