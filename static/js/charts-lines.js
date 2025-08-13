/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */
// Obtener datos inyectados desde Django
let chartDataJson = document.getElementById('chart-data-json');
let chartLabels = [];
let chartData = [];
if (chartDataJson) {
  try {
    let parsed = JSON.parse(chartDataJson.textContent);
    chartLabels = parsed.labels;
    chartData = parsed.data;
  } catch (e) {
    chartLabels = [];
    chartData = [];
  }
}

const lineConfig = {
  type: 'line',
  data: {
    labels: chartLabels,
    datasets: [
      {
        label: 'Posts por usuario',
        backgroundColor: '#0694a2',
        borderColor: '#0694a2',
        data: chartData,
        fill: false,
      }
    ],
  },
  options: {
    responsive: true,
    legend: {
      display: false,
    },
    tooltips: {
      mode: 'index',
      intersect: false,
    },
    hover: {
      mode: 'nearest',
      intersect: true,
    },
    scales: {
      x: {
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Month',
        },
      },
      y: {
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Value',
        },
      },
    },
  },
}

// change this to the id of your chart element in HMTL
const lineCtx = document.getElementById('line')
window.myLine = new Chart(lineCtx, lineConfig)
