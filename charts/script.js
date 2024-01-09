function loadData() {
  fetch('data.txt')
    .then(response => response.text())
    .then(data => {
      // Parse the text data into an array of objects
      const parsedData = data.split('\n').map(line => {
        const [time, cpu, memory, temperature] = line.split('\t');
        return { time, cpu, memory, temperature };
      });

      // Create an HTML table to display the data
      const table = document.createElement('table');
      const headerRow = table.insertRow();
      headerRow.innerHTML = '<th>Time</th><th>CPU</th><th>Memory</th><th>Temperature</th>';

      parsedData.forEach(rowData => {
        const row = table.insertRow();
        const timeCell = row.insertCell();
        const cpuCell = row.insertCell();
        const memoryCell = row.insertCell();
        const temperatureCell = row.insertCell();
        timeCell.textContent = rowData.time;
        cpuCell.textContent = rowData.cpu;
        memoryCell.textContent = rowData.memory;
        temperatureCell.textContent = rowData.temperature;
      });

      // Replace the existing content with the new table
      const dataContainer = document.getElementById('data-container');
      dataContainer.innerHTML = '';
      dataContainer.appendChild(table);
    });
}

// Load the data initially
loadData();

// Refresh the data every 5 seconds
setInterval(loadData, 5000);
