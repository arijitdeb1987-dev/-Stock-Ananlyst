import streamlit as st
import yfinance as yf

st.title("📈 iPad Stock Analyst 2026")

ticker = st.text_input("Enter Ticker:", "AAPL")

if st.button("Run Research"):
    data = yf.Ticker(ticker).info
    pe = data.get('forwardPE', 0)
    margin = data.get('profitMargins', 0) * 100
    
    st.metric("Price", f"${data.get('currentPrice')}")
    st.write(f"P/E Ratio: {pe:.2f}")
    st.write(f"Profit Margin: {margin:.1f}%")

    if pe < 25 and margin > 15:
        st.success("✅ BUY SIGNAL")
    else:
        st.warning("🟡 HOLD/WAIT")