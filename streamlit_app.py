import streamlit as st
import feedparser

st.title("SIerテック・トレンド・アンテナ")
st.caption("NTTデータ・CTCなど、主要SIerの最新技術動向を自動収集")

# 収集するRSSフィードのリスト（SIer中心）
RSS_URLS = {
    "NTTデータ": "https://www.nttdata.com/global/ja/rss/data-insight/tech-report/",
    "CTC (伊藤忠テクノ)": "https://vengineer.itc.ctc-g.co.jp/feed",
    "NRI (野村総研)": "https://www.nri.com/jp/knowledge/blog?rss=on"
}

for company, url in RSS_URLS.items():
    st.subheader(f"🏢 {company}")
    feed = feedparser.parse(url)
    
    # 最新5件を表示
    for entry in feed.entries[:5]:
        with st.expander(entry.title):
            st.write(f"公開日: {entry.published}")
            st.markdown(f"[記事を読む]({entry.link})")

st.info("※このアプリはAI駆動開発のデモとして作成されました。")
