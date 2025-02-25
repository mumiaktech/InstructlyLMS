//Navigation toggle code
document.addEventListener("DOMContentLoaded", function () {
    // Get the current URL path
    let currentUrl = window.location.pathname;

    // Get all navigation links
    let navLinks = document.querySelectorAll("nav a");

    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentUrl) {
            link.classList.add("active-link"); // Add highlight class
        }
    });
});


//FAQ toggle code
function toggleFaq(button) {
    const answer = button.nextElementSibling;
    const icon = button.querySelector('span');
    if (answer.classList.contains('hidden')) {
        answer.classList.remove('hidden');
        icon.textContent = '-';
    } else {
        answer.classList.add('hidden');
        icon.textContent = '+';
    }
}