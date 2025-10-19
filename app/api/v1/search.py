from fastapi import APIRouter, File, UploadFile
router = APIRouter()
@router.post("/visual")
async def visual_search(file: UploadFile = File(...)):
    # TODO: integrate Cloudinary + CLIP + vector search
    return {"filename": file.filename, "status": "not-implemented-yet"}
