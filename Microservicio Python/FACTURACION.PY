from fastapi import FastAPI
from config import settings
from cufe import generar_cufe   # asegúrate que la ruta sea correcta

app = FastAPI(title=settings.APP_NAME)


@app.post("/generar-cufe")
def crear_cufe(datos: dict):
    cufe = generar_cufe(datos)
    return {"CUFE": cufe}


@app.get("/hola")
def hola_mundo():
    return {"mensaje": "Hola Mundo soy tu dueño"}


@app.post("/datos")
def recibir_datos(data: dict):
    print(data)
    return {"mensaje": "Datos recibidos correctamente"}


@app.get("/empresa")
def empresa():
    return {
        "razon_social": settings.RAZON_SOCIAL,
        "nit": settings.NIT_EMPRESA,
        "entorno": settings.ENVIRONMENT,
        "ciudad": "Pereira",
        "sector": "Politecnico Metropolitano",
        "estado": "Activo"
    }


@app.post("/factura")
def crear_factura(datos: dict):

    cufe = generar_cufe(datos)

    factura = {
        "numero": datos["numero"],
        "cliente": datos["nit_cliente"],
        "total": datos["valor_total"],
        "cufe": cufe
    }

    return factura