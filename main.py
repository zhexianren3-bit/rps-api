from fastapi import FastAPI, Query
import random
app = FastAPI()
choices = ["石头", "剪刀", "布"]
@app.get("/")
def root(): return {"msg": "猜拳API"}
@app.get("/play")
def play(user: str = "石头"):
    com = random.choice(choices)
    result = {"你": user, "电脑": com}
    if user == com: result["结果"] = "平局"
    elif (user=="石头" and com=="剪刀") or (user=="剪刀" and com=="布") or (user=="布" and com=="石头"): result["结果"] = "你赢"
    else: result["结果"] = "你输"
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
