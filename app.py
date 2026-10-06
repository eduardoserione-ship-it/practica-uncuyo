import streamlit as st
import random
import time

# Configuración de la página para que se vea bien en el celu
st.set_page_config(page_title="Appy Matemática", page_icon="📱", layout="centered")

st.title("Appy Matemática - Entrenamiento SIR 🚀")
st.markdown("¡A entrenar para el ingreso! Resolvé lo más rápido que puedas.")

# Inicializar variables en el estado de la sesión
if 'ejercicio' not in st.session_state:
    st.session_state.ejercicio = ""
    st.session_state.respuesta_correcta = ""
    st.session_state.instruccion = ""
    st.session_state.inicio_tiempo = 0
    st.session_state.resuelto = False

# Selector de temas
tema = st.selectbox("Seleccioná el tema a practicar:", [
    "Números Complejos (Suma/Resta)",
    "Racionalización (Básica)",
    "Ecuaciones con Módulo",
    "Teorema del Resto",
    "Raíces Cuadráticas",
    "Sistemas de Ecuaciones (2x2)"
])

# Generador de ejercicios
if st.button("Generar Ejercicio"):
    st.session_state.resuelto = False
    st.session_state.inicio_tiempo = time.time()
    
    if tema == "Números Complejos (Suma/Resta)":
        a, b, c, d = [random.randint(-10, 10) for _ in range(4)]
        op = random.choice(['+', '-'])
        if op == '+':
            real = a + c
            imag = b + d
        else:
            real = a - c
            imag = b - d
        
        st.session_state.ejercicio = f"({a} {'+' if b>=0 else '-'} {abs(b)}i) {op} ({c} {'+' if d>=0 else '-'} {abs(d)}i)"
        st.session_state.respuesta_correcta = f"{real};{imag}"
        st.session_state.instruccion = "Ingresá la parte real y la imaginaria separadas por punto y coma (ej: 5;-2)"

    elif tema == "Racionalización (Básica)":
        num = random.randint(2, 10)
        raiz = random.choice([2, 3, 5, 7, 11])
        st.session_state.ejercicio = f"Racionalizar: {num} / √{raiz}"
        st.session_state.respuesta_correcta = f"{num};{raiz}"
        st.session_state.instruccion = "Ingresá el coeficiente del numerador y el denominador final separados por punto y coma (ej: si queda 3√5 / 5, ingresá 3;5)"

    elif tema == "Ecuaciones con Módulo":
        a = random.randint(1, 10)
        b = random.randint(1, 15)
        op = random.choice(['+', '-'])
        st.session_state.ejercicio = f"| x {op} {a} | = {b}"
        
        if op == '+':
            r1, r2 = b - a, -b - a
        else:
            r1, r2 = b + a, -b + a
            
        raices = sorted([r1, r2])
        st.session_state.respuesta_correcta = f"{raices[0]};{raices[1]}"
        st.session_state.instruccion = "Ingresá las dos soluciones de menor a mayor separadas por punto y coma (ej: -4;8)"

    elif tema == "Teorema del Resto":
        coef_2 = random.randint(1, 4)
        coef_1 = random.randint(-5, 5)
        indep = random.randint(-10, 10)
        a = random.randint(-3, 3)
        
        polinomio = f"{coef_2}x² {'+' if coef_1>=0 else '-'} {abs(coef_1)}x {'+' if indep>=0 else '-'} {abs(indep)}"
        divisor = f"x {'+' if a<0 else '-'} {abs(a)}" # Si a es positivo, x-a. Si a es negativo, x+a
        
        resto = coef_2*(a**2) + coef_1*a + indep
        
        st.session_state.ejercicio = f"Hallar el resto de dividir P(x) = {polinomio} por Q(x) = ({divisor})"
        st.session_state.respuesta_correcta = str(resto)
        st.session_state.instruccion = "Ingresá únicamente el valor numérico del resto (ej: 14)"

    elif tema == "Raíces Cuadráticas":
        r1 = random.randint(-6, 6)
        r2 = random.randint(-6, 6)
        b_coeff = -(r1 + r2)
        c_coeff = r1 * r2
        
        eq = "x² "
        if b_coeff != 0:
            eq += f"{'+' if b_coeff>0 else '-'} {abs(b_coeff)}x "
        if c_coeff != 0:
            eq += f"{'+' if c_coeff>0 else '-'} {abs(c_coeff)}"
        eq += " = 0"
        
        raices = sorted([r1, r2])
        st.session_state.ejercicio = f"Hallar las raíces de: {eq}"
        st.session_state.respuesta_correcta = f"{raices[0]};{raices[1]}"
        st.session_state.instruccion = "Ingresá las dos raíces de menor a mayor separadas por punto y coma (ej: -2;3). Si es raíz doble, repetila (ej: 4;4)"

    elif tema == "Sistemas de Ecuaciones (2x2)":
        x_sol = random.randint(-5, 5)
        y_sol = random.randint(-5, 5)
        
        A, B = random.randint(1, 4), random.randint(-4, -1)
        D, E = random.randint(-4, -1), random.randint(1, 4)
        
        C = A*x_sol + B*y_sol
        F = D*x_sol + E*y_sol
        
        st.session_state.ejercicio = f"Resolver el sistema:\n1) {A}x {'+' if B>=0 else '-'} {abs(B)}y = {C}\n2) {D}x {'+' if E>=0 else '-'} {abs(E)}y = {F}"
        st.session_state.respuesta_correcta = f"{x_sol};{y_sol}"
        st.session_state.instruccion = "Ingresá el valor de X y el de Y separados por punto y coma (ej: 2;-1)"

# Mostrar el ejercicio si existe
if st.session_state.ejercicio != "":
    st.markdown("---")
    st.subheader("📝 Ejercicio:")
    st.info(st.session_state.ejercicio)
    st.caption(st.session_state.instruccion)
    
    respuesta_usuario = st.text_input("Tu respuesta:", key="input_respuesta")
    
    if st.button("Verificar"):
        tiempo_total = round(time.time() - st.session_state.inicio_tiempo, 1)
        
        # Limpiamos los espacios por si escribís con espacios desde el celu
        resp_limpia = respuesta_usuario.replace(" ", "")
        correcta_limpia = st.session_state.respuesta_correcta.replace(" ", "")
        
        if resp_limpia == correcta_limpia:
            st.success(f"¡Excelente! 🎉 Respuesta correcta.")
            st.balloons()
            st.metric(label="Tiempo de resolución", value=f"{tiempo_total} segundos")
            st.session_state.resuelto = True
        else:
            st.error("Casi... revisá los signos o los cálculos e intentá de nuevo. 💪")
            st.warning(f"Ayudita -> La respuesta correcta era: {st.session_state.respuesta_correcta}")
