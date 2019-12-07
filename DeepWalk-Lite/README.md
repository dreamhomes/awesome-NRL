## DeepWalk-Lite
>
> source: [https://github.com/phanein/deepwalk](https://github.com/phanein/deepwalk)
>

### Dependencies
- python 3.7
- argparse>=1.2.1
- six>=1.7.3
- gensim>=1.0.0
- networkx>=2.0


### Usage
`cd DeepWalk-Lite`

`python main.py --input ../data/cora/cora.edgelist --output ../output/cora.embedding --model skipgram`

Note:

`--input` for an edge list, e.g:
```
1 2
1 3
1 4
...
```