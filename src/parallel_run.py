"""updated from ChatGPT"""
import multiprocessing
import tqdm
import time
from typing import Callable, List, Dict

def sample_function(x, y):
    time.sleep(1)
    return (x * y)


def parallel_run_with_progress_track(func: Callable, kwargs_list: List[Dict], n_processes: int) -> List:
    with tqdm.tqdm(total=len(kwargs_list)) as pbar:
        with multiprocessing.Pool(processes=n_processes) as pool:
            # Submit jobs asynchronously with index to preserve order
            results = []
            for idx, kwarg in enumerate(kwargs_list):
                result = pool.apply_async(
                    func=func, kwds=kwarg,
                    callback=lambda _: pbar.update()
                )
                results.append((idx, result))  # Store index with result
            
            # Close the pool and wait for jobs to complete
            pool.close()
            pool.join()

        # Collect results and sort by the original input order
        final_results = [r.get() for idx, r in sorted(results)]

    return final_results


if __name__ == "__main__":
    kwargs_list = [{'x': i, 'y': i + 1} for i in range(10)]
    final_results = parallel_run_with_progress_track(func=sample_function, kwargs_list=kwargs_list, n_processes=2)
    print(final_results)
