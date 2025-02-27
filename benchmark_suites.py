import time
import functools
import pyperf

# First function: Computes the sum of numbers up to n,
# with an artificial delay to simulate workload.
def function_a(n, delay):
    # Simulate work by sleeping for a given delay...
    time.sleep(delay)
    # Compute the sum of numbers from 0 to n-1.
    return sum(range(n))

# Second function: Computes the factorial of n,
# with an artificial delay to simulate workload.
def function_b(n, delay):
    time.sleep(delay)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def benchmark_functions():
    # Create a pyperf Runner instance.
    runner = pyperf.Runner()

    # Create an empty list to collect the benchmarks.
    benchmarks = []

    # Define a list of parameter sets for function_a.
    params_for_a = [
        {'n': 1000, 'delay': 0.001},
        {'n': 5000, 'delay': 0.001},
    ]

    # Define a list of parameter sets for function_b.
    params_for_b = [
        {'n': 10, 'delay': 0.001},
        {'n': 12, 'delay': 0.001},
    ]

    # Benchmark function_a with different parameters.
    for params in params_for_a:
        benchmark_name = f"function_a(n={params['n']}, delay={params['delay']})"
        bench = runner.bench_func(
            benchmark_name,
            functools.partial(function_a, **params)
        )
        benchmarks.append(bench)

    # Benchmark function_b with different parameters.
    for params in params_for_b:
        benchmark_name = f"function_b(n={params['n']}, delay={params['delay']})"
        bench = runner.bench_func(
            benchmark_name,
            functools.partial(function_b, **params)
        )
        print("bench: ", bench)
        benchmarks.append(bench)

    # Create a BenchmarkSuite from all collected benchmarks.
    print("BENCHMARKS: ", benchmarks)
    suite = pyperf.BenchmarkSuite(benchmarks)

    # Dump the benchmark suite to a JSON file.
    # This file will contain all the benchmark runs and metadata.
    suite.dump("suiteResults.json")

if __name__ == '__main__':
    benchmark_functions()
