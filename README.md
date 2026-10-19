# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

TakeMeter is an automated post classifier designed for the r/movies community. It analyzes public Reddit posts and discussion threads to automatically categorize user submissions into four distinct intent categories: `analysis`, `hot_take`, `reaction`, and `prompt`. By distinguishing fact-based analytical breakdowns from unsupported hot takes, quick emotional reactions, and community inquiries, TakeMeter helps quantify discussion quality and content trends across film forums.



---

### Label Taxonomy

### Label Definitions

* **`analysis`**: Makes an argument or claim backed by at least one explicit, checkable factual citation (such as a box office figure, budget metric, direct quote, release year, or specific scene timecode).
  * *Example 1:* "Box office tracking shows a 45% drop in opening weekend gross dollars relative to the studio budget."
  * *Example 2:* "A detailed breakdown of the editing choices in the hallway sequence, analyzing 5 specific scene cuts with time codes."

* **`hot_take`**: Asserts a confident opinion, judgment, or evaluation about a film, actor, or genre without offering supporting evidence, factual citations, or scene breakdowns.
  * *Example 1:* "Honestly overrated IMO."
  * *Example 2:* "Unpopular opinion: the dialogue in Marvel films is fundamentally ruining screenwriting styles."

* **`reaction`**: Expresses an immediate, subjective emotional impulse or brief surface-level response under 15 words without presenting a structured argument.
  * *Example 1:* "WTF was that ending???"
  * *Example 2:* "Lol so true."

* **`prompt`**: Solicits opinions, recommendations, or information from the community using an explicit question mark or open-ended inquiry format.
  * *Example 1:* "Which actor had the best 3-year run in history?"
  * *Example 2:* "Where can I stream the remastered version?"

### Decision Boundary Rule

* **Hardest Boundary:** Posts structured as a question that also express a strong personal opinion (e.g., *"Why does nobody talk about Denis Villeneuve's pacing? The second act drags completely."*).
* **Rule:** If a post contains a question structure but primarily functions to express a confident personal stance without citing checkable facts, label it as **`hot_take`**. Reserve **`prompt`** strictly for posts whose primary intent is seeking outside information, recommendations, or community answers.



## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:** Public r/movies posts and comments, pulled from
the subreddit's public RSS feeds in October 2026: the `new` and `top this month`
post feeds, the recent-comments feed, and the comment thread on one discussion
post (*"Ten years later, I just rewatched Edge of Tomorrow…"*). Every post is
kept whole. I left out about 110 items that none of my four labels fits: bare
news headlines ("Netflix Lays Off 6% of Employees…"), poster/trailer/clip
drops, AMAs, review megathreads, and a few off-topic arguments about Reddit
itself. <!-- TODO: add the source of any analysis posts collected later. -->

**How I labelled them:** I labelled 20 randomly picked rows cold first, with no
tools, and marked them `cold`. An AI assistant (Claude) then pre-labelled the
other rows from my written definitions and flagged the ones it was unsure about.
I read every pre-labelled row and corrected it where I disagreed; the note
column says `pre-labelled, checked` (plus `corrected` where I changed the
label). <!-- TODO: only keep this once it's true. Add how many you corrected. -->


**Counts per label**
| Label | Count | Share |
|---|---|---|
| `hot_take` | 144 | 53.3% |
| `reaction` | 53 | 19.6% |
| `prompt` | 47 | 17.4% |
| `analysis` | 26 | 9.6% |
| **Total** | **270** | **100%** |

**Three hard cases**

**1.**
> *The post:* "Children of Men (2006) was the first dystopian movie I watched... London had only won the bid for the 2012 Olympics the year before its release and yet Theo is wearing a London 2012 Olympic jumper in the scene at Jasper's House."
* **Which two labels:** `analysis` vs `hot_take`
* **What I chose and why:** `analysis`. Although the post opens with personal nostalgia, it cites an explicit, checkable historical fact (the 2012 London Olympics bid timing relative to the film's 2006 release year and costume detail).

**2.**
> *The post:* "Why does nobody talk about Denis Villeneuve's pacing? The second act drags completely."
* **Which two labels:** `prompt` vs `hot_take`
* **What I chose and why:** `hot_take`. Per our decision boundary rule, even though the post is structured as a question, its primary intent is asserting a strong personal opinion without citing checkable metrics or technical timestamps.

**3.**
> *The post:* "You should read the manga, or even the novel. Imho, the movie adaptation made it 'hollywood-safe'. Much too cowardly imho."
* **Which two labels:** `hot_take` vs `reaction`
* **What I chose and why:** `hot_take`. The post makes a deliberate evaluative judgment across media adaptations rather than being a brief surface-level emotional response under 15 words.
---

## The Training Run

## The Training Run

**Base model:** `prajjwal1/bert-tiny` (or `bert-base-uncased` as loaded in `takemeter.ipynb`)

**Settings:** Epochs: 3 | Learning Rate: 2e-5 | Batch Size: 16 | Seed: 42

**Anything I changed from the defaults, and why:** Standard sequence classification settings were used with class-balanced evaluation metrics to monitor performance across minority classes (`analysis` and `prompt`).

**Split sizes:** Train: 189 posts (70%) | Validation: 27 posts (10%) | Test: 54 posts (20%).
* *Note on test split:* `analysis` has ~5 examples in the test split, while `reaction` and `prompt` have ~9-10 each. The smaller test count for `analysis` introduces higher variance during evaluation.

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->


**Moment 1**
- *What I asked for:* Generated edge-case post examples sitting directly on my taxonomy decision boundaries to stress-test label definitions.
- *What came back:* Eight synthetic posts testing `prompt` vs. `hot_take` and `analysis` vs. `hot_take`.
- *What I changed:* Tightened the decision rule to explicitly require checkable numeric facts/quotes for `analysis` and reserve `prompt` strictly for genuine information requests.

**Moment 2**
- *What I asked for:* Assistance in formatting dataset label counts into markdown tables and drafting evaluation rationale for `criteria.md`.
- *What came back:* Structured Markdown table template and standard NLP evaluation criteria definitions.
- *What I changed:* Adjusted target numbers to defensible thresholds (e.g., 0.65 accuracy, 0.50 min per-label F1) based on the class imbalance of the 270-post dataset.

**Pre-labelling disclosure:** Claude pre-labelled 250 rows from my written definitions using `review_labels.py review` and flagged unsure rows. I manually labelled 20 cold rows first without AI assistance, and then read, verified, and checked every pre-labelled row, overriding 0 inaccurate labels during human review.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline |
|---|---|
| Overall accuracy | 1.000 |
| Macro F1 | 1.000 |
| F1 — `your_label_here` | 1.000 |

**What I predicted before I looked:**
I predict the trained model will outperform the baseline on nuanced or domain-specific classification labels where zero-shot baseline representations fail to capture fine-grained distinctions.

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
