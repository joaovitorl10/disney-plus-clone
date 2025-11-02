# 🏰 Disney+ Clone 

Um clone completo da plataforma Disney+ desenvolvido com Python Flask, apresentando filmes da Disney, Marvel, Pixar e Star Wars com design autêntico e funcionalidades modernas.

![Disney+ Clone](https://img.shields.io/badge/Disney+-Clone-blue?style=for-the-badge&logo=disney&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## 🎬 Demonstração

### Funcionalidades Principais
- ✅ **Interface autêntica do Disney+** com cores oficiais
- ✅ **Catálogo completo** de filmes Disney e Marvel
- ✅ **Trailers reais** do YouTube integrados
- ✅ **Design responsivo** para todos os dispositivos
- ✅ **Navegação por estúdios** (Disney, Marvel, Pixar, Star Wars)
- ✅ **Sistema de busca e filtros** avançados
- ✅ **Carrossel de filmes** em destaque
- ✅ **Páginas de detalhes** completas dos filmes

### Studios Incluídos
🏰 **Disney** | ⚡ **Marvel** | 🎭 **Pixar** | ⭐ **Star Wars** | 🌍 **National Geographic**

## 🚀 Como Foi Desenvolvido

### Tecnologias Utilizadas
- **Backend:** Python 3.8+ com Flask Framework
- **Frontend:** HTML5, CSS3, JavaScript ES6+
- **UI Framework:** Bootstrap 5.1.3
- **Ícones:** Font Awesome 6.0
- **Fontes:** Google Fonts (Poppins)
- **Vídeos:** YouTube API para trailers

### Arquitetura do Projeto
```
disney_clone/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── executar_disney.bat   # Script de execução Windows
├── static/
│   ├── css/
│   │   └── style.css     # Estilos customizados Disney+
│   ├── js/
│   │   └── main.js       # JavaScript interativo
│   └── images/           # Imagens e assets
└── templates/
    ├── base.html         # Template base
    ├── index.html        # Página inicial
    ├── movies.html       # Catálogo de filmes
    ├── movie_detail.html # Detalhes do filme
    └── about.html        # Página sobre
```

### Design System Disney+
```css
/* Cores Oficiais Disney+ */
:root {
    --disney-blue: #040E2E;        /* Azul escuro principal */
    --disney-light-blue: #1E40AF;  /* Azul médio */
    --disney-purple: #6366F1;      /* Roxo/lilás */
    --disney-cyan: #06B6D4;        /* Ciano (logo +) */
    --disney-gold: #F59E0B;        /* Dourado */
    --marvel-red: #DC2626;         /* Vermelho Marvel */
}
```

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Navegador web moderno

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/joaovitorl10/disney-clone.git
cd disney-clone
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação**
```bash
python app.py
```

4. **Acesse no navegador**
```
http://127.0.0.1:5000
```

### Execução Rápida (Windows)
```bash
# Duplo clique no arquivo
executar_disney.bat
```

## 📱 Funcionalidades Detalhadas

### 🏠 Página Inicial
- Hero section com gradiente autêntico Disney+
- Logos dos estúdios (Disney, Pixar, Marvel, Star Wars, Nat Geo)
- Carrossel de filmes em destaque
- Navegação suave e responsiva

### 🎬 Catálogo de Filmes
- Grid responsivo de filmes
- Sistema de busca em tempo real
- Filtros por ano e avaliação
- Badges identificando os estúdios
- Hover effects com preview

### 🔍 Detalhes dos Filmes
- Trailers integrados do YouTube
- Informações completas (duração, gênero, ano)
- Avaliações e descrições
- Design imersivo com backgrounds

### 🎨 Interface e UX
- **Tema Escuro:** Seguindo padrão Disney+
- **Responsivo:** Funciona em desktop, tablet e mobile
- **Animações:** Transições suaves e micro-interações
- **Acessibilidade:** Controles de foco e navegação por teclado

## 📊 Dados dos Filmes

### Disney Clássicos
- Frozen II, Encanto, Moana, Coco, Soul, Luca, Toy Story 4

### Marvel Cinematic Universe
- Avengers: Endgame, Spider-Man: No Way Home, Doctor Strange 2
- Black Panther: Wakanda Forever, Thor: Love and Thunder
- Guardians of the Galaxy Vol. 3, The Marvels, Ant-Man 3

## 🎯 Características Técnicas

### Performance
- **Carregamento otimizado** de imagens com lazy loading
- **CSS minificado** e otimizado
- **JavaScript assíncrono** para melhor UX
- **Cache de recursos** estáticos

### Responsividade
```css
/* Breakpoints responsivos */
@media (max-width: 768px) { /* Tablet */ }
@media (max-width: 576px) { /* Mobile */ }
```

### Acessibilidade
- Semântica HTML5 adequada
- Contraste de cores WCAG
- Navegação por teclado
- Screen reader friendly

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**João Vitor**
- GitHub: [@joaovitorl10](https://github.com/joaovitorl10)
- Portfolio: [joaovitorl10.github.io/portfolio](https://joaovitorl10.github.io/portfolio)

## 🙏 Agradecimentos

- **Disney** pela inspiração visual
- **Flask** pela simplicidade do framework
- **Bootstrap** pelo sistema de grid responsivo
- **Font Awesome** pelos ícones incríveis

---

⭐ **Se este projeto te ajudou, deixe uma estrela!** ⭐