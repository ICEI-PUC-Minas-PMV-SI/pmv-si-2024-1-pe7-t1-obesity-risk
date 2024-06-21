# Imagem base para a aplicação
FROM node:18-alpine AS builder

# Diretório de trabalho
WORKDIR /app

# Copia package.json e package-lock.json (se existir)
COPY package*.json ./

# Instala dependências
RUN npm install

# Copia o restante do código da aplicação
COPY . .

# Compila a aplicação React (ajuste o nome do script se necessário)
RUN npm run build

# Imagem para produção
FROM nginx:alpine

# Copia a aplicação compilada do builder para o Nginx
COPY --from=builder /app/build /usr/share/nginx/html

# Exporta a porta (ajuste se necessário)
EXPOSE 80

# Configura o comportamento padrão do Nginx
CMD ["nginx", "-g", "daemon off;"]
