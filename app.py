
import streamlit as st
import numpy as np

st.set_page_config(page_title="📊 Finansal Hesaplama Modülü", layout="wide")
st.title("📊 Finansal Hesaplama Modülü")

secenek = st.sidebar.selectbox(
    "Hesaplama Türü Seçin",
    (
        "Mevduat Faizi",
        "Kredi Taksit",
        "Hazine Bonosu",
        "Tahvil (Kuponlu)",
        "Finansman Bonosu (Basit Faizli)",
        "Finansman Bonosu (İskontolu)",
        "Forward Kur"
    )
)

# 1. Mevduat Faizi Hesaplama
if secenek == "Mevduat Faizi":
    st.header("🏦 Mevduat Faizi Hesaplama")
    anapara = st.number_input("Anapara (₺)", value=100_000)
    faiz_orani = st.number_input("Yıllık Faiz Oranı (%)", value=30.0)
    vade = st.number_input("Vade (gün)", value=90)
    net_getiri = anapara * (faiz_orani / 100) * (vade / 365)
    st.success(f"Net Getiri: ₺{net_getiri:,.2f}")

# 2. Kredi Taksit Hesaplama
elif secenek == "Kredi Taksit":
    st.header("🏠 Kredi Taksit Hesaplama")
    kredi_tutari = st.number_input("Kredi Tutarı (₺)", value=250_000)
    aylik_faiz = st.number_input("Aylık Faiz Oranı (%)", value=2.5)
    vade_ay = st.number_input("Vade (ay)", value=36)
    oran = aylik_faiz / 100
    taksit = kredi_tutari * (oran * (1 + oran)**vade_ay) / ((1 + oran)**vade_ay - 1)
    st.success(f"Aylık Taksit: ₺{taksit:,.2f}")

# 3. Hazine Bonosu
elif secenek == "Hazine Bonosu":
    st.header("💰 Hazine Bonosu Getiri Hesaplama")
    nominal = st.number_input("Nominal Değer (₺)", value=100_000)
    iskontolu_fiyat = st.number_input("İskontolu Satış Fiyatı (₺)", value=95_000)
    vade_gun = st.number_input("Vade (gün)", value=180)
    getiri = ((nominal - iskontolu_fiyat) / iskontolu_fiyat) * (365 / vade_gun) * 100
    st.success(f"Yıllık Basit Getiri: %{getiri:.2f}")

# 4. Tahvil Hesaplama
elif secenek == "Tahvil (Kuponlu)":
    st.header("📄 Tahvil Getiri Hesaplama")
    nominal = st.number_input("Nominal Değer", value=100_000)
    kupon_orani = st.number_input("Kupon Faizi (%)", value=20.0)
    piyasa_fiyati = st.number_input("Piyasa Fiyatı", value=98_000)
    kupon_getiri = nominal * (kupon_orani / 100)
    toplam_getiri = kupon_getiri + (nominal - piyasa_fiyati)
    st.success(f"Yıllık Kupon: ₺{kupon_getiri:,.2f}, Toplam Getiri: ₺{toplam_getiri:,.2f}")

# 5. Finansman Bonosu (Basit)
elif secenek == "Finansman Bonosu (Basit Faizli)":
    st.header("📉 Finansman Bonosu - Basit Faiz")
    nominal = st.number_input("Nominal Değer", value=100_000)
    faiz = st.number_input("Basit Faiz Oranı (%)", value=30.0)
    vade_gun = st.number_input("Vade (gün)", value=90)
    bugunku_fiyat = nominal / (1 + (faiz / 100) * (vade_gun / 365))
    st.success(f"Satış Fiyatı (İskontolu): ₺{bugunku_fiyat:,.2f}")

# 6. Finansman Bonosu (İskontolu)
elif secenek == "Finansman Bonosu (İskontolu)":
    st.header("🧾 Finansman Bonosu - İskontolu")
    nominal = st.number_input("Nominal Değer", value=100_000)
    satis_fiyat = st.number_input("Satış Fiyatı", value=95_000)
    vade_gun = st.number_input("Vade (gün)", value=180)
    net_getiri = ((nominal - satis_fiyat) / satis_fiyat) * (365 / vade_gun) * 100
    st.success(f"Yıllık Basit Getiri: %{net_getiri:.2f}")

# 7. Forward Kur Hesaplama
elif secenek == "Forward Kur":
    st.header("📈 Forward Kur Hesaplama")
    spot_kur = st.number_input("Spot Kur", value=32.00, format="%.4f")
    i_tl = st.number_input("TL Faiz Oranı (%)", value=45.0)
    i_usd = st.number_input("USD Faiz Oranı (%)", value=5.0)
    vade_gun = st.number_input("Vade (gün)", value=90)
    forward_kur = spot_kur * ((1 + (i_tl / 100) * (vade_gun / 360)) / (1 + (i_usd / 100) * (vade_gun / 360)))
    fark = forward_kur - spot_kur
    yorum = "Primli" if fark > 0 else "İskontolu" if fark < 0 else "Nötr"
    st.success(f"Forward Kur: ₺{forward_kur:.4f} ({yorum})")
