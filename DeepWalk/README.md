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

### Citation

```
@inproceedings{Perozzi:2014:DOL:2623330.2623732,
 author = {Perozzi, Bryan and Al-Rfou, Rami and Skiena, Steven},
 title = {DeepWalk: Online Learning of Social Representations},
 booktitle = {Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
 series = {KDD '14},
 year = {2014},
 isbn = {978-1-4503-2956-9},
 location = {New York, New York, USA},
 pages = {701--710},
 numpages = {10},
 url = {http://doi.acm.org/10.1145/2623330.2623732},
 doi = {10.1145/2623330.2623732},
 acmid = {2623732},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {deep learning, latent representations, learning with partial labels, network classification, online learning, social networks},
}

```