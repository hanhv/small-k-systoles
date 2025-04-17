# $k$-systoles for small $k$

### Input:
- A natural number $k$.

### Output:
- The set $S_{>= k}(Y)$ consists of plausible $k$-systoles.
    - Note: $S_{>= k}(Y)$ consists of $aB^k$ and plausible shortest ab-words with at least $k$ self-intersections and at most $2k$ strings (hence with ab-word length at most $2k$). This is because:
      - By Baribaud's result, $aB^k$ is the shortest geodesic with at least $2k+2$ strings.  
      - By the relations between number of strings and ab-word lengths, for $w \in S_{>= k}(Y) \setminus \lbrace aB^k \rbrace$, we have ab-word length of $w$ is at most $2k$.
      - If $w$ and ws are two reduced cyclic words then the hyperbolic length of $ws$ is longer than that of $w$.

### Procedure:
The set $S_{>= k}(Y)$ is generated and refined as follows: 
Starting with an initial set $\lbrace a \rbrace$, expands it by appending allowed letters $(a, A, b, B)$ to each word in the set while ensuring cyclic reduction, and evaluates the self-intersection number $i(w)$ for each word. 
Words with a self-intersection number of at least $k$ are added to $S_{>= k}(Y)$, and the corresponding branches stop generating (i.e., no further letters are appended to these words). 
Words with a self-intersection number less than $k$ are temporarily stored for further expansion if they remain within constraints (i.e., the number of strings is at most $2k$). 
The process ends when no new words are generated, and duplicates representing the same unoriented curve are removed from the final set.

1. **Initialization**:
   - Set $\mathcal{S}_{\ge k}(Y) = \lbrace aB^k \rbrace$.
   - Set `current set` $= \lbrace a \rbrace$.

2. **Main**:
   - **Repeat (while loop)**:
     - Initialize `temporary set` $= \emptyset$.
     - For each $u$ in `current set`, form three active words by adding a letter $x \in \lbrace a, A, b, B \rbrace$ at the end of $u$ such that $x$ is not the inverse of the last letter of $u$.
     
     - For each $w$ in the active words with ab-word length at most $2k$:
       - If $w$ is cyclically reduced (i.e., the last letter of $w$ is either $b$ or $B$):
         - Compute $i(w)$ (the self-intersection number of $w$).
         - If $i(w) \geq k$, check if $w$ is primitive, then add $w$ to $\mathcal{S}_{\ge k}(Y)$.
         - If $i(w) < k$, add $w$ to `temporary set`.
       - If $w$ is not cyclically reduced, add $w$ to `temporary set`.

     - If `temporary set` $= \emptyset$, end the loop.
     - Otherwise, update `current set = temporary set`.

3. **Remove duplicates**:
   - For words that represent the same unoriented curve, keep only one such word in $\mathcal{S}_{\ge k}(Y)$.
  