---
layout: post
title: Dice Wars game
date: 2020-04-16 13:04:00
tags: maths probability python plot matplotlib
categories: maths
description: calculation of probabilities in the game of dice wars
---

## Dicewars
A simplified version of game [DiceWars](http://www.gamedesign.jp/flash/dice/dice.html) between two players goes such that each player is assigned a stack of 6-sided dice which equate to relative power. On a player's turn, the player challenges other player. The challenge is resolved when each player rolls their dice, with the higher total winning.

Each player roll all of their dices and the value at the top of each dice is added to find the players score. Whoever has the higher score wins and the equal score is a tie.  The goal is to find the probability that, in a game between two players with $m$ and $k$ dice respectively,  any player wins over the other or there is a tie.

Before we calculate the probability of win or a draw, lets calculate the probability that a player with $k$ dices rolls a total of $n$. Since for a standard dice the number on each face is one of ${1,2,3,4,5,6}$. When the player rolls $k$ dices the minimum sum is $k$ when each dice rolls to be $1$ and a maximum of $6k$ when each one rolls to be $6$ thus  $ k \leq n \leq 6k$

The total exhaustive cases of rolling $k$ dice is $6^k$. The total possible ways we can get a sum of $n$ (subject to above constraint) when we roll $k$ dice is the same as the total number of ways we can write $n$ as a sum of $k$ integers such that each integer$n_i$ is between $1 \leq n_i \leq 6$. The order of integers that we break the number $n$ is important too.

Lets us define a function $f_k(n)$ such that it gives the total number of ways we can break $n$ into $k$ integers where each integer is one of ${1,2,3,4,5,6}$

Because of the constraint $k \leq n \leq 6k $ we can immediately write

\begin{align}
    f_k(n) = 0 \text{ if } n < k \text{ or } n > 6k
\end{align}
It is not hard to see the constraint 

\begin{align}
    f_1(n) = 
    \begin{cases}
        1 & \text{if } n > 0 \\
        0 & \text{otherwise}
    \end{cases}
\end{align}

These are the edge cases we can identify because of constraints in hand. Before trying to find the function for general $k$ and $n$ lets try a special case.

For a special case of $f_3(7)$, i.e., the number of ways we can express $7$ as a sum of $3$ integers between $1$ and $6$

We can write $7$ as a sum of 2 integers as

1 + 6 or 2 + 5 or 3 + 4 or 4 + 3 or 5 + 2 or 6 + 1 
There are a total of 6 ways we can do it. But if we want to express it as  sum of 3 integers then we can write the second integer as a sum of 2 integer. Then the number of ways we can express $7$ as a sum of three integers becomes the sum of the number of ways we can express 6 as sum of 2 integers plus the number of ways we can write 5 as a sum of 2 integers and so on.

This leads us to write 

\begin{align}
    f_3(7) = f_2(6) + f_2(5) + f_2(4) + f_2(3) + f_2(2) + f_2(1)
\end{align}

This suggests us a general expression  for $k \geq 2$

\begin{align}
    f_k(n) = \sum_i f_{k-1}(n-i) 
\end{align}

This is a recursive function the general expression for all $k$ then is 

\begin{align}
    f_k(n) = 
    \begin{cases}
        1 & \text{ if } k = 1 \\
        \sum_i f_{k-1}(n-i) & \text{ if } k > 1
    \end{cases}
\end{align}

Below is a python function that calculates this function


```python
def F(k,n,minno=1,maxno=6):
    if n < 1 or n < k:
        return 0
    if k == 1:
        return 0 if n > maxno else 1
    else:
        return sum([F(k-1,n-i) for i in np.arange(minno,maxno+1,1)])
```

The probability $p_k(m)$ that we get a total of $n$ when we roll $k$ dice can  then simply becomes
\begin{align}
    p_k(n) = \frac{f_k(n)}{6^k}
\end{align}

Where the denominator is the number of all possible ways of rolling $k$ dice.

Below is a python function that calculates this probability


```python
def p(k,n,dice_op=np.arange(1,6+1,1)):
    return F(k,n)/len(dice_op)** k #len (dice_op) is just 6
```

Before we go to the game of win an draw lets see graphically how do the number look like.  The plot below shows the count (left) and probability(right) of the sum (x-axis) when $m$ dice (inset) are rolled


```python
def plot_counts(ms,dice_op=np.arange(1,6+1,1),plpr=False,ax=None):
    for m in ms:
        total_op = len(dice_op)**int(m)
        ns = np.arange(m,6*m+1,1)
        cnts = [F(m,n) for n in ns]
            
        pvl = np.array(cnts)/total_op if plpr else cnts
        ax.plot(pvl,'-o',label=f'm={m}')

    ax.legend()
```


```python
fig,ax = plt.subplots(1,2,figsize=(18,6),sharex=True)
plot_counts([1,2,3,4],plpr=False,ax=ax[0])
plot_counts([1,2,3,4],plpr=True,ax=ax[1])
ax[0].set_xlabel('Sum'); ax[0].set_ylabel('Count')
ax[1].set_xlabel('Sum'); ax[1].set_ylabel('pmf');
plt.tight_layout()
plt.savefig('Prob_count',dpi=120,bbox_inches='tight')
```


<img src="{{'/static/img/Split_11_0.png' | prepend: site.baseurl | prepend: site.url }}"/>


# Probability of tie
The pobability of tie in a game of two players throwing $k$ and $m$ die respectively is simply the probability that they roll the same sum. The set of possible sum of player with k die is 

\begin{align}
    N_1 = \left\lbrace n_i | k \leq n_i \leq 6k \right\rbrace
\end{align}

Similarly for other player

\begin{align}
    N_2 = \left\lbrace n_i | m \leq n_i \leq 6m \right\rbrace
\end{align}

    
Which can be easily written as 

\begin{align}
    p(\text{tie}) = \sum_{n = N_1 \bigcap N_2} p(k,n) \cdot p(m,n)
\end{align}

The python function for this written as 


```python
def get_tie_prob(m,k):
    n1 = np.arange(m,6*m+1,1)
    n2 = np.arange(k,6*k+1,1)
    return sum([p(m,n)*p(k,n) for n in n1 if n in n2])
```

I have this helper function that calculates generates the table of values.


```python
def generate_table(ms,ks,func=get_tie_prob):
    prob_table = np.zeros(shape=(len(ms),len(ks)))
    for m in ms:
        for k in ks:
            prob_table[m-1][k-1] = func(m,k)
    df = pd.DataFrame(prob_table,columns=ms,index=ks)
    return df
```

Lets say $ms$ is the set of number of dice player1 has and $ks$ be the number of dice playe 2 has then


```python
maxn=6
ms = ks = np.arange(1,maxn+1,1)
```


```python
%time tie_prob_table = generate_table(ms,ks,get_tie_prob)
```

    CPU times: user 1.78 s, sys: 48 ms, total: 1.83 s
    Wall time: 1.78 s



```python
tie_prob_table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.166667</td>
      <td>0.069444</td>
      <td>0.015432</td>
      <td>0.001929</td>
      <td>0.000129</td>
      <td>0.000004</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.069444</td>
      <td>0.112654</td>
      <td>0.069444</td>
      <td>0.024884</td>
      <td>0.005955</td>
      <td>0.001017</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.015432</td>
      <td>0.069444</td>
      <td>0.092850</td>
      <td>0.065469</td>
      <td>0.029940</td>
      <td>0.009822</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.001929</td>
      <td>0.024884</td>
      <td>0.065469</td>
      <td>0.080944</td>
      <td>0.061479</td>
      <td>0.032624</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.000129</td>
      <td>0.005955</td>
      <td>0.029940</td>
      <td>0.061479</td>
      <td>0.072693</td>
      <td>0.057935</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.000004</td>
      <td>0.001017</td>
      <td>0.009822</td>
      <td>0.032624</td>
      <td>0.057935</td>
      <td>0.066539</td>
    </tr>
  </tbody>
</table>
</div>



The probability of tie when players have $(m,k)$ dice respectively corresponds to the cell $(m,k)$ in the table above.

# The probability for win

Similarly the probability of win for player with $m$ dice is the probability that the player $k$ throws a sum $i$ times the sum of probabilities of ways player $m$ throws $j$ dice such $j > i$ 


\begin{align}
    o(\text{win}) = \sum_{i = N_2} p(k,i) \cdot \left(  \sum_{j \in N_1 ; j > i}  p(m,j)  \right)
\end{align}

The python function implementing this function is 


```python
def get_win_prob(m,k):
    if m > k:
        wkm = get_win_prob(k,m)
        tkm = get_tie_prob(k,m)
        return  1 - wkm - tkm
    n1s = np.arange(m,6*m+1,1)
    n2s = np.arange(k,6*k+1,1)
    
    win_prob = sum([p(k,i) * sum([p(m,j) for j in n1s if j > i]) for i in n2s])
    
    return win_prob
```

Generating the table


```python
%time win_prob_table = generate_table(ms,ks,get_win_prob)
```

    CPU times: user 19.4 s, sys: 189 ms, total: 19.6 s
    Wall time: 19.5 s



```python
win_prob_table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.416667</td>
      <td>0.092593</td>
      <td>0.011574</td>
      <td>0.000772</td>
      <td>0.000021</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.837963</td>
      <td>0.443673</td>
      <td>0.152006</td>
      <td>0.035880</td>
      <td>0.006105</td>
      <td>0.000766</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.972994</td>
      <td>0.778549</td>
      <td>0.453575</td>
      <td>0.191701</td>
      <td>0.060713</td>
      <td>0.014879</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.997299</td>
      <td>0.939236</td>
      <td>0.742831</td>
      <td>0.459528</td>
      <td>0.220442</td>
      <td>0.083423</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.999850</td>
      <td>0.987940</td>
      <td>0.909347</td>
      <td>0.718078</td>
      <td>0.463654</td>
      <td>0.242449</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.999996</td>
      <td>0.998217</td>
      <td>0.975300</td>
      <td>0.883953</td>
      <td>0.699616</td>
      <td>0.466731</td>
    </tr>
  </tbody>
</table>
</div>



The probability of win for player $m$ when players have $(m,k)$ dice respectively corresponds to the cell $(m,k)$ in the table above.
