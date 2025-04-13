import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
import re 
from datetime import datetime

def le_dados():
    return pd.read_csv("Base Dados Candidatos.csv", encoding="latin1", sep=";")



def tratar_dataframe(df):
    """
    Trata o DataFrame aplicando as seguintes transformações:
    - Remove linhas com valores nulos ou vazios na coluna 'Nome'.
    - Converte valores textuais ou inconsistentes na coluna 'Nota' para valores numéricos.
    - Remove linhas com valores nulos na coluna 'Nota'.
    - Converte datas na coluna 'DataAvaliacao' para o formato '%d/%m/%y'.
    - Limpa texto em colunas que não sejam 'Nome', 'Nota' ou 'DataAvaliacao'.

    Parâmetros:
        df (pd.DataFrame): DataFrame original.

    Retorno:
        pd.DataFrame: DataFrame tratado.
    """
    import pandas as pd
    import re
    from datetime import datetime

    # Remover linhas com valores nulos ou vazios na coluna 'Nome'
    df = df[df["Nome"].notna() & (df["Nome"].str.strip() != "")]

    # Função para tratar a coluna 'Nota'
    def tratar_nota(valor):
        mapa = {
            "zero": 0, "um": 1, "dois": 2, "três": 3, "tres": 3,
            "quatro": 4, "cinco": 5, "seis": 6, "sete": 7,
            "oito": 8, "nove": 9, "dez": 10
        }
        if pd.isna(valor):
            return None
        if isinstance(valor, (int, float)):
            return float(valor)
        valor = str(valor).strip().lower().replace(",", ".")
        try:
            return float(valor)
        except:
            return mapa.get(valor, None)

    # Aplicar tratamento na coluna 'Nota'
    df["Nota"] = df["Nota"].apply(tratar_nota)

    # Remover linhas com valores nulos na coluna 'Nota'
    df = df[df["Nota"].notna()]

    # Função para tratar a coluna 'DataAvaliacao'
    def tratar_data(data):
        if pd.isna(data):
            return None
        formatos = ["%d/%m/%Y", "%d/%m/%y", "%d.%m.%y", "%B %d, %Y", "%b %d, %Y"]
        for f in formatos:
            try:
                return datetime.strptime(data.strip(), f).strftime("%d/%m/%y")
            except:
                continue
        try:
            return pd.to_datetime(data, dayfirst=True).strftime("%d/%m/%y")
        except:
            return None

    # Aplicar tratamento na coluna 'DataAvaliacao'
    df["DataAvaliacao"] = df["DataAvaliacao"].apply(tratar_data)

    # Função para limpar texto
    def limpar_texto(texto):
        if pd.isna(texto):
            return ""
        texto = re.sub(r"[^a-zA-ZáéíóúãõçâêîôûÁÉÍÓÚÃÕÇÂÊÎÔÛ ,.\s]", "", str(texto))
        return texto.lower().strip()

    # Limpar texto em colunas que não sejam 'Nome', 'Nota' ou 'DataAvaliacao'
    colunas_para_limpar = [col for col in df.columns if col not in ["Nome", "Nota", "DataAvaliacao"]]
    for col in colunas_para_limpar:
        df[col] = df[col].apply(limpar_texto)

    return df



def classifica_usuario(nome):
    df = le_dados()
    df = tratar_dataframe(df)
    # Filtrar o DataFrame para o usuário especificado
    df_usuario = df[df["Nome"].str.strip().str.lower() == nome.strip().lower()]
    
    if df_usuario.empty:
        return f"Usuário '{nome}' não encontrado."
    
    # Calcular a média das notas do usuário
    media = df_usuario["Nota"].mean()
    
    # Classificar com base na média
    if media > 4:
        return "Excepcional"
    elif media >= 3.5:
        return "Muito bom"
    elif media >= 3:
        return "Fez o básico"
    else:
        return "Precisa melhorar"
    
def obter_notas_usuario(df, nome_usuario):
    df = le_dados()
    df = tratar_dataframe(df)
    # Padronizar o nome do usuário para a busca
    nome_usuario = nome_usuario.strip().lower()
    
    # Filtrar o DataFrame para o usuário especificado
    df_usuario = df[df["Nome"].str.strip().str.lower() == nome_usuario]
    
    if df_usuario.empty:
        print(f"Usuário '{nome_usuario}' não encontrado.")
        return []
    
    return df_usuario["Nota"].tolist()[0:3]   