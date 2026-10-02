with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the problematic overrides
css = css.replace("""
.signage-card-gold {
    animation: pulseGlowGoldStatic 4s ease-in-out infinite alternate !important;
}
.signage-card-amber {
    animation: pulseGlowAmberStatic 4s ease-in-out infinite alternate !important;
}

/* Dynamic Entrance animations strictly for the active slide container */
@keyframes slideInUp {
    0% { opacity: 0; transform: translateY(50px) scale(0.98); }
    100% { opacity: 1; transform: translateY(0) scale(1); }
}
.slide.active > div {
    animation: slideInUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards !important;
}""", """
/* Apply continuous glows */
.signage-card-gold {
    box-shadow: 0 0 50px rgba(212, 175, 55, 0.4);
    animation: pulseGlowGoldStatic 4s ease-in-out infinite alternate;
}
.signage-card-amber {
    box-shadow: 0 0 50px rgba(245, 158, 11, 0.4);
    animation: pulseGlowAmberStatic 4s ease-in-out infinite alternate;
}

/* Dynamic Entrance animations strictly for the active slide container */
@keyframes slideInUp {
    0% { opacity: 0; transform: translateY(60px) scale(0.95); }
    100% { opacity: 1; transform: translateY(0) scale(1); }
}

.slide.active .signage-card-gold {
    animation: slideInUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards, pulseGlowGoldStatic 4s ease-in-out infinite alternate !important;
}
.slide.active .signage-card-amber {
    animation: slideInUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards, pulseGlowAmberStatic 4s ease-in-out infinite alternate !important;
}
""")

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
