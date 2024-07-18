document.addEventListener('DOMContentLoaded', function() {
    // Get the endpoint from the script tag's data-endpoint attribute
    const scriptTag = document.querySelector('script[data-endpoint]');
    
    if (!scriptTag) {
        console.error('Script tag with data-endpoint attribute not found.');
        return;
    }
    
    const endpoint = scriptTag.getAttribute('data-endpoint');

    if (!endpoint) {
        console.error('Data-endpoint attribute is missing or empty.');
        return;
    }

    fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            console.log("Data fetched from API:", data);
            const tableBody = document.querySelector('#data-table tbody');
            tableBody.innerHTML = '';
            data.forEach(row => {
                const tr = document.createElement('tr');
                for (const [key, value] of Object.entries(row)) {
                    const td = document.createElement('td');
                    td.textContent = value !== null ? value : '';  // Handle null values
                    tr.appendChild(td);
                }
                tableBody.appendChild(tr);
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});
