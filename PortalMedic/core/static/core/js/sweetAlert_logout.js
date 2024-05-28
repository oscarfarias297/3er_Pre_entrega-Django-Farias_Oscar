

document.addEventListener('DOMContentLoaded', function() {
        Swal.fire({
            title: "¡Sesión Cerrada Correctamente!",
            text: "Has cerrado sesión con éxito.",
            icon: "success"
        }).then(() => {
            window.location.href = "http://127.0.0.1:8000/"; 
        });
    });


