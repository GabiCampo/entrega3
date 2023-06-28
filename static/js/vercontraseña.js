jQuery(document).ready(function () {
    // Show password Button
    $(document).on('click', '#showpassword', function ()  {
        
        console.log('El evento se ha activado') 

        var pass = $("#id_txtContrasena");
        var pass2 = $("#id_txtRepetirContrasena");

        var fieldtype = pass.attr('type');
        var fieldtype2 = pass2.attr('type');

        if (fieldtype == 'password' & fieldtype2 == 'password') {
            pass.attr('type', 'text');
            pass2.attr('type', 'text');
            $(this).text("Ocultar Contraseña");
        } else {
            pass.attr('type', 'password');
            pass2.attr('type', 'password');
            $(this).text("Ver Contraseña");
        }

    });

});