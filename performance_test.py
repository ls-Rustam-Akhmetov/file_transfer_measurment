import time
from typing import Callable

from config_reader import get_test_config
from model import ServerAccess


def performance_test(
        measurable_file_loading_function: Callable[[ServerAccess], None],
        remove_remote_file_function: Callable[[ServerAccess], None],
        iterations_amount: int
):
    exec_time_list: list[float] = []
    print("---------------------------------------------------------------------------------")
    print("Started function cycles: ", measurable_file_loading_function.__name__)
    for i in range(0, iterations_amount):
        start_time = time.time()
        configs: ServerAccess = get_test_config()
        print("Function name: ", measurable_file_loading_function.__name__, " iteration: ", i)

        measurable_file_loading_function(configs)

        end_time = time.time()
        execution_time = end_time - start_time

        print("Function iteration execution ended. Execution time:", execution_time, "seconds or ", execution_time / 60,
              " minutes")
        exec_time_list.append(execution_time)

        remove_remote_file_function(configs)
        print("Remote files war cleaned")
        print("Ended iteration: ", i)
        print("---------------------------")

    sum_time: float = sum(exec_time_list)
    average_time: float = sum_time / iterations_amount

    print("Ended function cycles, iterations amount: ", iterations_amount, " average time in seconds: ", average_time,
          " in seconds and ", average_time / 60, " in minutes")
    print("---------------------------------------------------------------------------------")
