from fastapi import FastAPI, HTTPException, Request
import httpx

app = FastAPI()

up = {
    "schemaVersion": 1,
    "label": "uptime",
    "message": "up",
    "color": "brightgreen",
    "style": "flat-square",
    "cacheSeconds": "60"
}

down = {
    "schemaVersion": 1,
    "label": "uptime",
    "message": "down",
    "color": "critical",
    "style": "flat-square",
    "cacheSeconds": "60"
}


@app.get("/", response_model=dict)
async def check_proxy_status(request: Request):
    try:
        async with httpx.AsyncClient() as client:
            url = f"{request.headers.get('X-Forwarded-Proto')}://{request.headers.get('Host')}"
            print(f"checking server {url} health...")
            if url == "http://localhost:8383":
                return {"error": "Internal Server Error"}
            response = await client.get(url)
            response.raise_for_status()
        return up
    except httpx.RequestError:
        return down
    except Exception as e:
        print(f"{e}")
        return up
