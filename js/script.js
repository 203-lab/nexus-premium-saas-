/**
 * Main application script for the Premium Navbar
 * Features: Sticky header, mobile menu toggle, scroll spy for active links, and keyboard accessibility.
 */

document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------------------------------------
    // Preloader
    // ----------------------------------------------------------------------
    window.addEventListener('load', () => {
        const preloader = document.getElementById('preloader');
        if (preloader) {
            preloader.classList.add('hidden');
            setTimeout(() => {
                preloader.style.display = 'none';
            }, 500); // match css transition
        }
    });

    // ----------------------------------------------------------------------
    // Dark Mode Toggle
    // ----------------------------------------------------------------------
    const themeToggleBtn = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            if (isDark) {
                document.documentElement.removeAttribute('data-theme');
                localStorage.setItem('theme', 'light');
            } else {
                document.documentElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
            }
        });
    }
    // ----------------------------------------------------------------------
    // Elements Selection
    // ----------------------------------------------------------------------
    const header = document.getElementById('header');
    const menuToggle = document.getElementById('menu-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section');

    const scrollProgress = document.getElementById('scroll-progress');

    // ----------------------------------------------------------------------
    // Sticky Glassmorphism Header & Scroll Progress
    // ----------------------------------------------------------------------
    const handleScroll = () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        if (scrollProgress) {
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            scrollProgress.style.width = scrolled + "%";
        }
    };

    // Initialize state on load
    handleScroll();
    
    // Listen for scroll events (using passive listener for performance)
    window.addEventListener('scroll', handleScroll, { passive: true });

    // ----------------------------------------------------------------------
    // Mobile Menu Toggle
    // ----------------------------------------------------------------------
    const toggleMenu = () => {
        const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
        
        // Toggle aria state
        menuToggle.setAttribute('aria-expanded', !isExpanded);
        
        // Toggle active classes
        navMenu.classList.toggle('active');
        
        // Prevent body scrolling when menu is open on mobile
        document.body.style.overflow = isExpanded ? '' : 'hidden';
    };

    menuToggle.addEventListener('click', toggleMenu);

    // Close mobile menu when a link is clicked
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navMenu.classList.contains('active')) {
                toggleMenu();
            }
        });
    });

    // ----------------------------------------------------------------------
    // Active Link Highlighting (Intersection Observer)
    // ----------------------------------------------------------------------
    const observerOptions = {
        root: null,
        rootMargin: '-50% 0px -50% 0px', // Trigger when section is in middle of viewport
        threshold: 0
    };

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Get the id of the intersecting section
                const targetId = entry.target.getAttribute('id');
                
                // Remove active class from all links
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    link.removeAttribute('aria-current');
                    
                    // Add active class to corresponding link
                    if (link.getAttribute('href') === `#${targetId}`) {
                        link.classList.add('active');
                        link.setAttribute('aria-current', 'page');
                    }
                });
            }
        });
    }, observerOptions);

    // Observe all sections
    sections.forEach(section => {
        sectionObserver.observe(section);
    });

    // ----------------------------------------------------------------------
    // Keyboard Accessibility (Escape key closes menu)
    // ----------------------------------------------------------------------
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && navMenu.classList.contains('active')) {
            toggleMenu();
            menuToggle.focus(); // Return focus to button
        }
    });

    // ----------------------------------------------------------------------
    // Animated Counters (Intersection Observer)
    // ----------------------------------------------------------------------
    const counters = document.querySelectorAll('.counter-value');
    const speed = 100; // Lower is slower

    const animateCounters = (counter) => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;

            // Calculate increment based on target and speed
            const inc = target / speed;

            if (count < target) {
                // Add increment to count and output
                counter.innerText = Math.ceil(count + inc);
                // Call function every ms
                setTimeout(updateCount, 20);
            } else {
                counter.innerText = target;
            }
        };
        updateCount();
    };

    const counterObserverOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5 // Trigger when 50% of the element is visible
    };

    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters(entry.target);
                // Stop observing once animated
                observer.unobserve(entry.target);
            }
        });
    }, counterObserverOptions);

    counters.forEach(counter => {
        counterObserver.observe(counter);
    });

    // ----------------------------------------------------------------------
    // Testimonial Slider
    // ----------------------------------------------------------------------
    const track = document.getElementById('testimonial-track');
    const slides = document.querySelectorAll('.testimonial-slide');
    const prevBtn = document.getElementById('slider-prev');
    const nextBtn = document.getElementById('slider-next');
    const dotsContainer = document.getElementById('slider-dots');
    
    if (track && slides.length > 0) {
        let currentIndex = 0;
        let isDragging = false;
        let startPos = 0;
        let currentTranslate = 0;
        let prevTranslate = 0;
        let animationID;
        let autoSlideInterval;

        // Generate Dots
        slides.forEach((_, index) => {
            const dot = document.createElement('button');
            dot.classList.add('slider-dot');
            dot.setAttribute('aria-label', `Go to slide ${index + 1}`);
            if (index === 0) dot.classList.add('active');
            dot.addEventListener('click', () => goToSlide(index));
            dotsContainer.appendChild(dot);
        });

        const dots = document.querySelectorAll('.slider-dot');

        const updateDots = () => {
            dots.forEach(dot => dot.classList.remove('active'));
            dots[currentIndex].classList.add('active');
        };

        const setPositionByIndex = () => {
            currentTranslate = currentIndex * -track.offsetWidth;
            prevTranslate = currentTranslate;
            track.style.transform = `translateX(${currentTranslate}px)`;
            updateDots();
        };

        const goToSlide = (index) => {
            currentIndex = index;
            setPositionByIndex();
            resetAutoSlide();
        };

        const nextSlide = () => {
            currentIndex = (currentIndex + 1) % slides.length;
            setPositionByIndex();
        };

        const prevSlide = () => {
            currentIndex = (currentIndex - 1 + slides.length) % slides.length;
            setPositionByIndex();
        };

        // Buttons
        nextBtn.addEventListener('click', () => {
            nextSlide();
            resetAutoSlide();
        });
        
        prevBtn.addEventListener('click', () => {
            prevSlide();
            resetAutoSlide();
        });

        // Touch Events
        const touchStart = (event) => {
            isDragging = true;
            startPos = getPositionX(event);
            animationID = requestAnimationFrame(animation);
            track.style.transition = 'none'; // Disable transition while dragging
            clearInterval(autoSlideInterval);
        };

        const touchMove = (event) => {
            if (isDragging) {
                const currentPosition = getPositionX(event);
                currentTranslate = prevTranslate + currentPosition - startPos;
            }
        };

        const touchEnd = () => {
            isDragging = false;
            cancelAnimationFrame(animationID);
            track.style.transition = 'transform 0.5s cubic-bezier(0.4, 0, 0.2, 1)'; // Re-enable transition

            const movedBy = currentTranslate - prevTranslate;

            // Threshold for swipe
            if (movedBy < -50) {
                nextSlide();
            } else if (movedBy > 50) {
                prevSlide();
            } else {
                setPositionByIndex();
            }
            startAutoSlide();
        };

        const getPositionX = (event) => {
            return event.type.includes('mouse') ? event.pageX : event.touches[0].clientX;
        };

        const animation = () => {
            track.style.transform = `translateX(${currentTranslate}px)`;
            if (isDragging) requestAnimationFrame(animation);
        };

        slides.forEach((slide) => {
            // Prevent default drag behaviors
            slide.addEventListener('dragstart', (e) => e.preventDefault());

            // Touch events
            slide.addEventListener('touchstart', touchStart, { passive: true });
            slide.addEventListener('touchend', touchEnd);
            slide.addEventListener('touchmove', touchMove, { passive: true });

            // Mouse events
            slide.addEventListener('mousedown', touchStart);
            slide.addEventListener('mouseup', touchEnd);
            slide.addEventListener('mouseleave', () => {
                if(isDragging) touchEnd();
            });
            slide.addEventListener('mousemove', touchMove);
        });

        // Handle Resize
        window.addEventListener('resize', setPositionByIndex);

        // Auto Slide
        const startAutoSlide = () => {
            autoSlideInterval = setInterval(nextSlide, 6000); // 6 seconds
        };

        const resetAutoSlide = () => {
            clearInterval(autoSlideInterval);
            startAutoSlide();
        };

        startAutoSlide();
    }

    // ----------------------------------------------------------------------
    // FAQ Accordion
    // ----------------------------------------------------------------------
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const isExpanded = question.getAttribute('aria-expanded') === 'true';
            const answerId = question.getAttribute('aria-controls');
            const answerWrapper = document.getElementById(answerId);

            // Close all other FAQs (True accordion behavior)
            faqQuestions.forEach(q => {
                if (q !== question) {
                    q.setAttribute('aria-expanded', 'false');
                    const wrapper = document.getElementById(q.getAttribute('aria-controls'));
                    if (wrapper) {
                        wrapper.classList.remove('open');
                        wrapper.setAttribute('aria-hidden', 'true');
                    }
                }
            });

            // Toggle current FAQ
            question.setAttribute('aria-expanded', !isExpanded);
            if (answerWrapper) {
                if (!isExpanded) {
                    answerWrapper.classList.add('open');
                    answerWrapper.setAttribute('aria-hidden', 'false');
                } else {
                    answerWrapper.classList.remove('open');
                    answerWrapper.setAttribute('aria-hidden', 'true');
                }
            }
        });
    });

    // ----------------------------------------------------------------------
    // Scroll Reveal Animations
    // ----------------------------------------------------------------------
    const revealElements = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right, .reveal-zoom');
    
    const revealObserverOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, revealObserverOptions);

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // ----------------------------------------------------------------------
    // Contact Form Validation
    // ----------------------------------------------------------------------
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            let isValid = true;
            
            // Validate Name
            const nameInput = document.getElementById('name');
            if (nameInput.value.trim() === '') {
                nameInput.parentElement.classList.add('has-error');
                isValid = false;
            } else {
                nameInput.parentElement.classList.remove('has-error');
            }

            // Validate Email
            const emailInput = document.getElementById('email');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(emailInput.value.trim())) {
                emailInput.parentElement.classList.add('has-error');
                isValid = false;
            } else {
                emailInput.parentElement.classList.remove('has-error');
            }

            // Validate Subject
            const subjectInput = document.getElementById('subject');
            if (subjectInput.value.trim() === '') {
                subjectInput.parentElement.classList.add('has-error');
                isValid = false;
            } else {
                subjectInput.parentElement.classList.remove('has-error');
            }

            // Validate Message
            const messageInput = document.getElementById('message');
            if (messageInput.value.trim() === '') {
                messageInput.parentElement.classList.add('has-error');
                isValid = false;
            } else {
                messageInput.parentElement.classList.remove('has-error');
            }

            // Show Success
            if (isValid) {
                const successMsg = document.getElementById('form-success');
                successMsg.setAttribute('aria-hidden', 'false');
                contactForm.reset();
                
                // Hide success message after 5 seconds
                setTimeout(() => {
                    successMsg.setAttribute('aria-hidden', 'true');
                }, 5000);
            }
        });

        const formControls = contactForm.querySelectorAll('.form-control');
        formControls.forEach(control => {
            control.addEventListener('input', () => {
                control.parentElement.classList.remove('has-error');
            });
        });
    }

    // ----------------------------------------------------------------------
    // Custom Cursor
    // ----------------------------------------------------------------------
    const cursor = document.getElementById('custom-cursor');
    if (cursor) {
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        // Add hover effect to interactive elements
        const interactables = document.querySelectorAll('a, button, input, textarea, select, .service-card, .feature-block');
        interactables.forEach(el => {
            el.addEventListener('mouseenter', () => cursor.classList.add('cursor-hover'));
            el.addEventListener('mouseleave', () => cursor.classList.remove('cursor-hover'));
        });
    }

    // ----------------------------------------------------------------------
    // Button Ripple Effect
    // ----------------------------------------------------------------------
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const circle = document.createElement('span');
            circle.classList.add('ripple');
            
            const diameter = Math.max(rect.width, rect.height);
            circle.style.width = circle.style.height = diameter + 'px';
            circle.style.left = (x - diameter / 2) + 'px';
            circle.style.top = (y - diameter / 2) + 'px';
            
            const existingRipple = this.querySelector('.ripple');
            if (existingRipple) {
                existingRipple.remove();
            }
            
            this.appendChild(circle);
            
            setTimeout(() => {
                circle.remove();
            }, 600);
        });
    });
});
