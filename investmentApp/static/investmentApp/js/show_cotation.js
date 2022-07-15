document.addEventListener("DOMContentLoaded", function(e) {
    const data_raw = JSON.parse(document.getElementById('data').textContent);

    const data = {
        labels: data_raw.labels,
        datasets: [{
            label: 'Valor do ativo (' + data_raw.currency + ')',
            borderColor: '#1a4770',
            data: data_raw.data_raw,
        },
        {
            label: 'Valor mínimo do túnel(' + data_raw.currency + ')',
            borderColor: 'green',
            data: data_raw.min_price,
        },
        {
            label: 'Valor máximo do túnel(' + data_raw.currency + ')',
            borderColor: 'red',
            data: data_raw.max_price,
        }]
    };

    const config = {
        type: 'line',
        data: data,
        options: {
            responsive: true,
        }
    };

    const cotationChart = new Chart(document.getElementById('cotationChart'), config);
});