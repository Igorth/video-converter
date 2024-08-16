// Toggle theme button
const themeToggle = document.getElementById('theme-toggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});

// Feedback handling
const form = document.getElementById('upload-form');
const feedback = document.getElementById('feedback');

form.addEventListener('submit', function(event) {
    //event.preventDefault();

    feedback.className = '';
    feedback.textContent = 'Uploading...';
    feedback.classList.add('animate__animated', 'animate__fadeIn', 'text-info');

    // Simulate file upload
    setTimeout(() => {
        feedback.textContent = 'File uploaded and converted successfully!';
        feedback.classList.remove('text-info');
        feedback.classList.add('text-success');
    }, 2000)
})