/**
 * Disney Clone - Main JavaScript File
 * This file contains all the interactive functionality for the Disney Clone application
 */

// Global Variables
let isLoading = false;
const API_BASE_URL = '/api';

// DOM Content Loaded Event
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

/**
 * Initialize the application
 */
function initializeApp() {
    setupEventListeners();
    setupIntersectionObserver();
    setupSmoothScrolling();
    setupTooltips();
    setupLazyLoading();
    
    // Add loading states to async operations
    setupLoadingStates();
    
    console.log('Disney Clone App initialized successfully! ✨');
}

/**
 * Setup global event listeners
 */
function setupEventListeners() {
    // Navigation active state
    updateActiveNavLink();
    
    // Window events
    window.addEventListener('scroll', handleScroll);
    window.addEventListener('resize', debounce(handleResize, 250));
    
    // Form events
    const searchInputs = document.querySelectorAll('input[type="search"], input[id*="search"]');
    searchInputs.forEach(input => {
        input.addEventListener('input', debounce(handleSearch, 300));
    });
    
    // Modal events
    setupModalEvents();
}

/**
 * Update active navigation link based on current page
 */
function updateActiveNavLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

/**
 * Handle scroll events
 */
function handleScroll() {
    const navbar = document.querySelector('.navbar');
    const scrollTop = window.pageYOffset;
    
    // Add/remove scrolled class to navbar
    if (scrollTop > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
    
    // Parallax effect for hero sections
    const heroSections = document.querySelectorAll('.hero-section, .movie-hero');
    heroSections.forEach(section => {
        if (isElementInViewport(section)) {
            const rate = scrollTop * -0.5;
            section.style.transform = `translateY(${rate}px)`;
        }
    });
}

/**
 * Handle window resize events
 */
function handleResize() {
    // Update any size-dependent calculations
    updateCarouselHeight();
}

/**
 * Setup intersection observer for animations
 */
function setupIntersectionObserver() {
    if ('IntersectionObserver' in window) {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        
        // Observe elements that should animate on scroll
        const animateElements = document.querySelectorAll('.movie-card-item, .feature-card, .stat-item');
        animateElements.forEach(el => {
            observer.observe(el);
        });
    }
}

/**
 * Setup smooth scrolling for anchor links
 */
function setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Setup Bootstrap tooltips
 */
function setupTooltips() {
    if (typeof bootstrap !== 'undefined') {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
}

/**
 * Setup lazy loading for images
 */
function setupLazyLoading() {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        observer.unobserve(img);
                    }
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
}

/**
 * Setup loading states
 */
function setupLoadingStates() {
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.classList.contains('btn-loading')) {
                showButtonLoading(this);
            }
        });
    });
}

/**
 * Setup modal events
 */
function setupModalEvents() {
    // Trailer modal events
    const trailerModal = document.getElementById('trailerModal');
    if (trailerModal) {
        trailerModal.addEventListener('hidden.bs.modal', function () {
            const iframe = document.getElementById('trailerIframe');
            if (iframe) {
                iframe.src = '';
            }
        });
    }
    
    // Prevent modal close on video click
    const modalVideos = document.querySelectorAll('.modal iframe');
    modalVideos.forEach(video => {
        video.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    });
}

/**
 * Handle search functionality
 */
function handleSearch(event) {
    const searchTerm = event.target.value.toLowerCase();
    const searchResults = performSearch(searchTerm);
    displaySearchResults(searchResults);
}

/**
 * Perform search on movies
 */
function performSearch(searchTerm) {
    const movieCards = document.querySelectorAll('.movie-card');
    const results = [];
    
    movieCards.forEach(card => {
        const title = card.dataset.title || '';
        const visible = title.includes(searchTerm);
        card.style.display = visible ? 'block' : 'none';
        if (visible) results.push(card);
    });
    
    return results;
}

/**
 * Display search results
 */
function displaySearchResults(results) {
    const noResults = document.getElementById('noResults');
    const moviesCount = document.getElementById('moviesCount');
    
    if (noResults) {
        noResults.style.display = results.length === 0 ? 'block' : 'none';
    }
    
    if (moviesCount) {
        moviesCount.textContent = results.length;
    }
}

/**
 * Movie-related functions
 */
function openTrailer(trailerUrl, movieTitle) {
    const modal = document.getElementById('trailerModal');
    const iframe = document.getElementById('trailerIframe');
    const title = document.getElementById('trailerModalTitle');
    
    if (modal && iframe) {
        if (title) title.textContent = `${movieTitle} - Trailer`;
        iframe.src = trailerUrl;
        
        if (typeof bootstrap !== 'undefined') {
            new bootstrap.Modal(modal).show();
        }
    }
}

function addToFavorites(movieId) {
    // Simulate API call
    showToast('Filme adicionado aos favoritos!', 'success');
    
    // Update UI
    const heartBtn = event.target.closest('button');
    if (heartBtn) {
        heartBtn.classList.add('text-danger');
        heartBtn.innerHTML = '<i class="fas fa-heart"></i>';
    }
}

