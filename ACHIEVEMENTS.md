# GitHub Achievements — research notes

GitHub has never published an official Achievements list or thresholds, and
there is no REST or GraphQL API for them. The authoritative record of a badge
is GitHub's own profile UI: the badge sidebar and the per-badge detail
fragment at `/users/<user>/achievements/<slug>/detail`, which shows the tier,
unlock date and the milestone history behind it.

Tier figures below are **community-reported (unofficial)** and may change.

| Achievement | Requirement (unofficial) | Tiers |
|---|---|---|
| Pull Shark | Merged pull requests authored by the account | 2 / 16 / 128 / 1024 |
| Starstruck | Stars on a single repository you created | 16 / 128 / 512 / 4096 |
| Galaxy Brain | Accepted answers in repository Discussions | 2 / 8 / 16 / 32 |
| Pair Extraordinaire | Co-authored commits on merged pull requests | 1 / 10 / 24 / 48 |
| Quickdraw | Close an issue or PR within 5 minutes of opening it | single |
| YOLO | Merge your own pull request with no review | single |
| Public Sponsor | Sponsor someone through GitHub Sponsors | single |
| Finishing Touch | Reported in 2026 community catalogues; criteria unverified | unknown |

Retired / unavailable: Arctic Code Vault Contributor, Mars 2020 Helicopter
Contributor (historical events). Heart On Your Sleeve and Open Sourcerer are
reported switched off / experimental — monitored monthly, not pursued unless
they verifiably return.

See `ELIGIBILITY-MATRIX.md` for this account's status per badge.
