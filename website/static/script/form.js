var educationCount = 2;
var workExperienceCount = 2;
var projectCount = 2;
var leadershipExperienceCount = 2;

function addEducation() {
    if (educationCount <= 4) {
        var educationFieldset = document.getElementById('educationFieldset');

        var newEducationSection = createFieldset('educationSection', educationCount);
        addField(newEducationSection, `Qualification ${educationCount}`, 'degree');
        addField(newEducationSection, 'Institution Name', 'institution_name');
        addField(newEducationSection, 'From - Till', 'from_till');
        addField(newEducationSection, 'GPA', 'gpa');
        addField(newEducationSection, 'Coursework', 'coursework');

        addRemoveButton(educationFieldset, newEducationSection, 'education');
        educationCount++;
    }
}

function addWorkExperience() {
    if (workExperienceCount <= 3){
        var workExperienceFieldset = document.getElementById('wexFieldset');
        var newWorkExperienceSection = createFieldset('workExperienceSection', workExperienceCount);
        addField(newWorkExperienceSection, `Role Title ${workExperienceCount}`, 'role_name');
        addField(newWorkExperienceSection, 'Company Name - Location', 'company_name_location');
        addField(newWorkExperienceSection, 'Work From - Till', 'work_from_till');
        addTextarea(newWorkExperienceSection, 'Achievements', 'achievements');

        addRemoveButton(workExperienceFieldset, newWorkExperienceSection, 'workExperience');
        workExperienceCount++;
    }
}

function addProject() {
    if (projectCount <= 3) {
        var projectFieldset = document.getElementById('projectFieldset');
        var newProjectSection = createFieldset('projectSection', projectCount);
        addField(newProjectSection, `Project Title ${projectCount}`, 'project_title');
        addField(newProjectSection, 'Tech Stack', 'tech_stack');
        addTextarea(newProjectSection, 'Project Description', 'project_description');

        addRemoveButton(projectFieldset, newProjectSection, 'project');
        projectCount++;
    }
}

function addLeadershipExperience() {
    if (leadershipExperienceCount <= 3){
        var leadershipExperienceFieldset = document.getElementById('lexFieldset');
        var newLeadershipExperienceSection = createFieldset('leadershipExperienceSection', leadershipExperienceCount);
        addTextarea(newLeadershipExperienceSection, `Description ${leadershipExperienceCount}`, 'leadership_description');

        addRemoveButton(leadershipExperienceFieldset, newLeadershipExperienceSection, 'leadershipExperience');
        leadershipExperienceCount++;
    }
}

function createFieldset(idPrefix, count) {
    var newFieldset = document.createElement('fieldset');
    newFieldset.id = `${idPrefix}${count}`;
    return newFieldset;
}

function addField(fieldset, labelText, inputName) {
    var label = document.createElement('label');
    var input = document.createElement('input');
    label.textContent = `${labelText}:`;
    input.type = 'text';
    input.name = inputName + fieldset.id.split('Section')[1];
    input.required = true;

    fieldset.appendChild(label);
    fieldset.appendChild(input);
    fieldset.appendChild(document.createElement('br'));
}

function addTextarea(fieldset, labelText, textareaName) {
    var label = document.createElement('label');
    label.textContent = `${labelText}:`;
    var textarea = document.createElement('textarea');
    textarea.name = textareaName + fieldset.id.split('Section')[1];
    textarea.rows = '4';
    textarea.cols = '50';
    textarea.required = true;

    fieldset.appendChild(label);
    fieldset.appendChild(textarea);
    fieldset.appendChild(document.createElement('br'));
}

function addRemoveButton(parent, fieldset, fieldType) {
    var removeButton = document.createElement('button');
    removeButton.textContent = 'Remove';
    removeButton.className = 'remove-button';
    removeButton.type = 'button';
    removeButton.onclick = function() {
        parent.removeChild(fieldset);
        if (fieldType === 'education') {
            educationCount--;
        } else if (fieldType === 'workExperience') {
            workExperienceCount--;
        } else if (fieldType === 'project') {
            projectCount--;
        } else if (fieldType === 'leadershipExperience') {
            leadershipExperienceCount--;
        }
    };
    parent.appendChild(fieldset);
    fieldset.appendChild(removeButton);
}
