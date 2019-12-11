# LINE
This is Tensorflow implementation of LINE. 
> 
> PyTorch reference : [https://github.com/DMPierre/LINE](https://github.com/DMPierre/LINE)
>

## Dependencies
- TensorFlow 1.14.0

## Usage
`cd LINE`

`python main.py --input ../data/test.edgelist --output ../output/test.embedding --dimension 10 --K 2 --iter 50`

**Arguments:**

* --input : edgelist file path.
    ```
    1 2 1 (source target weight)
    2 3 2
    3 4 1
    ...
    ```
* --output : embedding output path
* --iter : number of iterations (optional)
* --proximity : depth for neighbour (first-order or second-order) (optional)


## Citation
```
Tang, J., Qu, M., Wang, M., Zhang, M., Yan, J., & Mei, Q. (2015, May). Line: Large-scale information network embedding. In Proceedings of the 24th international conference on world wide web (pp. 1067-1077). International World Wide Web Conferences Steering Committee.
```