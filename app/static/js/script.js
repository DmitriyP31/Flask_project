function updateClock() {
    const now = new Date();

    const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    };

    let dateTimeString = now.toLocaleString('en-US', options);

    document.querySelector('.time').textContent = "Today: " + dateTimeString;
}

setInterval(updateClock, 1000);

updateClock();