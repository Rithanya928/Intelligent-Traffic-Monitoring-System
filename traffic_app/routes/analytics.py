from fastapi import APIRouter
from ..models.density import calculate_density

router = APIRouter()

@router.get("/traffic-density")
def traffic_density(vehicle_count: int):
    density = calculate_density(vehicle_count)
    return {
        "vehicle_count": vehicle_count,
        "traffic_density": density
    }
