## **📊 Data Mining**

<p align="center">
  <img src="https://t3.ftcdn.net/jpg/03/77/82/48/360_F_377824892_DiW26NxApuUE11AqUxWeqSR3Mv2Cy4h1.jpg" alt="Bem-vindo ao seu Ambiente de Desenvolvimento">
</p>

## **🖥️ Configuração Local**
Caso queira rodar o projeto localmente sem Docker, siga os passos abaixo:

### **📌 Instalar o Python e Gerenciador de Pacotes**
```bash
sudo apt update    
sudo apt install python3-pip  
pip3 --version 
```

### **📌 Instalar as Bibliotecas Necessárias**
```bash
pip install matplotlib pandas scikit-learn
```

### **📌 Executar o Código**
```bash
python src/Alzheimer.py
```

## **🐳 Rodando com Docker**
Se preferir utilizar um ambiente isolado, siga as etapas abaixo para rodar com Docker.

### **📦 1. Criar a Imagem Docker**
```bash
docker build -t python-datascience .
```

### **🚀 2. Rodar o Contêiner**
```bash
docker run -it --name python_mining -v $(pwd):/app python-datascience
```

### **🛑 3. Parar o Contêiner**
```bash
docker stop python_mining
```

### **🔄 4. Reiniciar o Contêiner**
```bash
docker start -ai python_mining
```

### **📜 5. Executar o Código Dentro do Contêiner**
```bash
python src/Alzheimer.py
```

## **📌 Dicas**
- Se precisar remover o contêiner:
```bash
docker rm python_mining
```
- Se quiser listar os contêineres ativos:
```bash
docker ps
```
- Para listar todos os contêineres (inclusive parados):
```bash
docker ps -a
```
---