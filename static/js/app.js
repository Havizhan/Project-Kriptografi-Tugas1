/**
 * Kriptosistem Sederhana - JavaScript Application
 * Handles all frontend functionality for the cryptography web app
 */

// Global variables
let selectedFile = null;
let currentResult = '';

// Cipher information mapping
const cipherInfoMap = {
    'shift': {
        info: '<strong>Shift Cipher:</strong> Menggeser setiap huruf sejumlah posisi tertentu dalam alfabet.<br><strong>Kunci:</strong> Angka (0-25) yang menunjukkan jumlah pergeseran.',
        help: 'Masukkan angka untuk shift cipher (contoh: 3)'
    },
    'substitution': {
        info: '<strong>Substitution Cipher:</strong> Mengganti setiap huruf dengan huruf lain berdasarkan tabel substitusi.<br><strong>Kunci:</strong> String 26 huruf yang menentukan substitusi.',
        help: 'Masukkan 26 huruf unik untuk substitusi (contoh: ZYXWVUTSRQPONMLKJIHGFEDCBA)'
    },
    'affine': {
        info: '<strong>Affine Cipher:</strong> Menggunakan fungsi matematika E(x) = (ax + b) mod 26.<br><strong>Kunci:</strong> Dua angka a dan b (format: a,b).',
        help: 'Masukkan dua angka dipisahkan koma (contoh: 5,8). a harus coprime dengan 26.'
    },
    'vigenere': {
        info: '<strong>Vigenere Cipher:</strong> Menggunakan kunci berulang untuk enkripsi.<br><strong>Kunci:</strong> String huruf yang akan diulang.',
        help: 'Masukkan kata kunci (contoh: KEYWORD)'
    },
    'hill': {
        info: '<strong>Hill Cipher:</strong> Menggunakan matriks untuk enkripsi blok huruf.<br><strong>Kunci:</strong> String yang akan dikonversi menjadi matriks.',
        help: 'Masukkan string untuk matriks kunci (contoh: GYBNQKURP untuk matriks 3x3)'
    },
    'permutation': {
        info: '<strong>Permutation Cipher:</strong> Mengatur ulang posisi huruf dalam blok.<br><strong>Kunci:</strong> Urutan posisi (contoh: 2,0,1).',
        help: 'Masukkan urutan posisi dipisahkan koma (contoh: 2,0,1)'
    }
};

/**
 * Initialize the application when DOM is loaded
 */
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

/**
 * Initialize application components
 */
function initializeApp() {
    updateCipherInfo();
    setupEventListeners();
    setupFileUpload();
}

/**
 * Setup event listeners for various UI elements
 */
function setupEventListeners() {
    // Cipher type change
    const cipherTypeSelect = document.getElementById('cipherType');
    if (cipherTypeSelect) {
        cipherTypeSelect.addEventListener('change', updateCipherInfo);
    }

    // Input mode toggle
    const inputModeRadios = document.querySelectorAll('input[name="inputMode"]');
    inputModeRadios.forEach(radio => {
        radio.addEventListener('change', toggleInputMode);
    });

    // Format options
    const formatRadios = document.querySelectorAll('input[name="format"]');
    formatRadios.forEach(radio => {
        radio.addEventListener('change', formatResult);
    });
}

/**
 * Setup file upload functionality
 */
function setupFileUpload() {
    const fileUploadArea = document.querySelector('.file-upload-area');
    const fileInput = document.getElementById('fileInput');

    if (fileUploadArea && fileInput) {
        // Click to upload
        fileUploadArea.addEventListener('click', () => {
            fileInput.click();
        });

        // Drag and drop
        fileUploadArea.addEventListener('dragover', handleDragOver);
        fileUploadArea.addEventListener('dragleave', handleDragLeave);
        fileUploadArea.addEventListener('drop', handleDrop);

        // File selection
        fileInput.addEventListener('change', handleFileSelect);
    }
}

/**
 * Update cipher information based on selection
 */
function updateCipherInfo() {
    const cipherType = document.getElementById('cipherType').value;
    const keyHelp = document.getElementById('keyHelp');
    const cipherInfo = document.getElementById('cipherInfo');
    
    if (cipherInfoMap[cipherType]) {
        cipherInfo.innerHTML = cipherInfoMap[cipherType].info;
        if (keyHelp) {
            keyHelp.textContent = cipherInfoMap[cipherType].help;
        }
    }
}

/**
 * Toggle between text and file input modes
 */
function toggleInputMode() {
    const textSection = document.getElementById('textInputSection');
    const fileSection = document.getElementById('fileInputSection');
    const inputMode = document.querySelector('input[name="inputMode"]:checked').value;
    
    if (inputMode === 'text') {
        textSection.style.display = 'block';
        fileSection.style.display = 'none';
    } else {
        textSection.style.display = 'none';
        fileSection.style.display = 'block';
    }
}

/**
 * Handle file selection
 */
function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        selectedFile = file;
        displayFileInfo(file);
    }
}

/**
 * Handle drag over event
 */
