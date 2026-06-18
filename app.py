import streamlit as st

st.set_page_config(page_title="商品攝影提示詞生成器", layout="wide")

st.title("📸 商品攝影專業提示詞生成器")

# 基礎上傳區
uploaded_file = st.file_uploader("上傳商品白底照/去背照", type=['jpg', 'png'])
ref_image = st.file_uploader("上傳參考圖片 (選填)", type=['jpg', 'png'])

# --- 第一階段：構圖與角度 ---
st.header("第一階段：構圖與角度")
col1, col2 = st.columns(2)

with col1:
    photo_type = st.radio("照片類型", ["情境照", "單品照", "局部特寫照"])
    if photo_type == "局部特寫照":
        focus_area = st.text_input("輸入特寫範圍")
    
    aspect_ratio = st.radio("照片比例", ["1:1", "4:3", "5:3", "16:9"])
    angle = st.select_slider("拍攝角度", options=["仰拍15度", "水平", "15度", "30度", "45度", "60度", "75度", "俯拍90度"])

with col2:
    has_model = st.radio("是否有模特兒", ["否", "是"], index=0)
    if has_model == "是":
        model_part = st.multiselect("模特兒呈現範圍", ["全身", "雙手", "單手", "臉部", "頭部", "肚子", "背", "手臂", "臉部肌膚", "側臉", "嘴唇"])
        model_action = st.text_area("人物動作或鏡頭描述")

# --- 第二階段：風格 ---
st.header("第二階段：情緒風格")
mood = st.multiselect("選擇影像情緒風格", 
    ["奢華", "高級", "樸素", "低調", "高調", "簡約", "乾淨", "都會女性", "輕奢", "輕盈", "清透", "務實親切", "可愛", "少女", "成熟", "知性", "性感"])

# --- 第三階段：光影 ---
st.header("第三階段：燈光設定")
light_col1, light_col2, light_col3 = st.columns(3)

with light_col1:
    lighting = st.radio("燈光", ["軟光", "硬光"])
with light_col2:
    color_temp = st.selectbox("色溫", ["3000K", "4000K", "5500K", "6500K"])
with light_col3:
    light_dir = st.selectbox("光源方向", ["側逆光", "頂側逆光", "側光", "頂側光", "順光", "側順光", "頂光"], index=1)
    dir_spec = st.radio("是否指定方向", ["無", "左", "右"], index=0)

# --- 第四階段：背景 ---
st.header("第四階段：背景設定")
bg_type = st.radio("背景類型", ["桌面+背景", "無間隙牆", "無背景牆桌面", "自訂材質描述"])

materials = ["石膏", "粉刷", "木紋", "金屬", "大理石", "岩石紋理", "絲絨", "布", "鏡面", "水面", "皮革", "美紋紙", "漸層純色"]

if bg_type == "桌面+背景":
    desk_mat = st.selectbox("桌面材質", materials)
    desk_color = st.color_picker("桌面顏色", "#FFFFFF")
    bg_mat = st.selectbox("背景材質", materials + ["窗簾"])
    bg_color = st.color_picker("背景顏色", "#FFFFFF")
elif bg_type == "無間隙牆":
    wall_mat = st.selectbox("無間隙牆材質", materials)
    wall_color = st.color_picker("牆面顏色", "#FFFFFF")
elif bg_type == "無背景牆桌面":
    desk_mat = st.selectbox("桌面材質", materials)
    desk_color = st.color_picker("桌面顏色", "#FFFFFF")
else:
    bg_desc = st.text_area("詳細描述背景材質")

props = st.radio("是否添加背景道具", ["否", "是", "依照參考圖"])
if props == "是":
    prop_desc = st.text_area("詳細描述背景物件")

# --- 生成提示詞 ---
if st.button("生成專業提示詞"):
    # 這裡加入您的 Prompt 生成邏輯
    prompt = f"Professional product photography, {photo_type}, {aspect_ratio}, {angle}, lighting: {lighting}, color temp: {color_temp}, light direction: {light_dir}...請依照所提供的商品圖片以及參考圖片（若有參考圖片）製作成一張極具擬真 超高畫值的8K商業攝影照片 並須嚴格遵守以上列出之條件"
    st.text_area("生成的 Prompt", prompt, height=200)
    st.button("複製提示詞")
