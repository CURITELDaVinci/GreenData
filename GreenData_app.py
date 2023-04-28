# Import section
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime
import re
import pydeck as pdk
import base64

import streamlit.components.v1 as components
import streamlit as st

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

# Main page title
st.title("Green Data")

# Create the main sidebar section, useful for the filters

st.sidebar.image('./img/logo-removebg-preview.png', width=200)


st.sidebar.header('Index')
radio = st.sidebar.radio(label="Solution proposal contributions to step:",
                         options=["Conócenos",
                                  "Visor SIGPAC",
                                  "Subvenciones",
                                  "Servicios",
                                  "FAQ",
                                  "Contáctanos",
                                  "Workspace"])

# Load main datasets
# cap_basic_metrics = pd.read_csv('./results/cap_basic_metrics.csv').drop('Unnamed: 0', axis=1)

def add_example(texto):
    with open('examples.txt', 'a') as the_file:
        the_file.write(texto+'\n')

def read_file():
    examples = []
    f = open("examples.txt", "r")
    for x in f:
        examples.append(x)
    custom_examples = set([item for item in examples if item!='\n'])
    return custom_examples
    
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="900" height="850" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

if radio == 'Conócenos':

    # BASIC title
    st.header('Bienvenidos a Green Data!')
    st.markdown('### Conoce un poquito más de nuestra historia')

    # Set basic info
    st.write(''' \n
    En Green Data, creemos en el poder de la agricultura sostenible para alimentar al mundo. Estamos comprometidos con ayudar a los agricultores a implementar prácticas sostenibles y eficientes para aumentar la producción y reducir los costos.
    \n Nuestro equipo está compuesto por expertos en Inteligencia Artificial, manejo de datos y ayuda al agricultor, que están dedicados a brindar la mejor asesoría técnica y apoyo a nuestros clientes. Nos enorgullecemos de trabajar mano a mano con los agricultores para entender sus necesidades y brindar soluciones personalizadas que se ajusten a su presupuesto.
    \n En Green Data, entendemos que la agricultura es un negocio difícil y siempre estamos buscando formas de hacerlo más fácil para nuestros clientes. Desde el diseño de sistemas de riego eficientes hasta la ayuda al crear rutas de trabajo, estamos comprometidos con ayudar a los agricultores a mejorar su producción y aumentar sus ingresos.
    \n Si usted es un agricultor que busca mejorar su explotación de vid, no dude en ponerse en contacto con nosotros. Estamos aquí para ayudarlo a lograr el éxito que se merece.
    \n Gracias por visitar Green Data. Esperamos poder trabajar con usted pronto.
    ''')

if radio == 'Visor SIGPAC':
    
    # BASIC title
    st.header('Visor SIGPAC')
    st.markdown('### Encuentra tu parcela!')

    # Set basic info
    st.write(''' \n
    El SIGPAC (Sistema de Información Geográfica de Parcelas Agrícolas) es un sistema de información geográfica utilizado en España para la gestión de las parcelas agrícolas y ganaderas. Es una herramienta importante para la gestión del territorio y la planificación de la actividad agrícola, y se utiliza para la identificación, registro y gestión de las parcelas agrícolas y ganaderas, así como para la asignación de ayudas y subvenciones agrícolas. Además, para la gestión ambiental y la conservación del patrimonio natural. 
    \n Todos los clientes de Green Data pueden consultar el SIGPAC para poder localizar sus explotaciones desde una misma web.
    ''')

    html_string = '''
    <html>
    <head>
        <title>Yearly Symbol Prices</title>
    </head>
    <iframe src="https://sigpac.jccm.es/"
            frameborder="0"
            allowfullscreen
            style="width:100%;height:600px;">
    </iframe>
    </html>
    '''
    st.markdown(html_string, unsafe_allow_html=True)

    mostrar_informe = st.checkbox('Mostrar informe detallado de la parcela')
    if mostrar_informe:
        path_to_html = './data/parcela_a.html'
        # Read file and keep in variable
        with open(path_to_html,'r') as f: 
            html_data = f.read()

        ## Show in webpage
        st.image('./img/cabecera-consultas.jpg', use_column_width=True)
        st.components.v1.html(html_data, height=800)

