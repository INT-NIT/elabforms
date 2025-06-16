from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import shutil
import os
from template_builder import TemplateBuilder

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    # Render the upload form HTML page
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/generate-template/")
async def generate_template(
    template_parts_list_file: UploadFile = File(...),
    project_name: str = Form(...)
):
    working_dir = os.path.dirname(os.path.abspath(__file__))

    # Save the uploaded CSV file temporarily
    input_filename = os.path.join(working_dir, f"temp_{template_parts_list_file.filename}")
    with open(input_filename, "wb") as buffer:
        shutil.copyfileobj(template_parts_list_file.file, buffer)

    # Define the output JSON filename in the current directory
    output_filename = os.path.join(working_dir, f"{project_name}.json")

    try:
        original_cwd = os.getcwd()
        os.chdir(working_dir)

        # Call the backend TemplateBuilder to generate the JSON file
        TemplateBuilder(input_filename, output_filename)

        # Send the generated JSON file back for download
        return FileResponse(
            path=output_filename,
            filename=f"{project_name}.json",
            media_type='application/json'
        )

    except Exception as e:
        # Return error message in case of failure
        return {"error": str(e)}

    finally:
        os.chdir(original_cwd)
        # Clean up the temporary uploaded CSV file
        if os.path.exists(input_filename):
            os.remove(input_filename)
