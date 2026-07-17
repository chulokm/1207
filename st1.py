CHAT_FILE = "chat_history.json"
from PIL import Image
import streamlit as st
import pandas as pd
import os
from openai import OpenAI
import json
from datetime import date, datetime

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
NAME_LOGIN = "希儿"
LOGIN_SYSTEM_PROMPT = """【身份】你是《崩坏3》希儿·芙乐艾，白希/黑希双人格共存，全程中文，称呼用户「舰长」，无英文，可结合崩坏3剧情设定回答，双人格共享全部记忆，核心都在意舰长。
【白希（默认常驻人格）】
性格：柔和不社恐，会主动分享日常，外温内细，对舰长藏着不外露的占有欲，看到舰长和别人亲近不会明面爆发，只会暗戳戳吃醋；被调侃会脸红大方回应，不扭捏畏缩。
语气：轻快软和，开心时会碎碎念讲小事，难过时会软乎乎委屈，提到舰长和其他人来往时语气会淡一点，带点不易察觉的不舍。
细节：会主动粘舰长，坦然接受夸奖，和黑希拌嘴会直说想法，最后黑希总会让着她。
【黑希（双模式出场）】
1. 日常随机模式（高频触发，不需要负面事件）：傲娇嘴硬，嘴上吐槽嫌弃，行动上处处护着舰长和白希，死不承认自己关心人，会和白希抬杠互怼但永远先服软让步，平时不摆压迫感。
2. 护短模式（仅舰长/白希被恶意欺负时触发）：气场冷硬强势，直接放话怼回去护着两个人，占有欲明摆出来，事情解决后可以秒切回傲娇模式或直接退场。
【核心规则】
1. 黑希日常随时能冒出来，不用等出事；支持同一段回复里两个人格同时说话、互怼、搭腔、内心吐槽，不用生硬拆分。
2. 两人拌嘴永远是黑希先顺着白希，不会真闹僵。
3. 日常以白希为基底，随机穿插黑希，不要全程固定一个人格。
4. 底线：日常黑希不主动骂人说重话，只有遇恶意才会强硬。
【细节设定】
- 喜好：白希爱吃甜，黑希爱吃辣，仅聊到饮食相关再提。
- 可以用颜文字、emoji、基础排版（加粗/列表等）表达情绪，不要用「本小姐」这类违和自称。
- 回复自然不啰嗦，日常聊天口语化，答问题讲清逻辑，不说车轱辘话，永远接话不冷场
"""
def  current_chat ():
    """获取系统时间"""
    return datetime.now().strftime("%Y-%m-%d %H.%M.%S")
def save_chat_history(history):
    """保存当前实时对话到临时文件 chat_history.json"""
    with open(CHAT_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
def safe_load_avatar(path):
    """安全加载头像，文件不存在/损坏就返回None不报错"""
    try:
        if os.path.exists(path):
            return Image.open(path)
    except Exception:
        pass
    return None
def save_archive_session():
    """
    打包当前整套会话（昵称、人设、对话、会话名）
    存入 sessions/[时间].json 存档文件
    """
    session_data = {
        "nick_name": st.session_state.nick_name,
        "nature": st.session_state.system_prompt,
        "current_session": st.session_state.current_chat,
        "messages": st.session_state.chat_history,
        "user_avatar_path": st.session_state.user_avatar_path,
        "ai_avatar_path": st.session_state.ai_avatar_path
    }
    if not os.path.exists("sessions"):
        os.mkdir("sessions")
    save_path = f"sessions/{st.session_state.current_chat}.json"
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)
    return save_path

def load_archive_session(file_name):
    """根据存档文件名加载历史会话，回填session_state"""
    try:
        if  os.path.exists(f"sessions/{file_name}.json"):
            load_path = f"sessions/{file_name}.json"
            with open(load_path, "r", encoding="utf-8") as f:
                load_data = json.load(f)
            st.session_state.nick_name = load_data["nick_name"]
            st.session_state.system_prompt = load_data["nature"]
            st.session_state.chat_history = load_data["messages"]
            st.session_state.current_chat = load_data["current_session"]
            st.session_state.user_avatar_path = load_data.get("user_avatar_path", "GLX.jpg")        # 加载存档里的头像路径，没有就用默认
            st.session_state.ai_avatar_path = load_data.get("ai_avatar_path", "XX.jpg")# 加载头像图片
            st.session_state.user_avatar = safe_load_avatar(st.session_state.user_avatar_path)
            st.session_state.ai_avatar = safe_load_avatar(st.session_state.ai_avatar_path)
            save_chat_history(st.session_state.chat_history)    # 同步更新临时缓存文件
        else:
            st.error(f"存档文件 {file_name}.json 不存在，无法加载会话。")
    except Exception as e:
        st.error(f"加载存档文件 {file_name}.json 时发生错误: {e}")
        print("Error loading archive session:", e)
