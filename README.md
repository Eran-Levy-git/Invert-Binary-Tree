# Inverted Binary Tree

This project provides a solution for inverting a binary tree. It includes classes for representing a binary tree, a solution to invert the tree, and auxiliary functions for tree manipulation and visualization.

## Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Example](#examples)

## Introduction

Inverting a binary tree means swapping the left and right child nodes of each node in the tree. The `Solution` class provides a method `invert_tree` that recursively inverts the tree.

The `TreeNode` class represents a node in the binary tree and contains the value and references to its left and right child nodes.

The `Auxiliary` class provides auxiliary functions for tree manipulation, such as calculating the height of the tree and printing the tree in a visually appealing format.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/inverted-binary-tree.git
```

Import the required classes and functions:

```py
from inverted_binary_tree import TreeNode, Solution, Auxiliary
```
## Example

The output will be:


```markdown 
Original Tree:
   ┌── 9
┌── 7
│   └── 6
4
│   ┌── 3
└── 2
    └── 1

Inverted Tree:
   ┌── 1
┌── 2
│   └── 3
4
│   ┌── 6
└── 7
    └── 9
````
