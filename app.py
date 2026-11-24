import streamlit as st

from modules.integracion import integrar_datos
from modules.validacion import validar_datos
from modules.analisis import resumen_votos
from modules.visualizacion import grafico_votos

st.title("Sistema Analítico Electoral DataVoz")

datos = integrar_datos()

errores = validar_datos(datos)

if errores:

    st.error("Problemas encontrados:")

    for e in errores:
        st.write(e)

else:
    st.success("Datos validados correctamente")

resultado = resumen_votos(datos)

st.dataframe(resultado)

fig = grafico_votos(resultado)

st.plotly_chart(fig)

