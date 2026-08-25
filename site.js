document.querySelectorAll("details.language").forEach((picker) => {
  picker.addEventListener("toggle", () => {
    if (!picker.open) return;
    document.querySelectorAll("details.language").forEach((other) => {
      if (other !== picker) other.open = false;
    });
  });
});

document.addEventListener("click", (event) => {
  document.querySelectorAll("details.language[open]").forEach((picker) => {
    if (!picker.contains(event.target)) picker.open = false;
  });
});
