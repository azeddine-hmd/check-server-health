from fastapi import FastAPI, HTTPException, Request
import httpx

app = FastAPI()


@app.get("/", response_model=dict)
async def check_proxy_status(request: Request):
    try:
        async with httpx.AsyncClient() as client:
            url = f"http://{request.headers.get('Host')}"
            print(f"url: {url}")
            response = await client.get(url)
            response.raise_for_status()
        return {"status": "up"}
    except httpx.RequestError:
        return {"status": "down"}
    except Exception as e:
        print(f"{e}")
        return {"status": "up"}
