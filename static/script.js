document.addEventListener('DOMContentLoaded', function() {
    // Show/hide quantum input based on selected algorithm
    document.getElementById('algorithm').addEventListener('change', function() {
        var selectedAlgorithm = this.value;
        var quantumInput = document.getElementById('quantumInput');

        if (selectedAlgorithm === 'rr' || selectedAlgorithm === 'priority_rr') {
            quantumInput.style.display = 'block';
        } else {
            quantumInput.style.display = 'none';
        }
    });
});
