// sweetAlert.js
document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');
  form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevenir el envío del formulario para mostrar la alerta primero

      Swal.fire({
          title: '¿Estás seguro?',
          text: "¡Confirma que deseas efectuar los cambios!",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Sí, guardar cambios'
      }).then((result) => {
          if (result.isConfirmed) {
              Swal.fire(
                  '¡Guardado!',
                  'Los cambios han sido guardados.',
                  'success'
              ).then(() => {
                  form.submit(); // Enviar el formulario después de la confirmación
              });
          }
      });
  });
});