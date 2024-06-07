from fastapi import FastAPI, UploadFile, File
import uvicorn
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Its Abhay Here"

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Ensure the 'temp_files' directory exists
    os.makedirs("temp_files", exist_ok=True)

    # Read the uploaded file
    contents = await file.read()
    
    # Save the file locally
    file_location = f"temp_files/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(contents)
    
    # Placeholder response simulating a prediction
    result = {"filename": file.filename, "prediction": "Healthy"}  # Replace with actual prediction logic

    return JSONResponse(content=result)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=9000)
