# *QuickCV*
This website simplifies the process of creating [ATS](#ats) friendly resumes. User will input their data and the website will handle the creation. The generated resume is optimized for ATS compatibility without the hassle of tedious formatting.

Whether you are a newbie who does not know how to create resumes, or you simply want to bypass the hassle of formatting; this website is your answer!

The LaTex resume template used is one of the highly sought after FAANG resumes!


# Installation

bash
git clone https://github.com/nishantak/resume_builder.git
cd resume_builder
pip install flask
python main.py


Since this is a prototype, it is not, as of now, web-hosted. Access the website at your localhost at http://localhost:5000


### ATS

ATS (Applicant Tracking System) is software used by employers at almost all conglomerates, even more so at FAANG, to manage applicant screening, resume parsing, and candidate communication. The system streamlines the hiring process by automatically filtering and organizing incoming resumes based on specific criteria set by the employer.

- An ATS friendly resume is usually only a page long
- An ATS friendly resume sticks to a clean, easy-to-read layout with standard fonts and consistent formatting
- Tailor your resume by including relevant keywords from the job description to match the ATS filtering criteria
- ATS avoids graphics and images
- Clearly label sections such as "Work Experience," "Education," and "Skills" to help ATS categorize your information accurately