// sweetAlert.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevenir el envío del formulario para mostrar la alerta primero
        const swalWithBootstrapButtons = Swal.mixin({
            customClass: {
                confirmButton: "btn btn-success",
                cancelButton: "btn btn-danger"
            },
            buttonsStyling: false
        });
        swalWithBootstrapButtons.fire({
            title: "Se creará un nuevo usuario",
            text: "Confirme que desea crear su usuario",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "SI!",
            cancelButtonText: "NO",
            reverseButtons: true
        }).then((result) => {
            if (result.isConfirmed) {
                swalWithBootstrapButtons.fire({
                    title: "USUARIO!",
                    text: "Usuario Creado Correctamente!",
                    icon: "success"
                }).then(() => {
                    window.location.href = "submit";        //Código no funcional por error en redireccionamiento al submit, Corregir
                });
            } else if (result.dismiss === Swal.DismissReason.cancel) {
                swalWithBootstrapButtons.fire({
                    title: "Cancelar",
                    text: "Gracias Puedes seguir visitando el sitio",
                    icon: "error"
                }).then(() => {
                    window.location.href = "http://127.0.0.1:8000/";
                });
            }
        });
    });
});

