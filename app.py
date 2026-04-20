import streamlit as st
import yfinance as yf

st.title("📈 2026 Stock Analyst (Debug Mode)")

ticker = st.text_input("Enter Ticker (Use CAPITAL letters, e.g., AAPL):", "AAPL")

if st.button("Run Research"):
    with st.spinner('Fetching data from Yahoo Finance...'):
        try:
            stock = yf.Ticker(ticker)
            # This is the "Safety Net" check
            info = stock.info
            
            if not info or 'currentPrice' not in info:
                st.error(f"Could not find data for {ticker}. Please check the symbol.")
            else:
                # Display the data we found
                st.success(f"Connected to {ticker}!")
                
                price = info.get('currentPrice', 'N/A')
                pe = info.get('forwardPE', 'N/A')
                margin = info.get('profitMargins', 0) * 100
                
                st.metric("Current Price", f"${price}")
                st.write(f"**P/E Ratio:** {pe}")
                st.write(f"**Profit Margin:** {margin:.2f}%")
                
                # Simple Verdict logic
                if pe != 'N/A' and pe < 25 and margin > 15:
                    st.success("✅ Verdict: BUY")
                else:
                    st.warning("🟡 Verdict: HOLD / No clear signal")

        except Exception as e:
            st.error(f"An error occurred: {e}")