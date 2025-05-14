import functools

import pyperf


def quick_benchmark(n):
    return sum(range(n))


def benchmark_functions():
    runner = pyperf.Runner()
    runner.bench_func("quick_benchmark", functools.partial(quick_benchmark, n=3))


if __name__ == "__main__":
    benchmark_functions()

# run: python benchmarks.py -o results.json
# run: python -m pyperf compare_to results.json results2.json --table
