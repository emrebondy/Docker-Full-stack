document.addEventListener("DOMContentLoaded", async function() {
    try {
        const response = await fetch('/api/hello');

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        document.getElementById('responseMessage').innerText = data.message;

    } catch (error) {
        console.error('Error:', error);
        document.getElementById('responseMessage').innerText = 'Error: Could not fetch data';
    }
});
