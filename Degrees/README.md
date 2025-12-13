# Project 0: Degrees

## My Learning Journey

Honestly, this was a great intro to treating real-world data like a graph. The concept of "SIX degrees" makes sense abstractly, but seeing the program actually churn through thousands of IMDB entries to link **Emma Watson** to **Jennifer Lawrence** in 3 steps was pretty satisfying.

One thing that tripped me up initially was handling the fringe (the frontier). I had to make sure I wasn't just grabbing *any* path, but the shortest one. I also realized how quickly the search space explodes if you don't keep track of explored nodes—my first attempt would have probably run until the end of time if I didn't verify visited states properly.


