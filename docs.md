* Github Workflow
    Make sure to start a new branch whenever you're working on a change. 
    This will prevent a lot of issues down the road.

    1) Create new branch, pull from main
    2) Make your local changes
    3) Add changes, commit, and push to your branch
    4) Send a pull request on github and ask for a review from a team mate
    5) Team mate checks the commit on their machine and, if it works and doesn't break anything else, merges the branch with main
    6) Delete old branch (can be restored if problems come up with specific merges)

    *Example*
    I need to build a file that has an instance of a the "account" class called "checking"
    - Create a new branch from main called "nate-checking-account"
    - Finish working on the problem, add changes, commit, and push to "nate-checking-account"
        - Open pull request on github, mark my task as "review" on kanban board, and send a message in Discord to ask for someone to look it over
        - I pull your branch to my machine, check changes, and merge the "nate-checking-account" branch into main, then delete the old branch since the task is complete

Helpful Git Commands
    git add *
        Saves your local changes to your git workflow

    git commit -m ""
        Creates a new commit with a message describing changes

    git push
        Pushes your commit to the branch you're currently on

    git branch [example-branch]
        Creates a new branch, replace [example-branch] with your chosen name

    git branch --show-current
        Tells you what branch you're currently on, super helpful

    git checkout [example-branch]
        Basically the "cd" command for git, moves you into the branch you choose, replace [example branch]

# Directories

### classes