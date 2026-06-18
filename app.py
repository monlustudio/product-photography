import streamlit as st

st.set_page_config(page_title="商品攝影題詞器", layout="wide")

st.title("📸 商品攝影專用提示詞生成器")

# --- 階段一：基本設定 ---
st.header("第一階段：攝影設定")
col1, col2, col3 = st.columns(3)

with col1:
    photo_type = st.radio("照片類型", ["情境照", "單品照", "局部特寫照"])
    if photo_type == "局部特寫照":
        focus_range = st.text_input("輸入特寫範圍")
        
with col2:
    aspect_ratio = st.selectbox("照片比例", ["1:1", "4:3", "5:3", "16:9"])
    angle = st.select_slider("拍攝角度", options=["仰拍15度", "水平", "15度", "30度", "45度", "60度", "75度", "俯拍90度"])

with col3:
    has_model = st.radio("是否有模特兒", ["否", "是"], index=0)
    model_parts = []
    model_action = ""
    if has_model == "是":
        model_parts = st.multiselect("模特兒範圍", ["全身", "雙手", "單手", "臉部", "頭部", "肚子", "背", "手臂", "臉部肌膚", "側臉", "嘴唇"])
        model_action = st.text_input("人物動作或鏡頭描述")

# --- 階段二：風格 ---
st.header("第二階段：風格設定")
styles = st.multiselect("情緒風格", ["奢華", "高級", "樸素", "低調", "高調", "簡約", "乾淨", "都會女性", "輕奢", "輕盈", "清透", "務實親切", "可愛", "少女", "成熟", "知性", "性感"])

# --- 階段三：燈光 ---
st.header("第三階段：燈光設定")
col_l1, col_l2, col_l3, col_l4 = st.columns(4)
light_type = col_l1.radio("燈光", ["軟光", "硬光"])
color_temp = col_l2.selectbox("色溫", ["3000K", "4000K", "5500K", "6500K"])
light_dir = col_l3.selectbox("光源方向", ["側逆光", "頂側逆光", "側光", "頂徹光", "順光", "側順光", "頂光"], index=1)
light_pos = col_l4.radio("是否指定方向", ["無", "左", "右"], index=0)

# --- 階段四：背景 ---
st.header("第四階段：背景設定")
bg_option = st.radio("背景類型", ["1. 桌面與背景組合", "2. 背景材質描述", "3. 是否添加背景道具"])

materials = ["石膏", "粉刷", "木紋", "金屬", "大理石", "岩石紋理", "絲絨", "布", "鏡面", "水面", "皮革", "美紋紙", "漸層純色"]
bg_prompt = ""

if bg_option == "1. 桌面與背景組合":
    sub_type = st.radio("組合方式", ["桌面+背景", "無間隙牆", "無背景牆桌面"])
    if sub_type == "桌面+背景":
        desk_mat = st.selectbox("桌面材質", materials)
        desk_col = st.color_picker("桌面顏色", "#ffffff")
        bg_mat = st.selectbox("背景材質", materials + ["窗簾"])
        bg_col = st.color_picker("背景顏色", "#ffffff")
        bg_prompt = f"Background: {desk_mat} desk in {desk_col}, {bg_mat} backdrop in {bg_col}"
    elif sub_type == "無間隙牆":
        wall_mat = st.selectbox("牆面材質", materials)
        wall_col = st.color_picker("牆面顏色", "#ffffff")
        bg_prompt = f"Seamless backdrop, {wall_mat} texture, color {wall_col}"
    else:
        desk_mat = st.selectbox("桌面材質", materials)
        desk_col = st.color_picker("桌面顏色", "#ffffff")
        bg_prompt = f"Table top, {desk_mat} texture, color {desk_col}"

elif bg_option == "2. 背景材質描述":
    bg_prompt = st.text_area("請描述背景材質與環境")
else:
    bg_prompt = "Follow reference image style"

# --- 生成 ---
if st.button("生成提示詞"):
    prompt = f"請依照所提供的商品圖片以及參考圖片（若有參考圖片）製作成一張極具擬真 超高畫值的8K商業攝影照片 並須嚴格遵守以下列出之條件,Product photography, {photo_type}, {aspect_ratio}, {angle}, {light_type}, {color_temp}, {light_dir} light from {light_pos} side. "
    if has_model == "是":
        prompt += f"Model involved: {', '.join(model_parts)}, Action: {model_action}. "
    prompt += f"Style: {', '.join(styles)}. Background: {bg_prompt}."
    
    st.success("生成的提示詞：")
    st.code(prompt, language="text")
