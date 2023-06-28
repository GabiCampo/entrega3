

$("#formulario").validate({
    rules: {
        categoria: {
            required: true
        },
        producto: {
            required: true
        },
        cantidad: {
            required: true,
            number: true,
            min: 1,
            max: 30
        }
        // messages:{
        //     categoria: "ingrese una categoria",
        //     nombre:"seleccione una opcion",
        //     cantidad: "ingrese una cantidad"
        // }
    }
})

$("#guardar").click(function(){
    if($("#formulario").valid() == false){
        return;
    }
    let categoria = $("#categoria").val()
    let producto = $("#producto").val()
    let cantidad = $("#cantidad").val()
})