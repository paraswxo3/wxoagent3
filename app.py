from fastapi import FastAPI, File, Header, Depends, Security, HTTPException, Body, UploadFile,Request
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=True)
def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "Auth01234":
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key"
        )
    return api_key

app = FastAPI(dependencies=[Depends(verify_api_key)])  

class OrderAmount(BaseModel):
    order_amount: float

@app.post("/get_oroder_amount", response_model=OrderAmount)
def get_oroder_amount(request: Request,order_num: str = Body(..., embed=True)):
    header_value = request.headers.get("X-CUSTOM-CALLER-ID")  # Replace with your header name
    print("skill header",header_value)
    print("order_amount",30.15)
    return {"order_amount":30.15}


if __name__ == '__main__':
    import uvicorn
    print("starting.....")
    uvicorn.run(app, host='0.0.0.0', port=8080)

