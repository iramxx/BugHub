document.addEventListener("DOMContentLoaded", () => {
    console.log("JS Loaded!");

    const descField = document.getElementById("id_description");
    const counterDisplay = document.getElementById("descriptionCounter");
  
    if (descField && counterDisplay) {
      descField.addEventListener("input", () => {
        const length = descField.value.length;
        counterDisplay.textContent = `Characters: ${length}`;
      });
    }
  });
  