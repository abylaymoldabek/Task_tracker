def text_not(task):
    planning = f"Привет, твой таск {task.id} начался, и статус стоит на {task.status[1]}"
    active = f"Привет,статус твоего таска номером {task.id} изменился, стоит на {task.status[2]}"
    finished = f"Привет,статус твоего таска номером {task.id} изменился, стоит на {task.status[3]}"
    return planning, active, finished
