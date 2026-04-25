#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily Tech News Digest Collector
Collects global tech news, categorizes them, and sends via email
"""

import os
import json
import requests
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from urllib.parse import quote

# Configuration
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', EMAIL_USER)

NEWSAPI_ENDPOINT = 'https://newsapi.org/v2/everything'

# News Categories with keywords and colors
CATEGORIES = {
    '🤖 AI': {
        'keywords': ['artificial intelligence', 'machine learning', 'deep learning', 'neural network', 'AI', '人工智能', '機器學習', '深度學習'],
        'color': '#FF6B6B'
    },
    '🦾 機器人': {
        'keywords': ['robot', 'robotics', 'automation', 'autonomous', '機器人', '自動化', '自主系統'],
        'color': '#4ECDC4'
    },
    '🔬 基礎科學': {
        'keywords': ['quantum', 'physics research', 'scientific breakthrough', '量子', '物理研究', '科學突破'],
        'color': '#45B7D1'
    },
    '⚛️ 物理': {
        'keywords': ['particle physics', 'relativity', 'physics', 'space-time', '粒子物理', '相對論', '物理學'],
        'color': '#96CEB4'
    },
    '🧬 生物': {
        'keywords': ['biology', 'genetic', 'DNA', 'evolution', 'biotech', '生物', '基因', 'DNA', '進化'],
        'color': '#FFEAA7'
    },
    '🧪 化學': {
        'keywords': ['chemistry', 'chemical', 'molecule', 'reaction', '化學', '分子', '反應'],
        'color': '#DFE6E9'
    },
    '💊 醫療': {
        'keywords': ['medicine', 'medical', 'health', 'drug', 'hospital', 'treatment', '醫療', '醫學', '藥物', '治療'],
        'color': '#A29BFE'
    },
    '🚀 航空航天': {
        'keywords': ['space', 'aerospace', 'satellite', 'nasa', 'rocket', 'spacex', '太空', '航天', '衛星'],
        'color': '#FF7675'
    },
    '🧠 心理學': {
        'keywords': ['psychology', 'neuroscience', 'brain', 'cognitive', 'mental', '心理', '神經科學', '大腦', '認知'],
        'color': '#74B9FF'
    },
    '👥 社會學': {
        'keywords': ['sociology', 'culture', 'society', 'economy', 'social', '社會', '文化', '經濟'],
        'color': '#81ECEC'
    },
    '💻 信息工程': {
        'keywords': ['computer', 'software', 'network', 'cybersecurity', 'technology', '計算機', '軟件', '網絡', '技術'],
        'color': '#55EFC4'
    }
}

def fetch_news():
    """Fetch latest tech news from NewsAPI"""
    try:
        # Search for tech and science news
        query = 'technology OR artificial intelligence OR science OR innovation'
        params = {
            'q': query,
            'sortBy': 'publishedAt',
            'language': 'en',
            'pageSize': 100,
            'apiKey': NEWSAPI_KEY,
            'from': (datetime.now() - timedelta(days=1)).isoformat()
        }
        
        response = requests.get(NEWSAPI_ENDPOINT, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('status') != 'ok':
            print(f"API Error: {data.get('message')}")
            return []
        
        articles = data.get('articles', [])
        print(f"✅ Fetched {len(articles)} articles from NewsAPI")
        return articles
    
    except Exception as e:
        print(f"❌ Error fetching news: {e}")
        return []

def categorize_article(article):
    """Categorize article based on keywords"""
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    content = article.get('content', '').lower()
    
    combined_text = f"{title} {description} {content}"
    
    # Find matching categories
    matches = []
    for category, data in CATEGORIES.items():
        for keyword in data['keywords']:
            if keyword.lower() in combined_text:
                matches.append(category)
                break
    
    return matches if matches else ['💻 信息工程']  # Default category

def calculate_importance(article):
    """Calculate article importance score (0-100)"""
    score = 50  # Base score
    
    # Higher score for articles with images
    if article.get('urlToImage'):
        score += 10
    
    # Higher score for articles from major sources
    major_sources = ['bbc', 'cnn', 'techcrunch', 'wired', 'nature', 'science', 
                     'theverge', 'arstechnica', 'engadget', 'mit']
    source = article.get('source', {}).get('name', '').lower()
    if any(major in source for major in major_sources):
        score += 15
    
    # Consider published time (more recent = higher score)
    published = article.get('publishedAt', '')
    if published:
        pub_time = datetime.fromisoformat(published.replace('Z', '+00:00'))
        hours_old = (datetime.now(pub_time.tzinfo) - pub_time).total_seconds() / 3600
        if hours_old < 6:
            score += 20
        elif hours_old < 12:
            score += 10
    
    return min(100, score)

def process_articles(articles):
    """Process and categorize articles"""
    processed = []
    
    for article in articles:
        # Skip articles without content
        if not article.get('title') or not article.get('description'):
            continue
        
        categories = categorize_article(article)
        importance = calculate_importance(article)
        
        processed.append({
            'title': article.get('title', ''),
            'description': article.get('description', ''),
            'url': article.get('url', ''),
            'source': article.get('source', {}).get('name', 'Unknown'),
            'publishedAt': article.get('publishedAt', ''),
            'urlToImage': article.get('urlToImage', ''),
            'categories': categories,
            'importance': importance
        })
    
    # Sort by importance
    processed.sort(key=lambda x: x['importance'], reverse=True)
    
    # Limit to 20 articles
    return processed[:20]

def get_english_title(title):
    """Extract or generate English version of title"""
    # Simple heuristic: if title has both Chinese and English, split
    # Otherwise return as is
    return title

def generate_html_email(articles):
    """Generate beautiful HTML email"""
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Group articles by category
    by_category = {}
    for article in articles:
        for category in article['categories']:
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(article)
    
    # Find category colors
    category_colors = {cat: data['color'] for cat, data in CATEGORIES.items()}
    
    html = f"""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📰 每日科技新聞速報</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }}
        .container {{
            max-width: 800px;
            margin: 20px auto;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 28px;
            margin-bottom: 10px;
        }}
        .header p {{
            font-size: 14px;
            opacity: 0.9;
        }}
        .stats {{
            background-color: #f0f0f0;
            padding: 15px 20px;
            font-size: 14px;
            text-align: center;
        }}
        .content {{
            padding: 30px 20px;
        }}
        .category {{
            margin-bottom: 30px;
        }}
        .category-title {{
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        .article {{
            margin-bottom: 20px;
            padding: 15px;
            border-left: 4px solid #667eea;
            background-color: #f9f9f9;
            border-radius: 4px;
        }}
        .article-title {{
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #333;
        }}
        .article-meta {{
            font-size: 12px;
            color: #999;
            margin-bottom: 8px;
        }}
        .article-description {{
            font-size: 14px;
            color: #555;
            margin-bottom: 10px;
            line-height: 1.5;
        }}
        .article-link {{
            display: inline-block;
            color: #667eea;
            text-decoration: none;
            font-size: 13px;
            font-weight: bold;
        }}
        .article-link:hover {{
            text-decoration: underline;
        }}
        .footer {{
            background-color: #f0f0f0;
            padding: 20px;
            text-align: center;
            font-size: 12px;
            color: #999;
            border-top: 1px solid #ddd;
        }}
        .unsubscribe {{
            font-size: 11px;
            color: #999;
            margin-top: 15px;
        }}
        @media (max-width: 600px) {{
            .container {{
                margin: 10px;
            }}
            .header {{
                padding: 20px 15px;
            }}
            .header h1 {{
                font-size: 24px;
            }}
            .content {{
                padding: 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📰 每日科技新聞速報</h1>
            <p>Daily Tech News Digest</p>
        </div>
        
        <div class="stats">
            📊 {current_date} | 共 {len(articles)} 條新聞，{len(by_category)} 個分類
        </div>
        
        <div class="content">
    """
    
    # Add articles by category
    for category in CATEGORIES.keys():
        if category in by_category:
            articles_in_cat = by_category[category]
            color = category_colors.get(category, '#667eea')
            
            html += f"""
            <div class="category">
                <div class="category-title" style="border-bottom-color: {color};">
                    {category}
                </div>
            """
            
            for idx, article in enumerate(articles_in_cat, 1):
                pub_date = article['publishedAt'][:10] if article['publishedAt'] else 'Unknown'
                source = article['source']
                
                html += f"""
                <div class="article" style="border-left-color: {color};">
                    <div class="article-title">{idx}. {article['title']}</div>
                    <div class="article-meta">
                        📰 {source} | 🕐 {pub_date}
                    </div>
                    <div class="article-description">
                        {article['description']}
                    </div>
                    <a href="{article['url']}" class="article-link">
                        🔗 查看原文 / Read Full Article →
                    </a>
                </div>
                """
            
            html += """
            </div>
            """
    
    html += """
        </div>
        
        <div class="footer">
            <p>✨ 自動生成的每日科技新聞摘要 | Automatically Generated Daily Tech News Digest</p>
            <p style="margin-top: 10px; color: #bbb;">
                本郵件由 GitHub Actions 自動發送 | Sent by GitHub Actions
            </p>
            <p class="unsubscribe">
                如需停用此服務，請編輯 GitHub Actions 工作流配置
            </p>
        </div>
    </div>
</body>
</html>
    """
    
    return html

def send_email(subject, html_content):
    """Send email via Gmail SMTP"""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = EMAIL_USER
        msg['To'] = RECIPIENT_EMAIL
        
        # Attach HTML content
        msg.attach(MIMEText(html_content, 'html', 'utf-8'))
        
        # Send via Gmail SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, RECIPIENT_EMAIL, msg.as_string())
        
        print(f"✅ Email sent successfully to {RECIPIENT_EMAIL}")
        return True
    
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def save_digest_to_file(articles):
    """Save digest to file in repository"""
    try:
        # Create digests directory
        Path('digests').mkdir(exist_ok=True)
        
        current_date = datetime.now().strftime('%Y-%m-%d')
        filename = f"digests/digest_{current_date}.json"
        
        # Save articles as JSON
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(articles, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Digest saved to {filename}")
        return True
    
    except Exception as e:
        print(f"❌ Error saving digest: {e}")
        return False

def main():
    """Main function"""
    print("🚀 Starting Daily Tech News Digest Collector")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check configuration
    if not all([NEWSAPI_KEY, EMAIL_USER, EMAIL_PASSWORD]):
        print("❌ Missing required environment variables!")
        print("   Required: NEWSAPI_KEY, EMAIL_USER, EMAIL_PASSWORD")
        return False
    
    # Fetch news
    print("\n📡 Fetching news...")
    articles = fetch_news()
    
    if not articles:
        print("⚠️ No articles found")
        return False
    
    # Process articles
    print(f"\n📝 Processing {len(articles)} articles...")
    processed = process_articles(articles)
    
    if not processed:
        print("⚠️ No articles after processing")
        return False
    
    print(f"✅ Selected {len(processed)} articles for digest")
    
    # Generate email
    print("\n🎨 Generating email...")
    current_date = datetime.now().strftime('%Y-%m-%d')
    subject = f"📰 每日科技新聞速報 - {current_date} | Daily Tech News Digest"
    html_content = generate_html_email(processed)
    
    # Send email
    print("\n📧 Sending email...")
    if send_email(subject, html_content):
        # Save digest
        save_digest_to_file(processed)
        print("\n✅ Daily digest completed successfully!")
        return True
    else:
        print("\n❌ Failed to send email")
        return False

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
