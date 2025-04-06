from fastapi import FastAPI, Response
from src.player import *
from src.dartboard import Dartboard
from src.methods import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "3"}


@app.get("/throw/{level}")
def throw_three_darts(level: int = 10):
    player = Player(level)
    board = Dartboard()
    board.plot()
    try:
        i = 0
        while i<3 :
            player.aim(20, "Treble")
            throw = player.throw()
            polar = cartesian_to_polar(throw[0], throw[1])
            plt.scatter(polar[1], polar[0], s=3, c='aqua', marker='o', zorder=2)
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_bytes = buffer.getvalue()
            i += 1
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        print(f"Error: {e}")
        return Response(content=str(e), media_type="text/plain")


