async function fetchEvents() {
    const res = await fetch("webhook/events");
    const data = await res.json();

    const container = document.getElementById("events");
    container.innerHTML = "";

    data.forEach(event => {
        let text = "";

        if (event.type === "push") {
            text = `${event.author} pushed to ${event.to_branch} on ${event.timestamp}`;
        }
        else if (event.type === "pull_request") {
            text = `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch} on ${event.timestamp}`;
        }
        else if (event.type === "merge") {
            text = `${event.author} merged branch ${event.from_branch} to ${event.to_branch} on ${event.timestamp}`;
        }

        const p = document.createElement("p");
        p.innerText = text;
        container.appendChild(p);
    });
}

// Poll every 15 seconds
setInterval(fetchEvents, 15000);

// Initial load
fetchEvents();