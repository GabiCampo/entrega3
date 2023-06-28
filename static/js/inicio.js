$(document).ready(function() {
    $("#formulario1").validate({
        rules: {
            txtEmail: {
                required: true,
                
            },
            txtContrasena: {
                required: true,
            },
        }, // Fin de reglas
        messages: {
            txtEmail: {
                required: 'El email es un campo requerido',
                
            },
            txtContrasena: {
                required: 'La contraseña es un campo obligatorio',
            },
        },
    });
});

