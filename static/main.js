document.addEventListener('DOMContentLoaded', function () {
    const randomForm = document.querySelector('#randomForm');
    const copyBtn = document.querySelector('#copyBtn');
    const resultDiv = document.querySelector('#result');
    const timeDiv = document.querySelector('#time');
    const numOfNumbersInput = document.querySelector('#numOfNumbers');
    let randomNumbers = [];

    randomForm.addEventListener('submit', function (event) {
        event.preventDefault();
        generateRandomNumbers();
    });

    copyBtn.addEventListener('click', function () {
        copyToClipboard(randomNumbers.join(' '));
    });

    function generateRandomNumbers() {
        let startTime = performance.now();

        let numOfNumbers = parseInt(numOfNumbersInput.value, 10);
        if (numOfNumbers > 0) {
            randomNumbers = Array.from({ length: numOfNumbers }, () => Math.floor(Math.random() * numOfNumbers) + 1);
            updateResult();
        } else {
            alert('Please enter a valid number greater than 0.');
        }

        let endTime = performance.now();
        let executionTime = (endTime - startTime) * 1e6;

        displayExecutionTime(executionTime);
    }

    function updateResult() {
        resultDiv.textContent = randomNumbers.join(' ');
    }

    function copyToClipboard(text) {
        let tempInput = document.createElement('textarea');
        tempInput.value = text;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand('copy');
        document.body.removeChild(tempInput);
        alert('Copied to clipboard!');
    }

    function displayExecutionTime(time) {
        let timeUnits = ['femtoseconds', 'picoseconds', 'nanoseconds', 'microseconds', 'milliseconds', 'seconds'];
        let unitIndex = 0;

        while (time >= 1000 && unitIndex < timeUnits.length - 1) {
            time /= 1000;
            unitIndex++;
        }

        let timeDisplay = `${time.toFixed(5)} ${timeUnits[unitIndex]}`;
        timeDiv.textContent = `Execution Time: ${timeDisplay}`;
    }
});
