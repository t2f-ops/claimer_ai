import streamlit as st
from google import genai

API_KEY = st.secrets["API_KEY"]
client = genai.Client(api_key=API_KEY)


st.set_page_config(
    page_title="クレイマーAI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("クレイマーAI")
st.write("我々クレイマー財団は、世界を変える力を持っています。")
st.write("金の亡者が蔓延る現代、我々は消費者に寄り添い悪質な業者を処分します。")

with st.container():
    target_name = st.text_input("ターゲットの名前を入力してください", placeholder="例：お名前.com")
    details = st.text_area("詳細", placeholder="入力してください")   

    genarate_button = st.button("生成")

if genarate_button:
    if not target_name or not details:
        st.error("ターゲット名と理由を入力してください")
    else:
        with st.spinner("生成中..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=f"あなたは消費者保護の専門家です。{target_name}の{details}という問題に対し、消費者契約法を引用しつつ、冷徹にユーザーのクレームを代弁した最強のメール文面を最高400字以内作ってください。"
            )
        
            st.markdown("---")
            st.subheader("✅ 生成された抗議文テンプレート")
            st.info("以下の文面をコピーして、サービスの問い合わせ窓口やメールにそのまま貼り付けてください。")
            
            st.code(response.text, language="text")
            st.markdown("---")
            st.write("💡 **このツールが役に立ちましたか？**")
            st.write("このツールを使うことが役立つと思ったら、[Github](https://github.com/creamer-ai/creamer-ai)へお願いします。")
