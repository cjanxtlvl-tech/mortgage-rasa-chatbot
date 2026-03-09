# SETUP.md

Step-by-step beginner guide for VS Code to publish this project to GitHub and invite a collaborator.

## Prerequisites
- You have a GitHub account.
- You have Git installed (`git --version` should work in the terminal).
- You are inside this project folder in VS Code terminal:
  - `/home/chester-anderson/Documents/mortgage-rasa-chatbot`

## 1. Initialize Git In This Folder
Open VS Code terminal (`Terminal` -> `New Terminal`) and run:

```bash
git init
```

(Optional but recommended) Set your default branch name to `main`:

```bash
git branch -M main
```

## 2. Create A GitHub Repo Named `mortgage-rasa-chatbot`
1. Go to GitHub and click `New repository`.
2. Repository name: `mortgage-rasa-chatbot`
3. Keep it `Public` or `Private` based on your preference.
4. Do **not** add a README, .gitignore, or license (this folder already has files).
5. Click `Create repository`.

After creating it, GitHub shows a remote URL like one of these:
- HTTPS: `https://github.com/<your-username>/mortgage-rasa-chatbot.git`
- SSH: `git@github.com:<your-username>/mortgage-rasa-chatbot.git`

## 3. Connect Local Repo To GitHub
In terminal, add the remote (use your own URL):

```bash
git remote add origin https://github.com/<your-username>/mortgage-rasa-chatbot.git
```

Verify:

```bash
git remote -v
```

## 4. Make The First Commit
Stage all files:

```bash
git add .
```

Create initial commit:

```bash
git commit -m "Initial commit: starter mortgage Rasa chatbot project"
```

If Git asks for identity, set it once and re-run commit:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 5. Push To `main`
Push local branch to GitHub and set upstream:

```bash
git push -u origin main
```

If your local branch is not yet `main`, run this first, then push again:

```bash
git branch -M main
git push -u origin main
```

## 6. Invite A Developer As A Collaborator
1. Open your GitHub repository page.
2. Go to `Settings` -> `Collaborators and teams`.
3. Click `Add people`.
4. Enter the developer's GitHub username/email.
5. Send invitation.
6. Ask them to accept the invite from GitHub notifications/email.

## Quick Verification Commands
Run these to confirm everything is connected:

```bash
git status
git branch
git remote -v
```

## Common Beginner Fixes
- Error: `remote origin already exists`
  - Fix:
    ```bash
    git remote set-url origin https://github.com/<your-username>/mortgage-rasa-chatbot.git
    ```

- Error on push about authentication (HTTPS)
  - Use a GitHub Personal Access Token when prompted for password, or switch to SSH.

- Error: `src refspec main does not match any`
  - You likely have no commit yet. Run:
    ```bash
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git push -u origin main
    ```
