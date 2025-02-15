# Usa uma imagem base oficial com Python
FROM python:3.10

# Atualiza o gerenciador de pacotes do sistema
RUN apt-get update && apt-get install -y python3-pip

# Verifica a versão do pip (opcional)
RUN pip3 --version

# Instala as bibliotecas necessárias
RUN pip3 install matplotlib pandas scikit-learn

# Cria um diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos Python do seu diretório local para o contêiner
COPY . /app

# Comando padrão para manter o contêiner rodando (opcional)
CMD ["bash"]
