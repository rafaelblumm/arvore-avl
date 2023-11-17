from datetime import datetime
import streamlit as st

class Person:
    """
    Classe que representa dados de uma pessoa na base de dados.
    """
    def __init__(self, cpf: int, rg: int, name: str, birth: datetime, city: str):
        self.cpf = cpf
        self.rg = rg
        self.name = name
        self.birth = birth
        self.city = city
    
    def __repr__(self) -> str:
        if st.session_state['option'] == 'CPF':
            return str(self.format_cpf())
        elif st.session_state['option'] == 'Nome':
            return self.name
        else:
            return self.birth.strftime("%d/%m/%Y")

    def to_dict(self) -> dict:
        """
        Representação dos atributos da classe em formato de dicionário.
        :return dict
        """
        return {
            'CPF': [self.format_cpf()],
            'RG': [self._format_rg()],
            'Nome': [self.name],
            'Nascimento': [self.birth.strftime("%d/%m/%Y")],
            'Cidade:': [self.city]
        }
    
    def format_cpf(self) -> str:
        """
        Formata CPF no formato '999.999.999-99'.
        """
        s = str(self.cpf).zfill(11)
        return f"{s[0:3]}.{s[3:6]}.{s[6:9]}-{s[9:]}"
    
    def _format_rg(self) -> str:
        """
        Formata RG no formato '99.999.999-9'.
        """
        s = str(self.cpf).zfill(9)
        return f"{s[0:2]}.{s[2:5]}.{s[5:8]}-{s[8:]}"
