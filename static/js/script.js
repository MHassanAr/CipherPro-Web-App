document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const plaintextInput = document.getElementById('plaintext');
    const algorithmSelect = document.getElementById('algorithm');
    const encryptBtn = document.getElementById('encrypt-btn');
    const decryptBtn = document.getElementById('decrypt-btn');
    const resultOutput = document.getElementById('result');
    const copyBtn = document.getElementById('copy-btn');
    const errorMessage = document.getElementById('error-message');

    // Event Listeners
    encryptBtn.addEventListener('click', handleEncryption);
    decryptBtn.addEventListener('click', handleDecryption);
    copyBtn.addEventListener('click', copyToClipboard);

    // Functions for encryption/decryption
    function handleEncryption() {
        const text = plaintextInput.value.trim();
        const algorithm = algorithmSelect.value;

        if (!validateInput(text, algorithm)) return;

        fetchEncryptedData('/encrypt', text, algorithm);
    }

    function handleDecryption() {
        const text = plaintextInput.value.trim();
        const algorithm = algorithmSelect.value;

        if (!validateInput(text, algorithm)) return;

        fetchEncryptedData('/decrypt', text, algorithm);
    }

    function validateInput(text, algorithm) {
        hideError();

        if (!text) {
            showError('Please enter some text to encrypt/decrypt');
            return false;
        }

        if (!algorithm) {
            showError('Please select an encryption algorithm');
            return false;
        }

        return true;
    }

    function fetchEncryptedData(endpoint, text, algorithm) {
        fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                algorithm: algorithm
            })
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(data => {
                    throw new Error(data.error || 'Something went wrong');
                });
            }
            return response.json();
        })
        .then(data => {
            resultOutput.value = data.result;
        })
        .catch(error => {
            showError(error.message);
        });
    }

    function copyToClipboard() {
        resultOutput.select();
        document.execCommand('copy');

        // Visual feedback
        const originalText = copyBtn.textContent;
        copyBtn.textContent = 'Copied!';
        setTimeout(() => {
            copyBtn.textContent = originalText;
        }, 2000);
    }

    // Helper functions for displaying errors
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.remove('hidden');
    }

    function hideError() {
        errorMessage.classList.add('hidden');
    }
});