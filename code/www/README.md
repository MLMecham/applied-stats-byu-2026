# Static assets for 14-quiz-game-ui-app.py

The quiz app serves this folder at the web root. Drop two files here to power the
Goku power-up effect that fires on a correct answer:

- `goku.jpg` (or rename and point `GOKU_IMG` at it). A transparent PNG or an
  animated GIF looks even better than a JPG.
- `powerup.mp3` a short power-up / charging sound effect.

If a file is missing the app still runs: the CSS animation (zoom, golden aura,
screen shake) plays regardless; you just won't see the image or hear the sound.
You can also point `GOKU_IMG` / `POWERUP_SOUND` at any URL instead of a local file.
