from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_ty = set()
    for job in jobs_list:
        job_ty.add(job["job_type"])

    return job_ty


def filter_by_job_type(jobs, job_type):
    match_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            match_jobs.append(job)

    return match_jobs


def get_unique_industries(path):
    jobs_list = read(path)
    industry_list = set()
    for industry in jobs_list:
        if industry["industry"] != "":
            industry_list.add(industry["industry"])

    return industry_list


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    jobs_list = read(path)
    max_salary_list = set()
    highest_salary = 0
    for salary in jobs_list:
        if salary["max_salary"].isnumeric():
            max_salary_list.add(int(salary["max_salary"]))
            highest_salary = max(max_salary_list)
    return highest_salary


def get_min_salary(path):
    jobs_list = read(path)
    min_salary_list = set()
    lowest_salary = 0
    for salary in jobs_list:
        if salary["min_salary"].isnumeric():
            min_salary_list.add(int(salary["min_salary"]))
            lowest_salary = min(min_salary_list)
    return lowest_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
