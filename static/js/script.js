document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("form");
    if (!form) return;

    const fileInput = document.querySelector('input[type="file"]');
    const loader = document.querySelector(".loader");
    const fileNameElement = document.getElementById("fileName");

    let selectedFileName = "converted";

    function showLoader() {
        loader.classList.remove("hidden");
    }

    function hideLoader() {
        loader.classList.add("hidden");
    }

    function createLink(url) {
        const link = document.createElement("a");
        link.href = url;
        return link;
    }

    fileInput.addEventListener("change", () => {

        if (!fileInput.files.length) return;

        const file = fileInput.files[0];

        fileNameElement.textContent = file.name;

        selectedFileName = file.name.replace(/\.[^/.]+$/, "");
    });

    async function submit() {

        const data = new FormData(form);

        const response = await fetch("/convert", {
            method: "POST",
            body: data
        });

        if (!response.ok) {
            throw new Error("Erreur lors de la conversion");
        }

        const blob = await response.blob();

        const url = window.URL.createObjectURL(blob);

        const link = createLink(url);

        link.download = `${selectedFileName}.docx`;

        document.body.appendChild(link);

        link.click();

        link.remove();

        window.URL.revokeObjectURL(url);
    }

    form.addEventListener("submit", async (e) => {

        e.preventDefault();

        if (!fileInput.files.length) {
            alert("Veuillez sélectionner un fichier PDF.");
            return;
        }

        try {

            showLoader();

            await submit();

            alert("Conversion terminée avec succès.");

        } catch (error) {

            console.error(error);

            alert("Une erreur est survenue pendant la conversion.");

        } finally {

            hideLoader();

        }

    });

});