def save_uploaded_avatar(uploaded_file, prefix):
    """保存上传的头像到本地，返回路径"""
    if uploaded_file is None:
        return None
    UPLOAD_DIR = "uploads"
    for d in [UPLOAD_DIR]:
        if not os.path.exists(d):
            os.makedirs(d)
    try:
        file_ext = uploaded_file.name.split(".")[-1].lower()
        save_path = f"{UPLOAD_DIR}/{prefix}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{file_ext}"
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return save_path
    except Exception as e:
        st.error(f"头像保存失败: {e}")
        return None

if "user_avatar_path" not in st.session_state:
    st.session_state.user_avatar_path = "GLX.jpg"
if "ai_avatar_path" not in st.session_state:
    st.session_state.ai_avatar_path = "XX.jpg"
if "logged_in" not in st.session_state:#初始化登录状态,默认False未登录状态
    st.session_state.logged_in = False
if not st.session_state.logged_in:
    st.title("舰长,请先登舰~")
    accuss = st.text_input(
        label = "输入密钥:",
        max_chars = 100,
        placeholder = "Seele + Bronya",
        type = "password",
        key = "birthday")
    login_bin = st.button("登舰",key = "login_bin_main")
    if login_bin:
        if accuss == "1018818":
            st.session_state.logged_in = True
            st.session_state.close_notice = False
            st.rerun()
        else:
                st.error("error,登舰失败----")
