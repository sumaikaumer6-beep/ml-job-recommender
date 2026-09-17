import  pandas as pd
import numpy as np
def get_job_recommendations(user_skills, all_jobs):
    user_skills = [s.strip().lower() for s in user_skills.split(',')]
    data = []
    for job in all_jobs:
        match = sum(1 for s in user_skills if s in job.skills_required.lower())
        score = np.round((match/len(user_skills))* 100, 2) if user_skills else 0
        data.append((job, score))
    df = pd.DataFrame(data, columns=['job', 'score'])
    df = df.sort_values('score', ascending=False)
    return list(zip(df['job'], df['score']))