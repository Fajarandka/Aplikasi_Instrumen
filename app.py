import streamlit as st

st.title('Kalkulator sederhana :sunglasses:')
st.write('Ini adalah aplikasi untuk menemukan jati diri anda')

number1 = st.number_input("Masukkan angka pertama", 0)
number2 = st.number_input("Masukkan angka kedua", 0)

operation = st.selectbox("Pilih operasi:", ["Tambah", "Kurang", "Kali", "Bagi"])

if st.button("Hitung"):
    if operation == "Tambah":
        result = number1 + number2
    elif operation == "Kurang":
        result = number1 - number2
    elif operation == "Kali":
        result = number1 * number2
    elif operation == "Bagi":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Tidak bisa membagi dengan nol!"

    st.write("Hasil:", result)

import streamlit as st

# Daftar unsur golongan A dan massa atom relatifnya
elements_group_a = {
    'H': {'name': 'Hidrogen', 'atomic_mass': 1.008},
    'Li': {'name': 'Litium', 'atomic_mass': 6.94},
    'Na': {'name': 'Natrium', 'atomic_mass': 22.99},
    'K': {'name': 'Kalium', 'atomic_mass': 39.10},
    'Rb': {'name': 'Rubidium', 'atomic_mass': 85.47},
    'Cs': {'name': 'Cesium', 'atomic_mass': 132.91},
    'Fr': {'name': 'Fransium', 'atomic_mass': 223},  # Massa atom relatif tidak stabil
    'Be': {'name': 'Berilium', 'atomic_mass': 9.0122},
    'Mg': {'name': 'Magnesium', 'atomic_mass': 24.305},
    'Ca': {'name': 'Kalsium', 'atomic_mass': 40.078},
    'Sr': {'name': 'Strontium', 'atomic_mass': 87.62},
    'Ba': {'name': 'Barium', 'atomic_mass': 137.33},
    'Ra': {'name': 'Radium', 'atomic_mass': 226},  # Massa atom relatif tidak stabil
    'B': {'name': 'Boron', 'atomic_mass': 10.81},
    'C': {'name': 'Karbon', 'atomic_mass': 12.011},
    'N': {'name': 'Nitrogen', 'atomic_mass': 14.007},
    'O': {'name': 'Oksigen', 'atomic_mass': 15.999},
    'F': {'name': 'Fluorin', 'atomic_mass': 18.998},
    'Ne': {'name': 'Neon', 'atomic_mass': 20.180},
}

st.title('Massa Atom Relatif Unsur Golongan A :sunglasses:')
st.write('Pilih unsur golongan A untuk mengetahui massa atom relatifnya.')

# Pilih unsur dari dropdown
element_symbol = st.selectbox("Pilih simbol unsur:", list(elements_group_a.keys()))

if element_symbol:
    element_info = elements_group_a[element_symbol]
    st.write(f"Nama: {element_info['name']}")
    st.write(f"Massa Atom Relatif: {element_info['atomic_mass']} g/mol")

import streamlit as st

# Judul aplikasi
st.title("Deteksi Bilangan Ganjil atau Genap")

# Input bilangan dari pengguna
number = st.number_input("Masukkan sebuah bilangan", format="%f")

# Fungsi untuk menentukan apakah bilangan itu ganjil atau genap
def check_odd_even(number):
    if number % 2 == 0:
        return "Bilangan tersebut adalah Genap"
    else:
        return "Bilangan tersebut adalah Ganjil"

# Tombol untuk mendeteksi bilangan ganjil atau genap
if st.button("Deteksi"):
    result = check_odd_even(number)
    st.write(result)