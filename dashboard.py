import streamlit as st
from amdahl import Amdahl
from Pila import Pila

st.set_page_config(page_title="Ley de Amdahl", page_icon="⚡")

st.title("⚡ Calculadora de Aceleración (Ley de Amdahl)")

if "pila" not in st.session_state:
    st.session_state["pila"] = Pila()

with st.form("formulario_amdahl"):
    st.subheader("Ingresar nuevo proceso o elemento")

    nombre = st.text_input("Nombre del proceso o elemento a mejorar:")

    porcentaje = st.slider("Porcentaje mejorable (%)", min_value=0.0, max_value=100.0, step=0.1)
    
    factor = st.number_input("Factor de mejora (mayor que 0)", min_value=1)

    submit = st.form_submit_button("Calcular y agregar")

    if submit:
        if not nombre.strip():
            st.error("Por favor ingrese un nombre.")
        else:
            try:
                f = porcentaje / 100
                amdahl_obj = Amdahl(f, factor)
                aceleracion = amdahl_obj.aceleracion()

                st.session_state["pila"].apilar((nombre, porcentaje, factor, aceleracion))
                st.success(
                    f"✅ La aceleración de **{nombre}** es: **{aceleracion:.4f}x**"
                )
            except ValueError as e:
                st.error(f"Error: {e}")

pila = st.session_state["pila"]

if len(pila) > 0:
    n = min(3, len(pila))
    ultimos = pila.ver_x_elementos(n)

    st.subheader(f"📋 Últimos {n} elementos ingresados")
    
    st.table(
        {
            "Nombre": [item[0] for item in ultimos],
            "Porcentaje mejorable (%)": [f"{item[1]:.1f}" for item in ultimos],
            "Factor de mejora": [f"{item[2]}" for item in ultimos],
            "Aceleración (x)": [f"{item[3]:.4f}" for item in ultimos]
        }
    )

    mejor = max(ultimos, key=lambda x: x[3])
    mejor_nombre, mejor_aceleracion = mejor[0], mejor[3]

    st.info(
        f"🔎 **Conclusión:** De los últimos {n} elementos ingresados, "
        f"**{mejor_nombre}** es el más factible de mejorar, "
        f"con aceleración de **{mejor_aceleracion:.4f}x**."
    )
else:
    st.info("No se han ingresado elementos aún.")

if st.button("🔄 Reiniciar datos"):
    st.session_state["pila"] = Pila()
    st.rerun()