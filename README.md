# Recovered Erdős-problem research

Public index of existing work recovered from this machine on **7 October 2026**. The repositories preserve drafts, source programs, exact evidence, proof audits and failed approaches, with clear verification limits. This is research progress; no general conjecture is claimed solved by this recovery.

| Problem | Repository | Recovered progress and limits |
| --- | --- | --- |
| [151](https://www.erdosproblems.com/151) | [Graph experiments](https://github.com/cubres/erdos-151-experiments) | Five search programs. Fresh atlas replay: all graphs on 3..7 vertices, no counterexample under the program's convention. Historical through-12 claim is not presented as freshly verified. |
| [644](https://www.erdosproblems.com/644) | [Transversal research](https://github.com/cubres/erdos-644-research) | Latest six-sevenths v3 draft includes rank seven; structured bounds, counterexamples, internal reviews and exact certificates. General three-quarter conjecture remains unresolved. Editorial issues and human-verification placeholder are visible. |
| [954](https://www.erdosproblems.com/954) | [Existing exact-computation repository](https://github.com/cubres/erdos-954-computations) | Existing public repository reports a fully audited range through 10^14 with 15,956,975 positive terms. Its 10^15 extension is a target, not a completed dataset. This recovery checked its current README and reused the repository. |
| [1060](https://www.erdosproblems.com/1060) | [Arithmetic-fiber research](https://github.com/cubres/erdos-1060-research) | Partial bounds for k sigma(k) fibers, exact collisions, three-base exchanges, literature audit and finite verifier receipts. Uniform little-o bound remains unresolved in the recovered work. |

## Fresh verification

- Problem 644: all 2,008,516 branch checks for ranks 7..120 and explicit rank-seven response checks passed.
- Problem 1060: the selected audit, exact-certificate and three-base exchange checkers passed. The three-base finite regression covers all 669 primes below 5000.
- Problem 151: atlas counts 4, 11, 34, 156 and 1,044 for orders 3, 4, 5, 6 and 7; zero counterexamples.
- Problem 954: existing repository and README checked; its large data audit was not rerun as part of this recovery.

Fresh logs are included in each new problem repository. Finite tests and internal AI reviews do not constitute universal formal verification, external review or a priority proof.

## Recovery scope

The search inventoried accessible home-directory filenames, searched research text under Documents, Desktop and Downloads, inspected local Codex and Claude session records to recover source locations, inspected the specifically relevant Claude scratch workspace, and checked GitHub for existing Erdős repositories. The main source directories were Clauding/erdos-hunt, the September 19 Codex Problem 644 workspace, and ChatGPT/Research. Chat transcripts were used only for discovery and were not uploaded.

The problem repositories contain roughly 19,000 packaged source/evidence entries for 644, the complete recovered 1060 source/audit collection and datasets, and the five 151 programs. Evidence ZIPs are ordinary archives. The 644 extraction helper also reconstructs a few split compressed members and verifies their original hashes. Every archived source location is mapped by SHA-256 manifests. Oversized generated 644 proof traces are explicitly listed as **local-only**, rather than silently described as uploaded. Runtime databases, dependencies, caches and downloaded third-party literature are excluded.

Survey files in `survey/` preserve the September 14 research-selection snapshot and its parser. They identify possible targets, not original mathematical results on every listed problem. Their old statuses and priorities may be outdated; consult [Bloom's live problem database](https://www.erdosproblems.com/) and [the community data repository](https://github.com/teorth/erdosproblems).

The downloaded OpenAI/dottedcalculator papers on Problems 4, 740 and 854 and other third-party theorems were research references, so they are not republished as this user's mathematical progress. The concurrently active October 7 literature investigation is outside the completed-artifact snapshot; future actual results can be added with a new dated commit.

All original research files and notebook identities remain preserved. Upload commits are dated to the real recovery date, with no fabricated history. Earlier manuscript statements saying "nothing published" describe their preparation state before this upload. No new license is assigned to supplied manuscripts or third-party material. Work was developed with Claude and Codex assistance; attribution and human-verification limitations remain explicit.
