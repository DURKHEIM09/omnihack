# n8n robust pull request test

This pull request is intentionally larger than the previous smoke tests.

It includes:
- a Python code change in `main.py`
- a test file in `tests/test_main.py`
- this documentation marker
- a follow-up commit after PR creation to trigger a PR update event

Expected automation signal: GitHub emits a `pull_request` event for n8n when the PR is opened, and another event when the branch receives a new commit.

Follow-up commit marker: 2026-05-03 robust PR synchronize test.
