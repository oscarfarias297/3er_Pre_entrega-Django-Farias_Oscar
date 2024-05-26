
document.addEventListener('DOMContentLoaded', function() {
        Swal.fire({
            title: "¡Sesión Cerrada Correctamente!",
            text: "Has cerrado sesión con éxito.",
            icon: "success"
        }).then(() => {
            // Redirigir al usuario a la página de inicio de sesión
            window.location.href = "http://127.0.0.1:8000/"; // Cambia "login.html" por la URL de tu página de inicio de sesión
        });
    });
