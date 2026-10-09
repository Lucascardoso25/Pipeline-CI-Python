# 1. Imagem base oficial do Python
FROM python:3.12-slim

# 2. Diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia o restante do código-fonte
COPY . .

# 5. Porta exposta pela aplicação
EXPOSE 5000

# 6. Comando para iniciar a aplicação
CMD ["python", "app.py"]