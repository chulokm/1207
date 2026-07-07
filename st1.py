from PIL import Image
import streamlit as st
st.title("已载入")
st.divider()
st.header("加载中...")
st.divider()
st.subheader("加载完成")
st.divider()
st.markdown(":blue-badge[Captain on the bridge]")#标记
#st.badge("Captain on the bridge", color="blue")#标记
st.caption("舰长已抵达舰桥")#注释
img = Image.open(r"D:\图片\lvo\XT.jpg")#绝对路径获取
st.image(
    img,
    caption="正在工作-----",
    width=700,
    )
