# LearnDoc

AI-powered learning assistant — CLI and Web.

## 🌐 Web Version (GitHub Pages)

**URL:** https://yawningphantom.github.io/learndoc/

To enable:
1. Go to https://github.com/yawningphantom/learndoc/settings/pages
2. Select: **Deploy from a branch**
3. Branch: **main** / (root)
4. Click **Save**

## 💻 CLI Version (uses local Codex)

```bash
cd ~/learndoc
python learn.py explain docker
python learn.py quiz python
python learn.py teach rust
python learn.py test kubernetes
python learn.py summary ml
python learn.py history
python learn.py notes
python learn.py search docker
```

## Features

| Command | Description |
|---------|-------------|
| `explain` | Clear explanation with analogy + examples |
| `quiz` | 5 multiple choice questions |
| `teach` | Structured lesson |
| `test` | Interactive knowledge check |
| `summary` | Key takeaways + terms |
| `history` | Track what you've learned |
| `notes` | View saved markdown notes |
| `search` | Search all notes |

## Tech Stack

- **Web:** Pure HTML/JS (static, no build)
- **CLI:** Python + local Codex CLI
- **Storage:** localStorage (web), filesystem (CLI)

## Files

```
/
├── index.html           # Web UI (GitHub Pages)
├── learn.py            # CLI (uses local codex)
├── learn               # Shell wrapper
├── README.md
└── .github/
    └── workflows/
        └── pages.yml   # GitHub Pages deployment
```
