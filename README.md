# Data Mining

- Métodos para explorar um conjunto de dados, extraindo padrões  e auxiliando na descoberta de conhecimento

## Gerenciador de pacotes do python

```bash  
sudo apt update    
sudo apt install python3-pip  
pip3 --version 
```

## Bibliotecas

```bash  
 pip3 install matplotlib 
 pip install pandas
 pip install scikit-learn 
 ```

 ## Container

- Buildar a imagem
```bash  
 docker build -t python-datascience .
 ```
- Rodar o container uma primeira vez
```bash  
docker run -it --name Python_Mining -v $(pwd):/app python-datascience
 ```
- Parar o container
```bash  
docker stop Python_Mining
```
- Rodar o container
```bash  
docker start -ai Python_Mining
```
- Rodar o código dentro do container
 ```bash  
python src/Alzheimer.py
 ```