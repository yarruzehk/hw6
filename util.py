def snake_case(x: str):
    return x.lower().strip().replace(" ", "_")


def count_passing_tests(pytest_str: str):
    lines = [
        line.strip() for line in pytest_str.splitlines(False) if line.strip() != ""
    ]
    final_line = next(reversed(lines))
    results = final_line.split()
    try:
        pindex = results.index("passed")
        return int(results[pindex - 1])
    except ValueError:
        return 0
