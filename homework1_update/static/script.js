function apply() {
    let name = document.getElementById("name").value;
    let zipcode = document.getElementById("zipcode").value;

    fetch("/apply", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name, zipcode: zipcode })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("apply_result").innerText = "Application ID: " + data.application_id;
    });
}

function checkStatus() {
    let appId = document.getElementById("status_id").value;

    fetch("/status/" + appId)
    .then(response => response.json())

       .then(data => {
        document.getElementById("status_result").innerText = "Status: " + data.status;
    }
);
}

function updateStatus() {
    let appId = document.getElementById("update_id").value;
    let newStatus = document.getElementById("new_status").value;

    fetch("/update_status", 
        {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ application_id: parseInt(appId), status: newStatus })
    }
)
    .then(response => response.json())
    .then(data => {
        document.getElementById("update_result").innerText = data.message;
    });
}

