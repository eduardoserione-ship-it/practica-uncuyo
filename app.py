import streamlit as st
import random
import time

# Configuración de la página
st.set_page_config(page_title="Appy Matemática", page_icon="📱", layout="centered")

st.title("Appy Matemática - Entrenamiento SIR 🚀")
st.markdown("¡A entrenar para el ingreso! Resolvé lo más rápido que puedas.")

# Inicializar variables
if 'ejercicio_texto' not in st.session_state:
    st.session_state.ejercicio_texto = ""
    st.session_state.tipo_input = ""
    st.session_state.correctas = []
    st.session_state.opciones = []
    st.session_state.labels = []
    st.session_state.inicio_tiempo = 0

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
    st.session_state.inicio_tiempo = time.time()
    
    if tema == "Números Complejos":
        tipo_op = random.choice(["suma_resta", "multiplicacion"])
        a, b = random.randint(-6, 6), random.randint(-6, 6)
        c, d = random.randint(-6, 6), random.randint(-6, 6)
        
        if tipo_op == "suma_resta":
            op = random.choice(['+', '-'])
            real = a + c if op == '+' else a - c
            imag = b + d if op == '+' else b - d
            st.session_state.ejercicio_texto = f"Resolver: ({a} {'+' if b>=0 else '-'} {abs(b)}i) {op} ({c} {'+' if d>=0 else '-'} {abs(d)}i)"
        else:
            real = (a * c) - (b * d)
            imag = (a * d) + (b * c)
            st.session_state.ejercicio_texto = f"Multiplicar: ({a} {'+' if b>=0 else '-'} {abs(b)}i) * ({c} {'+' if d>=0 else '-'} {abs(d)}i)"
            
        st.session_state.tipo_input = "complejos"
        st.session_state.correctas = [str(real), str(imag)]

    elif tema == "Racionalización":
        coef_final = random.randint(2, 8)
        raiz = random.choice([2, 3, 5, 7, 11])
        numerador_inicial = coef_final * raiz 
        
        correcta = f"{coef_final}√{raiz}"
        opciones_crudas = [
            correcta,
            f"{coef_final * raiz}√{raiz}",
            f"{coef_final + 2}√{raiz}",
            f"{raiz}√{coef_final}"
        ]
        
        # Filtramos para que no haya opciones repetidas por casualidad
        opciones_unicas = list(set(opciones_crudas))
        while len(opciones_unicas) < 4:
            opciones_unicas.append(f"{random.randint(1,9)}√{raiz}")
            opciones_unicas = list(set(opciones_unicas))
            
        random.shuffle(opciones_unicas)
        
        st.session_state.ejercicio_texto = f"Racionalizar y simplificar: {numerador_inicial} / √{raiz}"
        st.session_state.tipo_input = "multiple_choice"
        st.session_state.opciones = opciones_unicas
        st.session_state.correctas = [correcta]

    elif tema == "Polinomios (Operaciones y Factoreo)":
        sub_tema = random.choice(["multiplicacion", "dif_cuadrados", "trinomio_cp"])
        
        if sub_tema == "multiplicacion":
            a, b = random.randint(1, 5), random.randint(-5, 5)
            c, d = random.randint(1, 5), random.randint(-5, 5)
            c2, c1, c0 = (a * c), (a * d + b * c), (b * d)
            
            st.session_state.ejercicio_texto = f"Multiplicar binomios: ({a}x {'+' if b>=0 else '-'} {abs(b)}) * ({c}x {'+' if d>=0 else '-'} {abs(d)})"
            st.session_state.tipo_input = "tres_valores"
            st.session_state.labels = ["Coef. de x²", "Coef. de x", "Independiente"]
            st.session_state.correctas = [str(c2), str(c1), str(c0)]
            
        elif sub_tema == "dif_cuadrados":
            a, b = random.randint(1, 6), random.randint(1, 10)
            st.session_state.ejercicio_texto = f"Factorizar la diferencia de cuadrados: {a**2}x² - {b**2}"
            st.session_state.tipo_input = "dos_valores"
            st.session_state.labels = ["Valor de 'a'", "Valor de 'b'"]
            st.session_state.correctas = [str(a), str(b)]
            
        elif sub_tema == "trinomio_cp":
            a, b = random.randint(1, 5), random.randint(1, 10)
            signo = random.choice([1, -1])
            b_signed = b * signo
            c2, c1, c0 = a**2, 2 * a * b_signed, b**2
            
            st.session_state.ejercicio_texto = f"Factorizar a binomio al cuadrado (ax+b)² el trinomio: {c2}x² {'+' if c1>=0 else '-'} {abs(c1)}x + {c0}"
            st.session_state.tipo_input = "dos_valores"
            st.session_state.labels = ["Coef. 'a' (con la x)", "Término 'b'"]
            st.session_state.correctas = [str(a), str(b_signed)]

    elif tema == "Ecuaciones con Módulo":
        a, b = random.randint(1, 10), random.randint(1, 15)
        op = random.choice(['+', '-'])
        st.session_state.ejercicio_texto = f"Resolver: | x {op} {a} | = {b}"
        
        r1, r2 = (b - a, -b - a) if op == '+' else (b + a, -b + a)
        raices = sorted([r1, r2])
        
        st.session_state.tipo_input = "dos_valores"
        st.session_state.labels = ["Solución Menor", "Solución Mayor"]
        st.session_state.correctas = [str(raices[0]), str(raices[1])]

    elif tema == "Teorema del Resto":
        coef_2, coef_1, indep = random.randint(1, 4), random.randint(-5, 5), random.randint(-10, 10)
        a = random.randint(-3, 3)
        
        polinomio = f"{coef_2}x² {'+' if coef_1>=0 else '-'} {abs(coef_1)}x {'+' if indep>=0 else '-'} {abs(indep)}"
        divisor = f"x {'+' if a<0 else '-'} {abs(a)}" 
        resto = coef_2*(a**2) + coef_1*a + indep
        
        st.session_state.ejercicio_texto = f"Hallar el resto de dividir P(x) = {polinomio} por Q(x) = ({divisor})"
        st.session_state.tipo_input = "un_valor"
        st.session_state.labels = ["Valor numérico del Resto"]
        st.session_state.correctas = [str(resto)]

    elif tema == "Raíces Cuadráticas":
        r1, r2 = random.randint(-6, 6), random.randint(-6, 6)
        b_coeff, c_coeff = -(r1 + r2), r1 * r2
        
        eq = "x² "
        if b_coeff != 0: eq += f"{'+' if b_coeff>0 else '-'} {abs(b_coeff)}x "
        if c_coeff != 0: eq += f"{'+' if c_coeff>0 else '-'} {abs(c_coeff)}"
        eq += " = 0"
        
        raices = sorted([r1, r2])
        st.session_state.ejercicio_texto = f"Hallar las raíces de: {eq}"
        st.session_state.tipo_input = "dos_valores"
        st.session_state.labels = ["Raíz Menor", "Raíz Mayor"]
        st.session_state.correctas = [str(raices[0]), str(raices[1])]

    elif tema == "Sistemas de Ecuaciones (2x2)":
        x_sol, y_sol = random.randint(-5, 5), random.randint(-5, 5)
        A, B = random.randint(1, 4), random.randint(-4, -1)
        D, E = random.randint(-4, -1), random.randint(1, 4)
        
        C, F = A*x_sol + B*y_sol, D*x_sol + E*y_sol
        
        st.session_state.ejercicio_texto = f"Resolver el sistema:\n1) {A}x {'+' if B>=0 else '-'} {abs(B)}y = {C}\n2) {D}x {'+' if E>=0 else '-'} {abs(E)}y = {F}"
        st.session_state.tipo_input = "dos_valores"
        st.session_state.labels = ["Valor de X", "Valor de Y"]
        st.session_state.correctas = [str(x_sol), str(y_sol)]

