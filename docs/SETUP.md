<!-- prettier-ignore-start -->
# 📰 每日科技新聞速報 - 快速設置指南

> **目標**: 每天早上 9 點自動收集全球科技新聞，整理成日報發到你的郵箱

## ⚡ 快速開始 (5 分鐘)

### 1️⃣ 獲取 NewsAPI 密鑰

1. 訪問 https://newsapi.org/
2. 點擊 "Get API Key"
3. 使用 Gmail 或其他帳號註冊
4. 複製你的 API Key (免費版每月 100 次請求)

### 2️⃣ 設置 GitHub Secrets

1. 打開你的倉庫 → **Settings**
2. 左側菜單 → **Secrets and variables** → **Actions**
3. 點擊 **New repository secret**，添加以下三個密鑰:

| 密鑰名稱 | 值 | 說明 |
|---------|-----|------|
| `NEWSAPI_KEY` | 從上面複製的 API Key | NewsAPI 密鑰 |
| `EMAIL_USER` | 你的 Gmail 地址 | 例: `your-email@gmail.com` |
| `EMAIL_PASSWORD` | Gmail 應用密碼 | 見下面說明 |

### 3️⃣ 生成 Gmail 應用密碼

> ⚠️ **重要**: 不能使用普通 Gmail 密碼，需要應用密碼

1. 訪問 https://myaccount.google.com/
2. 左側菜單 → **安全性**
3. 向下滾動 → **應用密碼**
4. 選擇 "Mail" 和 "Windows 電腦" (或你使用的設備)
5. 複製生成的 16 字符密碼，粘貼到 `EMAIL_PASSWORD`

![Gmail App Password](https://lh3.googleusercontent.com/SXbCPyR6gBQ_U5NkqLq8AWeqN3pVHVW-KKdKKkkQfZw=w300)

### 4️⃣ 啟用 GitHub Actions

1. 打開倉庫 → **Actions** 選項卡
2. 如果看到提示，點擊 "I understand my workflows, go ahead and enable them"

### 5️⃣ 測試

1. 打開 **Actions** 選項卡
2. 左側選擇 "Daily Tech News Digest" 工作流
3. 點擊 **Run workflow** → **Run workflow**
4. 等待 2-3 分鐘
5. 檢查你的郵箱 (可能在垃圾郵件文件夾)

✅ 完成！從明天早上 9 點開始，你將每天收到新聞速報。

---

## 🛠️ 常見問題 FAQ

### Q: 郵件未收到怎麼辦?

**A**: 按以下步驟檢查:

1. ✅ 檢查 **垃圾郵件** 和 **促銷郵件** 文件夾
2. ✅ 驗證 Secrets 中的 Gmail 地址和密碼是否正確
3. ✅ 確認已生成應用密碼 (不是普通密碼)
4. ✅ 檢查 NewsAPI 密鑰是否有效
5. ✅ 查看 Actions 工作流日誌查看錯誤信息

### Q: 如何改變發送時間?

**A**: 編輯 `.github/workflows/daily-digest.yml`:

```yaml
- cron: '0 1 * * *'  # 當前設置: UTC 01:00 (台北時間 09:00)
```

Cron 語法: `分 小時 * * *` (UTC 時間)
- 台北時間 09:00 → UTC 01:00 → `0 1 * * *`
- 台北時間 18:00 → UTC 10:00 → `0 10 * * *`
- 台北時間 21:00 → UTC 13:00 → `0 13 * * *`

### Q: 如何改變收件人郵箱?

**A**: 編輯 `.github/workflows/daily-digest.yml`:

```yaml
env:
  RECIPIENT_EMAIL: your-new-email@gmail.com
```

或編輯 `scripts/collect_news.py`:

```python
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', 'your-email@gmail.com')
```

### Q: NewsAPI 免費版有限制嗎?

**A**: 
- ✅ 免費版每月 100 個請求
- 📅 每天約 3 個請求，足以覆蓋整月
- 💳 如需更多，可升級付費版 ($19/月起)

### Q: 如何增加/減少新聞數量?

**A**: 編輯 `scripts/collect_news.py`:

```python
# 改變數字 20 為你想要的數量
articles = articles[:20]  # 改為例如 :30
```

### Q: 如何添加新的新聞分類?

**A**: 編輯 `scripts/collect_news.py` 中的 `CATEGORIES` 字典:

```python
CATEGORIES = {
    '新分類': {
        'keywords': ['關鍵詞1', '關鍵詞2', '關鍵詞3'],
        'color': '#HEXCOLOR'
    },
    # ...其他分類
}
```

---

## 📚 詳細說明

### 工作流工作原理

```
每天 09:00 (台北時間)
    ↓
GitHub Actions 自動觸發
    ↓
Python 腳本運行
    ↓
1. 通過 NewsAPI 收集新聞
2. 按 11 個分類標籤分類
3. 按重要度排序 (約 20 條)
4. 生成美觀的 HTML 郵件
5. 通過 Gmail 發送
6. 保存日報到倉庫
    ↓
✅ 郵件送達你的收件箱
```

### 支持的新聞分類

| 分類 | 關鍵詞示例 |
|-----|----------|
| 🤖 AI | 人工智能、機器學習、深度學習 |
| 🦾 機器人 | 機器人、自動化、自主系統 |
| 🔬 基礎科學 | 量子物理、突破性研究 |
| ⚛️ 物理 | 粒子物理、相對論 |
| 🧬 生物 | 基因工程、DNA 研究 |
| 🧪 化學 | 化學反應、分子研究 |
| 💊 醫療 | 醫學突破、藥物治療 |
| 🚀 航空航天 | 太空探索、衛星技術 |
| 🧠 心理學 | 神經科學、認知研究 |
| 👥 社會學 | 社會文化、經濟發展 |
| 💻 信息工程 | 計算機技術、網絡安全 |

### 郵件格式

你將收到的郵件包含:

```
📰 每日科技新聞速報
2026-04-25

📊 新聞統計: 20 條新聞，11 個分類

## 🤖 AI
1. 標題 (中英文)
   📰 來源 | 🕐 發布時間
   內容摘要...
   🔗 查看原文

2. 標題 (中英文)
   ...

## 🚀 航空航天
...
```

---

## 🔒 安全注意事項

- ✅ **Secrets 是加密的**: GitHub 不會顯示你的密鑰
- ✅ **廢止 App 密碼**: 如果洩露，可在 Gmail 設置中立即廢止
- ✅ **定期檢查**: 檢查 Gmail 的"安全性檢查"

---

## 📞 需要幫助?

1. 查看 GitHub Actions 日誌: Actions → Workflow Logs
2. 檢查 Secrets 是否設置正確
3. 驗證網絡連接
4. 查看錯誤消息

---

**祝你使用愉快！** 🎉

<!-- prettier-ignore-end -->
