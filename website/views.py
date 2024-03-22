from flask import Blueprint, render_template, request, send_file, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/ats')
def ats():
    return render_template('ats.html')


# def fill_latex_template(basic_info, educational_details, technical_skills, soft_skills, work_experience, projects, leadership_experience):
#     template = r"""
#     \documentclass{resume} 

#     \usepackage[left=0.4 in,top=0.4in,right=0.4 in,bottom=0.4in]{geometry} % Document margins
#     \newcommand{\tab}[1]{\hspace{.2667\textwidth}\rlap{#1}} 
#     \newcommand{\itab}[1]{\hspace{0em}\rlap{#1}}
#     \name{""" + basic_info['Full Name'] + r"} % Your name\n\n" + \
#     r"\address{" + basic_info['Mobile Number'] + r" \\ San Francisco, CA}\n" + \
#     r"\address{\href{mailto:" + basic_info['Email'] + r"}{contact@gmail.com} \\ \href{" + basic_info['Website'] + r"}{linkedin.com/} \\ \href{www..com}{www..com}}  %\n\n" + \
#     r"\begin{document}\n\n" + \
#     r"\begin{rSection}{OBJECTIVE}\n" + \
#     r"{" + basic_info['Objective'] + r"}\n" + \
#     r"\end{rSection}\n\n" + \
#     r"\begin{rSection}{Education}\n"

#     # Fill educational details
#     for i, edu in enumerate(educational_details, start=1):
#         template += r"{\bf " + edu['Degree'] + r"}, " + edu['Institution Name'] + r" \hfill {" + edu['From - Till'] + r"}\n" + \
#                     r"Relevant Coursework: " + edu['Coursework'] + r".\n\n"

#     template += r"\end{rSection}\n\n" + \
#                 r"\begin{rSection}{SKILLS}\n" + \
#                 r"\begin{tabular}{ @{} >{\bfseries}l @{\hspace{6ex}} l }\n" + \
#                 r"Technical Skills & " + ', '.join(technical_skills) + r" \\\\" + \
#                 r"Soft Skills & " + ', '.join(soft_skills) + r" \\\\\n" + \
#                 r"\end{tabular}\n" + \
#                 r"\end{rSection}\n\n" + \
#                 r"\begin{rSection}{EXPERIENCE}\n"

#     # Fill work experience
#     for exp in work_experience:
#         template += r"\textbf{" + exp['Role Name'] + r"} \hfill " + exp['Work From - Till'] + r"\n" + \
#                     exp['Company Name - Location'] + r"\n" + \
#                     r"\begin{itemize}\n" + \
#                     r"    \itemsep -3pt {}\n" + \
#                     r"    \item " + exp['Achievements'] + r"\n" + \
#                     r"\end{itemize}\n\n"

#     template += r"\end{rSection}\n\n" + \
#                 r"\begin{rSection}{PROJECTS}\n"

#     # Fill projects
#     for proj in projects:
#         template += r"\vspace{-1.25em}\n" + \
#                     r"\item \textbf{" + proj['Project Title'] + r".} " + proj['Project Description'] + r"\n"

#     template += r"\end{rSection}\n\n" + \
#                 r"\begin{rSection}{Extra-Curricular Activities}\n" + \
#                 r"\begin{itemize}\n"

#     # Fill leadership experience
#     for lead_exp in leadership_experience:
#         template += r"\item " + lead_exp['Leadership Description'] + r"\n"

#     template += r"\end{itemize}\n" + \
#                 r"\end{rSection}\n\n" + \
#                 r"\end{document}"

#     print(template)


# NLP Stuff
from nlp import modify_des

