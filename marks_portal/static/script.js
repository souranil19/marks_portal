// Mobile Menu Functionality
class MobileMenu {
  constructor() {
    this.menuBtn = document.getElementById("mobileMenuBtn");
    this.mobileNav = document.getElementById("mobileNav");
    this.menuIcon = document.getElementById("menuIcon");
    this.mobileNavLinks = document.querySelectorAll(".mobile-nav-link");
    this.mobileDropdownToggle = document.querySelector(".mobile-dropdown-toggle");
    this.mobileDropdown = document.querySelector(".mobile-nav-dropdown");

    this.init();
  }

  init() {
    // Toggle mobile menu when button is clicked
    this.menuBtn.addEventListener("click", () => {
      this.toggleMenu();
    });

    // Close mobile menu when a link is clicked
    this.mobileNavLinks.forEach((link) => {
      link.addEventListener("click", () => {
        // Don't close menu if it's the dropdown toggle
        if (!link.classList.contains("mobile-dropdown-toggle")) {
          this.closeMenu();
        }
      });
    });

    // Handle mobile dropdown toggle
    if (this.mobileDropdownToggle) {
      this.mobileDropdownToggle.addEventListener("click", (e) => {
        e.preventDefault();
        this.toggleMobileDropdown();
      });
    }

    // Close mobile menu when clicking outside
    document.addEventListener("click", (e) => {
      if (
        !this.menuBtn.contains(e.target) &&
        !this.mobileNav.contains(e.target)
      ) {
        this.closeMenu();
      }
    });

    // Close mobile menu on escape key
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        this.closeMenu();
      }
    });

    // Close mobile menu on window resize
    window.addEventListener("resize", () => {
      if (window.innerWidth >= 768) {
        this.closeMenu();
      }
    });
  }

  toggleMenu() {
    const isOpen = this.mobileNav.classList.contains("active");

    if (isOpen) {
      this.closeMenu();
    } else {
      this.openMenu();
    }
  }

  openMenu() {
    this.mobileNav.classList.add("active");
    this.menuIcon.classList.remove("fa-bars");
    this.menuIcon.classList.add("fa-times");
    document.body.style.overflow = "hidden"; // Prevent body scroll
  }

  closeMenu() {
    this.mobileNav.classList.remove("active");
    this.menuIcon.classList.remove("fa-times");
    this.menuIcon.classList.add("fa-bars");
    document.body.style.overflow = ""; // Restore body scroll
    
    // Close mobile dropdown when closing menu
    if (this.mobileDropdown) {
      this.mobileDropdown.classList.remove("active");
    }
  }

  toggleMobileDropdown() {
    if (this.mobileDropdown) {
      this.mobileDropdown.classList.toggle("active");
    }
  }
}

// Smooth Scrolling for Anchor Links
class SmoothScroll {
  constructor() {
    this.init();
  }

  init() {
    // Get all anchor links that start with #
    const anchorLinks = document.querySelectorAll('a[href^="#"]');

    anchorLinks.forEach((link) => {
      link.addEventListener("click", (e) => {
        const href = link.getAttribute("href");

        // Skip if it's just # or empty
        if (href === "#" || href === "") {
          return;
        }

        // Find the target element
        const targetElement = document.querySelector(href);

        if (targetElement) {
          e.preventDefault();

          // Calculate offset for fixed header
          const headerHeight = document.querySelector(".header").offsetHeight;
          const targetPosition = targetElement.offsetTop - headerHeight - 20;

          // Smooth scroll to target
          window.scrollTo({
            top: targetPosition,
            behavior: "smooth",
          });
        }
      });
    });
  }
}

// Header Scroll Effect
class HeaderScrollEffect {
  constructor() {
    this.header = document.querySelector(".header");
    this.lastScrollY = window.scrollY;

    this.init();
  }

  init() {
    window.addEventListener("scroll", () => {
      this.handleScroll();
    });
  }

