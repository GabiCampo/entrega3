$(document).ready(function() {
$("#formulario").validate({
    rules: {
        id: {
            required: true
        },
        Nombre: {
            required: true,
        },
        monto: {
            required: true,
            number: true
        },
        descripcion: {
            required: true,
            email: true
        },
        dessub: {
            required: true
        },
        desoferta: {
            required: true
        }
        
    },
    messages: { 
        id: {
            required: "El id es un campo obligatorio",
        },
        Nombre: {
            required: "Este Campo es obligatorio",
        },
        descripcion: {
            required: "Este Campo es obligatorio",
            descripcion:"Este Campo es obligatorio",
        },
        desoferta: {
            required: "Este Campo es obligatorio",
        },    
        monto: {
            required: "Este Campo es obligatorio",
        },
        dessub: {
            required: "Este Campo es obligatorio",
        },
    }
    });
});

