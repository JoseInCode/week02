
# Digital Systems — Autograded (Randomised, Auto‑Computed Answers)

This GitHub Classroom template generates **per‑student randomised questions** and auto‑computes the correct answers. Students fill `student/answers.json` using the generated `questions/generated.md`.

## How it works
1. **Generation step** (CI): `python scripts/generate_questions.py --seed "${{ github.actor }}:${{ github.run_id }}"` creates:
   - `meta/generated_spec.json` (random parameters)
   - `questions/generated.md` (student‑readable questions)
2. **Autograding tests** compute the expected answers from `generated_spec.json` and compare against `student/answers.json`.

## Answer keys & integrity
No static answer key is stored; expected values are computed in tests from the spec.

## What students do
- Edit **only** `student/answers.json` and push.

## Scoring
- 27 individual tests (1 point each): conversions (12), addition (3), subtraction (3), two’s complement (3), fixed‑point (3), limits (3).