  handleScroll() {
    const currentScrollY = window.scrollY;

    if (currentScrollY > 100) {
      this.header.style.backgroundColor = "rgba(255, 255, 255, 0.95)";
      this.header.style.backdropFilter = "blur(10px)";
    } else {
      this.header.style.backgroundColor = "var(--white)";
      this.header.style.backdropFilter = "none";
    }

    this.lastScrollY = currentScrollY;
  }
}

// Intersection Observer for Animations
class ScrollAnimations {
  constructor() {
    this.observerOptions = {
      threshold: 0.1,
      rootMargin: "0px 0px -50px 0px",
    };

    this.init();
  }

  init() {
    // Create intersection observer
    this.observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("animate-fade-in");
        }
      });
    }, this.observerOptions);

    // Observe elements that should animate
    const animateElements = document.querySelectorAll(
      ".facility-card, .achievement-card, .news-card, .value-item, .stat-item",
    );

    animateElements.forEach((el) => {
      this.observer.observe(el);
    });
  }
}

// Form Validation (for future contact forms)
class FormValidation {
  static validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  static validatePhone(phone) {
    const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
    return phoneRegex.test(phone.replace(/[\s\-\(\)]/g, ""));
  }

  static validateRequired(value) {
    return value.trim().length > 0;
  }
}

// Utility Functions
class Utils {
  // Debounce function for performance optimization
  static debounce(func, wait) {
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

  // Throttle function for scroll events
  static throttle(func, limit) {
    let inThrottle;
    return function () {
      const args = arguments;
      const context = this;
      if (!inThrottle) {
        func.apply(context, args);
        inThrottle = true;
        setTimeout(() => (inThrottle = false), limit);
      }
    };
  }

  // Check if element is in viewport
  static isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <=
        (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }

  // Get scroll position
  static getScrollPosition() {
    return {
      x: window.pageXOffset || document.documentElement.scrollLeft,
      y: window.pageYOffset || document.documentElement.scrollTop,
    };
  }
}

// Loading Indicator
class LoadingIndicator {
  constructor() {
    this.init();
  }

  init() {
    // Add loading class to body
    document.body.classList.add("loading");

    // Remove loading class when page is fully loaded
    window.addEventListener("load", () => {
      document.body.classList.remove("loading");

      // Add fade-in animation to main content
      const mainContent = document.querySelectorAll("section");
      mainContent.forEach((section, index) => {
        setTimeout(() => {
          section.style.opacity = "1";
          section.style.transform = "translateY(0)";
        }, index * 100);
      });
    });
  }
}

// Enhanced Error Handling
class ErrorHandler {
  static logError(error, context = "") {
    console.error(`Error in ${context}:`, error);

    // In production, you might want to send errors to a logging service
    // this.sendToLoggingService(error, context);
  }

  static handleAsyncError(asyncFunction) {
    return async (...args) => {
      try {
        return await asyncFunction(...args);
      } catch (error) {
        this.logError(error, asyncFunction.name);
        throw error;
      }
    };
  }
}

// Performance Monitoring
class PerformanceMonitor {
  constructor() {
    this.navigationTiming = performance.getEntriesByType("navigation")[0];
    this.init();
  }

  init() {
    // Log performance metrics when page loads
    window.addEventListener("load", () => {
      setTimeout(() => {
        this.logPerformanceMetrics();
      }, 0);
    });
  }

  logPerformanceMetrics() {
    if (this.navigationTiming) {
      const metrics = {
        pageLoadTime:
          this.navigationTiming.loadEventEnd -
          this.navigationTiming.loadEventStart,
        domContentLoaded:
          this.navigationTiming.domContentLoadedEventEnd -
          this.navigationTiming.domContentLoadedEventStart,
        timeToFirstByte:
          this.navigationTiming.responseStart -
          this.navigationTiming.requestStart,
        domInteractive:
          this.navigationTiming.domInteractive -
          this.navigationTiming.navigationStart,
      };

      console.log("Performance Metrics:", metrics);
    }
  }
}

// Accessibility Features
class AccessibilityEnhancements {
  constructor() {
    this.init();
  }

