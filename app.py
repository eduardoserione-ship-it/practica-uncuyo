import streamlit as st
import random
import time

# Configuración de la página
st.set_page_config(page_title="Appy Matemática", page_icon="📱", layout="centered")

st.title("Appy Matemática - Entrenamiento SIR 🚀")
st.markdown("¡A entrenar para el ingreso! Resolvé lo más rápido que puedas.")

# Inicializar variables
if 'ejercicio' not in st.session_state:
    st.session_state.ejercicio = ""
    st.session_state.respuesta_correcta = ""
    st.session_state.instruccion = ""
    st.session_state.inicio_tiempo = 0
    st.session_state.resuelto = False

# Selector de temas
tema = st.selectbox("Seleccioná el tema a practicar:", [
    "Números Complejos",
    "Racionalización",
    "Polinomios (Operaciones y Factoreo)",
    "Ecuaciones con Módulo",
    "Teorema del Resto",
    "Raíces Cuadráticas",
    "Sistemas de Ecuaciones (2x2)"
])

# Generador de ejercicios
if st.button("Generar Ejercicio"):
    st.session_state.resuelto = False
    st.session_state.inicio_tiempo = time.time()
    
    if tema == "Números Complejos":
        tipo_op = random.choice(["suma_resta", "multiplicacion"])
        a, b = random.randint(-6, 6), random.randint(-6, 6)
        c, d = random.randint(-6, 6), random.randint(-6, 6)
        
        if tipo_op == "suma_resta":
            op = random.choice(['+', '-'])
            real = a + c if op == '+' else a - c
            imag = b + d if op == '+' else b - d
            st.session_state.ejercicio = f"Resolver: ({a} {'+' if b>=0 else '-'} {abs(b)}i) {op} ({c} {'+' if d>=0 else '-'} {abs(d)}i)"
        else:
            real = (a * c) - (b * d)
            imag = (a * d) + (b * c)
            st.session_state.ejercicio = f"Multiplicar: ({a} {'+' if b>=0 else '-'} {abs(b)}i) * ({c} {'+' if d>=0 else '-'} {abs(d)}i)"
            
        st.session_state.respuesta_correcta = f"{real};{imag}"
        st.session_state.instruccion = "Ingresá la parte real y la imaginaria del resultado final, separadas por punto y coma (ej: 5;-2)"

    elif tema == "Racionalización":
        coef_final = random.randint(2, 8)
        raiz = random.choice([2, 3, 5, 7, 11])
        numerador_inicial = coef_final * raiz 
        
        st.session_state.ejercicio = f"Racionalizar y simplificar: {numerador_inicial} / √{raiz}"
        st.session_state.respuesta_correcta = f"{coef_final};{raiz}"
        st.session_state.instruccion = "Ingresá el coeficiente exterior y el número dentro de la raíz, separados por punto y coma (ej: si es 4√3, ingresá 4;3)"

    elif tema == "Polinomios (Operaciones y Factoreo)":
        sub_tema = random.choice(["multiplicacion", "dif_cuadrados", "trinomio_cp"])
        
        if sub_tema == "multiplicacion":
            a, b = random.randint(1, 5), random.randint(-5, 5)
            c, d = random.randint(1, 5), random.randint(-5, 5)
            c2, c1, c0 = (a * c), (a * d + b * c), (b * d)
            
            st.session_state.ejercicio = f"Multiplicar binomios: ({a}x {'+' if b>=0 else '-'} {abs(b)}) * ({c}x {'+' if d>=0 else '-'} {abs(d)})"
            st.session_state.respuesta_correcta = f"{c2};{c1};{c0}"
            st.session_state.instruccion = "Ingresá los coeficientes del trinomio resultante (x², x, indep.) separados por punto y coma (ej: 2;-3;5)"
            
        elif sub_tema == "dif_cuadrados":
            a, b = random.randint(1, 6), random.randint(1, 10)
            
            st.session_state.ejercicio = f"Factorizar la diferencia de cuadrados: {a**2}x² - {b**2}"
            st.session_state.respuesta_correcta = f"{a};{b}"
            st.session_state.instruccion = "Ingresá los valores de 'a' y 'b' del binomio factorizado (ax+b)(ax-b), separados por punto y coma (ej: 3;4)"
            
        elif sub_tema == "trinomio_cp":
            a, b = random.randint(1, 5), random.randint(1, 10)
            signo = random.choice([1, -1])
            b_signed = b * signo
            c2, c1, c0 = a**2, 2 * a * b_signed, b**2
            
            st.session_state.ejercicio = f"Factorizar el trinomio cuadrado perfecto: {c2}x² {'+' if c1>=0 else '-'} {abs(c1)}x + {c0}"
            st.session_state.respuesta_correcta = f"{a};{b_signed}"
            st.session_state.instruccion = "Ingresá el coeficiente de 'x' y el término independiente del binomio original (ax+b)², separados por punto y coma (ej: 2;-5)"

    elif tema == "Ecuaciones con Módulo":
        a, b = random.randint(1, 10), random.randint(1, 15)
        op = random.choice(['+', '-'])
        st.session_state.ejercicio = f"Resolver: | x {op} {a} | = {b}"
        
        r1, r2 = (b - a, -b - a) if op == '+' else (b + a, -b + a)
        raices = sorted([r1, r2])
        st.session_state.respuesta_correcta = f"{raices[0]};{raices[1]}"
        st.session_state.instruccion = "Ingresá las dos soluciones ordenadas de menor a mayor, separadas por punto y coma (ej: -4;8)"

    elif tema == "Teorema del Resto":
        coef_2, coef_1, indep = random.randint(1, 4), random.randint(-5, 5), random.randint(-10, 10)
        a = random.randint(-3, 3)
        
        polinomio = f"{coef_2}x² {'+' if coef_1>=0 else '-'} {abs(coef_1)}x {'+' if indep>=0 else '-'} {abs(indep)}"
        divisor = f"x {'+' if a<0 else '-'} {abs(a)}" 
        resto = coef_2*(a**2) + coef_1*a + indep
        
        st.session_state.ejercicio = f"Hallar el resto de dividir P(x) = {polinomio} por Q(x) = ({divisor})"
        st.session_state.respuesta_correcta = str(resto)
        st.session_state.instruccion = "Ingresá únicamente el valor numérico del resto (ej: 14)"

    elif tema == "Raíces Cuadráticas":
        r1, r2 = random.randint(-6, 6), random.randint(-6, 6)
        b_coeff, c_coeff = -(r1 + r2), r1 * r2
        
        eq = "x² "
        if b_coeff != 0: eq += f"{'+' if b_coeff>0 else '-'} {abs(b_coeff)}x "
        if c_coeff != 0: eq += f"{'+' if c_coeff>0 else '-'} {abs(c_coeff)}"
        eq += " = 0"
        
        raices = sorted([r1, r2])
        st.session_state.ejercicio = f"Hallar las raíces de: {eq}"
        st.session_state.respuesta_correcta = f"{raices[0]};{raices[1]}"
        st.session_state.instruccion = "Ingresá las dos raíces de menor a mayor separadas por punto y coma (ej: -2;3)"

    elif tema == "Sistemas de Ecuaciones (2x2)":
        x_sol, y_sol = random.randint(-5, 5), random.randint(-5, 5)
        A, B = random.randint(1, 4), random.randint(-4, -1)
        D, E = random.randint(-4, -1), random.randint(1, 4)
        
        C, F = A*x_sol + B*y_sol, D*x_sol + E*y_sol
        
        st.session_state.ejercicio = f"Resolver el sistema:\n1) {A}x {'+' if B>=0 else '-'} {abs(B)}y = {C}\n2) {D}x {'+' if E>=0 else '-'} {abs(E)}y = {F}"
        st.session_state.respuesta_correcta = f"{x_sol};{y_sol}"
        st.session_state.instruccion = "Ingresá el valor de X y el de Y en ese orden, separados por punto y coma (ej: 2;-1)"

# Mostrar el ejercicio y verificar respuesta
if st.session_state.ejercicio != "":
    st.markdown("---")
    st.subheader("📝 Ejercicio:")
    st.info(st.session_state.ejercicio)
    st.caption(st.session_state.instruccion)
    
    respuesta_usuario = st.text_input("Tu respuesta:", key="input_respuesta")
    
    if st.button("Verificar"):
        tiempo_total = round(time.time() - st.session_state.inicio_tiempo, 1)
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
