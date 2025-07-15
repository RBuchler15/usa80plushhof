
# 🧠 Git Workflow Cheat Sheet for Robin

## ✅ One-Time Setup (Already Done)
```bash
git init
git remote add origin https://github.com/RBuchler15/usa80plushhof.git
git branch -M main
git push -u origin main
```

---

## 🔁 Daily Workflow (Repeat Every Time You Work)

### 1. 🧭 Open Terminal in VS Code
Use `Ctrl + ~` or go to **View > Terminal**.

### 2. ⏬ Pull Latest from GitHub
(Only needed if you've made changes elsewhere or on GitHub directly)
```bash
git pull
```

### 3. ✍️ Make Your Changes
Edit, add, or delete files in VS Code.

### 4. ✅ See What Changed
```bash
git status
```

### 5. ➕ Stage Your Changes
```bash
git add .
```

### 6. 📝 Commit Your Changes
```bash
git commit -m "Describe what you changed"
```
Example:
```bash
git commit -m "Added thank-you page and updated sponsor logos"
```

### 7. 🚀 Push to GitHub
```bash
git push
```

---

## 📦 Optional: Use a Branch for Big Changes
If you want to experiment without touching `main`:

```bash
git checkout -b new-feature
# Do your work, then:
git push -u origin new-feature
```

When it's ready, you can merge it back into `main`.

---

📝 **Tip**: Commit often and write clear commit messages.
