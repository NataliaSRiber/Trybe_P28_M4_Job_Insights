from src.sorting import sort_by
# min_salary_key


jobs = [
    {
        "min_salary": 500,
        "max_salary": 1500,
        "date_posted": "2021-12-04",
    },
    {
        "min_salary": 1500,
        "max_salary": 2500,
        "date_posted": "2021-11-09",
    },
    {
        "min_salary": 800,
        "max_salary": 2900,
        "date_posted": "2021-09-23",
    },
    {
        "min_salary": 700,
        "max_salary": 1900,
        "date_posted": "2021-01-23",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == 500

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == 2900

    sort_by(jobs, "min_salary")
    assert jobs[0]["date_posted"] == "2021-12-04"
