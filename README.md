Django
======

Django practice area

How to create a local git instance:
$> mkdir ~/Hello-World
Creates a directory for your project called "Hello-World" in your user directory

$> cd ~/Hello-World
Changes the current working directory to your newly created directory

$> git init\n
Sets up the necessary Git files
Initialized empty Git repository in /Users/you/Hello-World/.git/

$> touch README
Creates a file called "README" in your Hello-World directory

How to create your initial commit:
$> git add README
Stages your README file, adding it to the list of files to be committed

$> git commit -m 'first commit'
Commits your files, adding the message "first commit"

How To Push your local to the repository:
$> git remote add origin https://github.com/username/Hello-World.git
Creates a remote named "origin" pointing at your GitHub repository

$> git push origin master
Sends your commits in the "master" branch to GitHub
