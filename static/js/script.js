document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form");
  if (!form) return;

  const file = document.querySelector('input[type="file"]');

  function displayMessage(message) {
    alert(message);
  }

  function createLink(value) {
    const link = document.createElement("a");
    link.setAttribute("href", value);
    return link;
  }

  function clear() {
    fetch("/clear", { method: "POST" });
  }

  async function submit() {
    const data = new FormData(form);
    const response = await fetch("/convert", {
      method: "POST",
      body: data,
    })
      .then((response) => response.blob())
      .then((blob) => {
        const url = window.URL.createObjectURL(blob);

        const a = createLink(url);
        a.download = "converted.docx";
        a.click();

        window.URL.revokeObjectURL(url);
      });
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    await submit();
    alert("Fichier convertis en pdf");
  });
});