if radio == 'Subvenciones':
    # BASIC title
    st.header('Subvenciones')
    st.markdown('### Automatización del proceso de solicitud de subvenciones!')

    # Set basic info
    st.write(''' \n
    \nDesde el equipo de Green Data somos conscientes de las complicaciones que suponen para los agricultores los procesos de solicitud de las subvenciones que disponen. Muchos agricultores ni siquiera saben de la existencia de estos pagos que les pertenecen y muchos desisten por lo complicado y tedioso del proceso. 
    \nPrecisamente por esto es que es necesario hacer más sencillos estos procesos burocráticos y nos comprometemos a hacerlo real a todos nuestros clientes, independientemente de su situación personal o extensión de su explotación.
    ''')

if radio == 'Servicios':
    # BASIC title
    st.header('Servicios')
    st.markdown('### Descubre el plan que mejor se adapta a tus necesidades!')

    # Set basic info
    st.write(''' \n
    En Green Data queremos ofrecer a los agricultores una amplia variedad de servicios para sacar el máximo rendimiento a su cultivo. El plan básico incluye acceso a un mercado donde los agricultores pueden alquilar sus herramientas y utensilios de trabajo a gente que las necesite. También trabajadores pueden exponer su conocimiento en las tareas que requiere el campo y vender estos servicios a agricultores que no puedan encargarse de todo por ellos mismos. También, los agricultores e incluso cooperativas pueden poner a la venta los productos que producen.
    ''')

    st.subheader("Planes detallados por servicios")
    df = pd.DataFrame({
        'Green Farmer' : ["✅", "✅", "✅", "", "", "", "", "", "", "", "", "","", "Gratuito", "Gratuito"],
        'Green Expert': ["✅", "✅", "✅", "✅", "✅", "✅", "", "", "", "", "", "","", "17,95 €", "179,95 €"],
        'Green Master': ["✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅","✅", "45,95 €", "525,95 €"]
    }, index=['Marketplace cooperativo', 'Bolsa de empleo', 'Alquiler de herramientas', 
              'Cuaderno de campo digital', 'Soporte solicitud de subvenciones', 'Optimización de rutas',
              'Instalación de sensores (Máximo 10)', 'Medición del impacto ambiental', 'Optimización de tareas', 'Toma de decisiones estratégica', 
              'Generación automática de insights', 'Alertas de valores anómalos', "Soporte 24/7", 'Precio mensual', 'Precio anual'])


    st.table(df)

if radio == 'FAQ':
    pass

if radio == 'Contáctanos':
    # BASIC title
    st.header('Contáctanos')
    st.markdown('### Si tienes una consulta no dudes en contactarnos!')

    # Set basic info
    st.write(''' \n
    Es normal que te surjan dudas, por eso estamos disponibles para ayudarte en lo que necesites. Rellena el siguiente formulario para ponerte en contacto con nosotros.
    ''')

    def clear_form():
        st.session_state["nombre"] = ""
        st.session_state["email"] = ""
        st.session_state["asunto"] = ""
        st.session_state["mensaje"] = ""
    
    with st.form("myform"):
        f1, f2 = st.columns([1, 1])
        with f1:
            st.text_input("Nombre completo", key="nombre")
        with f2:
            st.text_input("Email", key="email")
        st.text_input('Introduce el asunto principal de la consulta', key="asunto")
        mensaje = st.text_area('Describe tu consulta', key="mensaje")
        if st.form_submit_button(label="Enviar consulta", on_click=clear_form):
            st.write("Tu consulta se ha enviado correctamente. Nos pondremos en contacto contigo tan pronto como nos sea posible.")

        # Set basic info
        st.write(''' \n
        Si lo prefieres, también puedes ponerte en contacto con nosotros a través de la dirección de correo green.data.davinci@gmail.com o al +34 601 165 382.
        ''')

if radio == 'Workspace':
    tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
    tab1.write("this is tab 1")
    tab2.write("this is tab 2")

    with tab1:
        st.radio('Select one:', [1, 2])