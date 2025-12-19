from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from traffic_app.routes.video import router as video_router
from traffic_app.routes.analytics import router as analytics_router
from traffic_app.routes.signals import router as signal_router


app = FastAPI(
    title="AI Traffic Monitoring System",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(video_router, prefix="/video")
app.include_router(analytics_router, prefix="/analytics")
app.include_router(signal_router, prefix="/signals")

@app.get("/")
def root():
    return {"status": "Backend running successfully"}
