from fastapi import APIRouter

router = APIRouter()

@router.post("/control")
def signal_control(density: str):
    if density == "High":
        green_time = 90
    elif density == "Medium":
        green_time = 60
    else:
        green_time = 30

    return {
        "signal_status": "Auto",
        "green_time_seconds": green_time
    }
