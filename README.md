# DEVOPS 

## GIT – A Version controlling tool
###   Creating a GitHub Project Using  'git init'

#### 1. Initialize a New Local Git Repository
#####  Using your terminal, navigate to  where you want to create your local project.
######  Use the following commands to initialize a new Git repository
      mkdir your-project-name
      cd your-project-name
      git init

#### 2. Work on the Project Locally.
##### Using the text editor of your choice, open your project directory and create a README.md file and document your work.
      touch README.md

#### 3. Create a New Github Repository.
#####  Log in to your GitHub account, click the green(New) Icon, fill in details, set visibility, optionally add a license and click "Create repository".

#### 4. Connect your Local repository to the Remote repository
##### In the newly created repository, Under the "Quick setup" section, copy the URL of the remote repository 
      git remote add origin git@github.com:your-username/your-repo.git
##### Paste the above in your terminal and click Enter.

#### 5. Stage, commit and push  Changes.
##### Use the following commands to mark the changes for tracking, and store them in the git directory.
#### Provide a clear commit message that explains the what, why, and how of the changes.
      git add .
      git commit 
##### Use the following command to push your local project to the remote github repository.
     git push -u origin main
 
 