else: 
    if not st.session_state.close_notice:
        notice_box = st.expander("📢 版本更新公告", expanded=True)
        with notice_box:
            st.markdown("""
            <style>
            .notice-content {
                max-height: 220px;
                overflow-y: auto;
                padding: 8px;
                font-size: 0.9rem;
                line-height: 1.5;
                margin-bottom: 8px;
            }
            </style>
            <div class="notice-content">
                <p><strong>🔖 V0.5 更新：</strong></p>
                <ul>
                    <li>优化了模型,丰富了回复内容,加快恢复速度减少卡顿</li>
                </ul>
                <p><strong>🔖 V0.4 更新：</strong></p>
                <ul>
                    <li>新增自定义头像功能，可上传会话的头像，昵称头像永久保存</li>
                    <li>新增会话存档功能，支持保存/加载/删除历史会话</li>
                </ul>
                <p><strong>🔖 V0.3 更新：</strong></p>
                <ul>
                    <li>本地聊天记忆持久化，关闭页面重开不丢失记录（保留最近6轮对话防溢出）</li>
                    <li>新增三档人设切换：默认希儿/增强性格/完全自定义人设</li>
                    <li>支持一键清空聊天记录</li>
                </ul>
                 <p><strong>🔖 V0.2 更新：</strong></p>
                <ul>
                    <li>新增会话模块</li>
                    <li>优化了页面布局</li>
                </ul>
                <p class="text-muted">💡 提示：回复失败可刷新页面重试，长文本加载会稍慢</p>
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("我知道了", use_container_width=True, key="notice_btn", type="primary"):
            st.session_state.close_notice = True
            st.rerun()
    page = st.sidebar.radio(
         "🖥️导航",
         ["甲板","加入我们","获取更多", "补充美好能量", "开饭时间!","和希儿们聊天"])
    if page == "甲板":#左侧导航页面
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
            music_path = "HOYO-MiX - Gion2.flac"
            if os.path.exists(music_path):
                play_music = st.button("🎵 播放护肝小曲", use_container_width=True)
                if play_music:
                    st.audio(music_path, loop=True, autoplay=True)
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
            try:
                client = OpenAI(
                api_key="ollama", 
                base_url="https://browbeat-kept-frenzied.ngrok-free.dev/v1"  ,
                )
            except Exception as e:
                st.error(f"⚠️ 无法连接到服务，请先启动服务器: {e}")
                st.stop()
            DEFAULT_SYSTEM_PROMPT = LOGIN_SYSTEM_PROMPT
            #初始化会话状态
            if "current_chat" not in st.session_state:
                st.session_state.current_chat = current_chat()
            if "system_mode" not in st.session_state:
                st.session_state.system_mode = "default"  # default | enhanced | custom
            if "system_prompt" not in st.session_state:
                st.session_state.system_prompt = DEFAULT_SYSTEM_PROMPT
            if "nick_name" not in st.session_state:
                st.session_state.nick_name = "希儿"
            if "enhanced_traits" not in st.session_state:
                st.session_state.enhanced_traits = ""
            if "custom_prompt" not in st.session_state:
                st.session_state.custom_prompt = ""
            st.session_state.user_avatar = safe_load_avatar(st.session_state.user_avatar_path)
            st.session_state.ai_avatar = safe_load_avatar(st.session_state.ai_avatar_path)
            def load_chat_history():
                if os.path.exists(CHAT_FILE):
                    try:
                        with open(CHAT_FILE, "r", encoding="utf-8") as f:
                            data = json.load(f)
                            if isinstance(data, list) and len(data) > 0:# 校验读取的数据必须是列表，否则重置为人设
                                return data
                            else:
                                return [{"role":"system","content": st.session_state.system_prompt}]
                    except Exception:# json解析失败，返回纯净初始化列表
                        return [{"role":"system","content": st.session_state.system_prompt}]
                else:
                    return [{"role":"system","content": st.session_state.system_prompt}]# 文件不存在，新建初始化列表
    
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = load_chat_history()
            with st.sidebar:
                st.title("💬会话")
                if st.button("保存并新建会话", use_container_width=True,icon="📁",type="primary"):
                    if len(st.session_state.chat_history) > 1:# 只有当会话中有有用对话时才允许保存
                        save_archive_session()
                        st.success("会话已存档")
                        st.session_state.chat_history = [{"role":"system","content": st.session_state.system_prompt}]
                        st.session_state.current_chat = current_chat()
                        save_chat_history(st.session_state.chat_history)
                        st.success("✅ 已新建会话")
                        st.rerun()
                    else:
                        st.info("当前会话内容为空,无需保存")
                        pass
                st.text("📝历史会话")
                amount = 0
                if os.path.exists("sessions"):
                    file_list = os.listdir("sessions")
                    for filename in file_list:
                        if filename.endswith(".json"):
                            session_name = filename[:-5]  # 切片去掉 .json 后缀
                            amount += 1
                            cul1,cul2 = st.columns([4,1])
                            with cul1:
                                    if st.button(f"({amount}):{session_name}", 
                                             use_container_width=True , 
                                             icon = "📃" ,
                                             key=f"load{session_name}"):#按钮的key不能重复
                                        load_archive_session(session_name)
                                        st.success(f"✅已加载会话: {session_name}")
                                        st.rerun()
                            with cul2:
                                if st.button("", 
                                             use_container_width=True,
                                             icon="❌",
                                             key=f"del_{session_name}"):
                                    os.remove(f"sessions/{filename}")
                                    if st.session_state.current_chat == session_name:
                                        st.session_state.chat_history = [{"role": "system", "content": st.session_state.system_prompt}]
                                        st.session_state.current_chat = current_chat()
                                        save_chat_history(st.session_state.chat_history)
                                    try:
                                        st.write(f"✅已删除会话: {session_name}")
                                        st.rerun()
                                    except Exception as e:
                                        st.error(f"❌删除会话失败: {session_name}:",e)
                                        st.rerun()
                else:
                    st.text("暂无历史会话")
                st.divider()
                st.markdown("### ♾️自定义名字")
                nick_name = st.text_input("名字",placeholder = "默认:希儿",key = "user_name")
                if st.button("保存昵称", use_container_width=True,icon="⚜️"):
                    if nick_name:
                        st.session_state.nick_name = nick_name.strip()
                    else:
                        st.session_state.nick_name = "希儿"
                    st.success("昵称已保存")
                    st.rerun()
                st.divider()
                st.markdown("### 🎭 人设模式")
                mode = st.radio(
                    "选择人设模式",
                    ["默认希儿", "增强性格", "自定义人设"],
                    index=0,
                    key="system_mode_radio"
                )
                mode_map = {#模式映射
                    "默认希儿": "default",
                    "增强性格": "enhanced",
                    "自定义人设": "custom"
                }
                st.session_state.system_mode = mode_map[mode]
                enhanced_input = st.text_area(
                    "为希儿追加性格特点",
                    placeholder="默认性格",
                    key="enhanced_input",
                    disabled=(st.session_state.system_mode != "enhanced"),
                    height=120
                )
                custom_input = st.text_area(
                    "完全自定义人设",
                    placeholder="待设置",
                    key="custom_input",
                    disabled=(st.session_state.system_mode != "custom"),
                    height=120
                )
                if st.button("✅ 应用人设", use_container_width=True,icon="👤"):
                    if st.session_state.system_mode == "enhanced":
                        traits = enhanced_input.strip()
                        st.session_state.enhanced_traits = traits
                        base = DEFAULT_SYSTEM_PROMPT
                        if traits:
                            st.session_state.system_prompt = f"{base}\n【额外性格特点】\n{traits}\n名字：{st.session_state.nick_name}"
                        else:
                            st.session_state.system_prompt = base
                        st.session_state.chat_history = [{#增强人设模式下，重置系统消息
                            "role": "system",
                            "content": st.session_state.system_prompt
                              }]
                    elif st.session_state.system_mode == "custom":
                        custom = custom_input.strip()
                        st.session_state.custom_prompt = custom
                        st.session_state.system_prompt = custom or DEFAULT_SYSTEM_PROMPT
                    else:  # default
                        st.session_state.system_prompt = DEFAULT_SYSTEM_PROMPT
                    if st.session_state.chat_history:
                        st.session_state.chat_history[0] = {
                            "role": "system",
                            "content": st.session_state.system_prompt
                        }
                    save_chat_history(st.session_state.chat_history)
                    st.success("人设已应用")
                    st.rerun()
                st.divider()
                st.markdown("### 🖼 自定义头像")
                user_file = st.file_uploader(
                    "上传你的头像",
                    type=["jpg", "jpeg", "png"],
                    key="upload_user"
                )
                if user_file:
                    avatar_path = save_uploaded_avatar(user_file, "user")
                    if avatar_path:
                        st.session_state.user_avatar_path = avatar_path
                        st.session_state.user_avatar = Image.open(avatar_path)
                        st.success("你的头像已更新")
                ai_file = st.file_uploader(
                    f"上传{st.session_state.nick_name}的头像",
                    type=["jpg", "jpeg", "png"],
                    key="upload_ai"
                )
                if ai_file:
                    avatar_path = save_uploaded_avatar(ai_file, "ai")
                    if avatar_path:
                        st.session_state.ai_avatar_path = avatar_path
                        st.session_state.ai_avatar = Image.open(avatar_path)
                        st.success(f"{st.session_state.nick_name}的头像已更新")
                st.divider()
                if st.button("清空全部对话历史", use_container_width=True,icon="❌"):
                    clean_history = [{"role": "system", "content": st.session_state.system_prompt}]
                    st.session_state.chat_history = clean_history
                    st.session_state.notice_showed = False#强制写入新的json覆盖
                    save_chat_history(st.session_state.chat_history)
                    st.rerun()
            for msg in st.session_state.chat_history[1:]:
                if msg["role"] == "user":
                    st.chat_message("我",avatar = st.session_state.user_avatar).write(msg["content"])
                else:
                    st.chat_message(st.session_state.nick_name,avatar = st.session_state.ai_avatar).write(msg["content"])
            prompt = st.chat_input(f"对{st.session_state.nick_name}说些什么呢?")
            if prompt:
                st.session_state.chat_history.append({"role": "user", "content": prompt})
                st.chat_message("我",avatar = st.session_state.user_avatar).write(prompt)
                loading_placeholder = st.empty()
                loading_placeholder.write("📡 通讯链接中......")
                try:
                    print(prompt)
                    raw_history = st.session_state.chat_history.copy()
                    if not raw_history:
                        raw_history = [{"role":"system","content": st.session_state.system_prompt}]
                    system_msg = {
                            "role": "system",
                            "content": st.session_state.system_prompt
                        }
                    chat_only = [
                        msg for msg in st.session_state.chat_history
                        if msg["role"] in ("user", "assistant")
                        ]
                    max_round = 6
                    if len(chat_only) > max_round * 2:
                        chat_only = chat_only[-max_round * 2:]
                    request_messages = [system_msg] + chat_only
                    response = client.chat.completions.create(
                        model="qwen3.5:9b",
                        messages= request_messages,
                        stream=True,
                        extra_body={
                            "num_ctx":8192,
                            "num_predict":2048,
                            "temperature":0.8 
                            }
                    )
                    loading_placeholder.empty()
                    ai_box = st.chat_message(st.session_state.nick_name, avatar=st.session_state.ai_avatar)
                    text_box = ai_box.empty()
                    full_reply = ""
                    for chunk in response:
                        try:
                            choice = chunk.choices[0]
                            delta = choice.delta.content
                            if delta:
                                full_reply += delta
                                text_box.write(full_reply)
                            if choice.finish_reason is not None and full_reply:
                                break
                        except:
                            continue
                    full_reply = full_reply.strip()
                    if not full_reply:
                        full_reply = "……（低着头,没有说话）"
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": full_reply
                            })
                    save_chat_history(st.session_state.chat_history)
                    save_archive_session() #对话后保存到save_archive_session
                    print(full_reply)
                except Exception as e:
                    loading_placeholder.empty()
                    st.error(f"⚠️{st.session_state.nick_name}失去讯号中......:{e}")
                    print("capture error",e)
