# LearnDoc

AI-powered learning assistant — available as CLI and Web.

## 🌐 Web Version (GitHub Pages)

**Live at:** https://yawningphantom.github.io/learndoc/

Features:
- Learn, quiz, teach, test, summarize
- Notes saved in localStorage
- History tracking
- All client-side (no backend needed)

## 💻 CLI Version

```bash
# Setup
export ANTHROPIC_API_KEY='your-key'

# Learn
python learn.py explain docker
python learn.py quiz python
python learn.py teach rust
python learn.py test kubernetes
python learn.py summary ml

# Review
python learn.py history
python learn.py notes
python learn.py search docker
```

## Commands (CLI)

| Command | Description |
|---------|-------------|
| `explain` | Clear explanation with analogy + examples |
| `quiz` | 5 multiple choice questions |
| `teach` | Structured lesson |
| `test` | Interactive knowledge check |
| `summary` | Key takeaways + terms |
| `history` | Show learning history |
| `notes` | View saved markdown notes |
| `search` | Search all notes |

## Files

```
/
├── index.html      # Web UI (GitHub Pages)
├── learn.py       # CLI version
├── learn          # CLI wrapper script
└── README.md
```

## Tech Stack

- **Web:** Pure HTML/JS (no build needed)
- **CLI:** Python + Anthropic API
- **Storage:** localStorage (web), filesystem (CLI)
