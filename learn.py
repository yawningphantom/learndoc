#!/usr/bin/env python3
"""
LearnDoc - Learn using Codex CLI locally

Usage:
    python learn.py explain docker
    python learn.py quiz python decorators
    python learn.py teach rust ownership
    python learn.py test kubernetes
    python learn.py summary machine learning
"""

import os
import sys
import json
from pathlib import Path
import subprocess

# Configuration
NOTES_DIR = Path.home() / ".learndoc" / "notes"
NOTES_DIR.mkdir(parents=True, exist_ok=True)
HISTORY_FILE = Path.home() / ".learndoc" / "history.json"


def load_history():
    if HISTORY_FILE.exists():
        return json.loads(HISTORY_FILE.read_text())
    return []


def save_history(topic, action="learned"):
    history = load_history()
    from datetime import datetime
    history.append({
        "topic": topic,
        "action": action,
        "timestamp": datetime.now().isoformat()
    })
    HISTORY_FILE.write_text(json.dumps(history, indent=2))


def call_codex(prompt):
    """Call Codex CLI directly."""
    result = subprocess.run(
        ["codex", "exec", prompt],
        capture_output=True,
        text=True,
        timeout=120
    )
    
    if result.returncode != 0:
        print(f"❌ Codex error: {result.stderr}")
        sys.exit(1)
    
    return result.stdout


def cmd_explain(topic):
    prompt = f"""Explain "{topic}" in a clear, educational way. 
- Start with a simple analogy
- Build up concepts gradually
- Use examples
- End with a summary
- Keep it concise but complete"""
    
    print(f"\n📚 Learning: {topic}\n" + "="*50)
    response = call_codex(prompt)
    print(response)
    save_history(topic, "explained")
    save_note(topic, response)


def cmd_quiz(topic):
    prompt = f"""Create a 5-question quiz on "{topic}".
For each question:
- Question number and text
- 4 multiple choice options (A, B, C, D)
- Correct answer with brief explanation

Format:
1. [Question]
   A) [Option]
   B) [Option]
   C) [Option]
   D) [Option]
ANSWER: [Letter] - [Brief explanation]"""
    
    print(f"\n🎯 Quiz: {topic}\n" + "="*50)
    response = call_codex(prompt)
    print(response)
    save_history(topic, "quizzed")


def cmd_teach(topic):
    prompt = f"""Teach me about "{topic}" as if I'm a beginner.

Structure:
1. 2-3 sentence intro (what is it, why it matters)
2. Core concepts (3-5 bullet points)
3. First simple example (code or analogy)
4. Key terminology (3-5 terms with definitions)
5. Next steps (what to learn next)
6. Resources (2-3 concrete next steps)

Keep it practical and actionable."""
    
    print(f"\n📖 Teaching: {topic}\n" + "="*50)
    response = call_codex(prompt)
    print(response)
    save_history(topic, "taught")
    save_note(topic, response)


def cmd_test(topic):
    prompt = f"""Test my knowledge of "{topic}" with 5 questions.

For each question:
- One challenging question that tests understanding
- Not just recall, but application
- Provide answer and brief feedback after each

Questions should range from easy to hard."""
    
    print(f"\n🧪 Test: {topic}\n" + "="*50)
    response = call_codex(prompt)
    print(response)
    save_history(topic, "tested")


def cmd_summary(topic):
    prompt = f"""Give me a comprehensive summary of "{topic}".

Include:
- 3-5 key takeaways (bullet points)
- 1 paragraph overview
- 3-5 important terms with one-line definitions
- What's next to learn

Be concise but complete."""
    
    print(f"\n📝 Summary: {topic}\n" + "="*50)
    response = call_codex(prompt)
    print(response)
    save_history(topic, "summarized")
    save_note(topic, response)


def cmd_notes(topic=None):
    if topic:
        note_file = NOTES_DIR / f"{topic.lower().replace(' ', '_')}.md"
        if note_file.exists():
            print(f"\n📖 Notes: {topic}\n" + "="*50)
            print(note_file.read_text())
        else:
            print(f"❌ No notes found for: {topic}")
    else:
        print("\n📚 All Notes:")
        print("-"*30)
        for f in sorted(NOTES_DIR.glob("*.md")):
            print(f"  • {f.stem.replace('_', ' ').title()}")
        print()


def cmd_history():
    history = load_history()
    if not history:
        print("\n📭 No learning history yet.")
        print("   Try: python learn.py explain docker")
        return
    
    print("\n📅 Learning History:")
    print("-"*40)
    from datetime import datetime
    for entry in reversed(history[-20:]):
        date = datetime.fromisoformat(entry["timestamp"]).strftime("%Y-%m-%d")
        action_icons = {"explained": "📚", "quizzed": "🎯", "taught": "📖", "tested": "🧪", "summarized": "📝"}
        icon = action_icons.get(entry["action"], "•")
        print(f"  {icon} {date} - {entry['topic']}")
    print()


def cmd_clear():
    if HISTORY_FILE.exists():
        HISTORY_FILE.unlink()
        print("✅ History cleared")
    else:
        print("📭 No history to clear")


def save_note(topic, content):
    filename = topic.lower().replace(' ', '_')[:50] + ".md"
    note_file = NOTES_DIR / filename
    from datetime import datetime
    content = f"# {topic}\n\n_Learned on {datetime.now().strftime('%Y-%m-%d')}_\n\n{content}"
    note_file.write_text(content)
    print(f"💾 Saved note: {note_file.name}")


def cmd_search(topic):
    from datetime import datetime
    results = []
    for note_file in NOTES_DIR.glob("*.md"):
        content = note_file.read_text().lower()
        if topic.lower() in content:
            results.append(note_file)
    
    if results:
        print(f"\n🔍 Found '{topic}' in {len(results)} note(s):")
        for f in results:
            print(f"  • {f.stem.replace('_', ' ').title()}")
    else:
        print(f"\n❌ No notes found containing: {topic}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n📖 Examples:")
        print("  python learn.py explain docker")
        print("  python learn.py quiz python decorators")
        print("  python learn.py teach rust ownership")
        print("  python learn.py test kubernetes")
        print("  python learn.py summary machine learning")
        print("  python learn.py notes")
        print("  python learn.py history")
        print("  python learn.py search 'function'")
        sys.exit(1)
    
    command = sys.argv[1]
    topic = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else None
    
    commands = {
        "explain": cmd_explain,
        "quiz": cmd_quiz,
        "teach": cmd_teach,
        "test": cmd_test,
        "summary": cmd_summary,
        "notes": lambda t: cmd_notes(t) if t else cmd_notes(),
        "history": cmd_history,
        "clear": cmd_clear,
        "search": cmd_search,
    }
    
    if command in commands:
        if command in ["notes", "history", "clear"]:
            commands[command]()
        else:
            if not topic:
                print(f"❌ Error: '{command}' requires a topic")
                print(f"   Usage: python learn.py {command} <topic>")
                sys.exit(1)
            commands[command](topic)
    else:
        print(f"❌ Unknown command: {command}")
        print("   Available: explain, quiz, teach, test, summary, notes, history, search")
        sys.exit(1)


if __name__ == "__main__":
    main()
