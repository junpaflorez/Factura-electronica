const express = require('express');
const app = express();
const PORT = 3000;

// Middleware para leer JSON
app.use(express.json());

// Endpoint GET - Hola Mundo
app.get('/hola', (req, res) => {
    res.json({ mensaje: "Hola Mundo Del Poli🚀" });
});

// Endpoint POST - Recibir JSON
app.post('/datos', (req, res) => {
    const datos = req.body;

    console.log("📥 JSON recibido:");
    console.log(datos);

    res.json({
        mensaje: "Datos recibidos correctamente",
        datosRecibidos: datos
    });
});

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`✅ Microservicio corriendo en http://localhost:${PORT}`);
});
