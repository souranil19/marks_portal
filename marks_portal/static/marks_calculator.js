/**
 * Marks Calculation JavaScript
 * Handles all calculations for student marksheet
 */

function calculateMarks() {
    // Initialize totals
    let firstTheoryTotal = 0;
    let firstPracticalTotal = 0;
    let secondTheoryTotal = 0;
    let secondPracticalTotal = 0;
    let thirdTheoryTotal = 0;
    let thirdPracticalTotal = 0;
    let grandTotal = 0;

    // Calculate for each subject row
    document.querySelectorAll('.subject-row').forEach(function(row) {
        // Get marks for this subject
        const firstTheory = parseInt(row.querySelector('.first-theory').textContent) || 0;
        const firstPractical = parseInt(row.querySelector('.first-practical').textContent) || 0;
        const secondTheory = parseInt(row.querySelector('.second-theory').textContent) || 0;
        const secondPractical = parseInt(row.querySelector('.second-practical').textContent) || 0;
        const thirdTheory = parseInt(row.querySelector('.third-theory').textContent) || 0;
        const thirdPractical = parseInt(row.querySelector('.third-practical').textContent) || 0;

        // Calculate subject total
        const subjectTotal = firstTheory + firstPractical + secondTheory + secondPractical + thirdTheory + thirdPractical;
        const subjectPercentage = (subjectTotal / 300 * 100).toFixed(1);  // Still 300 total (100 per term: 70+30)

        // Update subject total and percentage
        row.querySelector('.subject-total').textContent = subjectTotal;
        row.querySelector('.subject-percentage').textContent = subjectPercentage;

        // Add to grand totals
        firstTheoryTotal += firstTheory;
        firstPracticalTotal += firstPractical;
        secondTheoryTotal += secondTheory;
        secondPracticalTotal += secondPractical;
        thirdTheoryTotal += thirdTheory;
        thirdPracticalTotal += thirdPractical;
        grandTotal += subjectTotal;
    });

    // Update total row
    document.getElementById('firstTheoryTotal').textContent = firstTheoryTotal;
    document.getElementById('firstPracticalTotal').textContent = firstPracticalTotal;
    document.getElementById('secondTheoryTotal').textContent = secondTheoryTotal;
    document.getElementById('secondPracticalTotal').textContent = secondPracticalTotal;
    document.getElementById('thirdTheoryTotal').textContent = thirdTheoryTotal;
    document.getElementById('thirdPracticalTotal').textContent = thirdPracticalTotal;
    document.getElementById('grandTotal').textContent = grandTotal;
    
    // Calculate overall percentage
    const overallPercentage = (grandTotal / 2100 * 100).toFixed(1);
    document.getElementById('overallPercentage').textContent = overallPercentage;
}

// Additional utility functions for marksheet
function printMarksheet() {
    window.print();
}

function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    if (toast) {
        toast.textContent = message;
        toast.className = `toast-${type}`;
        toast.style.display = 'block';
        
        // Hide after 3 seconds
        setTimeout(() => {
            toast.style.display = 'none';
        }, 3000);
    }
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    calculateMarks();
    
    // Show welcome message
    showToast('Marksheet loaded successfully!');
    
    // Add print button functionality
    const printButton = document.getElementById('printButton');
    if (printButton) {
        printButton.addEventListener('click', function() {
            printMarksheet();
        });
    }
});
