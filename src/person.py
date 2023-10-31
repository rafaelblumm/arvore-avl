import datetime

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
        date = self.birth.strftime("%d/%m/%Y")
        return  f"NOME: {self.nome}\n" \
                f"CPF: {self.cpf}\n" \
                f"RG: {self.rg}\n" \
                f"NASCIMENTO: {date}" \
                f"CIDADE: {self.city}"

    def to_dict(self) -> dict:
        """
        Representação dos atributos da classe em formato de dicionário.
        :return dict
        """
        return {
            'CPF': [self.cpf],
            'RG': [self.rg],
            'Nome': [self.name],
            'Nascimento': [self.birth],
            'Cidade:': [self.city]
        }