#!/usr/bin/env python3
import sys, subprocess, os, litellm

litellm.drop_params = True

# Usage: git diff | python3 git-mind.py
def main():
    diff_input = sys.stdin.read().strip() if not sys.stdin.isatty() else ""
    if not diff_input:
        try:
            diff_input = subprocess.check_output(['git', 'diff', '--staged'], text=True).strip()
        except: pass
        if not diff_input:
            print("No staged changes found. Did you `git add`?")
            return

    model = os.getenv("MODEL", "gpt-4o-mini")
    sys.stderr.write(f"Thinking with {model}...\n")
    
    prompt = "You are an expert developer. Read the following git diff and write a PERFECT 'conventional commit' message. Just output the commit message string, nothing else. No markdown formatting. Format: <type>(<scope>): <subject>\n\n<body if necessary>\n\nDIFF:\n" + diff_input
    
    try:
        res = litellm.completion(model=model, messages=[{"role": "user", "content": prompt}])
        print(res.choices[0].message.content.strip())
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
