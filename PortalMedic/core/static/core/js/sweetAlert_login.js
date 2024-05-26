document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');
  form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevenir el envío del formulario para mostrar la alerta primero
      Swal.fire({
          title: "Good job!",
          text: "You clicked the button!",
          icon: "success"
      }).then(() => {
          window.location.href = "http://127.0.0.1:8000/";
      });
  });
});