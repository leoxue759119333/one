from openai import OpenAI
import streamlit as st
import time

#asst_VAbeueJgrQ4nCBXsAXblrPix精神康复医院id
jingshenkangfu_id='asst_VAbeueJgrQ4nCBXsAXblrPix'
title_text='😬口袋心理专家😬'
welcome_text='欢迎来到口袋心理专家,你可以问我关于心理健康的问题，例如：有几个月不想说话，我是不是抑郁了？'
wait_prompt='等待投喂问题哦'

print('start--------------------------------------------------')
if 'threadid' not in st.session_state:
	st.session_state['threadid'] = ''
	print('set st.session_state["threadid"] = “”')

threadid=''
print('0')
print(threadid)
client = OpenAI(api_key='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')
print(client)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)
