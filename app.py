import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dữ liệu mẫu 10 sinh viên
data = {
    'Ho_va_ten': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyen_can': [8.0, 9.0, 7.5, 9.5, 8.0, 6.0, 9.0, 7.0, 7.5, 9.5],
    'Giua_ky': [7.5, 8.0, 6.5, 9.0, 7.0, 6.5, 8.5, 7.5, 7.0, 9.0],
    'Cuoi_ky': [8.0, 8.5, 6.0, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.0]
}
df = pd.DataFrame(data)

# Tính toán điểm tổng kết (20% Chuyên cần + 30% Giữa kỳ + 50% Cuối kỳ)
df['Tong_ket'] = (0.2 * df['Chuyen_can']) + (0.3 * df['Giua_ky']) + (0.5 * df['Cuoi_ky'])
df['Tong_ket'] = df['Tong_ket'].round(2)

# Hàm xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5: 
        return 'Giỏi'
    elif diem >= 7.0: 
        return 'Khá'
    elif diem >= 5.0: 
        return 'Trung bình'
    else: 
        return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# Giao diện Web App Streamlit
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("1. Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)

st.subheader("2. Thống kê chung")
dtb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

st.write(f"- **Điểm trung bình của lớp:** {dtb_lop:.2f}")
st.write(f"- **Sinh viên cao điểm nhất:** {sv_max['Ho_va_ten']} ({sv_max['Tong_ket']} điểm)")
st.write(f"- **Sinh viên thấp điểm nhất:** {sv_min['Ho_va_ten']} ({sv_min['Tong_ket']} điểm)")
st.write(f"- **Số sinh viên đạt (>= 5.0):** {so_sv_dat}")

st.subheader("3. Tra cứu thông tin theo sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Ho_va_ten'])
student_info = df[df['Ho_va_ten'] == selected_student].iloc[0]

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Chuyên cần", student_info['Chuyen_can'])
col2.metric("Giữa kỳ", student_info['Giua_ky'])
col3.metric("Cuối kỳ", student_info['Cuoi_ky'])
col4.metric("Tổng kết", student_info['Tong_ket'])
col5.metric("Xếp loại", student_info['Xep_loai'])

st.subheader("4. Biểu đồ điểm tổng kết của lớp")
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(df['Ho_va_ten'], df['Tong_ket'], color='cornflowerblue')
ax.set_xlabel('Điểm tổng kết')
ax.set_ylabel('Sinh viên')
ax.set_xlim(0, 10)
ax.invert_yaxis()
st.pyplot(fig)

# Thông tin người tạo ở cuối trang
st.markdown("---")
st.markdown("<p style='font-size: small; color: gray;'>Người tạo: [Phạm Đăng Quốc Huy] - MSSV: [046208009248]</p>", unsafe_allow_html=True)

