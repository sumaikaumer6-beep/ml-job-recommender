# ML Job Recommender System
An intelligent job recommendation system that matches job seekers with relevant jobs using machine Learning and content-based Filtering.
### Key Features
- User Authentication & profile Management
- Skill-based Job Matching using ML
- Personalized Job Recommendations
- Admin Dashboard for Job Management
### Tech Stack
- **Backend:** Django, Python
- **Machine Learning:** pandas, NumPy
- **Frontend:** HTML, CSS
  ### How ML Works
  1. User skills are vectorized
  2. Job descriptions are also vectorized
  3. Cosine Similarity calculates match score
  4. Top matched jobs are recommended to user
  ### How to Run Locally
  ```bash
  cd ml-job-recommender
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
  python manage.py migrate
  python manage.py runserver
