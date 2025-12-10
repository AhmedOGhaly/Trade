import streamlit as st
from modules.data_loader import load_data
from modules.data_cleaner import clean_data
from modules.analysis_engine import analyze_data
from modules.report_generator import generate_report

st.title("🔎 Trade Remedies – Import Analysis Tool")
st.write("تطبيق لتحليل الواردات لدعم تحقيقات المعالجات التجارية")

uploaded_file = st.file_uploader("ارفع ملف الواردات (CSV)", type="csv")

if uploaded_file:
    df = load_data(uploaded_file)
    st.subheader("📌 البيانات الأصلية")
    st.dataframe(df)

    df_clean = clean_data(df)
    st.subheader("📌 البيانات بعد التنظيف")
    st.dataframe(df_clean)

    results = analyze_data(df_clean)
    st.subheader("📌 نتائج التحليل")
    st.write(results)

    report = generate_report(results)
    st.download_button("📥 Download Report", report, file_name="analysis_report.txt")
