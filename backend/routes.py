from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from ai_core.gemini_generator import generate_document

router = APIRouter()


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    effective_date: str


@router.post("/generate")
async def generate(request: DocumentRequest):
    try:
        result = generate_document(
            request.document_type,
            request.parties,
            request.terms,
            request.effective_date,
        )

        return {
            "status": "success",
            "document": result,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    