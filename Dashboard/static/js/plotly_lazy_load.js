
// plotly_lazy_load.js

// Fungsi untuk merender plot
function renderPlot() {
    const plotElement = document.getElementById('myPlot');
    if (plotElement.getAttribute('data-plotly-rendered') !== 'true') {
        // Asumsikan plotData sudah di-set sebagai global variable atau di-pass ke script ini
        Plotly.newPlot('myPlot', plotData.data, plotData.layout);
        plotElement.setAttribute('data-plotly-rendered', 'true');
    }
}

// Event listener untuk scroll
window.addEventListener('scroll', function() {
    const plotElement = document.getElementById('myPlot');
    const rect = plotElement.getBoundingClientRect();
    const isInViewport = rect.top < window.innerHeight && rect.bottom >= 0;
    if (isInViewport) {
        renderPlot();
    }
});

// Merender plot jika sudah dalam viewport saat halaman dimuat
document.addEventListener('DOMContentLoaded', function() {
    renderPlot();
});
