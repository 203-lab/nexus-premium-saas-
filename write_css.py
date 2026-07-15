import os

css_content = """
/* ==========================================================================
   Premium Aurora Glassmorphism CSS - Nexus 2.0
   ========================================================================== */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

:root {
    /* Aurora Deep Space Colors */
    --clr-bg: #030014;
    --clr-surface: rgba(10, 10, 25, 0.4);
    
    /* Vibrant Gradients */
    --clr-primary: #8b5cf6; 
    --clr-primary-hover: #a855f7;
    --clr-accent-1: #ec4899; /* Pink */
    --clr-accent-2: #06b6d4; /* Cyan */
    
    /* Text */
    --clr-text-main: #ffffff;
    --clr-text-muted: #94a3b8;
    
    /* Borders & Glass */
    --clr-border: rgba(255, 255, 255, 0.08);
    --glass-bg: rgba(15, 15, 30, 0.6);
    --glass-border: rgba(255, 255, 255, 0.1);
    --glass-shadow: 0 30px 60px -10px rgba(0,0,0,0.8), 0 0 40px rgba(139, 92, 246, 0.1);
    --glass-blur: blur(20px);

    /* Typography */
    --font-heading: 'Outfit', sans-serif;
    --font-primary: 'Plus Jakarta Sans', sans-serif;
    
    /* Sizing */
    --fs-sm: 0.875rem;
    --fs-base: 1rem;
    --fs-lg: 1.125rem;
    --fs-xl: 1.25rem;
    --fs-h3: 1.75rem;
    --fs-h2: 2.75rem;
    --fs-h1: 4.5rem;
    
    /* Spacing */
    --space-sm: 0.5rem;
    --space-md: 1rem;
    --space-lg: 2rem;
    --space-xl: 4rem;
    --header-height: 90px;
    
    --transition-fast: 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
    --transition-normal: 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
}

/* Base */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
html { scroll-behavior: smooth; }
body {
    font-family: var(--font-primary);
    background-color: var(--clr-bg);
    color: var(--clr-text-main);
    line-height: 1.6;
    overflow-x: hidden;
}
a { text-decoration: none; color: inherit; }
ul { list-style: none; }
button { cursor: pointer; border: none; background: none; font-family: inherit; }

/* Custom Cursor */
.custom-cursor {
    position: fixed; top: 0; left: 0; width: 24px; height: 24px;
    border: 1px solid rgba(255,255,255,0.5); border-radius: 50%;
    pointer-events: none; z-index: 10000;
    transform: translate(-50%, -50%); transition: width 0.3s, height 0.3s, background 0.3s;
    backdrop-filter: blur(2px);
}
.custom-cursor.cursor-hover { width: 50px; height: 50px; background: rgba(255,255,255,0.1); border-color: transparent; }

/* Layout */
.container { width: 100%; max-width: 1300px; margin: 0 auto; padding: 0 2rem; position: relative; z-index: 2; }
.section { padding: 8rem 0; position: relative; border-bottom: 1px solid rgba(255,255,255,0.02); }

/* Typography */
h1, h2, h3, h4, .logo-text { font-family: var(--font-heading); font-weight: 700; }
.section h2 { font-size: var(--fs-h2); margin-bottom: 1rem; }
.section p { font-size: var(--fs-lg); color: var(--clr-text-muted); max-width: 600px; margin: 0 auto 4rem; }
.section-header { text-align: center; margin-bottom: 5rem; }
.align-left { text-align: left; }
.align-left p { margin-left: 0; }

.text-gradient {
    background: linear-gradient(to right, #fff, #a1a1aa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.text-gradient-primary {
    background: linear-gradient(135deg, var(--clr-primary), var(--clr-accent-1), var(--clr-accent-2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    animation: gradientFlow 8s ease infinite; background-size: 200% 200%;
}
@keyframes gradientFlow { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }

/* Buttons */
.btn {
    display: inline-flex; align-items: center; justify-content: center;
    padding: 1rem 2rem; border-radius: 100px; font-weight: 600;
    transition: var(--transition-normal); position: relative; overflow: hidden;
    letter-spacing: 0.5px;
}
.btn-primary {
    background: linear-gradient(135deg, var(--clr-primary), var(--clr-accent-1));
    color: #fff; box-shadow: 0 10px 20px -5px rgba(139, 92, 246, 0.4);
}
.btn-primary:hover {
    transform: translateY(-3px) scale(1.02); box-shadow: 0 15px 30px -5px rgba(236, 72, 153, 0.5);
}
.btn-outline {
    background: rgba(255, 255, 255, 0.03); color: #fff;
    border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px);
}
.btn-outline:hover {
    background: rgba(255, 255, 255, 0.1); transform: translateY(-3px);
    border-color: rgba(255, 255, 255, 0.2);
}

/* Header */
.header {
    position: fixed; top: 0; left: 0; width: 100%; height: var(--header-height); z-index: 1000;
    transition: var(--transition-normal); display: flex; align-items: center;
    border-bottom: 1px solid transparent;
}
.header.scrolled {
    background: var(--glass-bg); backdrop-filter: var(--glass-blur); -webkit-backdrop-filter: var(--glass-blur);
    border-bottom: 1px solid var(--glass-border); height: 75px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
.navbar { display: flex; justify-content: space-between; align-items: center; width: 100%; }
.logo-text { font-size: 1.8rem; letter-spacing: -1px; color: #fff; }
.nav-menu { display: flex; gap: 2.5rem; }
.nav-link { font-size: 0.95rem; font-weight: 500; color: #cbd5e1; transition: var(--transition-fast); }
.nav-link:hover, .nav-link.active { color: #fff; text-shadow: 0 0 10px rgba(255,255,255,0.3); }
.nav-actions { display: flex; align-items: center; gap: 1.5rem; }

/* Aurora Background Blobs */
.hero-bg-blobs { position: absolute; inset: 0; overflow: hidden; z-index: 0; pointer-events: none; }
.blob { position: absolute; border-radius: 50%; filter: blur(100px); opacity: 0.5; animation: floatBlob 20s infinite alternate cubic-bezier(0.4, 0, 0.2, 1); }
.blob-1 { top: -10%; left: -10%; width: 600px; height: 600px; background: var(--clr-primary); }
.blob-2 { bottom: -20%; right: -10%; width: 500px; height: 500px; background: var(--clr-accent-1); animation-delay: -5s; animation-duration: 25s; }
.blob-3 { top: 40%; left: 50%; width: 800px; height: 800px; background: var(--clr-accent-2); opacity: 0.3; transform: translate(-50%, -50%); animation-delay: -10s; }
@keyframes floatBlob { 0% { transform: translate(0, 0) scale(1) rotate(0deg); } 100% { transform: translate(100px, 150px) scale(1.2) rotate(45deg); } }

/* Hero */
.hero-section { min-height: 100vh; display: flex; align-items: center; padding-top: var(--header-height); text-align: center; }
.hero-content { max-width: 1000px; margin: 0 auto; position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; gap: 2rem; }
.hero-badge {
    padding: 0.5rem 1rem; border-radius: 100px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);
    font-size: 0.9rem; font-weight: 500; display: inline-flex; align-items: center; gap: 0.5rem;
    backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
.pulse-dot { width: 8px; height: 8px; background: #10b981; border-radius: 50%; box-shadow: 0 0 15px #10b981; animation: pulse 2s infinite; }
.hero-title { font-size: clamp(3rem, 6vw, 5.5rem); line-height: 1.1; letter-spacing: -0.03em; margin: 0; }
.hero-subtitle { font-size: 1.25rem; max-width: 750px; margin: 0; color: #94a3b8; }
.hero-ctas { display: flex; gap: 1rem; margin-top: 1rem; }

/* Grid Layouts */
.features-grid, .services-grid, .stats-grid {
    display: grid; gap: 2rem; position: relative; z-index: 2;
}
.features-grid { grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); }
.services-grid { grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); }
.stats-grid { grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
.about-grid, .why-us-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }

/* Cards & Glassmorphism */
.feature-card, .service-card, .stat-card, .testimonial-card {
    background: rgba(20, 20, 30, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 24px; padding: 3rem 2rem;
    backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
    transition: var(--transition-normal); position: relative; overflow: hidden;
}
.feature-card::before, .service-card::before {
    content: ''; position: absolute; inset: 0; border-radius: 24px; padding: 2px;
    background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0));
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor; mask-composite: exclude; opacity: 0.5; transition: var(--transition-normal);
}
.feature-card:hover, .service-card:hover {
    transform: translateY(-10px); background: rgba(30, 30, 45, 0.6);
    box-shadow: 0 30px 60px -15px rgba(0,0,0,0.8), 0 0 40px rgba(139, 92, 246, 0.15);
}
.feature-card:hover::before, .service-card:hover::before {
    background: linear-gradient(135deg, var(--clr-primary), var(--clr-accent-1)); opacity: 1;
}

/* Icons */
.feature-icon-wrapper, .service-icon, .stat-icon-wrapper {
    width: 60px; height: 60px; border-radius: 16px; display: flex; align-items: center; justify-content: center;
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); margin-bottom: 2rem;
    color: var(--clr-primary); transition: var(--transition-normal);
}
.feature-icon, .service-icon svg, .stat-icon-wrapper svg { width: 30px; height: 30px; }
.feature-card:hover .feature-icon-wrapper, .service-card:hover .service-icon {
    background: linear-gradient(135deg, var(--clr-primary), var(--clr-accent-1)); color: #fff; transform: scale(1.1) rotate(5deg);
    border-color: transparent; box-shadow: 0 10px 20px rgba(139, 92, 246, 0.3);
}

/* Card Content */
.feature-title, .service-card h3 { font-size: 1.5rem; margin-bottom: 1rem; color: #fff; }
.feature-description, .service-card p { color: var(--clr-text-muted); line-height: 1.7; font-size: 1.05rem; }

/* Images & About */
.about-image-wrapper, .why-us-image-wrapper { position: relative; border-radius: 30px; overflow: hidden; }
.about-image-wrapper::after, .why-us-image-wrapper::after {
    content: ''; position: absolute; inset: 0; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.1); border-radius: 30px; pointer-events: none;
}
.about-image, .why-us-image { width: 100%; height: auto; border-radius: 30px; filter: contrast(1.1) brightness(0.9); transition: var(--transition-normal); }
.about-image-wrapper:hover .about-image { transform: scale(1.05); filter: contrast(1.1) brightness(1); }
.feature-list { margin-top: 2rem; display: flex; flex-direction: column; gap: 1rem; }
.feature-list li { display: flex; align-items: center; gap: 1rem; font-size: 1.1rem; }
.check-icon-wrapper {
    width: 28px; height: 28px; border-radius: 50%; background: rgba(16, 185, 129, 0.1);
    color: #10b981; display: flex; align-items: center; justify-content: center;
}
.check-icon { width: 16px; height: 16px; }

/* Stats */
.stat-card { text-align: center; padding: 2rem; }
.stat-card:hover { transform: translateY(-5px); border-color: var(--clr-primary); }
.stat-icon-wrapper { margin: 0 auto 1.5rem; }
.stat-number { font-size: 3.5rem; font-weight: 700; font-family: var(--font-heading); color: #fff; line-height: 1; }
.stat-suffix { font-size: 2rem; color: var(--clr-primary); font-weight: 700; }
.stat-label { display: block; margin-top: 0.5rem; color: var(--clr-text-muted); font-size: 1.1rem; text-transform: uppercase; letter-spacing: 1px; }

/* Testimonials */
.testimonial-track { display: flex; gap: 2rem; overflow-x: auto; padding-bottom: 2rem; scroll-snap-type: x mandatory; }
.testimonial-track::-webkit-scrollbar { height: 6px; }
.testimonial-track::-webkit-scrollbar-track { background: rgba(255,255,255,0.05); border-radius: 10px; }
.testimonial-track::-webkit-scrollbar-thumb { background: var(--clr-primary); border-radius: 10px; }
.testimonial-slide { min-width: 400px; scroll-snap-align: center; }
.testimonial-card { padding: 3rem; text-align: left; height: 100%; display: flex; flex-direction: column; }
.quote-icon { color: rgba(255,255,255,0.1); width: 40px; height: 40px; margin-bottom: 1.5rem; }
.testimonial-text { font-size: 1.15rem; font-style: italic; color: #e2e8f0; flex-grow: 1; margin-bottom: 2rem; }
.client-info { display: flex; align-items: center; gap: 1rem; }
.client-avatar { width: 50px; height: 50px; border-radius: 50%; background: linear-gradient(135deg, var(--clr-primary), var(--clr-accent-1)); display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.2rem; }
.client-name { margin: 0; font-size: 1.1rem; }
.client-role { color: var(--clr-text-muted); font-size: 0.9rem; }

/* Responsive */
@media (max-width: 992px) {
    .about-grid, .why-us-grid { grid-template-columns: 1fr; gap: 3rem; }
    .hero-title { font-size: 3.5rem; }
    .nav-menu { display: none; }
    .menu-toggle { display: block; }
}
@media (max-width: 768px) {
    .hero-title { font-size: 2.5rem; }
    .section { padding: 5rem 0; }
    .btn { padding: 0.8rem 1.5rem; width: 100%; }
    .hero-ctas { flex-direction: column; width: 100%; }
}

/* Footer & Utilities */
.footer { background: #010008; padding: 4rem 0 2rem; border-top: 1px solid rgba(255,255,255,0.05); }
.d-none { display: none !important; }
"""

with open('C:\\xampp\\htdocs\\IndustrialTrainingKit\\css\\style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("CSS updated successfully!")
