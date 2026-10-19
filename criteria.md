# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall accuracy is at least 0.70 on the held-out test split, in all three seeds

**Why this target:** With four labels, a random guesser gets about 25%. A model
that always says `analysis` would get about 45%, because that is roughly how
often it showed up in my 40-post reading log. So 0.70 has to clear a real
floor, not only chance. My test split is only about 30 posts, so each post is
worth about 3 points. I set the target low enough that one unlucky seed with
two extra misses doesn't sink it, but high enough that I'd actually trust the
tool to sort a feed.

---

## 2. Every label has an F1 of at least 0.50 in every seed, and `analysis` and `reaction` each reach at least 0.65

**Why this target:** `analysis` and `reaction` have something you can point at.
`analysis` has a checkable number, quote or timecode. `reaction` is under 15
words and full of things like "lol", "WTF" and "???". So I expect them to do
better. `hot_take` overlaps both `prompt` (a question that's really an opinion,
like post 6) and `reaction` (short opinions like "Movie was mid tbh"). `prompt`
looks like my smallest label, with about 6 of 40 posts in the log. That's why
those two only get the looser 0.50 floor. Anything under 0.50 would mean the
model mostly can't find that label.

---

## 3. No label is more than 45% of `labels.csv`, and no label is under 15% (at least 30 of 200 posts)

**Why this target:** The brief's cap is 70%, but in my reading log `analysis`
was already about 45% (18 of 40) without me trying. If I let it grow past that,
the model can score well by leaning on `analysis`. At the other end, 30
examples puts only about 5 of a label in the test split. With fewer than that,
a single post moves its F1 by 0.15 or more, so the per-label score in
criterion 2 would just be noise.

---

## 4. I agree with the staff labels on at least 21 of the 30 staff posts (70%)

**Why this target:** I'm labelling those 30 under the staff taxonomy, not my
own, and some were picked to be ambiguous on purpose. So I don't expect 90%.
But if I can't stick to a written rule on 21 of 30, I probably wasn't
consistent across my own 200 either, especially on the `hot_take`/`prompt`
question rule. A model can't learn a boundary I drew two different ways.

---

## 5. Accuracy on the model's most-confident third is at least 0.20 higher than on its least-confident third, in all three seeds

**Why this target:** Short `reaction` posts and stat-heavy `analysis` posts
should be easy calls that the model is sure of and gets right. Questions with
an opinion attached should be the unsure ones it misses. With about 30 test
posts, each third is about 10 posts, so 0.20 is two posts' difference. A
smaller gap could just be one lucky post. If the two thirds score about the
same, then the model's confidence tells me nothing about when to trust it.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
