import streamlit as st
import seaborn as sns
import yfinance as yf
import plotly.express as px 
df=sns.load_dataset('iris')

st.title('APP 1')
st.write('Mi primera pagina')
name=st.text_input('Ingresa tu nombre')
if name:
    st.write(f"hola{name}")
st.dataframe(df)
nombre_del_activo = st.text_input("Ingresa el symbol (e.g., NVDA, BTC-USD)", "NVDA")
stock = yf.Ticker(nombre_del_activo)
df_stocks = stock.history(period="1y")
fig = px.line(df_stocks)
st.plotly_chart(fig)