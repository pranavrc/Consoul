import os

def playmedia(tune):

	"""Plays the input file"""

	import pyglet


	music = pyglet.media.load(tune, streaming=True)
	music.play()


	def exiter(dt):
	        pyglet.app.exit()

	pyglet.clock.schedule_once(exiter, music.duration)

	pyglet.app.run()
