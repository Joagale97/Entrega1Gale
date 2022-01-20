





const btnsEliminacion=document.querySelectorAll('.btnEliminacion')


(function(){

    btnsEliminacion.forEach(btn => {
        btn.addEventlistener('click' , function(e) {
            let confirmacion=confirm ("¿Confirma la eliminacion del curso?");
            if (!confirmacion) {
                e.preventDefault();
            }
        })
        
    });
});