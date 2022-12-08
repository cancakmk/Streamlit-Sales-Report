from ReadXLSX import ReadXLSX
import streamlit as st


table_width=700

if st.session_state["xlsxFile"] != None:
    #Date Information

    xlsx = ReadXLSX(st.session_state["my_input"])
    st.header("📅 "+xlsx.dateInfos[0] + " - " + xlsx.dateInfos[1])
    st.subheader(xlsx.dateInfos[2] + " Günlük Veri")

    df = xlsx.df
    # sidebar
    st.sidebar.header("Filtrele:")
    kategori = st.sidebar.multiselect("Kategori Seçiniz:", options=df["Kategori"].unique(),
                                      default=df["Kategori"].unique())
    urun =st.sidebar.multiselect("Ürün Seçiniz:", options=df["ÜrünAdı"].unique())

    df_selection = df.query("Kategori ==@kategori | ÜrünAdı==@urun")

    # Filtered Df
    st.dataframe(df_selection.style.format(precision=0),width=table_width)

    # Category Df
    st.write("Kategori Bazlı Veriler")
    st.dataframe(xlsx.getSumByCategory().style.format(precision=0),width=table_width)

    # Category Df by Percent
    st.write("Kategori Bazlı Veriler (%)")
    st.dataframe(xlsx.getPercentByCategory().style.format(precision=2),width=table_width)
else:
    st.warning("Lütfen Anasayfa'dan Dosya Seçiniz: ")
