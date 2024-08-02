// static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Example: Add a click event to buttons
    const buttons = document.querySelectorAll('button');
    
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            alert('Button clicked!');
        });
    });
});
