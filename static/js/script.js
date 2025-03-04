// Ensure the script runs only after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    console.log("Script loaded!");

    // Highlight active navigation link
    let currentUrl = window.location.pathname;
    let navLinks = document.querySelectorAll("nav a");

    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentUrl) {
            link.classList.add("active-link"); // Add highlight class
        }
    });

    // Help & Support Search Bar
    const searchInput = document.getElementById('faqSearch');
    if (searchInput) { // Ensure element exists
        searchInput.addEventListener('input', function () {
            let searchText = this.value.toLowerCase();
            let faqs = document.querySelectorAll('.faq-item');

            faqs.forEach(faq => {
                let question = faq.querySelector('h2').textContent.toLowerCase();
                faq.style.display = question.includes(searchText) ? 'block' : 'none';
            });
        });
    }
});

// Move this function outside so it's globally accessible
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
