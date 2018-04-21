genres = [
"Minesweeper",
"Frogger",
"Pacman",
"Pong",
"Pool",
"Sports",
"Golf",
"MMORPG",
"Oregon Trail",
"Text Based",
"Horror",
"Survival",
"Rougelike",
"Sports",
"Video",
"Game Show",
"Racing",
"Topdown Racer",
"Battle Racer",
"3D Sim Real Racer",
"Card Game",
"CCG",
"Multiplayer",
"Solataire",
"FPS",
"Walking Simulator",
"Shooter",
"Puzzle",
"Logic",
"Interactive Fiction",
"Story",
"Point and Click",
"Platformer",
"Role Playing",
"Fighting",
"Simulation",
"Stealth",
"Hack And Slash",
"Side Scroller",
"Tower Defense",
"Visual Novel",
"THird Person",
"Flight Sim",
"Space Flight Sim",
"Shoot em Up",
"Beat em Up",
"Open World",
"Rhythm",
"Nonviolent",
"Music",
"God Game",
"Falling Sand",
"Dungeon Crawl",
"Dating",
"Management",
"City Builder",
"Browser",
"Business Simualation",
"Clicker",
"Battle Royale",
"Artillery",
"Art",
"4X",
"Drawing",
"Indie Casual",
"Free 2 Play",
"Atmospheric",
"Difficult",
"Co-op",
"Pixel",
"Sandbox",
"Arcade",
"Turn Based",
"Exploration",
"Education",
"PvP",
"RTS",
"BulletHell",
"Minimalist",
"Procedural",
"ISometric",
"Board Game",
"Perma Death",
"3d Platformer",
"Metroidvania",
"Economy",
"Detective",
"Linear",
"Voxel",
"CRPG",
"Score Attack",
"Hunting",
"Quick Time",
"Heist",
"Historical",
"Football",
"Soccer",
"Programming",
"Sailing",
"VR",
"Typing",
"AD",
"Intentionally Awkward Contrals",
"Bikes",
"Spelling",
"Choices Matter",
"Time",
"Light Gun Shooter",
"Aliens",
"Asteroids",
"Chess",
"Go",
"Marble",
"Pinball",
"Basketball",
"Skiball" ]

# Example usage, generate 10 combos
# ./picker.py 10

import random
import sys

count = int(sys.argv[1])

for x in range(0, count):
	a = random.choice(genres)
	b = random.choice(genres)
	print(a + " " + b)