document.addEventListener("DOMContentLoaded", function () {

    // Registration form validation

    const form = document.getElementById("registrationForm");

    if (form) {

        form.addEventListener("submit", function (event) {

            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const phone = document.getElementById("phone").value.trim();

            if (name.length < 3) {
                alert("Please enter your full name.");
                event.preventDefault();
                return;
            }

            if (!email.includes("@")) {
                alert("Please enter a valid email address.");
                event.preventDefault();
                return;
            }

            if (!/^[0-9]{10}$/.test(phone)) {
                alert("Please enter a valid 10 digit mobile number.");
                event.preventDefault();
                return;
            }

        });

    }


    // Event search

    const searchInput = document.getElementById("eventSearch");

    if (searchInput) {

        searchInput.addEventListener("input", function () {

            const searchValue =
                searchInput.value.toLowerCase();

            const cards =
                document.querySelectorAll(".full-event-card");

            cards.forEach(function (card) {

                const name =
                    card.dataset.name.toLowerCase();

                if (name.includes(searchValue)) {
                    card.style.display = "flex";
                } else {
                    card.style.display = "none";
                }

            });

        });

    }


    // Admin table search

    const tableSearch =
        document.getElementById("tableSearch");

    if (tableSearch) {

        tableSearch.addEventListener("input", function () {

            const value =
                tableSearch.value.toLowerCase();

            const rows =
                document.querySelectorAll("#registrationTable tbody tr");

            rows.forEach(function (row) {

                row.style.display =
                    row.innerText.toLowerCase().includes(value)
                        ? ""
                        : "none";

            });

        });

    }

});


// Event filters

function filterEvents(category) {

    const cards =
        document.querySelectorAll(".full-event-card");

    const buttons =
        document.querySelectorAll(".filter");

    buttons.forEach(function (button) {
        button.classList.remove("active-filter");
    });

    event.target.classList.add("active-filter");

    cards.forEach(function (card) {

        if (
            category === "all" ||
            card.dataset.category === category
        ) {

            card.style.display = "flex";

        } else {

            card.style.display = "none";

        }

    });

}


// Delete confirmation

function confirmDelete() {

    return confirm(
        "Are you sure you want to delete this registration?"
    );

}