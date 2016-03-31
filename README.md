### James Moloney
#### G00304978

# Countdown Letters Game Solver
Creating an algorithm that solves the nine letter Countdown game according to the rules of the game.
Also to create the wordlist used in the project but for the mean time we'll use wordsEn.txt.


## Background
The first task I completed as part of this project was to Google "countdown letters game solver".
Google gave me two relevant results on the first page, these are [Countdown solver][1] and [Countdown letters game solver][2].
The rules of the game are to be found [here][4]


## Words list
My words list is in the file [wordsEN.txt](wordsEn.txt) in this repository/gist.
I got my words list from the [English Wordlists ][3] website.
However my list of 9 (and less than) letter wordlist is [nineOrLess.txt](nineOrLess.txt)


## Python scripts

### countdownAlgo.py
My first run is a very naive solution. 1*9*8*7*6 = 3024 searches through the wordlist in the worst of cases.
And that's only to the fifth letter search. In conjunction with a search through the wordlist array to find a matching hashedWord and the time for a search was staggered throughout the if statements lasting up to several seconds.

```python
if not answer:
      print("to the possible 5s")
      for i in range(len(letters)):
          answer8 = letters[0:(i)] + letters[(i+1):]
          for j in range(len(answer8)):
              answer7 = answer8[0:(j)] + answer8[(j+1):]
              for k in range(len(answer7)):
                  answer6 = answer7[0:(k)] + answer7[(k+1):]
                  for l in range(len(answer6)):
                      answer5 = answer6[0:(l)] + answer6[(l+1):]
                      hashed5Anagram = processWordToHash(answer5)
                      answer = searcher(hashed5Anagram, hashedWords, wordList)
  return answer

```
It worked but it didn't work too well, so I changed it.


### solver.py
My script is in the files [solver.py](solver.py) in this repository and it works as follows.
The most important section is:

```python

for i in range(0, count):
    combs = itertools.combinations(sortedLetters, count)
    #this allows for a maximum of 9c9+c98+9c7+.... which comes to a totol of 502 maximum calls to the
    comb += ["".join(line) for line in combs]
    count -=1
    for combination in comb:
        #print (combination)
        if combination in wordDict.keys():
            return(wordDict[combination])


```


## Preprocessing
My script preprocesses the dictionary, which only needs to be run once.
Once the preprocessing is done we can run the game solver again and again without that overhead.

I had a look at Arjuns Gist preprocessing and followed map would allow for much quicker access time. Python allows of data structures called dict().

```python
def preprocess():
    count=0
    f = open('nineOrLess.txt', 'r')
    words = f.read().split()
    for word in words:
        sortedKey = processWord(word)
        count +=1
        addToDic(sortedKey,word)

def addToDic(key,value):
    if(len(key)>2 and len(key)<10):
        if key in wordDict:
            wordDict.get(key).append(value)
        else:
            wordDict.update({key:[value]})

```
This code implements a dict() structure with keys and values of all the words in my wordlist from 3 to 9 in length. The keys are the words sorted.


## Efficiency
### countdownAlgo.py
My first run is a very naive solution. 9*8*7*6 = 3024 searches through the wordlist in the worst of cases.
And thats only to the fifth letter search.


Using the itertools.combination allows for

```python
nCr  =  	n!
          -----------
         	r!(n - r)!
```

| forumla (n)  | sum   |
|----------|------------|
| 9C9 = 1  |  &nbsp;1   |
| 9C8 = 9  |  &nbsp;10  |
| 9C7 = 36 |  &nbsp;46  |
| 9C6 = 84 |  &nbsp;130 |
| 9C5 = 126| &nbsp;256  |
| 9C4 = 126| &nbsp;382  |
| 9C3 = 84 | &nbsp;466  |
| 9C2 = 36 | &nbsp;502  | possible maximum iterations
| 9C1 = 9  | &nbsp;511  |

http://www.mathcelebrity.com/permutation.php?num=9&den=3&pl=Combinations


## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Countdown letters game.
Testing on 10000 calls with a little preprocessing takes 1.2 seconds
```python
if __name__=='__main__':
    print(algoRunner())
    import timeit
    print(timeit.timeit("algoRunner()",setup="from __main__ import algoRunner", number = 10000))
```

with the sorts of the results like these.

```bash
C:\Users\g0030\Documents\GitHub\AnagramFinder>Solver.py
['carnages']
1.1154833541941422
C:\Users\g0030\Documents\GitHub\AnagramFinder>Solver.py
['cuddled']
1.1015514750372393
C:\Users\g0030\Documents\GitHub\AnagramFinder>Solver.py
['satiated']
1.160394817437988
C:\Users\g0030\Documents\GitHub\AnagramFinder>Solver.py
['outage']
1.1388079622200877
```




## References
[1]: http://incoherency.co.uk/countdown/
[2]: http://datagenetics.com/blog/august52014/index.html
[3]: http://www-01.sil.org/linguistics/wordlists/english/
[4]: https://en.wikipedia.org/wiki/Countdown_(game_show)#Letters_round
