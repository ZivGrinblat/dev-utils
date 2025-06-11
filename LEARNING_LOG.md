# 🧠 LEARNING_LOG.md – Git Mastery Roadmap Tracker

## Week 1 – Local Git Fundamentals

- [ ] Day 1: Init, Stage, Commit, Status  
  ⬜ Created first repo and committed 3–4 changes  
  ⬜ Reflected on `git add` vs `git commit`

- [ ] Day 2: Git Object Store  
  ⬜ Explored `.git/objects/`  
  ⬜ Used `git cat-file` and `git ls-tree`  
  ⬜ Wrote short description of blobs, trees, commits

- [ ] Day 3: Branching and Merging  
  ⬜ Created feature branch and merged into main  
  ⬜ Resolved a simple conflict manually

- [ ] Day 4: Undoing and Recovering  
  ⬜ Practiced `git reset`, `restore`, `reflog`  
  ⬜ Logged recovery examples

- [ ] Day 5: Mini Project  
  ⬜ Simulated real dev flow (branching, merging, conflicts)  
  ⬜ Clean commit history

---

## Week 2 – GitHub Workflows and Collaboration

- [ ] Day 8: Connect to Remote  
  ⬜ Added GitHub remote and pushed main  
  ⬜ Pushed a feature branch

- [ ] Day 9: Pull Request Flow  
  ⬜ Created feature branch and PR  
  ⬜ Wrote clean commits and PR description

- [ ] Day 10: Fork and Upstream  
  ⬜ Added upstream remote  
  ⬜ Rebasing onto upstream main

- [ ] Day 11: Conflict Resolution  
  ⬜ Resolved conflict manually + on GitHub

- [ ] Day 12: Reviewing PRs  
  ⬜ Reviewed PR (yours or someone else’s)  
  ⬜ Practiced line comments

---

## Week 3 – Rewriting, Debugging, Recovery

- [ ] Day 15: Rewriting History  
  ⬜ Used `git rebase -i` to squash + reword commits

- [ ] Day 16: Reflog + Safety Nets  
  ⬜ Simulated commit loss and recovery via `reflog`

- [ ] Day 17: Git Bisect  
  ⬜ Used `git bisect` to isolate a bug commit

- [ ] Day 18: Final PR  
  ⬜ Created clean, reviewable final PR with docs

- [ ] Day 19: GitHub Actions (Optional)  
  ⬜ Setup a basic `.yml` CI workflow

---

# 🛠️ RECOVERY_LOG.md – Mistakes + Recoveries

## Example

### Date: 2025-06-12
- **Mistake**: Ran `git reset --hard` on wrong branch
- **What I lost**: Two commits I hadn’t pushed
- **How I recovered**: Used `git reflog` → found commit hash → `git checkout <hash>` → recovered to new branch

---

# ⚔️ CONFLICT_LOG.md – Conflict Resolution Journal

## Example

### Date: 2025-06-13
- **Conflict File**: `utils/logger.py`
- **Cause**: Two branches edited the same function signature
- **How I solved**:
  - Used `git status` to identify conflict
  - Manually edited file
  - Ran `git add`, then `git commit`
  - Verified with `git log` and `git diff`

---

Use these logs continuously — they are your Git lab notebook. Each mistake is experience, and each log entry is your personal debug history.
