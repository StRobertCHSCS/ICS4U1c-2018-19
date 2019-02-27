# ICS4U1c-2018-19
Working repo for Grade 12 Computer Science - Spring 2019

### Fork this repository
* From the upstream(parent) repository (StRobertCHSCS/ICS4U1c-2018-19), click on *Fork* at the top right of your screen.
* Choose your account to fork to.

### Clone your Fork
* From *your* fork [your_account]/ICS4U1c-2018-19, click on the **Clone or Download** button (the green one on the right) and copy the URL
* From within your PycharmProjects directory on your computer, using the terminal (or command prompt), type in `git clone [the URL of your fork]`
* In PyCharm, you can now open this new project by going to `File --> Open --> Select the directory of your new fork`
* repeat this for any computer you will be working on


### Commit and push Changes to your fork in github
* make the necessary changes to your code or other project files
* In the terminal (make sure you are in the directory of your project (type `pwd` on the terminal to verify your current directory):

* `git add yourfilename` to track a single file or `git add -A` to track all files in the project
then

```
git commit -m "type a short meaningful message in present tense about your changes"
git push origin master
```


### Pull changes from your fork on github down to a your local repository
* In the terminal, be sure your are in the directory containing your fork on your computer (type `pwd` on the terminal to verify your current directory).
* type in `git pull origin master`



### Pull Changes from the Upstream Repository
Do this when there are updates to pull from the upstream(parent) repository StRobertCHSCS/ICS4U1c-2018-19 (not your fork)
* first you will need to add and upstream remote (you only need to do this once)
    * `git remote add upstream https://github.com/[Original Owner Username]/[Original Repository].git`
    * for example `git remote add upstream https://github.com/StRobertCHSCS/ICS4U1c-2018-19.git`
* now any time you want to pull from the upstream remote: **`git pull upstream master`**


### Changing the git user name
Before you make any changes when working on the school laptops (class chromebooks),  it's a good idea to check that you are the current git user.
* To check the current git user: `git config user.name`
* To change the current git user:
```text
git config user.name "your_git_username"
git config user.email "your_git_account_email"

```







