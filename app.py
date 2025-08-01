from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.title("Lesson21: Streamlitを活用したWebアプリ開発")

st.write("##### 動作モード1: 健康に関するお悩み相談")
st.write("入力フォームに質問を入力し、「実行」ボタンを押すことで質問に回答します。")
st.write("##### 動作モード2: 子育てに関するお悩み相談")
st.write("入力フォームに質問を入力し、「実行」ボタンを押すことで質問に回答します。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["健康に関するお悩み相談", "子育てに関するお悩み相談"]
)

st.divider()

if selected_item == "健康に関するお悩み相談":
    input_message = st.text_input(label="健康に関する質問を入力してください。")
else:
    input_message = st.text_input(label="子育てに関する質問を入力してください。")

if st.button("実行"):
    st.divider()

    if input_message.strip():  # 入力が空白のみでないかチェック
        # 選択されたモードに応じてシステムメッセージを設定
        if selected_item == "健康に関するお悩み相談":
            system_content = "あなたは健康に関する専門家です。親身になって相談者の悩みを聞き、適切なアドバイスを提供してください。"
        else:
            system_content = "あなたは子育てに関する専門家です。親の立場を理解し、実践的で温かいアドバイスを提供してください。"
        
        # ローディング表示
        with st.spinner("回答を生成中..."):
            try:
                # メッセージを作成してLLMに送信
                messages = [
                    SystemMessage(content=system_content),
                    HumanMessage(content=input_message),
                ]

                result = llm(messages)
                
                # 回答を表示
                st.success("回答:")
                st.write(result.content)
                
            except Exception as e:
                st.error(f"エラーが発生しました: {str(e)}")
                st.info("しばらく時間をおいてから再度お試しください。")
    else:
        st.warning("質問を入力してください。")