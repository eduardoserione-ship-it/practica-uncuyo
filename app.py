import streamlit as st
import random
import time
import math

# Configuración de la interfaz
st.set_page_config(page_title="MathMicro UNCUYO", layout="centered")
st.title("⚡ MathMicro - Entrenamiento Intensivo")

# Menú lateral / superior para elegir el tema
modulo = st.selectbox("Elige el tema a practicar:", ["Números Complejos", "Racionalización"])

# Inicializar estados si no existen o si se cambió de módulo
if 'modulo_actual' not in st.session_state or st.session_state.modulo_actual != modulo:
    st.session_state.modulo_actual = modulo
    st.session_state.generar_nuevo = True

if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# Funciones generadoras
def generar_complejos():
    st.session_state.z1_r = random.randint(-6, 6)
    st.session_state.z1_i = random.randint(-6, 6)
    st.session_state.z2_r = random.randint(-6, 6)
    st.session_state.z2_i = random.randint(-6, 6)
    st.session_state.op = random.choice(["+", "-", "*"])
    st.session_state.start_time = time.time()
    st.session_state.generar_nuevo = False

def generar_racionalizacion():
    A = random.randint(2, 12)
    B = random.choice([2, 3, 5, 6, 7, 8, 10, 11]) # Evitamos raíces exactas
    st.session_state.A = A
    st.session_state.B = B
    
    # Racionalización correcta: A / sqrt(B) = (A * sqrt(B)) / B
    # Simplificamos la fracción A/B
    divisor = math.gcd(A, B)
    num = A // divisor
    den = B // divisor
    
    # Armamos la opción correcta en formato matemático (LaTeX)
    if den == 1:
        if num == 1: correcta = f"\\sqrt{{{B}}}"
        else: correcta = f"{num}\\sqrt{{{B}}}"
    else:
        if num == 1: correcta = f"\\frac{{\\sqrt{{{B}}}}}{{{den}}}"
        else: correcta = f"\\frac{{{num}\\sqrt{{{B}}}}}{{{den}}}"
        
    # Inventamos opciones incorrectas creíbles
    opciones = [
        correcta, 
        f"\\frac{{{A}\\sqrt{{{B}}}}}{{{A}}}", # Error común: no simplificar
        f"\\frac{{{num}}}{{{den}\\sqrt{{{B}}}}}", # Error común: dejar la raíz abajo
        f"\\frac{{{B}\\sqrt{{{A}}}}}{{{den}}}" # Error de distracción
    ]
    random.shuffle(opciones)
    
    st.session_state.opciones = opciones
    st.session_state.correcta = correcta
    st.session_state.letras = ["A", "B", "C", "D"]
    st.session_state.correcta_letra = st.session_state.letras[opciones.index(correcta)]
    st.session_state.start_time = time.time()
    st.session_state.generar_nuevo = False

# Generar ejercicio si corresponde
if st.session_state.generar_nuevo:
    if modulo == "Números Complejos":
        generar_complejos()
    elif modulo == "Racionalización":
        generar_racionalizacion()

st.divider()

# ----------------- MÓDULO NÚMEROS COMPLEJOS -----------------
if modulo == "Números Complejos":
    st.subheader("Módulo: Números Complejos")
    st.markdown("Resuelve mentalmente y lo más rápido que puedas:")
    
    def fmt_comp(real, imag):
        signo = "+" if imag >= 0 else "-"
        return f"({real} {signo} {abs(imag)}i)"
        
    z1 = complex(st.session_state.z1_r, st.session_state.z1_i)
    z2 = complex(st.session_state.z2_r, st.session_state.z2_i)
    op = st.session_state.op
    
    if op == "+": correct_z = z1 + z2
    elif op == "-": correct_z = z1 - z2
    else: correct_z = z1 * z2
    
    st.latex(f"{fmt_comp(z1.real, z1.imag)} \\ {op} \\ {fmt_comp(z2.real, z2.imag)}")
    
    col1, col2 = st.columns(2)
    with col1: user_r = st.number_input("Parte Real:", step=1, value=0)
    with col2: user_i = st.number_input("Parte Imaginaria:", step=1, value=0)
    
    if st.button("Comprobar"):
        tiempo_total = int(time.time() - st.session_state.start_time)
        if user_r == correct_z.real and user_i == correct_z.imag:
            st.success(f"¡Excelente! Lo resolviste en {tiempo_total} segundos. ⏱️")
        else:
            st.error(f"¡Cuidado! Tardaste {tiempo_total} segundos y hubo un error.")
            st.info(f"El resultado correcto era: Real {int(correct_z.real)}, Imaginaria {int(correct_z.imag)}")

# ----------------- MÓDULO RACIONALIZACIÓN -----------------
elif modulo == "Racionalización":
    st.subheader("Módulo: Racionalización")
    st.markdown("Racionaliza la siguiente expresión matemática:")
    
    # Mostramos el problema
    st.latex(f"\\frac{{{st.session_state.A}}}{{\\sqrt{{{st.session_state.B}}}}}")
    st.markdown("---")
    st.markdown("**Opciones de resultado (simplificado):**")
    
    # Mostramos las opciones A, B, C y D usando LaTeXa
    colA, colB = st.columns(2)
    with colA:
        st.latex(f"A) \\quad {st.session_state.opciones[0]}")
        st.latex(f"B) \\quad {st.session_state.opciones[1]}")
    with colB:
        st.latex(f"C) \\quad {st.session_state.opciones[2]}")
        st.latex(f"D) \\quad {st.session_state.opciones[3]}")
    
    # El usuario elige una letra
    eleccion = st.radio("Selecciona tu respuesta:", ["A", "B", "C", "D"], horizontal=True)
    
    if st.button("Comprobar"):
        tiempo_total = int(time.time() - st.session_state.start_time)
        if eleccion == st.session_state.correcta_letra:
            st.success(f"¡Impecable! Lo resolviste en {tiempo_total} segundos. ⏱️")
        else:
            st.error(f"Error. Tardaste {tiempo_total} segundos.")
            st.info(f"La respuesta correcta era la {st.session_state.correcta_letra}.")
            st.latex(st.session_state.correcta)
            st.markdown("*Recuerda multiplicar arriba y abajo por la raíz del denominador, y luego simplificar los números de afuera.*")

st.divider()
if st.button("Siguiente Ejercicio ➡️", type="primary"):
    st.session_state.generar_nuevo = True
    st.rerun()
