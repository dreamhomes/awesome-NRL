## DeepWalk
>
> source: [https://github.com/phanein/deepwalk](https://github.com/phanein/deepwalk)
>

### Dependencies
- python 3.7
- wheel>=0.23.0
- Cython>=0.20.2
- argparse>=1.2.1
- futures>=2.1.6
- six>=1.7.3
- gensim>=1.0.0
- scipy>=0.15.0
- psutil>=2.1.1
- networkx>=2.0


### Usage
`cd DeepWalk`

`python main.py --format edgelist --input D:/VScodeWorkspace/awesome-NRL/data/cora/cora.edgelist --output D:/VScodeWorkspace/awesome-NRL/output/cora.embedding --undir 
ected false`

Note:

`--format edgelist` for an edge list, e.g:
```
1 2
1 3
1 4
...
```