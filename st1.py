from PIL import Image
import streamlit as st
import pandas as pd
st.title("已载入")
st.divider()
st.header("加载中...")
st.divider()
st.subheader("加载完成")
st.divider()
st.markdown(":blue-badge[Captain on the bridge]")#标记
#st.badge("Captain on the bridge", color="blue")#标记
st.caption("舰长已抵达舰桥")#注释
df = pd.DataFrame({
    "运行人":["重装小兔","Bronya"],
    "身份":["协同者","BOSS"]})
st.dataframe(df)
img = Image.open(r"XT.jpg")#绝对路径获取
click_js = """
 <script>
 setTimeout(()=>{
     let b = window.parent.document.querySelector('button');
     if(b) b.click();
 }, 300)
 </script>
 """#脚本,自动模拟点击
placeholder = st.empty()#把开始播放藏在按钮里
with placeholder:
     if st.button(""):
         st.audio(r"HOYO-MiX - Gion2.flac", loop=True, autoplay=True)
st.markdown(":blue-badge[----点击方块循环护肝的小曲----]")
st.image(
    img,
    caption="正在工作-----",
    width="stretch",
    )
st.video(r"HD1.mp4")#仅image自带caption
st.caption("正在看海")
st.logo(r"YY.jpg")#左上角logo
