document.addEventListener("DOMContentLoaded", function () {
    const inputs = document.querySelectorAll(".contact-input");

    inputs.forEach((input, index) => {
        input.addEventListener("focus", function () {
            const prev = document.querySelector(".active-ring");
            if (prev) {
                prev.classList.remove("active-ring");
            }

            // Add active ring to the focused input
            this.classList.add("active-ring");
        });

        input.addEventListener("blur", function () {
            setTimeout(() => {
                this.classList.remove("active-ring");
            }, 200); // Delay to allow smooth transition before removing
        });
    });
});
