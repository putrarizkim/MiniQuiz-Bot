import streamlit as st

# Data Soal dan Jawaban (Topik: Teknologi & Blockchain, 20 Soal)

questions = [
    {"question": "Apa singkatan dari CPU?", "options": ["Central Process Unit", "Central Processing Unit", "Computer Processing Unit", "Control Processing Unit"], "answer": "Central Processing Unit"},
    {"question": "Manakah dari berikut ini yang merupakan sistem operasi?", "options": ["Python", "Windows", "HTML", "Photoshop"], "answer": "Windows"},
    {"question": "Bahasa pemrograman manakah yang umum digunakan untuk pengembangan web?", "options": ["Python", "Java", "JavaScript", "C++"], "answer": "JavaScript"},
    {"question": "Perangkat keras apa yang berfungsi menyimpan data secara permanen?", "options": ["RAM", "SSD", "Cache", "CPU"], "answer": "SSD"},
    {"question": "Apa kepanjangan dari URL dalam dunia internet?", "options": ["Universal Resource Location", "Uniform Resource Locator", "Unified Reference Link", "Uniform Route Locator"], "answer": "Uniform Resource Locator"},
    {"question": "Apa fungsi utama dari firewall dalam jaringan komputer?", "options": ["Meningkatkan kecepatan internet", "Memblokir virus dari perangkat", "Melindungi jaringan dari akses tidak sah", "Menyimpan data pengguna"], "answer": "Melindungi jaringan dari akses tidak sah"},
    {"question": "Teknologi manakah yang digunakan untuk menyimpan data di internet dan dapat diakses kapan saja?", "options": ["Cloud Computing", "Quantum Computing", "Edge Computing", "Blockchain"], "answer": "Cloud Computing"},
    {"question": "Apa nama alat input yang menggunakan gerakan jari di layar?", "options": ["Keyboard", "Touchpad", "Scanner", "Touchscreen"], "answer": "Touchscreen"},
    {"question": "Teknologi manakah yang menjadi dasar dari cryptocurrency seperti Bitcoin?", "options": ["Artificial Intelligence", "Cloud Storage", "Blockchain", "Machine Learning"], "answer": "Blockchain"},
    {"question": "Apa nama perusahaan yang mengembangkan sistem operasi Android?", "options": ["Apple", "Microsoft", "Google", "Samsung"], "answer": "Google"},
    {"question": "Apa fungsi utama dari RAM?", "options": ["Menyimpan data permanen", "Memproses data", "Menyimpan data sementara", "Mengelola perangkat lunak"], "answer": "Menyimpan data sementara"},
    {"question": "Manakah dari berikut ini merupakan contoh perangkat IoT?", "options": ["Laptop", "Smartwatch", "Keyboard", "Printer"], "answer": "Smartwatch"},
    {"question": "Teknologi AI sering digunakan dalam...?", "options": ["Pengolahan kata", "Prediksi cuaca", "Pemutar musik", "Scanner"], "answer": "Prediksi cuaca"},
    {"question": "Protokol internet manakah yang digunakan untuk mentransfer halaman web?", "options": ["FTP", "HTTP", "SMTP", "IP"], "answer": "HTTP"},
    {"question": "Perangkat keras manakah yang digunakan untuk menampilkan output visual?", "options": ["Monitor", "Keyboard", "Router", "Modem"], "answer": "Monitor"},
    {"question": "Apa nama dari kecerdasan buatan buatan OpenAI?", "options": ["Alexa", "Siri", "Google Assistant", "ChatGPT"], "answer": "ChatGPT"},
    {"question": "Manakah dari ini merupakan web browser?", "options": ["Chrome", "Ubuntu", "MySQL", "Photoshop"], "answer": "Chrome"},
    {"question": "Perangkat lunak pengolah angka adalah...?", "options": ["Word", "Excel", "PowerPoint", "Photoshop"], "answer": "Excel"},
    {"question": "Blockchain menyimpan data dalam bentuk...?", "options": ["List", "Array", "Block", "Tree"], "answer": "Block"},
    {"question": "Untuk apa VPN digunakan?", "options": ["Mempercepat internet", "Mengamankan koneksi dan menyembunyikan lokasi", "Menghapus virus", "Menghubungkan printer"], "answer": "Mengamankan koneksi dan menyembunyikan lokasi"},
]


if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answers = [None] * len(questions)
    st.session_state.finished = False

def next_question():
    if st.session_state.index < len(questions) - 1:
        st.session_state.index += 1

def prev_question():
    if st.session_state.index > 0:
        st.session_state.index -= 1

def submit():
    st.session_state.finished = True
    st.session_state.score = sum([
        1 for i, q in enumerate(questions)
        if st.session_state.answers[i] == q["answer"]
    ])

def restart():
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answers = [None] * len(questions)
    st.session_state.finished = False
    st.experimental_rerun()

st.markdown("""
    <style>
        .stApp {
            background-color: #000000;
            color: #ffffff;
        }
        h1, h2, h3, h4, h5, h6, p, div {
            color: #ffffff !important;
        }
        .stButton>button {
            background-color: #00ff99;
            color: black;
            font-weight: bold;
            border-radius: 8px;
            padding: 8px 16px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #00cc77;
            color: white;
        }
        .stRadio>div {
            background-color: #111111;
            padding: 10px;
            border-radius: 10px;
        }
        .stRadio label {
            color: #ffffff;
        }
        .stMarkdown {
            color: #ffffff !important;
        }
        .css-1offfwp {  /* Untuk pertanyaan dan caption */
            color: #ffffff !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center;'>
        <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='300'>
        <p style='font-size:20px; color:#00ff99; font-weight:bold;'>Good Luck! 🎉</p>
    </div>
""", unsafe_allow_html=True)

st.title("🎯 Mini Quiz")
st.caption("Jawab Semua Pertanyaan Seakurat Mungkin!")


if not st.session_state.finished:
    q = questions[st.session_state.index]
    st.subheader(f"Soal {st.session_state.index + 1} dari {len(questions)}")
    st.write(q["question"])

    st.session_state.answers[st.session_state.index] = st.radio(
        "Pilih jawaban:",
        q["options"],
        index=q["options"].index(st.session_state.answers[st.session_state.index]) if st.session_state.answers[st.session_state.index] else 0,
        key=st.session_state.index
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.session_state.index > 0:
            st.button("⬅️ Sebelumnya", on_click=prev_question)

    with col2:
        if st.session_state.index < len(questions) - 1:
            st.button("➡️ Selanjutnya", on_click=next_question)

    with col3:
        if st.session_state.index == len(questions) - 1:
            st.button("✅ Selesai", on_click=submit)
else:
    st.balloons()
    st.success(f"🎉 Skor akhir kamu: {st.session_state.score} dari {len(questions)}")
    st.write("Jawaban kamu:")
    for i, q in enumerate(questions):
        is_correct = st.session_state.answers[i] == q["answer"]
        result = "✅ Benar" if is_correct else "❌ Salah"
        st.markdown(f"**{i+1}. {q['question']}**")
        st.write(f"Jawaban kamu: {st.session_state.answers[i]} | {result}")
        st.write(f"Jawaban benar: {q['answer']}")
        st.markdown("---")