function shareMovie() {
    if (navigator.share) {
        navigator.share({
            title: document.title,
            url: window.location.href
        }).then(() => {
            showToast('Compartilhado com sucesso!', 'success');
        }).catch(err => {
            console.log('Erro ao compartilhar:', err);
            copyToClipboard(window.location.href);
        });
    } else {
        copyToClipboard(window.location.href);
    }
}

/**
 * Utility functions
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function showToast(message, type = 'info') {
    // Create toast if it doesn't exist
    let toastContainer = document.querySelector('.toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.className = 'toast-container position-fixed bottom-0 end-0 p-3';
        document.body.appendChild(toastContainer);
    }
    
    const toastId = 'toast-' + Date.now();
    const toastHtml = `
        <div id="${toastId}" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="toast-header">
                <i class="fas fa-${getToastIcon(type)} text-${type} me-2"></i>
                <strong class="me-auto">Disney Clone</strong>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">${message}</div>
        </div>
    `;
    
    toastContainer.insertAdjacentHTML('beforeend', toastHtml);
    
    const toastElement = document.getElementById(toastId);
    if (typeof bootstrap !== 'undefined') {
        const toast = new bootstrap.Toast(toastElement);
        toast.show();
        
        // Remove toast element after it's hidden
        toastElement.addEventListener('hidden.bs.toast', () => {
            toastElement.remove();
        });
    }
}

function getToastIcon(type) {
    const icons = {
        success: 'check-circle',
        error: 'exclamation-circle',
        warning: 'exclamation-triangle',
        info: 'info-circle'
    };
    return icons[type] || icons.info;
}

function copyToClipboard(text) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            showToast('Link copiado para a área de transferência!', 'success');
        }).catch(() => {
            fallbackCopyTextToClipboard(text);
        });
    } else {
        fallbackCopyTextToClipboard(text);
    }
}

function fallbackCopyTextToClipboard(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    textArea.style.top = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    
    try {
        document.execCommand('copy');
        showToast('Link copiado para a área de transferência!', 'success');
    } catch (err) {
        showToast('Erro ao copiar link', 'error');
    }
    
    document.body.removeChild(textArea);
}

function showButtonLoading(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Carregando...';
    button.disabled = true;
    
    // Simulate loading time
    setTimeout(() => {
        button.innerHTML = originalText;
        button.disabled = false;
    }, 1500);
}

function updateCarouselHeight() {
    const carousels = document.querySelectorAll('.carousel');
    carousels.forEach(carousel => {
        const items = carousel.querySelectorAll('.carousel-item');
        let maxHeight = 0;
        
        items.forEach(item => {
            const height = item.offsetHeight;
            if (height > maxHeight) maxHeight = height;
        });
        
        if (maxHeight > 0) {
            carousel.style.height = maxHeight + 'px';
        }
    });
}

/**
 * API Functions
 */
async function fetchMovies() {
    try {
        setLoading(true);
        const response = await fetch(`${API_BASE_URL}/movies`);
        const movies = await response.json();
        return movies;
    } catch (error) {
        console.error('Erro ao buscar filmes:', error);
        showToast('Erro ao carregar filmes', 'error');
        return [];
    } finally {
        setLoading(false);
    }
}

async function fetchMovie(movieId) {
    try {
        setLoading(true);
        const response = await fetch(`${API_BASE_URL}/movie/${movieId}`);
        const movie = await response.json();
        return movie;
    } catch (error) {
        console.error('Erro ao buscar filme:', error);
        showToast('Erro ao carregar filme', 'error');
        return null;
    } finally {
        setLoading(false);
    }
}

function setLoading(loading) {
    isLoading = loading;
    const loadingElements = document.querySelectorAll('.loading-indicator');
    loadingElements.forEach(el => {
        el.style.display = loading ? 'block' : 'none';
    });
}

/**
 * Animation helpers
 */
function animateCounter(element, target, duration = 2000) {
    const start = parseInt(element.textContent) || 0;
    const increment = (target - start) / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target;
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current);
        }
    }, 16);
}

function staggerAnimation(elements, delay = 100) {
    elements.forEach((element, index) => {
        setTimeout(() => {
            element.classList.add('animate-in');
        }, index * delay);
    });
}

// Export functions for global use
window.DisneyClone = {
    openTrailer,
    addToFavorites,
    shareMovie,
    fetchMovies,
    fetchMovie,
    showToast,
    animateCounter,
    staggerAnimation
};

// Add some fun console messages
console.log(`
🏰 Disney Clone Application
✨ Bem-vindo ao mundo mágico da Disney!
🎬 Desenvolvido com Python e Flask
🌟 Aproveite a experiência!
`);

// Performance monitoring
if ('performance' in window) {
    window.addEventListener('load', () => {
        const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
        console.log(`⚡ Página carregada em ${loadTime}ms`);
    });
}