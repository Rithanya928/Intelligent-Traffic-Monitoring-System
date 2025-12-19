Write-Host "Activating venv..."
.\venv\Scripts\activate

Write-Host "Installing requirements (if needed)..."
pip install -r requirements.txt

Write-Host "Starting backend (uvicorn)..."
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
