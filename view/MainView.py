import streamlit as st
from streamlit_option_menu import option_menu
import controller
from controller.EvalController import EvaluadorController
from view.Inicio import consultar_instrucciones
from view.CrearActa import listar_evaluacion, agregar_evaluacion
from view.CrearActa import instrucciones
from view.CalificarActa import *
from CalificarActa import calificar_acta
from ImprimirActa import imp_acta
from CrearCriterio import Nuevo_Criterio
from ListarCriterios import Listar_Criterios

class MainView:
    def __init__(self) -> None:
        super().__init__()

        # Estretagia para manejar el "estado" del controllador y del modelo entre cada cambio de ventana
        if 'main_view' not in st.session_state:
            self.menu_actual = "About"

            # Conexión con el controlador
            self.controller = EvaluadorController()

            st.session_state['main_view'] = self
        else:

            # Al exisir en la sesión entonces se actualizan los valores
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller

        self._dibujar_layout()

    def _dibujar_layout(self):
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Sistema de gestion de notas", page_icon='https://www.javerianacali.edu.co/sites/default/files/favicon_0.ico', layout="wide", initial_sidebar_state="collapsed", menu_items=None)
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3, self.col4 = st.columns([1, 1, 1, 1])

        # Define lo que abrá en la barra de menu
        with st.sidebar:
            st.image('https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png', '',
                     300, )
            self.menu_actual = option_menu("Menu", ["Inicio", 'Imprimir Acta', 'Crear Acta', 'Listar Actas', 'Calificar Actas','Crear Criterios','Listar Criterios'],
                                        icons=['house', 'bi bi-printer', 'bi bi-file-earmark-plus-fill','archive','bi bi-clipboard-check','bi bi-node-plus','archive'], menu_icon="bi bi-view-list", default_index=0, orientation="horizontal")
    def controlar_menu(self):
        st.image('https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png', '', 300, )
        if self.menu_actual == "Inicio":
            consultar_instrucciones(st, self.controller)
        elif self.menu_actual == "Imprimir Acta":
            imp_acta(st, self.controller)
        elif self.menu_actual == "Crear Acta":
            texto1 = instrucciones()
            st.write(texto1)
            agregar_evaluacion(st, self.controller)
        elif self.menu_actual == "Listar Actas":
            listar_evaluacion(st, self.controller)
            #exp_acta(st, self.controller)
        elif self.menu_actual == "Calificar Actas":
            calificar_acta(st, self.controller)
        elif self.menu_actual == "Crear Criterios":
            Nuevo_Criterio(st,self.controller)
        elif self.menu_actual == "Listar Criterios":
            Listar_Criterios(st,self.controller)

# Main call
if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()