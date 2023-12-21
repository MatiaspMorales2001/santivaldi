document.addEventListener('DOMContentLoaded', function () {
    // Realizar una solicitud a la API de ipify para obtener la dirección IP del usuario
    fetch('https://api.ipify.org/?format=json')
        .then(response => response.json())
        .then(data => {
            // Obtener la dirección IP del usuario
            var userIP = data.ip;
            console.log('Dirección IP del usuario:', userIP); 
            // Lista de direcciones IP permitidas
            var allowedIPs = ["179.57.114.147",]; // Reemplaza con tus direcciones IP permitidas

            // Validar la dirección IP del usuario
            if (allowedIPs.includes(userIP)) {
                // Mostrar elementos del menú si la dirección IP está permitida
                var panaderia = document.getElementById("panaderia");
                var reposteria = document.getElementById("reposteria");
                var abarrotes = document.getElementById("abarrotes");
                var iniciarSesion = document.getElementById("iniciar-sesion");


                if (panaderia) panaderia.style.display = 'block';
                if (reposteria) reposteria.style.display = 'block';
                if (abarrotes) abarrotes.style.display = 'block';
                if (iniciarSesion) iniciarSesion.style.display = 'block';
            } else {
                console.log('Usuario IP no permitida');  // Agrega este console.log
                // Ocultar elementos del menú si la dirección IP no está permitida  
                var iniciarSesion = document.getElementById("iniciar-sesion");
                var cerrarSesion = document.getElementById("cerrar-sesion");
                if (iniciarSesion) iniciarSesion.style.display = 'none';
                if (cerrarSesion) cerrarSesion.style.display = 'none';
            }

        })
        .catch(error => {
            console.error('Error al obtener la dirección IP:', error);
        });
});