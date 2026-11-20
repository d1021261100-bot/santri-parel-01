"""
Tugas Besar - Aplikasi Perhitungan Biaya Laundry Kiloan
Nama : Farel Ihza Mahendra
NIM  : D1021261113

Jalankan dengan:
    pip install streamlit
    streamlit run Tugasbesar_FarelIhzaMahendra_D1021261113.py
"""

import streamlit as st

# ----------------------------------------------------------------------------
# KONFIGURASI HALAMAN
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Laundry Kiloan | Farel Ihza Mahendra",
    page_icon="🧺",
    layout="centered",
)

NAMA = "Farel Ihza Mahendra"
NIM_SAYA = "D1021261113"

# ----------------------------------------------------------------------------
# CSS / DESAIN
# ----------------------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Poppins', sans-serif;
}
.stApp {
    background: radial-gradient(circle at 15% 10%, #1e3a8a 0%, transparent 45%),
                radial-gradient(circle at 90% 20%, #7c3aed 0%, transparent 40%),
                radial-gradient(circle at 50% 100%, #0891b2 0%, transparent 50%),
                #0b1020;
    background-attachment: fixed;
}
header[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 2rem; max-width: 820px; }

/* HERO */
.hero {
    background: linear-gradient(135deg, rgba(56,189,248,.25), rgba(168,85,247,.25));
    border: 1px solid rgba(255,255,255,.18);
    backdrop-filter: blur(14px);
    border-radius: 24px;
    padding: 28px 30px;
    margin-bottom: 22px;
    box-shadow: 0 20px 50px rgba(0,0,0,.35);
    display: flex; align-items: center; gap: 20px;
}
.hero .icon {
    font-size: 54px; width: 90px; height: 90px; border-radius: 22px;
    display: flex; align-items: center; justify-content: center;
    background: linear-gradient(135deg, #22d3ee, #6366f1);
    box-shadow: 0 10px 30px rgba(34,211,238,.45);
    flex-shrink: 0;
}
.hero h1 {
    margin: 0; font-size: 30px; font-weight: 800; color: #fff; line-height: 1.15;
}
.hero p { margin: 4px 0 10px; color: #cbd5e1; font-size: 14px; }
.badge {
    display: inline-block; padding: 5px 14px; border-radius: 999px;
    font-size: 12.5px; font-weight: 600; margin-right: 8px; margin-top: 4px;
    background: rgba(255,255,255,.12); color: #e0f2fe;
    border: 1px solid rgba(255,255,255,.22);
}

/* KARTU */
.card-title {
    color: #f8fafc; font-weight: 700; font-size: 18px; margin: 6px 0 2px;
}
.card-sub { color: #94a3b8; font-size: 13px; margin-bottom: 8px; }

/* INPUT */
div[data-testid="stTextInput"] label p {
    color: #e2e8f0 !important; font-weight: 600; font-size: 14px;
}
div[data-testid="stTextInput"] input {
    background: rgba(15,23,42,.75) !important;
    color: #fff !important;
    border: 1.5px solid rgba(148,163,184,.35) !important;
    border-radius: 12px !important;
    padding: 12px 14px !important;
    font-size: 16px !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #22d3ee !important;
    box-shadow: 0 0 0 3px rgba(34,211,238,.25) !important;
}

/* TOMBOL */
div[data-testid="stButton"] > button {
    width: 100%; border-radius: 12px; font-weight: 700; font-size: 15px;
    padding: 11px 0; border: none; transition: all .2s ease;
}
div[data-testid="stColumn"]:nth-of-type(1) div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #06b6d4, #6366f1); color: #fff;
    box-shadow: 0 8px 22px rgba(99,102,241,.45);
}
div[data-testid="stColumn"]:nth-of-type(2) div[data-testid="stButton"] > button {
    background: rgba(255,255,255,.10); color: #e2e8f0;
    border: 1.5px solid rgba(255,255,255,.25);
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px); filter: brightness(1.12);
}

/* HASIL */
.section-h {
    color: #f8fafc; font-weight: 700; font-size: 18px; margin: 22px 0 12px;
}
.grid {
    display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px;
}
.tile {
    border-radius: 18px; padding: 16px 18px; color: #fff;
    border: 1px solid rgba(255,255,255,.18);
    box-shadow: 0 10px 28px rgba(0,0,0,.28);
}
.tile .lbl { font-size: 12.5px; opacity: .85; font-weight: 500; }
.tile .val { font-size: 21px; font-weight: 800; margin-top: 2px; }
.t1 { background: linear-gradient(135deg, #0ea5e9, #2563eb); }
.t2 { background: linear-gradient(135deg, #a855f7, #7c3aed); }
.t3 { background: linear-gradient(135deg, #10b981, #047857); }
.t4 { background: linear-gradient(135deg, #f59e0b, #ea580c); }
.total {
    margin-top: 14px; border-radius: 20px; padding: 20px 24px;
    background: linear-gradient(135deg, #84cc16, #22c55e, #14b8a6);
    color: #052e16; display: flex; justify-content: space-between;
    align-items: center;
    box-shadow: 0 14px 34px rgba(34,197,94,.45);
}
.total .lbl { font-weight: 700; font-size: 16px; }
.total .val { font-weight: 800; font-size: 30px; }

.empty {
    text-align: center; color: #94a3b8; padding: 26px 10px; font-size: 14px;
    border: 1.5px dashed rgba(148,163,184,.35); border-radius: 18px;
    margin-top: 18px;
}
.footer {
    text-align: center; color: #94a3b8; font-size: 12.5px; margin-top: 30px;
}
div[data-testid="stAlert"] { border-radius: 14px; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# FUNGSI BANTU
# ----------------------------------------------------------------------------
def rupiah(angka: int) -> str:
    """Format angka ke Rupiah, contoh: 80750 -> Rp 80.750"""
    return "Rp " + f"{int(angka):,}".replace(",", ".")


def nim_valid(nim: str) -> bool:
    """NIM valid jika terdiri dari tepat 10 digit angka (0-9)."""
    return len(nim) == 10 and all(c in "0123456789" for c in nim)


def hitung_digit_genap(nim: str) -> int:
    """Banyak digit genap (0,2,4,6,8) pada seluruh NIM."""
    return sum(1 for c in nim if int(c) % 2 == 0)


def reset_form():
    """Mengosongkan kotak isian dan hasil."""
    st.session_state["input_nim"] = ""
    st.session_state["input_berat"] = ""
    st.session_state["hasil"] = None
    st.session_state["error"] = None


# ----------------------------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------------------------
for key, default in {
    "input_nim": "",
    "input_berat": "",
    "hasil": None,
    "error": None,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


# ----------------------------------------------------------------------------
# HEADER
# ----------------------------------------------------------------------------
st.markdown(
    f"""
<div class="hero">
  <div class="icon">🧺</div>
  <div>
    <h1>Laundry Kiloan</h1>
    <p>Aplikasi perhitungan biaya laundry cepat &amp; akurat</p>
    <span class="badge">👤 {NAMA}</span>
    <span class="badge">🎓 NIM {NIM_SAYA}</span>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# FORM INPUT
# ----------------------------------------------------------------------------
st.markdown('<div class="card-title">📝 Data Pelanggan</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="card-sub">Masukkan NIM (10 digit) dan berat cucian (bilangan bulat, kg).</div>',
    unsafe_allow_html=True,
)

nim_input = st.text_input(
    "NIM (10 digit)", key="input_nim", placeholder="contoh: 2411001347", max_chars=30
)
berat_input = st.text_input(
    "Berat Cucian (kg)", key="input_berat", placeholder="contoh: 10"
)

col1, col2 = st.columns(2)
with col1:
    tombol_hitung = st.button("🧮 Hitung", use_container_width=True)
with col2:
    st.button("🔄 Reset", use_container_width=True, on_click=reset_form)

# ----------------------------------------------------------------------------
# PROSES PERHITUNGAN
# ----------------------------------------------------------------------------
if tombol_hitung:
    nim = nim_input.strip()
    berat_txt = berat_input.strip()
    st.session_state["hasil"] = None
    st.session_state["error"] = None

    # 1) Validasi NIM
    if not nim_valid(nim):
        st.session_state["error"] = (
            "NIM tidak valid! NIM harus terdiri dari tepat 10 digit angka."
        )
    else:
        # 2) Validasi berat (bilangan bulat > 0)
        try:
            berat = int(berat_txt)
        except ValueError:
            berat = None

        if berat is None:
            st.session_state["error"] = (
                "Berat cucian tidak valid! Masukkan bilangan bulat (contoh: 4)."
            )
        elif berat <= 0:
            st.session_state["error"] = "Berat cucian harus lebih dari 0."
        else:
            # 3) Perhitungan
            digit_terakhir = int(nim[-1])
            tarif = 5000 + digit_terakhir * 500
            digit_genap = hitung_digit_genap(nim)
            persen_diskon = digit_genap  # digit genap x 1 %
            biaya_normal = berat * tarif
            potongan = persen_diskon * biaya_normal // 100
            total = biaya_normal - potongan

            st.session_state["hasil"] = {
                "nim": nim,
                "berat": berat,
                "tarif": tarif,
                "digit_genap": digit_genap,
                "diskon": persen_diskon,
                "normal": biaya_normal,
                "potongan": potongan,
                "total": total,
            }

# ----------------------------------------------------------------------------
# TAMPILAN HASIL / ERROR
# ----------------------------------------------------------------------------
if st.session_state["error"]:
    st.error("⚠️ " + st.session_state["error"])

h = st.session_state["hasil"]
if h:
    st.markdown('<div class="section-h">📊 Rincian Perhitungan</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
<div class="grid">
  <div class="tile t1"><div class="lbl">🏷️ Tarif per kg</div><div class="val">{rupiah(h['tarif'])}</div></div>
  <div class="tile t2"><div class="lbl">％ Persen Diskon ({h['digit_genap']} digit genap)</div><div class="val">{h['diskon']} %</div></div>
  <div class="tile t3"><div class="lbl">🧾 Biaya Normal ({h['berat']} kg)</div><div class="val">{rupiah(h['normal'])}</div></div>
  <div class="tile t4"><div class="lbl">✂️ Potongan</div><div class="val">{rupiah(h['potongan'])}</div></div>
</div>
<div class="total"><span class="lbl">💰 Total Bayar</span><span class="val">{rupiah(h['total'])}</span></div>
""",
        unsafe_allow_html=True,
    )
elif not st.session_state["error"]:
    st.markdown(
        '<div class="empty">✨ Hasil perhitungan akan tampil di sini setelah kamu menekan tombol <b>Hitung</b>.</div>',
        unsafe_allow_html=True,
    )

# ----------------------------------------------------------------------------
# SIDEBAR: RUMUS
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"### 👤 {NAMA}")
    st.markdown(f"**NIM:** {NIM_SAYA}")
    st.divider()
    st.markdown("### 📐 Rumus")
    st.markdown(
        """
- Tarif per kg = Rp 5.000 + (digit terakhir NIM × Rp 500)
- Persen diskon = jumlah digit genap pada NIM × 1 %
- Biaya normal = berat × tarif per kg
- Potongan = persen diskon × biaya normal
- Total bayar = biaya normal − potongan
"""
    )

st.markdown(
    f'<div class="footer">Dibuat dengan ❤️ menggunakan Python &amp; Streamlit • {NAMA} ({NIM_SAYA})</div>',
    unsafe_allow_html=True,
)
