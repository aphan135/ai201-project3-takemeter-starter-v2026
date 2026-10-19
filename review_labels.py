"""Walk through labels.csv one row at a time.

    python review_labels.py cold     # label the 20 cold rows (text only, no suggestion)
    python review_labels.py review   # check every AI pre-label

Keys: Enter = keep the shown label, a/h/r/p = analysis/hot_take/reaction/prompt,
x = flag as a hard case (asks for a note), q = save and quit.
Progress is saved after every row, so you can stop and come back.
"""
import csv
import sys

PATH = "labels.csv"
KEYS = {"a": "analysis", "h": "hot_take", "r": "reaction", "p": "prompt"}
UNCHECKED = "pre-labelled by AI, NOT YET CHECKED"


def save(rows):
    with open(PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["text", "label", "note"])
        w.writeheader()
        w.writerows(rows)


def ask_label(prompt, default):
    while True:
        k = input(prompt).strip().lower()
        if k == "q":
            return "QUIT", None
        if k == "" and default:
            return default, None
        if k in KEYS:
            return KEYS[k], None
        if k == "x":
            lab = ask_label("  label for this hard case [a/h/r/p]: ", default)[0]
            if lab == "QUIT":
                return "QUIT", None
            why = input("  hard case - which two labels, and why you chose this one: ").strip()
            return lab, why
        print("  Enter, a, h, r, p, x or q")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode not in ("cold", "review"):
        sys.exit(__doc__)
    rows = list(csv.DictReader(open(PATH, newline="")))
    if mode == "cold":
        todo = [r for r in rows if r["note"].startswith("cold") and not r["label"]]
    else:
        todo = [r for r in rows if r["note"].startswith(UNCHECKED)]
    print(f"{len(todo)} rows to go.  a=analysis h=hot_take r=reaction p=prompt x=hard case q=quit\n")
    for n, r in enumerate(todo, 1):
        print("=" * 70)
        print(f"[{n}/{len(todo)}]  {len(r['text'].split())} words\n")
        print(r["text"], "\n")
        if mode == "review":
            hint = r["note"].split("AI unsure: ")[1] if "AI unsure: " in r["note"] else ""
            print(f"AI label: {r['label']}" + (f"   (AI unsure: {hint})" if hint else ""))
            lab, why = ask_label("Enter to keep, or a/h/r/p/x/q: ", r["label"])
        else:
            lab, why = ask_label("Your label a/h/r/p/x/q: ", None)
        if lab == "QUIT":
            break
        changed = mode == "review" and lab != r["label"]
        r["label"] = lab
        if mode == "cold":
            r["note"] = "cold"
        else:
            r["note"] = "pre-labelled, checked" + ("; corrected" if changed else "")
        if why:
            r["note"] += f"; HARD CASE: {why}"
        save(rows)
    left = sum(1 for r in rows if r["note"].startswith(UNCHECKED) or (r["note"] == "cold" and not r["label"]))
    print(f"\nSaved. {left} rows still unlabelled or unchecked.")


if __name__ == "__main__":
    main()
