# AutomaticTrading RD-Agent — Release Publication Trigger Governance

**Status:** Proposed change in an isolated draft PR; **not merged or active on main**.

## Identified conflict

The upstream-derived `.github/workflows/release.yml` previously used `push` on `main` as its trigger. Its `release_and_publish` job invokes `release-please-action`, and when a release is created it can run `make upload` with `PYPI_TOKEN`. The source proves a possible automated publishing path, **not** that any release or upload actually occurred, or that the required secret is configured.

This conflicts with the intended organizational gate requiring explicit review before publishing distributable artifacts.

## Proposed code change

The isolated branch replaces the automatic `push(main)` trigger with `workflow_dispatch`, and requires the main branch as the job's ref. The existing build, release, and PyPI commands are otherwise unchanged. This does not grant any agent or service the right to trigger the manual workflow.

**Manual dispatch is necessary but not sufficient proof of owner approval.** Effective GitHub environment protection, actor restrictions, secrets access and exact SHA attestation must be independently verified before any publishing action. The original workflow may still be active on the default branch until a separately authorized merge.

## Review checklist

- Verify `release.yml` has **no `push` trigger** in the proposed branch and the job only runs when manually requested from `main`.
- Verify no separate release/publish or external GitHub App can independently release without owner review.
- Check effective environment and required-reviewer controls; do not copy or print `PYPI_TOKEN` or other secret values.
- Verify exact source SHA, wheel/dist artifact digest, license, SBOM, and Python dependency lock before any future release.
- Confirm existing release process behavior and whether manually invoking `release-please` is functionally sufficient. If not, design a separately approved workflow; **do not bypass** release checks.
- Run harmless static tests and PR CI. **Do not invoke `workflow_dispatch` during this audit.**

## Non-goals

No changes to production RD-Agent services, OpenClaw, Python runtime, RAG, Qlib, PostgreSQL, ELK, MT5, broker, datasets, secrets or artifact registry. No package is published. No snapshot is created.

## Conflict mapping

INT-025, GOV-02, GOV-04, GOV-08 remain under review. Mark only `PATCH_IN_DRAFT_PR` until owner-reviewed merge and proof of effective controls.
