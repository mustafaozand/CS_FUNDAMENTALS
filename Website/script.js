// script.js
let currentInput = '';

function appendToDisplay(value) {
    currentInput += value;
    document.getElementById('display').textContent = currentInput;
}

function clearDisplay() {
    currentInput = '';
    document.getElementById('display').textContent = '';
}

function calculate() {
    try {
        currentInput = eval(currentInput).toString(); // Use eval to evaluate the expression
        document.getElementById('display').textContent = currentInput;
    } catch (e) {
        document.getElementById('display').textContent = 'Error';
    }
}