function displayEstDateTime() {
    const now = new Date();
    const estOffset = -5; // EST is UTC-5

    const estDate = new Date(now.toLocaleString('en-US', { timeZone: 'America/New_York' }));

    const year = estDate.getFullYear();
    const month = estDate.toLocaleString('en-US', { month: 'short' }); // Get the 3-letter month abbreviation
    const day = String(estDate.getDate()).padStart(2, '0');
    const hours = String(estDate.getHours()).padStart(2, '0');
    const minutes = String(estDate.getMinutes()).padStart(2, '0');
    const seconds = String(estDate.getSeconds()).padStart(2, '0');

    const formattedDateTime = `${day}-${month}-${year} ${hours}:${minutes}:${seconds}`;
  
    // Update the content of the DTG element
    document.getElementById('dtg').textContent = formattedDateTime;
}

// Update the date and time every second
setInterval(displayEstDateTime, 1000);

// Initial call to display the date and time immediately
displayEstDateTime();

