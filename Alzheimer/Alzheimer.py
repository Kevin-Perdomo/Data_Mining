import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt


# Definir o caminho do arquivo CSV 
file_path = 'data/alzheimers_disease_data.csv'

def carregar_dados(file_path):
    """
    Carrega os dados do CSV informado.
    """
    try:
        df = pd.read_csv(file_path)
        print("Dados carregados com sucesso!")
        print("Visualizando as 5 primeiras linhas:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        exit(1)

def preprocessar_dados(df):
    """
    Realiza o pré-processamento dos dados:
    - Remove colunas irrelevantes
    - Converte colunas categóricas para numéricas
    - Lida com valores ausentes
    """
    # Remover colunas desnecessárias
    colunas_para_remover = ['DoctorInCharge']  # Adicione outras colunas se necessário
    df = df.drop(columns=colunas_para_remover, errors='ignore')

    # Remover colunas não numéricas que não podem ser convertidas diretamente
    for col in df.select_dtypes(include=['object']).columns:
        if col != 'Diagnosis':  # Mantemos a coluna alvo sem transformação
            df[col] = df[col].astype(str)  # Garante que os valores sejam strings
            df = pd.get_dummies(df, columns=[col], drop_first=True)  # Converte para numérico

    # Separar features (X) e alvo (y)
    if 'Diagnosis' not in df.columns:
        print("Erro: a coluna 'Diagnosis' não foi encontrada no CSV.")
        exit(1)

    X = df.drop('Diagnosis', axis=1)
    y = df['Diagnosis']

    return X, y

# Carregar e pré-processar os dados
df = carregar_dados(file_path)
X, y = preprocessar_dados(df)

# Dividir os dados em treino e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo de Árvore de Decisão
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Realizar predições
y_pred = clf.predict(X_test)

# Avaliação do modelo
acuracia_Tree = accuracy_score(y_test, y_pred)
precisao_Tree = precision_score(y_test, y_pred, average='macro')
recall_Tree = recall_score(y_test, y_pred, average='macro')
f1_Tree = f1_score(y_test, y_pred, average='macro')

print(f"\nResultados do modelo Árvore de Decisão")
print(f"\nAcurácia do modelo: {acuracia_Tree*100:.2f}%")
print(f"Precisão: {precisao_Tree*100:.2f}%")
print(f"Recall: {recall_Tree*100:.2f}%")
print(f"F1-score: {f1_Tree*100:.2f}%")


# Criar e treinar o modelo KNN
knn = KNeighborsClassifier(n_neighbors=50)  # Número de vizinhos pode ser ajustado
knn.fit(X_train, y_train)

# Realizar predições e avaliar o modelo
y_pred = knn.predict(X_test)

# Avaliação do modelo
acuracia_KNN = accuracy_score(y_test, y_pred)
precisao_KNN = precision_score(y_test, y_pred, average='macro')
recall_KNN = recall_score(y_test, y_pred, average='macro')
f1_KNN = f1_score(y_test, y_pred, average='macro')

print(f"\nResultados do modelo KNN")
print(f"\nAcurácia do modelo: {acuracia_KNN*100:.2f}%")
print(f"Precisão: {precisao_KNN*100:.2f}%")
print(f"Recall: {recall_KNN*100:.2f}%")
print(f"F1-score: {f1_KNN*100:.2f}%")


# Criar e treinar o modelo SVM
model = svm.SVC(kernel='linear', random_state=42)  # Kernel linear pode ser alterado para 'rbf', 'poly', etc.
model.fit(X_train, y_train)

# Realizar predições e avaliar o modelo
y_pred = model.predict(X_test)

# Avaliação do modelo
acuracia_SVM = accuracy_score(y_test, y_pred)
precisao_SVM = precision_score(y_test, y_pred, average='macro')
recall_SVM = recall_score(y_test, y_pred, average='macro')
f1_SVM = f1_score(y_test, y_pred, average='macro')

print(f"\nResultados do modelo SVM")
print(f"\nAcurácia do modelo: {acuracia_SVM*100:.2f}%")
print(f"Precisão: {precisao_SVM*100:.2f}%")
print(f"Recall: {recall_SVM*100:.2f}%")
print(f"F1-score: {f1_SVM*100:.2f}%")



algoritmos = ['Decision Tree', 'KNN', 'SVM']
acuracias = [acuracia_Tree, acuracia_KNN, acuracia_SVM]
precisoes = [precisao_Tree, precisao_KNN, precisao_SVM]
recalls = [recall_Tree, recall_KNN, recall_SVM]
f1_score = [f1_Tree, f1_KNN, f1_SVM]

# Define a largura das barras
bar_width = 0.25

# Define as posições das barras no eixo x
r1 = range(len(algoritmos))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
# Cria as barras para cada métrica
plt.bar(r1, acuracias, color='#B03F3F', width=bar_width, label='Acurácia')
plt.bar(r2, precisoes, color='#4B4BD5', width=bar_width, label='Precisão')
plt.bar(r3, recalls, color='#E28239', width=bar_width, label='Recall')
plt.bar(r4, f1_score, color='#AE41AE', width=bar_width, label='F1 Score')

# Define os rótulos do eixo x
plt.xticks([r + bar_width for r in range(len(algoritmos))], algoritmos)

# Adiciona título e legenda
plt.title('Comparação de Métricas dos Algoritmos')
plt.xlabel('Algoritmos')
plt.ylabel('Valor da Métrica')
plt.legend()

# Salva o gráfico em um arquivo
plt.savefig('grafico.png')

# Exibe o gráfico
plt.show()