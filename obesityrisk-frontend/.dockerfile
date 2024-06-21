# Use a imagem base do Node.js
FROM node:14 AS build

# Defina o diretório de trabalho na imagem Docker
WORKDIR /app

# Copie o package.json e package-lock.json
COPY package*.json ./

# Instale as dependências
RUN npm install

# Copie o restante da aplicação para o diretório de trabalho
COPY . .

# Construa a aplicação React
RUN npm run build

# Use uma imagem nginx para servir a aplicação
FROM nginx:alpine

# Copie os arquivos construídos para o diretório nginx
COPY --from=build /app/build /usr/share/nginx/html

# Exponha a porta que a aplicação vai rodar
EXPOSE 80

# Comando para iniciar o nginx
CMD ["nginx", "-g", "daemon off;"]
