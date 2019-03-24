def SynchronizingTables(N,ids,salary):
    new_salary = sorted(salary)
    new_ids = sorted(ids)
    for i in range(N):
        for j in range(N):
            if ids[i] == new_ids[j]:
                salary[i] = new_salary[j]
    return salary
