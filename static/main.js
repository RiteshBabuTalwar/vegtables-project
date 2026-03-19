// main.js - Handles image preview on the index page
document.addEventListener('DOMContentLoaded', () => {
    const uploadInput = document.querySelector('input[type="file"]');
    if (uploadInput) {
        uploadInput.addEventListener('change', function() {
            if (this.files && this.files[0]) {
                console.log("File selected: " + this.files[0].name);
                // Additional UI logic for previews can be added here
            }
        });
    }
});