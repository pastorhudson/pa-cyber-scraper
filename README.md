# pa-cyber-scraper
This project scrapes https://myschool.pacyber.org to tell me my son's current Academic Snapshot / Grades.
You can use this from the commandline or pipe the output into another script to send daily emails, txt, etc.

### Setup:
- Clone this repo
    - `git clone https://github.com/pastorhudson/pa-cyber-scraper.git`
- Edit `secrets_env` and save it as `secrets.env`
    - Edit the two fields replacing the xxxxx with your Username and Password
    - `TBLOGIN='xxxxxxxxx'`
    - `TBPASSWORD='xxxxxx'`
- Install requirements
    - `pip install -r requirements.txt`
    - Or individually:
        - `pip install beautifulsoup4 python-dotenv requests`

### Run The Program
- `python3 get_grades.py` 
- It will print out the Current academic snapshot.

```
English 9
Enrollment: Aug 26, 2020 to Jun 07, 2021
Grade: XX%
Assignments: 35 of 173
Pacing: 2 assignments behind
Last Activity: Oct 29, 2020

Geometry
Enrollment: Aug 26, 2020 to Jun 07, 2021
Grade: XX%
Assignments: 16 of 72
Pacing: 1 assignment ahead
Last Activity: Oct 29, 2020

Biology
Enrollment: Aug 26, 2020 to Jun 07, 2021
Grade: XX%
Assignments: 24 of 95
Pacing: 1 assignment ahead
Last Activity: Oct 29, 2020

Civics
Enrollment: Aug 26, 2020 to Jun 07, 2021
Grade: XX%
Assignments: 49 of 194
Pacing: 2 assignments ahead
Last Activity: Oct 29, 2020

Explorations in Media Arts
Enrollment: Aug 26, 2020 to Jun 07, 2021
Grade: XX%
Assignments: 6 of 138
Pacing: 3 assignments behind
Last Activity: Oct 26, 2020

Physical Education 9
Enrollment: Aug 26, 2020 to Jun 07, 2021
Grade: 
Assignments: 4 of 24
Pacing: 1 assignments behind
Last Activity: Oct 08, 2020

Introduction to Digital Photography
Enrollment: Aug 26, 2020 to Jun 07, 2021
Grade: XX%
Assignments: 18 of 91
Pacing: 3 assignments behind
Last Activity: Oct 16, 2020

Health
Enrollment: Aug 26, 2020 to Jun 07, 2021
Grade: XX%
Assignments: 14 of 67
Pacing: 2 assignments behind
Last Activity: Oct 22, 2020
```