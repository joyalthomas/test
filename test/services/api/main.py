from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/upload-file1")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"/files/{uploaded_file.filename}"
    with open(file_location, "wb") as file_object:
        file_object.write(uploaded_file.file.read())
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}

@app.post("/upload-file")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
        return {"info": "success"}



@app.get("/")
async def health_check():
       
        
    return {"info": "success"}