#!/usr/bin/env python
from binance.um_futures import UMFutures
import time
import streamlit as st

key1 = 'Huj5XUXd7NXAi7ARFHbPVX3Hq4A0zWCaDoZWhvZno4ZZ9sgj9Mu04HkwS1OcOzVS'
secret1 = 'O6jfnwHSvksaEGncV0D8G5zlVCl6IrxiDfZXrtsoFELvJRBk2Zq2VsMm1fIfOvfx'

um_futures_client = UMFutures(key=key1, secret=secret1)

precio = um_futures_client.ticker_price("BTCUSDT")

aa=float(precio['price'])
st.write(aa)
while 1==1:
    time.sleep(10)
    precio = um_futures_client.ticker_price("BTCUSDT")
    bb=float(precio['price'])
    st.write(bb)
    st.write("porcentaje = ",round(((bb/aa)-1)*100,2)," %")
    aa=bb
