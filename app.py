
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 1. Tao du lieu sinh vien
data = {
    "Ho ten": [
        "Nguyen Van An", "Tran Thi Binh",
        "Le Van Cuong", "Pham Thi Dung",
        "Hoang Van Em", "Vo Thi Giang",
        "Dang Van Hung", "Bui Thi Lan",
        "Do Van Minh", "Nguyen Thi Nga"
    ],
    "Chuyen can": [9, 8, 7, 10, 6, 8, 9, 7, 5, 10],
    "Giua ky": [8, 7, 6, 9, 5, 8, 7, 6, 4, 9],
    "Cuoi ky": [9, 8, 5, 9, 4, 7, 8, 6, 3, 10]
}

df = pd.DataFrame(data)

# 2. Tinh diem tong ket
df["Tong ket"] = (
    df["Chuyen can"] * 0.2
    + df["Giua ky"] * 0.3
    + df["Cuoi ky"] * 0.5
)

# 3. Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep loai"] = df["Tong ket"].apply(xep_loai)

# 4. Hien thi bang diem
st.subheader("1. Bang diem sinh vien")
st.dataframe(df.round(2), use_container_width=True)

# 5. Thong ke
st.subheader("2. Thong ke ket qua")

diem_tb = df["Tong ket"].mean()
cao_nhat = df.loc[df["Tong ket"].idxmax()]
thap_nhat = df.loc[df["Tong ket"].idxmin()]
so_sv_dat = int((df["Tong ket"] >= 5).sum())

c1, c2, c3 = st.columns(3)

c1.metric("Diem trung binh lop", round(diem_tb, 2))
c2.metric("So sinh vien dat", so_sv_dat)
c3.metric("Tong so sinh vien", len(df))

st.write(
    "Sinh vien co diem cao nhat:",
    cao_nhat["Ho ten"],
    "-", round(cao_nhat["Tong ket"], 2)
)

st.write(
    "Sinh vien co diem thap nhat:",
    thap_nhat["Ho ten"],
    "-", round(thap_nhat["Tong ket"], 2)
)

# 6. Chon sinh vien de tra cuu
st.subheader("3. Tra cuu sinh vien")

ten = st.selectbox("Chon sinh vien", df["Ho ten"])
sv = df[df["Ho ten"] == ten].iloc[0]

st.write("Ho ten:", sv["Ho ten"])
st.write("Chuyen can:", sv["Chuyen can"])
st.write("Giua ky:", sv["Giua ky"])
st.write("Cuoi ky:", sv["Cuoi ky"])
st.write("Tong ket:", round(sv["Tong ket"], 2))
st.write("Xep loai:", sv["Xep loai"])

# 7. Ve bieu do cot
st.subheader("4. Bieu do diem tong ket")

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df["Ho ten"], df["Tong ket"])

ax.set_xlabel("Ho ten sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", rotation=45)

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 8. Thong tin nguoi tao
st.divider()
st.caption("Nguoi tao: Pham Ngoc Tri | STT: 50")
