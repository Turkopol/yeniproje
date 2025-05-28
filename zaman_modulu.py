import pandas as pd
import plotly.express as px
import networkx as nx
import streamlit as st
from utils import calculate_critical_path

def zaman_modulu():
    st.header("🕒 Zaman Planlama Modülü (Gantt & Kritik Yol)")

    st.subheader("📌 Görev Bilgilerini Girin")
    num_tasks = st.number_input("Toplam görev sayısı", min_value=1, max_value=20, step=1)

    tasks = []
    for i in range(int(num_tasks)):
        st.markdown(f"### Görev {i+1}")
        name = st.text_input(f"Görev Adı {i+1}", key=f"name_{i}")
        start_date = st.date_input(f"Başlangıç Tarihi {i+1}", key=f"start_{i}")
        duration = st.number_input(f"Süre (gün) {i+1}", min_value=1, step=1, key=f"duration_{i}")
        dependency = st.text_input(f"Bağlı olduğu görev(ler) (Görev adı, yoksa boş bırakın) {i+1}", key=f"dep_{i}")
        tasks.append({
            "Görev": name,
            "Başlangıç": start_date,
            "Süre": duration,
            "Bitiş": start_date + pd.Timedelta(days=duration),
            "Bağımlılık": dependency
        })

    df = pd.DataFrame(tasks)

    if not df.empty:
        st.subheader("📊 Gantt Şeması")
        gantt_df = df.copy()
        gantt_df["Başlangıç"] = pd.to_datetime(gantt_df["Başlangıç"])
        gantt_df["Bitiş"] = pd.to_datetime(gantt_df["Bitiş"])
        fig = px.timeline(gantt_df, x_start="Başlangıç", x_end="Bitiş", y="Görev", color="Görev")
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("🧩 Kritik Yol Hesaplaması")
        try:
            critical_path, duration = calculate_critical_path(df)
            st.success(f"Kritik Yol: {' → '.join(critical_path)} (Toplam Süre: {duration} gün)")
        except Exception as e:
            st.error(f"Hata: Kritik yol hesaplanamadı. {e}")
