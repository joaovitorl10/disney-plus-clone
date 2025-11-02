# 🏰 Disney Clone - Python Flask Web App

Um clone da Disney criado com Python e Flask, apresentando uma interface moderna e responsiva para explorar filmes Disney com trailers, fotos e informações detalhadas.

## ✨ Características

- 🎬 **Catálogo de Filmes**: Navegue por uma coleção de filmes Disney populares
- 🎥 **Trailers Integrados**: Assista aos trailers diretamente na plataforma
- 🔍 **Busca e Filtros**: Encontre filmes por título, ano ou avaliação
- 📱 **Design Responsivo**: Funciona perfeitamente em todos os dispositivos
- 🎨 **Tema Disney**: Interface com cores e estilo inspirados na Disney
- ⚡ **Interativo**: Animações suaves e experiência de usuário moderna

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.8+ com Flask
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Framework CSS**: Bootstrap 5
- **Ícones**: Font Awesome 6
- **Fontes**: Google Fonts (Poppins)

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Navegador web moderno

## 🚀 Como Executar

### 1. Clone ou baixe o projeto
```bash
# Se usando Git
git clone [url-do-repositorio]
cd disney_clone

# Ou baixe e extraia o arquivo ZIP
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv

# No Windows
venv\Scripts\activate

# No macOS/Linux
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação
```bash
python app.py
```

### 5. Acesse no navegador
Abra seu navegador e vá para: `http://localhost:5000`

## 📁 Estrutura do Projeto

```
disney_clone/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── README.md             # Este arquivo
├── static/               # Arquivos estáticos
│   ├── css/
│   │   └── style.css     # Estilos personalizados
│   ├── js/
│   │   └── main.js       # JavaScript customizado
│   └── images/           # Imagens do projeto
└── templates/            # Templates HTML
    ├── base.html         # Template base
    ├── index.html        # Página inicial
    ├── movies.html       # Lista de filmes
    ├── movie_detail.html # Detalhes do filme
    └── about.html        # Página sobre
```

## 🎮 Funcionalidades

### Página Inicial
- Hero section com animações
- Carousel de filmes em destaque
- Estatísticas animadas
- Call-to-action interativo

### Catálogo de Filmes
- Grid responsivo de filmes
- Sistema de busca em tempo real
- Filtros por ano e ordenação
- Modais para trailers
- Sistema de favoritos

### Detalhes do Filme
- Página dedicada para cada filme
- Trailer incorporado
- Informações completas
- Sistema de compartilhamento
- Design imersivo

### Recursos Interativos
- Modais para trailers do YouTube
- Animações CSS personalizadas
- Lazy loading de imagens
- Tooltips informativos
- Toasts para feedback

## 🎨 Personalização

### Cores do Tema Disney
```css
:root {
    --disney-blue: #1e3a8a;
    --disney-light-blue: #3b82f6;
    --disney-gold: #fbbf24;
    --disney-dark-gold: #f59e0b;
    --disney-purple: #7c3aed;
}
```

### Adicionando Novos Filmes
Edite o array `DISNEY_MOVIES` em `app.py`:
```python
{
    'id': 9,
    'title': 'Nome do Filme',
    'year': 2024,
    'genre': 'Animação, Aventura',
    'duration': '120 min',
    'rating': 8.5,
    'description': 'Descrição do filme...',
    'poster': 'URL_da_imagem',
    'trailer': 'URL_do_trailer_youtube',
    'featured': True  # Para aparecer em destaque
}
```

## 🌐 API Endpoints

A aplicação inclui endpoints de API para desenvolvimento:

- `GET /api/movies` - Lista todos os filmes
- `GET /api/movie/<id>` - Detalhes de um filme específico

## 🔧 Desenvolvimento

### Modo Debug
O Flask está configurado para executar em modo debug por padrão:
```python
app.run(debug=True, host='127.0.0.1', port=5000)
```

### Estrutura de Roteamento
- `/` - Página inicial
- `/movies` - Catálogo de filmes
- `/movie/<id>` - Detalhes do filme
- `/about` - Sobre o projeto

## 📱 Responsividade

O design é totalmente responsivo com breakpoints para:
- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px
- **Mobile**: 576px - 767px
- **Small Mobile**: < 576px

## 🎯 Melhorias Futuras

- [ ] Sistema de usuários e autenticação
- [ ] Banco de dados real (SQLite/PostgreSQL)
- [ ] Sistema de avaliações
- [ ] Listas de reprodução personalizadas
- [ ] Comentários nos filmes
- [ ] Integração com APIs de filmes reais
- [ ] Sistema de notificações
- [ ] Modo escuro/claro

## 🐛 Solução de Problemas

### Erro "Module not found"
```bash
pip install -r requirements.txt
```

### Porta já em uso
Mude a porta em `app.py`:
```python
app.run(debug=True, host='127.0.0.1', port=5001)
```

### Problemas com templates
Verifique se a pasta `templates` está no mesmo diretório de `app.py`

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é apenas para fins educacionais e demonstração. Todas as imagens e conteúdos dos filmes pertencem à Disney.

## 👨‍💻 Autor

Desenvolvido com ❤️ usando Python e Flask

---

**Nota**: Este é um projeto educacional que demonstra como criar uma aplicação web moderna com Python. Não é afiliado à Disney de forma alguma.