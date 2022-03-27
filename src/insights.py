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
    filtered_industries = []
    for industry1 in jobs:
        if industry1["industry"] == industry:
            filtered_industries.append(industry1)
    return filtered_industries


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


#  fonte: https://pt.stackoverflow.com/questions/210010/como
# -verificar-se-o-valor-de-vari%C3%A1vel-string-%C3%A9-numero
def matches_salary_range(job, salary):
    if ("max_salary" or "min_salary") not in job:
        raise ValueError  # ou ValueError()
    elif type(job["max_salary"]) != int or type(job["min_salary"]) != int:
        raise ValueError
    elif job["max_salary"] < job["min_salary"]:
        raise ValueError
    elif type(salary) != int:
        raise ValueError
    else:
        return (salary <= job["max_salary"] and salary >= job["min_salary"])


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
