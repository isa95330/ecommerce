// scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const title = document.querySelector(".title");
    const letters = document.querySelectorAll(".letter");
    const navbar = document.querySelector(".navbar");
    const intro = document.querySelector(".intro");

    // GSAP Timeline
    const tl = gsap.timeline({
        onComplete: function () {
            console.log('Animation terminée');
            // Afficher la barre de navigation après l'animation
            gsap.to(navbar, {
                opacity: 1,
                y: 0,
                duration: 0.7, /* Réduit la durée pour une transition plus rapide */
                onComplete: function() {
                    navbar.classList.add('visible');
                }
            });

            // Cacher la section intro après l'animation
            gsap.to(intro, {
                duration: 0.5,
                height: 0,
                opacity: 0,
                onComplete: function () {
                    intro.classList.add('hidden');
                }
            });
        }
    });

    tl
        .fromTo(letters,
            {
                x: -100,
                opacity: 0,
            },
            {
                x: 0,
                opacity: 1,
                stagger: 0.33,
                delay: 0.7
            }
        )
        .to(title, {
            y: 45,
            delay: 0.7
        })
        .to(letters, {
            margin: "0 5vw",
            delay: 0.8,
            duration: 0.5
        })
        .to(letters, {
            margin: "0",
            delay: 0.8,
            duration: 0.5
        })
        .to(letters, {
            x: -title.clientWidth,
            delay: 1,
            duration: 2,
            rotate: -360
        })
        .to(intro, {
            height: "2vh", // Réduit la hauteur de la section
            delay: 1,
            duration: 1
        })
        .to(intro, {
            opacity: 0,
            delay: 1.5,
            duration: 1
        })
        .to(window, {
            duration: 0.5,
            scrollTo: "#nextSection"
        })
        .to("#nextSection", {
            backgroundColor: "#000",
            color: "#fff",
            duration: 0.2
        })
        .to(title, {
            y: 0
        })
        .to(letters, {
            x: 0,
            delay: 1,
            duration: 2
        });
});

document.querySelectorAll('.navbar a').forEach(link => {
  link.addEventListener('mouseenter', onEnter);
  link.addEventListener('mouseleave', onLeave);
});



document.addEventListener('DOMContentLoaded', function () {
            const loginIcon = document.getElementById('login-icon');
            const popup = document.getElementById('login-popup');
            const closeBtn = document.getElementById('close-popup');

            if (loginIcon && popup && closeBtn) {
                // Afficher la popup
                loginIcon.addEventListener('click', function () {
                    popup.style.display = 'flex';
                    popup.setAttribute('aria-hidden', 'false');
                });

                // Fermer la popup
                closeBtn.addEventListener('click', function () {
                    popup.style.display = 'none';
                    popup.setAttribute('aria-hidden', 'true');
                });

                // Fermer la popup lorsque l'utilisateur clique en dehors du contenu
                window.addEventListener('click', function (event) {
                    if (event.target === popup) {
                        popup.style.display = 'none';
                        popup.setAttribute('aria-hidden', 'true');
                    }
                });
            } else {
                console.error('Un ou plusieurs éléments nécessaires n\'ont pas été trouvés.');
            }
        });

// script.js
document.addEventListener('DOMContentLoaded', function() {
    const introSection = document.querySelector('.intro');
    const navbar = document.querySelector('.navbar');
    const title = document.querySelector('.title');

    if (introSection && navbar && title) {
        // Observer la fin de l'animation du texte
        title.addEventListener('animationend', function() {
            setTimeout(() => {
                introSection.style.display = 'none'; // Cacher la section après la disparition du texte
                navbar.classList.remove('hidden');
                navbar.classList.add('visible');
            }, 400); // Délai pour s'assurer que l'animation de disparition du texte est terminée
        });
    }
});

