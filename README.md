# Conway's Game of Life

## Project Details

This project is made to simulate [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## Instructions

Run the code. Left click to activate the cell. Right click to disable it. Pressing any key will start/stop the simulation.

Adjust width and height

```python
WIDTH = 800
HEIGHT = 600
```

Adjust scale of grid

```python
SCALE = 10
```

Extend invisible outer border (offset) to prevent edge cells from misbehaving

```python
OFFSET = 10
```

Set target FPS

```python
TARGET_FPS = 25
```
Change colours

```python
BACKGROUND = (0,5,24)
AXIS_COLOUR = (17,24,53)
WHITE = (255,255,255)
```

## Requirements

`pip install pygame`  