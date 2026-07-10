from random import choice
from PIL import Image
import streamlit as st
import pandas as pd
st.set_page_config(#页面设置,需要写在import之下最上面
    page_title = "休伯利安",
    page_icon = "DLS.jpg",
    layout = "wide",
    menu_items = {
        "Get Help":"https://www.bh3.com/main ",
        "Report a bug":"https://m.miyoushe.com/bh3 ",
       "About":""" 
        补充美好能量:https://www.bilibili.com/video/BV1b44y1q7Cb

        开饭时间:https://b23.tv/KL7BNyd
        """})
if "logged_in" not in st.session_state:#初始化登录状态,默认False未登录状态
    st.session_state.logged_in = False
if not st.session_state.logged_in:
    accuss = st.text_input(
        label = "输入密钥:",
        max_chars = 100,
        placeholder = "Seele + Bronya",
        type = "password",
        key = "birthday")
    if st.button("登舰"):
        if accuss == "1018818":
            st.session_state.logged_in = True
        else:
                st.error("error,登舰失败----")
else: 
    page = st.sidebar.radio(
    "导航",
    ["首页","加入我们","获取更多", "补充美好能量", "开饭时间!"])
    if page == "首页":
        st.title("欢迎登舰~")
        st.subheader("已载入")
        st.divider()
        st.markdown(":blue-badge[Captain on the bridge]")#标记
        #st.badge("Captain on the bridge", color="blue")#标记
        st.caption("舰长已抵达舰桥")#注释
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
        st.markdown(":blue-badge[⬆️点击方块循环护肝的小曲----]")
        st.image(
            img,
            caption="正在工作-----",
            width="stretch",
            )
        st.video(r"HD1.mp4")#仅image自带caption
        st.caption("正在看海")
        st.logo(r"YY.jpg")#左上角logo
        txt=st.text_input(
        label = "正在寻找",
        value = "",
        max_chars = 100,
        placeholder = "(白希/黑希/Bro)",
        key = "sore")
        if txt:
            if txt == "白希":
                img1 = Image.open(r"BX1.jpg")
                st.image(
                img1,
                caption="你好呀,舰长~",
                width="stretch",
                )
            elif txt == "黑希":
                img2 = Image.open(r"HX1.jpg")
                st.image(
                img2,
                caption="找我有什么事吗,舰长?",
                width="stretch",
                )
            elif txt == "Bro":
                img3 = Image.open(r"YY1.jpg")
                st.image(
                img3,
                caption="舰长你深渊掉到第11名了",
                width="stretch",
                )
            else:
                st.write("什么都没有发生------")
        choice = st.radio(
            label = "现在要做什么呢?:",
            options = ["和Bronya玩游戏","和希儿们出去玩","扫甲板"],
            index = None,
            key = 1018,
            help = "发呆中-------",
            captions = ["Bronya正在等待","希儿们两眼放光","爱衣的肯定"])
        if choice == "和希儿们出去玩":
                col1,col2 = st.columns(2)#多图片并排
                with col1:
                        st.image("HX2.png",caption = "快跟上,舰长")
                with col2:
                        st.image("BX3.png",caption = "我们快出发吧~") 
        elif choice == "和Bronya玩游戏":
                img2 = Image.open(r"YY2.jpg")
                st.image(
                img2,
                caption="别楞着了,快拿着",
                width="stretch",
                )
        elif choice == "扫甲板":
                img3 = Image.open(r"AY.jpg")
                st.image(
                img3,
                caption="老板还真是勤奋呢~",
                width="stretch",
                )
        df = pd.DataFrame({
            "运行人":["重装小兔","Bronya"],
            "身份":["协同者","BOSS"]})
        st.dataframe(df)
    elif page == "加入我们":
        st.link_button("正在前往","https://www.bh3.com/main")
    elif page == "获取更多":
        st.link_button("即将掉入","https://m.miyoushe.com/bh3")
    elif page == "补充美好能量":
        st.link_button("正在补充----","https://www.bilibili.com/video/BV1b44y1q7Cb")
    elif page == "开饭时间!":
        st.link_button("#饭就要煮好了#","https://b23.tv/KL7BNyd")
