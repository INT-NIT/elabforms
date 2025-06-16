from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import shutil
import os
from template_builder import TemplateBuilder

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")

# Définir la racine pour servir le formulaire HTML
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    # Affiche la page HTML du formulaire d'upload
    return templates.TemplateResponse(
        "upload.html", {"request": request}
    )

@app.post("/generate-template/")
async def generate_template(
    template_parts_list_file: UploadFile = File(...),
    project_name: str = Form(...)
):
    working_dir = os.path.dirname(os.path.abspath(__file__))

    # Sauvegarde temporaire du fichier CSV uploadé
    input_filename = os.path.join(
        working_dir, f"temp_{template_parts_list_file.filename}"
    )
    with open(input_filename, "wb") as buffer:
        shutil.copyfileobj(
            template_parts_list_file.file, buffer
        )

    # Définir le nom du fichier JSON de sortie
    output_filename = os.path.join(
        working_dir, f"{project_name}.json"
    )

    try:
        original_cwd = os.getcwd()
        os.chdir(working_dir)

        # Générer le JSON avec TemplateBuilder
        TemplateBuilder(input_filename, output_filename)

        # Retourner le fichier JSON généré
        return FileResponse(
            path=output_filename,
            filename=f"{project_name}.json",
            media_type="application/json"
        )

    except Exception as e:
        # Retourner un message d'erreur en cas d'échec
        return {"error": str(e)}

    finally:
        os.chdir(original_cwd)
        # Nettoyer le fichier CSV temporaire
        if os.path.exists(input_filename):
            os.remove(input_filename)