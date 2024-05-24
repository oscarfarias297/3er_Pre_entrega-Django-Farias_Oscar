document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevenir el envío del formulario para mostrar la alerta primero
        Swal.fire({
            title: "Good job!",
            text: "You clicked the button!",
            icon: "success"
          }).then(() => {
            return render("core:index.html");});
    });
  });