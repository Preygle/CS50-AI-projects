# Project 1: Minesweeper

## My Learning Journey

This was arguably one of the coolest projects. Watching the AI sweep through a board instantly is satisfying. As someone who's been into video games for quite a while, this opened up the logic of how the **CPU Player** works in a game!! 

The tricky part was implementing the **Subset Inference**. It’s easy to understand visually ("If the inner ring has 1 mine, and the outer ring includes the inner ring + 2 others and has 2 mines total, the extra 1 mine must be in the outer 2 cells"). converting that into set algebra in Python took some scribbling on paper.

I also ran into issues where the AI would get "stuck" because it stopped updating its knowledge base after finding a safe cell. I had to ensure that every time it learned something new, it re-checked *everything* it knew to see if that triggered a chain reaction of new discoveries.