@views.route('/generate_resume', methods=['POST'])
def gen_res():
    con = request.form.get('context_description')

    # Get basic information
    basic_info = {
        'Full Name': request.form.get('full_name'),
        'Email': request.form.get('email'),
        'Mobile Number': request.form.get('mobile_number'),
        'Gender': request.form.get('gender'),
        'Website': request.form.get('website'),
        'Objective': request.form.get('objective')
    }

    # Educational Details
    educational_details = []
    for i in range(1, 5):
        qualification = request.form.get(f'qualification{i}')
        degree = request.form.get(f'degree{i}')
        institution_name = request.form.get(f'institution_name{i}')
        from_till = request.form.get(f'from_till{i}')
        gpa = request.form.get(f'gpa{i}')
        coursework = request.form.get(f'coursework{i}')

        if degree:
            educational_details.append({
                f'Qualification {i}': qualification,
                'Degree': degree,
                'Institution Name': institution_name,
                'From - Till': from_till,
                'GPA': gpa,
                'Coursework': coursework
            })

    # Skills
    technical_skills = request.form.get('technical_skills').split(', ')
    technical_proficiency = request.form.get('technical_proficiency').split(', ')
    soft_skills = request.form.get('soft_skills').split(',')
    soft_proficiency = request.form.get('soft_proficiency').split(',')

    technical_dict = dict(zip(technical_skills, technical_proficiency))
    soft_dict = dict(zip(soft_skills, soft_proficiency))

    # Work Experience
    work_experience = []
    for i in range(1, 4):
        role_name = request.form.get(f'role_name{i}')
        company_name_location = request.form.get(f'company_name_location{i}')
        work_from_till = request.form.get(f'work_from_till{i}')
        achievements = request.form.get(f'achievements{i}')

        if role_name:
            work_experience.append({
                'Role Name': role_name,
                'Company Name - Location': company_name_location,
                'Work From - Till': work_from_till,
                'Achievements': modify_des(con, achievements, 'wex')
            })

    # Projects
    projects = []
    for i in range(1, 4):
        project_title = request.form.get(f'project_title{i}')
        tech_stack = request.form.get(f'tech_stack{i}')
        project_description = request.form.get(f'project_description{i}')

        if project_title:
            projects.append({
                'Project Title': project_title,
                'Tech Stack': tech_stack,
                'Project Description': modify_des(con, project_description, 'proj')
            })

    # Leadership Experience
    leadership_experience = []
    for i in range(1, 4):
        leadership_description = request.form.get(f'leadership_description{i}')

        if leadership_description:
            leadership_experience.append({
                'Leadership Description': modify_des(con, leadership_description, 'lex')
            })
    
	# fill_latex_template(basic_info, educational_details, technical_skills, soft_skills, work_experience, projects, leadership_experience)
            
    try:
        # Writing data to file
        with open('website/1.txt', 'w') as file:
            # Write basic information
            file.write('Basic Information:\n')
            for key, value in basic_info.items():
                file.write(f"{key}: {value}\n")

            # Write educational details
            file.write('\nEducational Details:\n')
            for edu in educational_details:
                for key, value in edu.items():
                    file.write(f"{key}: {value}\n")
                file.write('\n')

            # Write skills
            file.write('\nSkills:\nTechnical Skills:\n')
            for skill, proficiency in technical_dict.items():
                file.write(f"{skill}: {proficiency}\n")

            file.write('\nSoft Skills:\n')
            for skill, proficiency in soft_dict.items():
                file.write(f"{skill}: {proficiency}\n")

            # Write work experience
            file.write('\nWork Experience:\n')
            for exp in work_experience:
                for key, value in exp.items():
                    file.write(f"{key}: {value}\n")
                file.write('\n')

            # Write projects
            file.write('\nProjects:\n')
            for proj in projects:
                for key, value in proj.items():
                    file.write(f"{key}: {value}\n")
                file.write('\n')

            # Write leadership experience
            file.write('\nLeadership Experience:\n')
            for leader_exp in leadership_experience:
                for key, value in leader_exp.items():
                    file.write(f"{key}: {value}\n")
                file.write('\n')
        
        return send_file('1.txt')  

    except Exception as e:
        return f"Error occurred: {str(e)}"
