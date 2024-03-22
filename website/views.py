from flask import Blueprint, render_template, request, send_file, redirect, url_for
import subprocess

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template('index.html')

@views.route('/ats')
def ats():
	return render_template('ats.html')


#NLP stff
from .nlp import modify_des

@views.route('/generate_resume', methods=['POST'])
def gen_res():
	#NLP Context
	con = request.form.get('context_description')
	print(con)

    # Get basic information
	basic_info = {
		'Full Name': request.form.get('full_name'),
		'Email': request.form.get('email'),
		'Mobile Number': request.form.get('mobile_number'),
		'Gender': request.form.get('gender'),
		'Website': request.form.get('website')
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
				f'Qualification {i}' : qualification,
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
				f'Role Name {i}': role_name,
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
				f'Project Title {i}': project_title,
				'Tech Stack': tech_stack,
				'Project Description': modify_des(con, project_description, 'proj')
			})

	# Leadership Experience
	leadership_experience = []
	for i in range(1, 4):
		leadership_description = request.form.get(f'leadership_description{i}')

		if leadership_description:
			leadership_experience.append({
				f'Leadership Description {i}': modify_des(con, leadership_description, 'lex')
			})

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

		return send_file("1.txt")	
	
	except Exception as e:
   		return f"Error occurred: {str(e)}"

