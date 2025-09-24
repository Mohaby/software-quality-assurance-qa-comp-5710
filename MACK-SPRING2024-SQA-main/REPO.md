# REPORT

## Activity: Unpack the project MLForensics.zip.
***Objective:*** Extract the contents of the MLForensics.zip file to access the project files.   
***Approach:*** Locate MLForensics, download, and unzip into appropriate REPO   
***Outcome:*** Project files are unpacked and ready to be used for project and development  
***Lessons Learned:***  
1. Understanding of file compression and decompression techniques. 
2. Familiarity with handling archived files. 
3. Ability to extract project files from a compressed archive.

## Activity: Upload project as a GitHub repo on GitHub.com. Format of the repo name is TEAMNAME-SPRING2024-SQA
***Objective:*** Share the project on GitHub, so we can work together easily, keep track of changes, and make it visible to others.  
***Approach:*** Create a new repository on GitHub named according to the specified format (TEAMNAME-SPRING2024-SQA) and upload the project files.  
***Outcome:*** The project is successfully hosted on GitHub, allowing team members to access, contribute, and track changes efficiently.  
***Lessons Learned:***
1. Proficiency in creating a new repository on GitHub.
2. Understanding of version control concepts. 
3. Experience in uploading project files to a remote repository. 
4. Knowledge of repository naming conventions for effective organization.

## Activity: In your project repo create README.md listing your team name and team members.
***Objective:*** Share important details about the team and its members in the project repository.  
***Approach:*** Create a README.md file containing the team name and a list of team members.  
***Outcome:*** The project repository includes a README.md file with clear identification of the team and its members, enhancing collaboration and communication.  
***Lessons Learned:***
1. Ability to create and edit Markdown files. 
2. Understanding the importance of project documentation. 
3. Experience in communicating team information effectively within the project repository.

## Activity: Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed.
***Objective:*** Boost security by automatically pinpointing and reporting any vulnerabilities lurking within the project's codebase.  
***Approach:*** Develop a Git pre-commit hook script to trigger a security scanning tool (e.g., Bandit) whenever a Python file is changed and committed. Generate a CSV report containing the identified security weaknesses  
***Outcome:*** Security vulnerabilities are promptly detected and reported during the development process, improving overall code quality and reducing security risks.  
***Lessons Learned:***
1. Understanding of Git hooks and their usage for automating tasks. 
2. Familiarity with security scanning tools for code analysis. 
3. Experience in configuring pre-commit hooks to enhance code security. 
4. Knowledge of reporting mechanisms for identified security weaknesses.

## Activity: Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the fuzz.py file. fuzz.py will be automatically executed from GitHub actions.
***Objective:*** Identify and report bugs through automated fuzz testing of selected Python methods.  
***Approach:*** Develop a fuzz.py script to fuzz test days_between, getDevEmailForCommit, make_Chunks, getPythonFileCount, dumpContentIntoFile methods. Configure GitHub Actions to automatically execute fuzz.py and report any discovered bugs.  
***Outcome:*** Bugs and vulnerabilities are identified early in the development cycle, allowing for timely resolution and improved software reliability.  
***Lessons Learned:***
1. Understanding of fuzz testing concepts and techniques. 
2. Proficiency in developing fuzz testing scripts. 
3. Experience in identifying and reporting software bugs through automated testing. 
4. Knowledge of integrating fuzz testing into CI/CD pipelines for continuous validation.

## Activity: Integrate forensics by modifying 5 Python methods of your choice.
***Objective:*** Enhance traceability and debugging capabilities by integrating forensics techniques into selected Python methods.  
***Approach:*** Modify five chosen Python methods to incorporate forensics instrumentation, such as logging and error handling mechanisms. Ensure modifications do not compromise method functionality.  
***Outcome:*** Improved traceability and debugging capabilities enable more effective diagnosis and resolution of issues during development and production stages.  
***Lessons Learned:***
1.  Understanding of forensics techniques for software analysis. 
2. Experience in modifying code to incorporate forensics instrumentation. 
3. Familiarity with logging and error handling mechanisms for forensic analysis. 
4. Ability to enhance traceability and debugging capabilities within the codebase.

## Activity: Integrate continuous integration with GitHub Actions. 
***Objective:*** Establish automated CI workflows to streamline the development process and ensure code quality.  
***Approach:*** Configure GitHub Actions workflows to trigger on code changes, run tests, and deploy artifacts. Integrate automated testing suites, including security scanning and fuzz testing.  
***Outcome:*** Continuous integration improves code quality, reliability, and security by automating build, test, and deployment processes, leading to faster feedback and more robust software.  
***Lessons Learned:***
1. Proficiency in configuring CI workflows using GitHub Actions. 
2. Understanding of automated testing and deployment processes. 
3. Experience in integrating security scanning and fuzz testing into CI pipelines. 
4. Ability to automate code validation and deployment for improved software quality and reliability.
