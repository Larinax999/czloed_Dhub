from requests import post
from random import choice
from time import sleep

def gen_amongus(color_):
	color = f"{color_}_square"
	return f"""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬛:{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}:⬛⬜⬜
⬜⬜⬛:{color}::{color}::{color}::{color}:⬛⬛⬛⬛⬛⬛⬜⬜
⬜⬜⬛:{color}::{color}::{color}:⬛🟦🟦⬜⬜⬜⬜⬛⬜
⬜:{color}:⬛:{color}::{color}::{color}:⬛🟦🟦🟦🟦🟦🟦⬛⬜
⬜:{color}:⬛:{color}::{color}::{color}:⬛🟦🟦🟦🟦🟦🟦⬛⬜
⬜:{color}:⬛:{color}::{color}::{color}::{color}:⬛⬛⬛⬛⬛⬛⬜⬜
⬜:{color}:⬛:{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}:⬛⬜⬜
⬜⬜⬛:{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}:⬛⬜⬜
⬜⬜⬛:{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}:⬛⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"""

for _ in ["red","yellow","purple","brown","orange","green"]:
    post("https://discord.com/api/webhooks/898925904389111819/jvCvQsMvRieGd-J0uvaDSi10FYGpa6oTfYRG-dhHtIei2pu2c_GiQeYbT7kZztII0fyU",json={"content":gen_amongus(_)})
    sleep(1.5)