# UI: Mostrar ejercicio y formulario de respuesta
if st.session_state.ejercicio_texto != "":
    st.markdown("---")
    st.subheader("📝 Ejercicio:")
    st.info(st.session_state.ejercicio_texto)
    
    with st.form("form_respuesta"):
        respuestas_usuario = []
        
        if st.session_state.tipo_input == "complejos":
            col1, col2 = st.columns(2)
            with col1:
                r_real = st.text_input("Parte Real")
            with col2:
                r_imag = st.text_input("Parte Imaginaria")
            respuestas_usuario = [r_real, r_imag]
            
        elif st.session_state.tipo_input == "multiple_choice":
            r_mc = st.radio("Elegí la opción correcta:", st.session_state.opciones)
            respuestas_usuario = [r_mc]
            
        elif st.session_state.tipo_input == "dos_valores":
            col1, col2 = st.columns(2)
            with col1:
                r1 = st.text_input(st.session_state.labels[0])
            with col2:
                r2 = st.text_input(st.session_state.labels[1])
            respuestas_usuario = [r1, r2]
            
        elif st.session_state.tipo_input == "tres_valores":
            col1, col2, col3 = st.columns(3)
            with col1:
                r1 = st.text_input(st.session_state.labels[0])
            with col2:
                r2 = st.text_input(st.session_state.labels[1])
            with col3:
                r3 = st.text_input(st.session_state.labels[2])
            respuestas_usuario = [r1, r2, r3]
            
        elif st.session_state.tipo_input == "un_valor":
            r1 = st.text_input(st.session_state.labels[0])
            respuestas_usuario = [r1]

        submit = st.form_submit_button("Verificar")

    if submit:
        tiempo_total = round(time.time() - st.session_state.inicio_tiempo, 1)
        
        # Limpiar respuestas de espacios en blanco
        resp_limpias = [str(r).replace(" ", "") for r in respuestas_usuario]
        correctas_limpias = [str(c).replace(" ", "") for c in st.session_state.correctas]
        
        if resp_limpias == correctas_limpias:
            st.success("¡Excelente! 🎉 Respuesta correcta.")
            st.balloons()
            st.metric(label="Tiempo de resolución", value=f"{tiempo_total} segundos")
        else:
            st.error("Casi... revisá los signos o los cálculos e intentá de nuevo. 💪")
            st.warning(f"Ayudita -> La respuesta correcta era: {' | '.join(st.session_state.correctas)}")
