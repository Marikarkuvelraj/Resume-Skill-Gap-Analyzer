from app import app

def run_tests():
    with app.test_client() as c:
        r = c.get('/api/job_roles')
        print('JOB_ROLES:', r.get_data(as_text=True))
        payload = {'resume_text':'I have experience with python and excel','job_role':'Data Analyst'}
        r2 = c.post('/api/analyze', json=payload)
        print('ANALYZE:', r2.get_data(as_text=True))

if __name__ == '__main__':
    run_tests()
