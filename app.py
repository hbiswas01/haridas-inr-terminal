import streamlit as st
import pandas as pd

# --- ১. টার্মিনাল পেজ সেটআপ (Zerodha Style) ---
st.set_page_config(page_title="Haridas NSE Terminal", layout="wide", initial_sidebar_state="expanded")

# --- ২. Custom CSS (ZeroDha Kite Dark Theme Look) ---
st.markdown("""
    <style>
        /* মেইন ব্যাকগ্রাউন্ড এবং টেক্সট কালার */
        .stApp {
            background-color: #121212;
            color: #dfdfdf;
        }
        /* সাইডবার বা ওয়াচলিস্ট এরিয়া */
        [data-testid="stSidebar"] {
            background-color: #1e1e1e !important;
            border-right: 1px solid #2b2b2b;
        }
        /* টপ হেডার হাইড করা */
        header {visibility: hidden;}
        
        /* কাস্টম ওয়াচলিস্ট আইটেম ডিজাইন */
        .watchlist-row {
            display: flex;
            justify-content: space-between;
            padding: 10px 5px;
            border-bottom: 1px solid #2b2b2b;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            cursor: pointer;
        }
        .watchlist-row:hover { background-color: #2b2b2b; }
        .symbol { font-size: 14px; font-weight: 600; }
        .price { font-size: 14px; font-weight: 600; }
        .percent-up { color: #4caf50; font-size: 12px; } /* Zerodha Green */
        .percent-down { color: #e53935; font-size: 12px; } /* Zerodha Red */
        
        /* SMC অ্যালার্ট বক্স ডিজাইন */
        .smc-box {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #2b2b2b;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- ৩. সাইডবার: ওয়াচলিস্ট এবং রুটিন স্ক্যানার ---
with st.sidebar:
    st.markdown("### ⏱️ Scanner & Watchlist")
    
    # তোমার ট্রেডিং রুটিন
    routine = st.selectbox(
        "Select Timeframe Scan:",
        ["09:15 AM (Opening 2% Move)", "09:20 AM (Short Covering + OI)", "03:30 PM (Closing 5% Move)", "Historical (3 Days)"]
    )
    
    st.markdown("<hr style='margin: 10px 0; border-color: #2b2b2b;'>", unsafe_allow_html=True)
    
    # ডেমো লাইভ ওয়াচলিস্ট (জিরোদা স্টাইল)
    st.markdown("""
        <div class="watchlist-row">
            <div><div class="symbol">NIFTY 50</div><div class="percent-down">-1.27%</div></div>
            <div style="text-align: right;"><div class="price">24,450.45</div><div class="percent-down">-315.45</div></div>
        </div>
        <div class="watchlist-row">
            <div><div class="symbol">RELIANCE</div><div class="percent-up">+2.10%</div></div>
            <div style="text-align: right;"><div class="price">2,950.00</div><div class="percent-up">+60.50</div></div>
        </div>
        <div class="watchlist-row">
            <div><div class="symbol">HDFCBANK</div><div class="percent-down">-1.50%</div></div>
            <div style="text-align: right;"><div class="price">1,450.20</div><div class="percent-down">-22.10</div></div>
        </div>
        <div class="watchlist-row">
            <div><div class="symbol">TCS</div><div class="percent-up">+0.80%</div></div>
            <div style="text-align: right;"><div class="price">4,100.00</div><div class="percent-up">+32.00</div></div>
        </div>
    """, unsafe_allow_html=True)


# --- ৪. মেইন এরিয়া: ড্যাশবোর্ড এবং SMC লজিক ---
st.markdown("## 📈 HARIDAS NSE TERMINAL")

# জিরোদার মতো ন্যাভিগেশন ট্যাব
tab1, tab2, tab3 = st.tabs(["Dashboard & Charts", "SMC & Momentum Logic", "Positions"])

with tab1:
    st.markdown("#### 📊 Live Chart Area (NIFTY 50)")
    # চার্টের জায়গা (পরে এখানে TradingView বা Plotly লাইভ চার্ট বসাব)
    st.info("এখানে তোমার লাইভ ক্যান্ডেলস্টিক চার্ট বসবে।")
    
    # স্ক্যানারের রেজাল্ট এখানে দেখাবে
    st.write(f"**Current Scan Result for:** {routine}")
    # একটি ডেমো ডেটাফ্রেম
    df = pd.DataFrame({
        'Symbol': ['RELIANCE', 'TCS'],
        'LTP': [2950, 4100],
        'SMC Setup': ['Bullish FVG Hit', 'Order Block Mitigated'],
        'Action': ['Buy CE', 'Wait']
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

with tab2:
    st.markdown("#### ⚙️ Smart Money & Momentum Status")
    
    # তোমার আগের ছবির ড্যাশবোর্ডের মতো এনার্জি এবং বায়াস
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="smc-box">
                <h3 style="margin:0; color:#e53935;">Bearish</h3>
                <p style="color:#9e9e9e; margin:0;">Current Trend Phase</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="smc-box">
                <h3 style="margin:0; color:#ffb300;">17% (Fading)</h3>
                <p style="color:#9e9e9e; margin:0;">Momentum Energy</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="smc-box">
                <h3 style="margin:0; color:#4caf50;">24,306.05</h3>
                <p style="color:#9e9e9e; margin:0;">Next Liquidity Target</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.warning("🚨 Alert: Price is approaching Bearish Order Block at 24,658. Look for Short entries on rejection.")

with tab3:
    st.markdown("#### 💼 Open Positions")
    st.write("তোমার কোনো রানিং ট্রেড থাকলে এখানে দেখাবে।")
