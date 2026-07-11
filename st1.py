from random import choice
from PIL import Image
import streamlit as st
import pandas as pd
import os
from openai import OpenAI

st.set_page_config(#页面设置,需要写在import之下最上面
    page_title = "休伯利安",
    page_icon = "DLS.jpg",
    layout = "wide",
    initial_sidebar_state="expanded",
    menu_items = {
        "Get Help":"https://www.bh3.com/main ",
        "Report a bug":"https://m.miyoushe.com/bh3 ",
       "About":""" 
        补充美好能量:https://www.bilibili.com/video/BV1b44y1q7Cb

        开饭时间:https://b23.tv/KL7BNyd
        """})
st.write("",unsafe_allow_html = True)
st.markdown(
        """
        <style>
        .stApp {
            background-image: url("图片/lvo/BX4.jpg");
            background-size: cover;
            background-position:center;
            background-repeat:no-repeat;
            background-attachment:fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
        )
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
        ["首页","加入我们","获取更多", "补充美好能量", "开饭时间!","和希儿们聊天"])
        if page == "首页":#左侧导航页面
            st.title("欢迎登舰~")
            st.subheader("已载入")
          #  st.divider()
          #  st.header("加载中...")
           # st.divider()
           # st.subheader("加载完成")
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
                captions = ["Bronya正在等待","希儿两眼放光","爱衣的肯定"])
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
        elif page == "和希儿们聊天":
            client = OpenAI(
            api_key="ollama", 
            base_url="https://browbeat-kept-frenzied.ngrok-free.dev/v1"  ,
            timeout = 120)
            system_prompt = """
"""
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = [{"role": "system", "content": system_prompt}]
            prompt = st.chat_input("说些什么呢?")
            if prompt:
                st.chat_message("我").write(prompt)
                try:
                    response =  client.chat.completions.create(
                        model="qwen3.5:9b",
                        messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt},
                        ],
                        timeout = 120,
                        stream=True)
                    with st.spinner("......"):
                        placeholder =st.empty()
                        full_text = ""
                        for chunk in response:
                            if chunk.choices[0].delta.content:
                                full_text += chunk.choices[0].delta.content
                                placeholder.write(full_text)
                    ai_reply = response.choices[0].message.content
                    print("-----结果:",ai_reply)
                    st.chat_message("希儿").write(ai_reply)
                except Exception as e:
                    st.error(f"希儿失去讯号中......:{e}")
            for msg in st.session_state.chat_history[1:]:
                if msg["role"] == "user":
                    st.chat_message("我").write(msg["content"])
                else:
                    st.chat_message("希儿").write(msg["content"])
