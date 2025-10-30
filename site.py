from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import webbrowser
import threading
import time

# HTML содержимое
HTML_CONTENT = '''
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HireUp - Рекрутингове агентство</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #3a86ff;
            --secondary: #ff006e;
            --accent: #8338ec;
            --light: #f8f9fa;
            --dark: #212529;
            --success: #38b000;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #f5f7fb;
            color: var(--dark);
            line-height: 1.6;
            scroll-behavior: smooth;
        }
        
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 15px;
        }
        
        /* Header */
        header {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: white;
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            display: flex;
            align-items: center;
        }
        
        .logo i {
            margin-right: 10px;
            color: var(--secondary);
        }
        
        nav ul {
            display: flex;
            list-style: none;
        }
        
        nav ul li {
            margin-left: 1.5rem;
        }
        
        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
            padding: 5px 10px;
            border-radius: 5px;
        }
        
        nav ul li a:hover {
            color: var(--secondary);
            background: rgba(255,255,255,0.1);
        }
        
        .mobile-menu {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: white;
        }
        
        /* Hero Section */
        .hero {
            padding: 5rem 0;
            background: linear-gradient(rgba(58, 134, 255, 0.9), rgba(131, 56, 236, 0.9));
            color: white;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto 2rem;
        }
        
        .btn {
            display: inline-block;
            background-color: var(--secondary);
            color: white;
            padding: 0.8rem 1.8rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
            border: none;
            cursor: pointer;
        }
        
        .btn:hover {
            background-color: #e0005e;
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        /* Services Section */
        .services {
            padding: 5rem 0;
            background-color: white;
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .section-title h2 {
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 1rem;
        }
        
        .section-title p {
            color: #666;
            max-width: 700px;
            margin: 0 auto;
        }
        
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .service-card {
            background-color: var(--light);
            border-radius: 10px;
            padding: 2rem;
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        }
        
        .service-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        }
        
        .service-icon {
            font-size: 3rem;
            color: var(--primary);
            margin-bottom: 1.5rem;
        }
        
        .service-card h3 {
            margin-bottom: 1rem;
            color: var(--dark);
        }
        
        /* About Section */
        .about {
            padding: 5rem 0;
            background: linear-gradient(135deg, #f5f7fb, #e3e8f0);
        }
        
        .about-content {
            display: flex;
            align-items: center;
            gap: 3rem;
        }
        
        .about-text {
            flex: 1;
        }
        
        .about-image {
            flex: 1;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            background: linear-gradient(45deg, var(--primary), var(--accent));
            height: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5rem;
            text-align: center;
            padding: 2rem;
        }
        
        .about-text h2 {
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 1.5rem;
        }
        
        .about-text p {
            margin-bottom: 1.5rem;
            color: #555;
        }
        
        .stats {
            display: flex;
            justify-content: space-between;
            margin-top: 2rem;
        }
        
        .stat {
            text-align: center;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--primary);
        }
        
        .stat-text {
            color: #666;
            font-weight: 500;
        }
        
        /* Contact Section */
        .contact {
            padding: 5rem 0;
            background-color: white;
        }
        
        .contact-content {
            display: flex;
            gap: 3rem;
        }
        
        .contact-info {
            flex: 1;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: white;
            padding: 3rem;
            border-radius: 10px;
        }
        
        .contact-form {
            flex: 1;
        }
        
        .contact-info h3 {
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
        }
        
        .contact-item {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
        }
        
        .contact-icon {
            font-size: 1.5rem;
            margin-right: 1rem;
            color: var(--secondary);
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }
        
        .form-control {
            width: 100%;
            padding: 0.8rem 1rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }
        
        textarea.form-control {
            min-height: 150px;
            resize: vertical;
        }
        
        /* Footer */
        footer {
            background-color: var(--dark);
            color: white;
            padding: 3rem 0 1.5rem;
        }
        
        .footer-content {
            display: flex;
            justify-content: space-between;
            margin-bottom: 2rem;
        }
        
        .footer-logo {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        
        .footer-links h4, .footer-social h4 {
            margin-bottom: 1rem;
            font-size: 1.2rem;
        }
        
        .footer-links ul {
            list-style: none;
        }
        
        .footer-links ul li {
            margin-bottom: 0.5rem;
        }
        
        .footer-links ul li a {
            color: #ccc;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .footer-links ul li a:hover {
            color: var(--secondary);
        }
        
        .social-icons {
            display: flex;
            gap: 1rem;
        }
        
        .social-icons a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background-color: rgba(255,255,255,0.1);
            border-radius: 50%;
            color: white;
            text-decoration: none;
            transition: all 0.3s;
        }
        
        .social-icons a:hover {
            background-color: var(--secondary);
            transform: translateY(-3px);
        }
        
        .copyright {
            text-align: center;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(255,255,255,0.1);
            color: #aaa;
            font-size: 0.9rem;
        }
        
        /* Responsive */
        @media (max-width: 992px) {
            .about-content, .contact-content {
                flex-direction: column;
            }
            
            .footer-content {
                flex-direction: column;
                gap: 2rem;
            }
        }
        
        @media (max-width: 768px) {
            nav ul {
                display: none;
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background: linear-gradient(135deg, var(--primary), var(--accent));
                flex-direction: column;
                padding: 1rem;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            
            nav ul.show {
                display: flex;
            }
            
            nav ul li {
                margin: 0.5rem 0;
            }
            
            .mobile-menu {
                display: block;
            }
            
            .hero h1 {
                font-size: 2.2rem;
            }
            
            .hero p {
                font-size: 1rem;
            }
            
            .section-title h2 {
                font-size: 2rem;
            }
            
            .stats {
                flex-direction: column;
                gap: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <i class="fas fa-arrow-up"></i>
                    HireUp
                </div>
                <nav>
                    <ul id="navMenu">
                        <li><a href="#home">Головна</a></li>
                        <li><a href="#services">Послуги</a></li>
                        <li><a href="#about">Про нас</a></li>
                        <li><a href="#contact">Контакти</a></li>
                    </ul>
                </nav>
                <div class="mobile-menu" id="mobileMenu">
                    <i class="fas fa-bars"></i>
                </div>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="container">
            <h1>Знаходимо найкращих спеціалістів для вашого бізнесу</h1>
            <p>HireUp - це українське рекрутингове агентство, яке допомагає компаніям знаходити таланти, а кандидатам - ідеальну роботу</p>
            <a href="#contact" class="btn">Зв'язатися з нами</a>
        </div>
    </section>

    <!-- Services Section -->
    <section class="services" id="services">
        <div class="container">
            <div class="section-title">
                <h2>Наші послуги</h2>
                <p>Ми пропонуємо повний спектр рекрутингових послуг для бізнесу будь-якого розміру</p>
            </div>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-search"></i>
                    </div>
                    <h3>Прямий пошук</h3>
                    <p>Активний пошук та залучення пасивних кандидатів, які не шукають роботу активно</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-users"></i>
                    </div>
                    <h3>Масовий рекрутинг</h3>
                    <p>Ефективний підбір великої кількості співробітників за короткий термін</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-user-tie"></i>
                    </div>
                    <h3>Executive Search</h3>
                    <p>Пошук керівних позицій та висококваліфікованих фахівців</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-handshake"></i>
                    </div>
                    <h3>HR-консалтинг</h3>
                    <p>Консультації з питань управління персоналом та оптимізації HR-процесів</p>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="about" id="about">
        <div class="container">
            <div class="about-content">
                <div class="about-text">
                    <h2>Про наше агентство</h2>
                    <p>HireUp - це українське рекрутингове агентство, яке спеціалізується на пошуку та підборі кваліфікованих спеціалістів для компаній різних галузей.</p>
                    <p>Наша команда складається з досвідчених рекрутерів, які розуміють ринок праці та можуть знайти ідеального кандидата для вашої компанії.</p>
                    <p>Ми працюємо як з українськими, так і з міжнародними компаніями, допомагаючи їм будувати сильні команди.</p>
                    <div class="stats">
                        <div class="stat">
                            <div class="stat-number">500+</div>
                            <div class="stat-text">Успішних placements</div>
                        </div>
                        <div class="stat">
                            <div class="stat-number">98%</div>
                            <div class="stat-text">Клієнтів рекомендують нас</div>
                        </div>
                        <div class="stat">
                            <div class="stat-number">50+</div>
                            <div class="stat-text">Компаній-партнерів</div>
                        </div>
                    </div>
                </div>
                <div class="about-image">
                    <div>Наша команда професіоналів</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact" id="contact">
        <div class="container">
            <div class="section-title">
                <h2>Контакти</h2>
                <p>Зв'яжіться з нами для обговорення ваших потреб у підборі персоналу</p>
            </div>
            <div class="contact-content">
                <div class="contact-info">
                    <h3>Наші контакти</h3>
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fab fa-telegram"></i>
                        </div>
                        <div>
                            <p>Телеграм: @Anastasiiya90</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-phone"></i>
                        </div>
                        <div>
                            <p>Телефон: +380959799013</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <div>
                            <p>Email: recrytHireUp@gmail.com </p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-id-card"></i>
                        </div>
                        <div>
                            <p>ФОП: 10000003181443</p>
                        </div>
                    </div>
                </div>
                <div class="contact-form">
                    <form id="contactForm">
                        <div class="form-group">
                            <label for="name">Ваше ім'я</label>
                            <input type="text" id="name" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input type="email" id="email" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="phone">Телефон</label>
                            <input type="tel" id="phone" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for="message">Повідомлення</label>
                            <textarea id="message" class="form-control" required></textarea>
                        </div>
                        <button type="submit" class="btn">Надіслати повідомлення</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-about">
                    <div class="footer-logo">HireUp</div>
                    <p>Українське рекрутингове агентство, що спеціалізується на пошуку талантів для бізнесу.</p>
                </div>
                <div class="footer-links">
                    <h4>Швидкі посилання</h4>
                    <ul>
                        <li><a href="#home">Головна</a></li>
                        <li><a href="#services">Послуги</a></li>
                        <li><a href="#about">Про нас</a></li>
                        <li><a href="#contact">Контакти</a></li>
                    </ul>
                </div>
                <div class="footer-social">
                    <h4>Соціальні мережі</h4>
                    <div class="social-icons">
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-telegram"></i></a>
                    </div>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2023 HireUp. Всі права захищені.</p>
            </div>
        </div>
    </footer>

    <script>
        // Mobile menu toggle
        document.getElementById('mobileMenu').addEventListener('click', function() {
            const navMenu = document.getElementById('navMenu');
            navMenu.classList.toggle('show');
        });
        
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                    
                    // Close mobile menu after click
                    const navMenu = document.getElementById('navMenu');
                    navMenu.classList.remove('show');
                }
            });
        });
        
        // Form submission
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Дякуємо за ваше повідомлення! Ми зв\'яжемося з вами найближчим часом.');
            this.reset();
        });
        
        // Add animation on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);
        
        // Observe elements for animation
        document.querySelectorAll('.service-card, .about-text, .about-image, .contact-info, .contact-form').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });
    </script>
</body>
</html>
'''

class HireUpHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode('utf-8'))
        else:
            super().do_GET()

def run_server():
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, HireUpHandler)
    
    print(f"Сервер запущено на http://localhost:{port}")
    print("Сайт HireUp готов до використання!")
    print("Натисніть Ctrl+C для зупинки сервера")
    
    # Автоматично відкриваємо браузер
    def open_browser():
        time.sleep(1)
        webbrowser.open(f'http://localhost:{port}')
    
    threading.Thread(target=open_browser).start()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nЗупинка сервера...")
        httpd.shutdown()

if __name__ == '__main__':
    run_server()