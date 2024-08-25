document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('captcha-form').addEventListener('submit', function(event) {
        event.preventDefault();
        let response = grecaptcha.getResponse();
        if (response.length === 0) {
            document.getElementById('captcha-message').innerText = "Please complete the CAPTCHA";
            return;
        }

        fetch('/verify-captcha', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ response: response })
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                window.location.href = '/result';
            } else {
                document.getElementById('captcha-message').innerText = "CAPTCHA verification failed. Please try again.";
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('captcha-message').innerText = "An error occurred. Please try again.";
        });
    });
});