function handleDragOver(event) {
    event.preventDefault();
    event.currentTarget.classList.add('dragover');
}

/**
 * Handle drag leave event
 */
function handleDragLeave(event) {
    event.currentTarget.classList.remove('dragover');
}

/**
 * Handle drop event
 */
function handleDrop(event) {
    event.preventDefault();
    event.currentTarget.classList.remove('dragover');
    
    const files = event.dataTransfer.files;
    if (files.length > 0) {
        selectedFile = files[0];
        displayFileInfo(files[0]);
    }
}

/**
 * Display file information
 */
function displayFileInfo(file) {
    const fileName = document.getElementById('fileName');
    const fileSize = document.getElementById('fileSize');
    const fileInfo = document.getElementById('fileInfo');
    
    if (fileName && fileSize && fileInfo) {
        fileName.textContent = file.name;
        fileSize.textContent = formatFileSize(file.size);
        fileInfo.style.display = 'block';
    }
}

/**
 * Format file size for display
 */
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

/**
 * Show loading indicator
 */
function showLoading() {
    const loadingIndicator = document.getElementById('loadingIndicator');
    const resultsSection = document.getElementById('resultsSection');
    
    if (loadingIndicator) {
        loadingIndicator.style.display = 'block';
    }
    if (resultsSection) {
        resultsSection.style.display = 'none';
    }
}

/**
 * Hide loading indicator
 */
function hideLoading() {
    const loadingIndicator = document.getElementById('loadingIndicator');
    if (loadingIndicator) {
        loadingIndicator.style.display = 'none';
    }
}

/**
 * Show results
 */
function showResults(result, isFile = false) {
    currentResult = result;
    const resultText = document.getElementById('resultText');
    const resultsSection = document.getElementById('resultsSection');
    const downloadSection = document.getElementById('downloadSection');
    const formatSection = document.getElementById('formatSection');
    
    if (resultText) {
        resultText.textContent = result;
        resultText.classList.add('result-text');
    }
    
    if (resultsSection) {
        resultsSection.style.display = 'block';
        resultsSection.classList.add('fade-in');
    }
    
    if (isFile) {
        if (downloadSection) {
            downloadSection.style.display = 'block';
        }
        if (formatSection) {
            formatSection.style.display = 'none';
        }
    } else {
        if (downloadSection) {
            downloadSection.style.display = 'none';
        }
        if (formatSection) {
            formatSection.style.display = 'block';
        }
    }
}

/**
 * Show error message
 */
function showError(message) {
    // Create error alert
    const errorAlert = document.createElement('div');
    errorAlert.className = 'alert alert-danger error-message';
    errorAlert.innerHTML = `
        <i class="fas fa-exclamation-triangle me-2"></i>
        ${message}
    `;
    
    // Insert at top of main container
    const mainContainer = document.querySelector('.main-container');
    if (mainContainer) {
        mainContainer.insertBefore(errorAlert, mainContainer.firstChild);
        
        // Auto remove after 5 seconds
        setTimeout(() => {
            if (errorAlert.parentNode) {
                errorAlert.parentNode.removeChild(errorAlert);
            }
        }, 5000);
    }
}

/**
 * Show success message
 */
function showSuccess(message) {
    // Create success alert
    const successAlert = document.createElement('div');
    successAlert.className = 'alert alert-success success-message';
    successAlert.innerHTML = `
        <i class="fas fa-check-circle me-2"></i>
        ${message}
    `;
    
    // Insert at top of main container
    const mainContainer = document.querySelector('.main-container');
    if (mainContainer) {
        mainContainer.insertBefore(successAlert, mainContainer.firstChild);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            if (successAlert.parentNode) {
                successAlert.parentNode.removeChild(successAlert);
            }
        }, 3000);
    }
}

/**
 * Encrypt function
 */
async function encrypt() {
    const cipherType = document.getElementById('cipherType').value;
    const key = document.getElementById('keyInput').value;
    const inputMode = document.querySelector('input[name="inputMode"]:checked').value;
    
    if (!key) {
        showError('Masukkan kunci terlebih dahulu!');
        return;
    }
    
    showLoading();
    
    try {
        if (inputMode === 'text') {
            await encryptText(cipherType, key);
        } else {
            await encryptFile(cipherType, key);
        }
    } catch (error) {
        showError('Terjadi kesalahan: ' + error.message);
    }
    
    hideLoading();
}

/**
 * Encrypt text
 */
async function encryptText(cipherType, key) {
    const text = document.getElementById('plainText').value;
    if (!text) {
        showError('Masukkan teks terlebih dahulu!');
        return;
    }
    
    const response = await fetch('/encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            cipher_type: cipherType,
            text: text,
            key: key
        })
    });
    
    const result = await response.json();
    
    if (result.success) {
        showResults(result.encrypted_text);
        showSuccess('Teks berhasil dienkripsi!');
    } else {
        showError('Error: ' + result.error);
    }
}

/**
 * Encrypt file
 */
