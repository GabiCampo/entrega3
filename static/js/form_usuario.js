$(document).ready(function() {
    $("#formulario").validate({
        rules: {
            id: {
                required: true
            },
            rut: {
                required: true,
                rutChileno: true
            },
            Nombre: {
                required: true,
            },
            Apellido: {
                required: true,
            },
            email: {
                required: true,
                email: true
            },
            txtDireccion: {
                required: true,
            },
            genderr: {
                required: true
            },
            password: {
                required: true
            }
        },    // --> Fin de reglas
    messages: { 
        id: {
            required: "El id es un campo obligatorio",
        },
        rut: {
            required: "El rut es un campo obligatorio",
            rutChileno: "El formato del rut no es válido"
        },
        Nombre: {
            required: 'El Nombre es un campo obligatorio',
        },
        Apellido: {
            required: 'El Apellido  es un campo obligatorio',
        },
        txtDireccion: {
            required: 'Ingrese Dirección',
        },    
        email: {
            required: "El email es un campo requerido",
            email: "El email no cumple el formato de un correo",
        },
        Subscripcion: {
            required: "Seleccione una opción de subscripción"
        },
        password: {
            required: "La contraseña es una campo obligatorio",
            minlength: "Mínimo 5 caracteres",
        },
    }
    });
});