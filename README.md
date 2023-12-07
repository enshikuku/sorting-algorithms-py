# Sorting Algorithms in Python

This repository contains various sorting algorithms implemented in Python. Additionally, it includes a random number generator implemented in HTML and Python.

## Random Numbers Generator

Preview the [Random Numbers Generator](https://enshikuku.github.io/sorting-algorithms-py/random-generator.html) implemented in HTML.

## Files and Directories

- [`all-sorting.py`](all-sorting.py): A Python script that combines all sorting algorithms into a single file.
- [`random-generator.html`](random-generator.html): An HTML file for a random number generator.
- [`random-numbers.py`](random-numbers.py): A Python script for generating random numbers.
- `sortings/`: Directory containing individual sorting algorithm implementations.
  - [`bubble-sort.py`](sortings/bubble-sort.py): Bubble Sort implementation.
  - [`bucket-sort.py`](sortings/bucket-sort.py): Bucket Sort implementation.
  - [`heap-sort.py`](sortings/heap-sort.py): Heap Sort implementation.
  - [`insertion-sort.py`](sortings/insertion-sort.py): Insertion Sort implementation.
  - [`merge-sort.py`](sortings/merge-sort.py): Merge Sort implementation.
  - [`quick-sort.py`](sortings/quick-sort.py): Quick Sort implementation.
  - [`radix-sort.py`](sortings/radix-sort.py): Radix Sort implementation.
  - [`selection-sort.py`](sortings/selection-sort.py): Selection Sort implementation.
  - [`shell-sort.py`](sortings/shell-sort.py): Shell Sort implementation.

  Each sorting algorithm is accompanied by a brief explanation and instructions on how to run them independently.

- `static/`: Directory containing static assets.
  - [`favicon.png`](static/favicon.png): Favicon for the repository.
  - [`main.js`](static/main.js): JavaScript file for dynamic content.
  - [`style.css`](static/style.css): Cascading Style Sheets for styling.

## Sorting Algorithms

### Bubble Sort
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

#### How to Run:
Navigate to the `sortings/` directory and run the following command:

```bash
python bubble-sort.py
```

### Bucket Sort
Bucket Sort is a sorting algorithm that distributes the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sorting algorithm.

#### How to Run:
Navigate to the `sortings/` directory and run the following command:

```bash
python bucket-sort.py
```

### Heap Sort
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to build a max-heap and then performs a heap deletion to extract the maximum element and rebuild the heap.

#### How to Run:
Navigate to the `sortings/` directory and run the following command:

```bash
python heap-sort.py
```

### Insertion Sort
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

#### How to Run:
Navigate to the `sortings/` directory and run the following command:

```bash
python insertion-sort.py
```

### Merge Sort
Merge Sort is a divide-and-conquer algorithm that divides the unsorted list into n sublists, each containing one element, and then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining.

#### How to Run:
Navigate to the `sortings/` directory and run the following command:

```bash
python merge-sort.py
```

### Quick Sort
Quick Sort is an efficient, in-place sorting algorithm that uses a divide-and-conquer strategy to divide the array into smaller subarrays and then sorts the subarrays.

#### How to Run:
Navigate to the `sortings/` directory and run the following command:

```bash
python quick-sort.py
```

### Radix Sort
Radix Sort is a non-comparative sorting algorithm that sorts numbers by processing individual digits. It sorts numbers with the least significant digit first and the most significant digit last.

#### How to Run:
Navigate to the `sortings/` directory and run the following command:

```bash
python radix-sort.py
```

### Selection Sort
Selection Sort is a simple sorting algorithm that divides the input list into a sorted and an unsorted region. It repeatedly selects the smallest (or largest) element from the unsorted region and swaps it with the first element of the unsorted region.

#### How to Run:
Navigate to the `sortings/` directory and run the following command:

```bash
python selection-sort.py
```

### Shell Sort
Shell Sort is an in-place comparison sort. It starts by sorting pairs of elements far apart from each other, then progressively reduces the gap between elements to be compared.

#### How to Run:
Navigate to the `sortings/` directory and run the following command:

```bash
python shell-sort.py
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/enshikuku/sorting-algorithms-py.git
```

2. Navigate to the repository:

```bash
cd sorting-algorithms-py
```

3. Run the sorting algorithms:

```bash
python all-sorting.py
```

4. Open `random-generator.html` in a web browser to use the random number generator.

Feel free to explore and use the individual sorting algorithm scripts in the `sortings/` directory for specific algorithms.

## Contribution

To contribute, follow the steps outlined in the [Contribution Guide](CONTRIBUTING.md).
