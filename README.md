# GLOSSY GIRLS CLUB 2.0

卡诗 GLOSS ABSOLU Wave 2 品牌方提案 Web 与交付文档。

## 当前入口

- 线上部署：Zeabur 自动部署，推送 `main` 后触发。
- Web 首页：`web/index.html`
- 根目录：`index.html` 自动跳转到 `web/index.html`
- 主要静态资源：`web/assets/`

## 主要交付

- `web/index.html`：完整品牌方提案页面，包含策略、平台规划、话题方向、推文 demo、KOL / 线下 / 电商 / 直播规划与执行节奏。
- `PRD.md`：完整 PRD。
- `docs/platform-topic-library.md`：平台话题库。
- `docs/post-demo-library.md`：推文 Demo 文案库。
- `docs/kol-brief.md`：达人 Brief。
- `docs/ppt-outline.md`：PPT 大纲。
- `docs/client-proposal.md`：品牌方提案正文。
- `HANDOFF.md`：给接手程序员的维护说明。

## 本地预览

```bash
python3 -m http.server 8765
```

打开：

```text
http://127.0.0.1:8765/web/index.html
```

## 部署规则

- 新增图片必须使用 WebP；不要提交 PNG / JPG。
- 不提交 `.env`、API key、GitHub token 或任何密钥。
- Zeabur 使用平台注入端口，线上端口按 `8080` 规则排查；本地预览端口不要反写到线上配置。