  init() {
    // Add skip to content link
    this.addSkipToContentLink();

    // Improve keyboard navigation
    this.enhanceKeyboardNavigation();

    // Add ARIA labels where needed
    this.addAriaLabels();
  }

  addSkipToContentLink() {
    const skipLink = document.createElement("a");
    skipLink.href = "#main-content";
    skipLink.textContent = "Skip to main content";
    skipLink.className = "skip-link";
    skipLink.style.cssText = `
      position: absolute;
      top: -40px;
      left: 6px;
      background: var(--navy);
      color: white;
      padding: 8px;
      text-decoration: none;
      border-radius: 4px;
      z-index: 100;
      transition: top 0.3s;
    `;

    skipLink.addEventListener("focus", () => {
      skipLink.style.top = "6px";
    });

    skipLink.addEventListener("blur", () => {
      skipLink.style.top = "-40px";
    });

    document.body.insertBefore(skipLink, document.body.firstChild);
  }

  enhanceKeyboardNavigation() {
    // Ensure all interactive elements are keyboard accessible
    const interactiveElements = document.querySelectorAll(
      "button, a, input, select, textarea, [tabindex]",
    );

    interactiveElements.forEach((element) => {
      if (
        !element.hasAttribute("tabindex") &&
        !element.href &&
        element.tagName !== "INPUT"
      ) {
        element.setAttribute("tabindex", "0");
      }
    });
  }

  addAriaLabels() {
    // Add ARIA labels to navigation
    const nav = document.querySelector(".nav-desktop");
    if (nav) {
      nav.setAttribute("aria-label", "Main navigation");
    }

    const mobileNav = document.querySelector(".mobile-nav");
    if (mobileNav) {
      mobileNav.setAttribute("aria-label", "Mobile navigation");
    }

    // Add ARIA labels to social media links
    const socialLinks = document.querySelectorAll(".social-links a");
    socialLinks.forEach((link, index) => {
      const platforms = ["Facebook", "Twitter", "Instagram", "YouTube"];
      if (platforms[index]) {
        link.setAttribute("aria-label", `Visit our ${platforms[index]} page`);
      }
    });
  }
}

// Desktop Dropdown Functionality
class DesktopDropdown {
  constructor() {
    this.dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    this.init();
  }

  init() {
    this.dropdownToggles.forEach(toggle => {
      const dropdown = toggle.closest('.nav-dropdown');
      
      // Add click functionality as backup
      toggle.addEventListener('click', (e) => {
        e.preventDefault();
        
        // Close other dropdowns
        document.querySelectorAll('.nav-dropdown').forEach(otherDropdown => {
          if (otherDropdown !== dropdown) {
            otherDropdown.classList.remove('active');
          }
        });
        
        // Toggle current dropdown
        dropdown.classList.toggle('active');
      });
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.nav-dropdown')) {
        document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
          dropdown.classList.remove('active');
        });
      }
    });
  }
}

// Initialize all components when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
  try {
    // Core functionality
    new MobileMenu();
    new SmoothScroll();
    new HeaderScrollEffect();
    new ScrollAnimations();
    new LoadingIndicator();
    new AccessibilityEnhancements();
    new DesktopDropdown();

    // Performance monitoring (optional)
    if (window.location.hostname !== "localhost") {
      new PerformanceMonitor();
    }

    console.log("Vidyavihar School website initialized successfully");
  } catch (error) {
    ErrorHandler.logError(error, "Initialization");
  }
});

// Service Worker Registration (for future PWA capabilities)
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    // Uncomment when you add a service worker
    // navigator.serviceWorker.register('/sw.js')
    //   .then(registration => {
    //     console.log('SW registered: ', registration);
    //   })
    //   .catch(registrationError => {
    //     console.log('SW registration failed: ', registrationError);
    //   });
  });
}

// Export classes for potential future use
window.VidyaviharSchool = {
  MobileMenu,
  SmoothScroll,
  HeaderScrollEffect,
  ScrollAnimations,
  FormValidation,
  Utils,
  ErrorHandler,
  PerformanceMonitor,
  AccessibilityEnhancements,
};
