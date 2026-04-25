# 更新日誌 | Changelog

## [1.0.0] - 2026-04-25

### ✨ 初始版本發布 | Initial Release

#### 🎉 核心功能
- ✅ 多源新聞聚合（7個RSS源）
- ✅ 智能新聞分類（11個類別）
- ✅ AI 驅動的內容摘要（Claude API）
- ✅ 每日自動郵件發送（HTML格式）
- ✅ GitHub Actions 工作流自動化
- ✅ 完全免費運行

#### 📰 支持的新聞源
- HackerNews
- ArXiv (AI & Physics)
- Nature
- Science Daily
- TechCrunch
- MIT News
- 多源聚合

#### 📂 覆蓋的11個類別
1. AI（人工智能）
2. 機器人
3. 信息工程
4. 基礎科學
5. 物理
6. 生物
7. 化學
8. 醫療
9. 航空航天
10. 心理學
11. 社會學

#### 📁 項目文件
- `scripts/main.py` - 主協調程式
- `scripts/news_fetcher.py` - RSS 新聞爬蟲
- `scripts/classifier.py` - 新聞自動分類器
- `scripts/summarizer.py` - Claude AI 摘要生成
- `scripts/email_sender.py` - HTML 郵件生成和發送
- `.github/workflows/daily-digest.yml` - GitHub Actions 工作流
- `requirements.txt` - Python 依賴
- `README.md` - 完整文檔
- `SETUP_GUIDE.md` - 設置指南
- `CHANGELOG.md` - 本文件

#### 🚀 自動化配置
- ⏰ 每天早上 9:00（台灣時間）自動執行
- 📧 自動發送到指定 Gmail
- 🔄 完全無人值守

#### 🔐 安全功能
- GitHub Secrets 管理敏感信息
- 不在代碼中存儲 API 金鑰
- Gmail 應用密碼隔離

#### 📚 文檔
- 中英文完整 README
- 分步設置指南
- 故障排除文檔
- 代碼註釋

---

## 計劃中的功能 | Planned Features

### v1.1.0 (計劃中)
- [ ] 支持更多新聞源（Reddit、ProductHunt 等）
- [ ] 用戶自定義分類
- [ ] 郵件語言選擇
- [ ] 多個收件人支持

### v1.2.0 (計劃中)
- [ ] Web 界面查看歷史日報
- [ ] 數據庫存儲（SQLite/PostgreSQL）
- [ ] 新聞趨勢分析

### v2.0.0 (計劃中)
- [ ] 機器學習改進分類
- [ ] 用戶偏好設置
- [ ] 多語言支持
- [ ] REST API 接口

---

## 已知問題 | Known Issues

無當前已知問題。

如發現問題，請在 [GitHub Issues](https://github.com/kuo348/newtechinfo/issues) 報告。

---

## 版本歷史 | Version History

| 版本 | 發布日期 | 說明 |
|------|---------|------|
| 1.0.0 | 2026-04-25 | 初始版本發布 |

---

## 貢獻指南 | Contributing

歡迎提交 Issue 和 Pull Request！

改進方向：
- 新聞源擴展
- 分類算法優化
- 摘要質量提升
- 界面開發
- 國際化支持

---

## 許可證 | License

MIT License - 詳見倉庫 LICENSE 文件

---

## 聯繫方式 | Contact

- 📧 Email: kuo348@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/kuo348/newtechinfo/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/kuo348/newtechinfo/discussions)

---

# English Version

## [1.0.0] - 2026-04-25

### ✨ Initial Release

#### 🎉 Core Features
- ✅ Multi-source news aggregation (7 RSS feeds)
- ✅ Intelligent news classification (11 categories)
- ✅ AI-powered content summarization (Claude API)
- ✅ Daily automated email delivery (HTML format)
- ✅ GitHub Actions workflow automation
- ✅ Completely free to run

#### 📰 Supported News Sources
- HackerNews
- ArXiv (AI & Physics)
- Nature
- Science Daily
- TechCrunch
- MIT News
- Multi-source aggregation

#### 📂 11 Supported Categories
1. AI (Artificial Intelligence)
2. Robotics
3. Information Engineering
4. Basic Science
5. Physics
6. Biology
7. Chemistry
8. Medicine
9. Aerospace
10. Psychology
11. Sociology

#### 📁 Project Files
- `scripts/main.py` - Main orchestrator
- `scripts/news_fetcher.py` - RSS news crawler
- `scripts/classifier.py` - Automatic news classifier
- `scripts/summarizer.py` - Claude AI summarizer
- `scripts/email_sender.py` - HTML email generator
- `.github/workflows/daily-digest.yml` - GitHub Actions workflow
- `requirements.txt` - Python dependencies
- `README.md` - Complete documentation
- `SETUP_GUIDE.md` - Setup instructions
- `CHANGELOG.md` - This file

#### 🚀 Automation
- ⏰ Automatic execution at 9:00 AM (Taiwan Time) daily
- 📧 Automatic delivery to specified Gmail
- 🔄 Completely unattended

#### 🔐 Security Features
- GitHub Secrets management
- No API keys in code
- Isolated Gmail app password

#### 📚 Documentation
- English & Chinese README
- Step-by-step setup guide
- Troubleshooting guide
- Code comments

---

## Planned Features

### v1.1.0 (Planned)
- [ ] More news sources (Reddit, ProductHunt, etc.)
- [ ] User custom categories
- [ ] Email language selection
- [ ] Multiple recipients support

### v1.2.0 (Planned)
- [ ] Web interface for digest history
- [ ] Database storage (SQLite/PostgreSQL)
- [ ] News trend analysis

### v2.0.0 (Planned)
- [ ] Machine learning improved classification
- [ ] User preference settings
- [ ] Multi-language support
- [ ] REST API interface

---

## Known Issues

No known issues at this time.

Please report issues at [GitHub Issues](https://github.com/kuo348/newtechinfo/issues).

---

## Version History

| Version | Release Date | Description |
|---------|--------------|-------------|
| 1.0.0 | 2026-04-25 | Initial release |

---

## Contributing

Issues and Pull Requests are welcome!

Areas for improvement:
- News source expansion
- Classification algorithm optimization
- Summarization quality enhancement
- UI development
- Internationalization support

---

## License

MIT License - See LICENSE file in repository

---

## Contact

- 📧 Email: kuo348@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/kuo348/newtechinfo/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/kuo348/newtechinfo/discussions)
