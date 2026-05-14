console.log("AI Fitness Coach Loaded ✅");

// Show a loading state when the form is submitted
const form = document.querySelector("form");
const btn = document.getElementById("submit-btn");

if (form && btn) {
    form.addEventListener("submit", function () {
        btn.disabled = true;
        btn.textContent = "⏳ Generating your plan...";
    });
}
