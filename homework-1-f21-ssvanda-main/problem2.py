#!/usr/bin/python3

# In the following lines, choose the correct git commands to perform each of the actions.
# Print the corresponding variable following the print example given.

# We have defined a variable called 'filename' that holds the file, 'git_commands.py' that you need to work with
filename = 'git_commands.py'

# Commands
cmd0 = 'Replace This'  # Relace cmd0 in each question with the correct command (e.g, cmd1)
cmd = 'git'
cmd1 = 'pull'           #Updates your local repository with any changes that are on GitHub and have not yet been reflected in your local repository.
                        #Note that there may be some conflicts between what GitHub knows about a file and what your local repository knows, and this 
                        #command will notify you if that happens (fixing those conflicts requires more work). You should always run `git pull` and resolve any conflicts before running `git push`.
cmd2 = 'add --all'
cmd3 = 'clone'          #This sets up a local repository on your machine by "cloning" (copying) a remote repository; in this case, a repository set up on GitHub.
cmd4 = 'commit -m'      #Creates a new version of your code. This new version is, essentially, all the files you called `git add` on, plus all the _other_ files 
                        #in the previous version (that you have not `add`ed). This new version only exists in your local repository.
cmd5 = 'add'            #When you have changed a file, you can "stage" it for the next version (i.e., tell git that you want the changes in this file to appear in the next version) using this command.
                        #(Note, when you want to just add/stage changes made to all files in a directory, consider "git add --all". Changes may include deletion of certain files.)
cmd6 = 'push'           # Updates the remote repository (on GitHub) with all the changes that you have `commit`ted to your local repository. Note that uncommitted changes will not appear on GitHub.

# Example #
print('Example: What command should I use to download my assignment from GitHub?')
print(cmd + ' ' + cmd1 + ' https://github.com/johndoe/ConfusedStudent.git')

# Question 1
print('Question 1: If `git_commands.py` is a new working file that I`ve just created on my local machine, then what commands should I use to submit it to the remote repository?')
# Step 1: Stage the file for the next version
# Step 2: Create a new version (update local repository)
# Step 3: Update the remote repository
print('step 1 ', cmd + ' ' + cmd5 + ' ' + filename)  # Replace cmd0 in each question with the correct command (e.g, cmd1)
print('step 2 ', cmd + ' ' + cmd4 + ' ' + "'First version of file is done. I should pay my consultant.'")  # Replace cmd0 in each question with the correct command (e.g, cmd1)
print('step 3 ', cmd + ' ' + cmd6)  # Replace cmd0 in each question with the correct command (e.g, cmd1)

# Question 2
print('Question 2: If I modified `git_commands.py` on my local machine, then what commands should I use to update the file on the remote repository?')
# Step 1: Stage the file for the next version
# Step 2: Create a new version (update local repository)
# Step 3: Update the remote repository
print('step 1 ', cmd + ' ' + cmd5 + ' ' + filename)  # Replace cmd0 in each question with the correct command (e.g, cmd1)
print('step 2 ', cmd + ' ' + cmd4 + ' ' + "'Problem fixed and file updated. My consultant is cool and deserves $20.'")  # Replace cmd0 in each question with the correct command (e.g, cmd1)
print('step 3 ', cmd + ' ' + cmd6)  # Replace cmd0 in each question with the correct command (e.g, cmd1)

# Question 3
print('Question 3: If `git_commands.py` has been removed from my local machine, then what commands should I use to remove it from the remote repository?')
# Step 1: Stage the removal of the file
# Step 2: Create a new version
# Step 3: Update the repository
print('step 1 ', cmd + ' ' + cmd5 + ' ' + filename)  # Replace cmd0 in each question with the correct command (e.g, cmd1)
print('step 2 ', cmd + ' ' + cmd4 + ' ' + "'Removed File from Repository.'")  # Replace cmd0 in each question with the correct command (e.g, cmd1)
print('step 3 ', cmd + ' ' + cmd6)  # Replace cmd0 in each question with the correct command (e.g, cmd1)

# Question 4
print('Question 4: If the remote repository on Github has new changes that are not on my local machine, what command should I use to update my local machine?')
print(cmd + ' ' + cmd5)  # Replace cmd0 in each question with the correct command (e.g, cmd1)