async function encryptFile(cipherType, key) {
    if (!selectedFile) {
        showError('Pilih file terlebih dahulu!');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', selectedFile);
    formData.append('cipher_type', cipherType);
    formData.append('key', key);
    
    const response = await fetch('/encrypt', {
        method: 'POST',
        body: formData
    });
    
    const result = await response.json();
    
    if (result.success) {
        showResults('File berhasil dienkripsi!', true);
        window.encryptedFilePath = result.file_path;
        window.encryptedFileName = result.file_name;
        showSuccess('File berhasil dienkripsi!');
    } else {
        showError('Error: ' + result.error);
    }
}

/**
 * Decrypt function
 */
async function decrypt() {
    const cipherType = document.getElementById('cipherType').value;
    const key = document.getElementById('keyInput').value;
    const inputMode = document.querySelector('input[name="inputMode"]:checked').value;
    
    if (!key) {
        showError('Masukkan kunci terlebih dahulu!');
        return;
    }
    
    showLoading();
    
    try {
        if (inputMode === 'text') {
            await decryptText(cipherType, key);
        } else {
            await decryptFile(cipherType, key);
        }
    } catch (error) {
        showError('Terjadi kesalahan: ' + error.message);
    }
    
    hideLoading();
}

/**
 * Decrypt text
 */
async function decryptText(cipherType, key) {
    const text = document.getElementById('plainText').value;
    if (!text) {
        showError('Masukkan teks terlebih dahulu!');
        return;
    }
    
    const response = await fetch('/decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            cipher_type: cipherType,
            text: text,
            key: key
        })
    });
    
    const result = await response.json();
    
    if (result.success) {
        showResults(result.decrypted_text);
        showSuccess('Teks berhasil didekripsi!');
    } else {
        showError('Error: ' + result.error);
    }
}

/**
 * Decrypt file
 */
async function decryptFile(cipherType, key) {
    if (!selectedFile) {
        showError('Pilih file terlebih dahulu!');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', selectedFile);
    formData.append('cipher_type', cipherType);
    formData.append('key', key);
    formData.append('original_file_name', selectedFile.name);
    
    const response = await fetch('/decrypt', {
        method: 'POST',
        body: formData
    });
    
    const result = await response.json();
    
    if (result.success) {
        showResults('File berhasil didekripsi!', true);
        window.decryptedFilePath = result.file_path;
        window.decryptedFileName = result.file_name;
        showSuccess('File berhasil didekripsi!');
    } else {
        showError('Error: ' + result.error);
    }
}

/**
 * Format result text
 */
function formatResult() {
    const format = document.querySelector('input[name="format"]:checked').value;
    const resultText = document.getElementById('resultText');
    
    if (!resultText || !currentResult) return;
    
    let formattedText = currentResult;
    
    if (format === 'group5') {
        // Group into 5-character chunks
        formattedText = currentResult.replace(/\s/g, '').replace(/(.{5})/g, '$1 ').trim();
    } else {
        // Remove all spaces
        formattedText = currentResult.replace(/\s/g, '');
    }
    
    resultText.textContent = formattedText;
}

/**
 * Download result file
 */
function downloadResult() {
    const filePath = window.encryptedFilePath || window.decryptedFilePath;
    const fileName = window.encryptedFileName || window.decryptedFileName;
    
    if (filePath) {
        window.open(`/download/${encodeURIComponent(filePath)}`, '_blank');
        showSuccess('File berhasil didownload!');
    } else {
        showError('Tidak ada file untuk didownload!');
    }
}

/**
 * Clear all inputs and results
 */
function clearAll() {
    // Clear text input
    const plainText = document.getElementById('plainText');
    if (plainText) {
        plainText.value = '';
    }
    
    // Clear key input
    const keyInput = document.getElementById('keyInput');
    if (keyInput) {
        keyInput.value = '';
    }
    
    // Clear file selection
    selectedFile = null;
    const fileInput = document.getElementById('fileInput');
    if (fileInput) {
        fileInput.value = '';
    }
    
    // Hide file info
    const fileInfo = document.getElementById('fileInfo');
    if (fileInfo) {
        fileInfo.style.display = 'none';
    }
    
    // Hide results
    const resultsSection = document.getElementById('resultsSection');
    if (resultsSection) {
        resultsSection.style.display = 'none';
    }
    
    // Reset to text mode
    const textMode = document.getElementById('textMode');
    if (textMode) {
        textMode.checked = true;
        toggleInputMode();
    }
    
    showSuccess('Semua input telah dibersihkan!');
}

/**
 * Copy result to clipboard
 */
async function copyResult() {
    const resultText = document.getElementById('resultText');
    if (!resultText || !resultText.textContent) {
        showError('Tidak ada hasil untuk disalin!');
        return;
    }
    
    try {
        await navigator.clipboard.writeText(resultText.textContent);
        showSuccess('Hasil berhasil disalin ke clipboard!');
    } catch (error) {
        showError('Gagal menyalin ke clipboard!');
    }
}

// Export functions for global access
window.encrypt = encrypt;
window.decrypt = decrypt;
window.formatResult = formatResult;
window.downloadResult = downloadResult;
window.clearAll = clearAll;
window.copyResult = copyResult;
