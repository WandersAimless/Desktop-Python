document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll("section");
    window.addEventListener("scroll", function() {
        sections.forEach(function(section) {
            if (section.getBoundingClientRect().top < window.innerHeight) {
                section.classList.add("visible");
            }
        });
    });
});
