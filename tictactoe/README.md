# Project 0: Tic-Tac-Toe

## My Learning Journey

Okay, writing an AI that you literally *cannot* beat is kind of a power trip.

The biggest challenge here was wrapping my head around the recursion. It’s one thing to understand "it calls itself," but visualizing the tree of moves for even a simple game like Tic-Tac-Toe is wild. There are over 200,000 terminal states if you don't optimize!

I actually implemented playing against it and realized it was a bit slow at first on the opening move. It has to think about *everything*. I learned that for larger games (like Chess), this raw Minimax approach is impossible without optimizations like Alpha-Beta pruning.

