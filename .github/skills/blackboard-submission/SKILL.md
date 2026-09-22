---
name: blackboard-submission
description: Safely prepare and, only with explicit final confirmation, submit this CSCI 6032 homework to its Blackboard submission page.
---

# Blackboard submission

Use this workflow for this repository only. Keep permission boundaries visible: do not assume shell, filesystem, network, GitHub, or browser access; request each needed tool or permission at the point of use. Do not add an `allowed-tools` frontmatter field.

## Safety gates

- Confirm the working repository is the expected homework repository before doing anything else:
  - repository name: `csi6032-hw2-ajradka`
  - expected remote: `https://github.com/ajradka/csi6032-hw2-ajradka.git`
  - required notebook: `CSCI6032_hw2\CSCI6032_hw2.ipynb`
- Run a preflight covering the current branch, complete git status, recent commits, exact fetch/push remote URL, and required homework files. Do not open Blackboard during preflight.
- Stop and report the blocking condition if the tree is not clean, the reviewed branch is not the intended branch, required artifacts are absent, the remote is unexpected, or credentials, tokens, private keys, browser data, or other unresolved private data are apparent. Never print or inspect the contents of suspected secrets.
- Do not commit, push, delete, reset, amend, or change history unless the student separately and explicitly authorizes that action.
- Confirm that the reviewed commit/branch has already been pushed by checking the branch’s remote tracking state and comparing the reviewed `HEAD` with its upstream. If it is not pushed, stop and ask the student to push it personally.

## Dry run and package preparation

Support a dry run by default. A dry run performs every possible repository, artifact, privacy, archive, and submission-data check without opening Blackboard, controlling a browser tab, uploading a file, or submitting anything.

After all preflight gates pass:

1. Resolve the student’s GitHub username without requesting or reading credentials. If it is not unambiguous, ask the student to provide or confirm it.
2. Build `csci6032-hw2-<github-username>.tar.gz` from the committed `HEAD`, not from an arbitrary working directory. The archive must not contain `.git`, credentials, tokens, private keys, browser data, caches (including `__pycache__` and notebook checkpoints), generated receipts/screenshots, or unrelated files.
3. Verify the archive’s file list before using it. If an excluded or unexpected path appears, stop and do not upload the archive.
4. List the final archive contents and show, for student review:
   - the exact notebook path;
   - the exact archive path and byte size;
   - the exact repository URL;
   - the exact Blackboard submission text.
5. Keep the archive outside the public repository when practical. Never commit the archive, Blackboard screenshots, receipts, browser profiles, browser storage, or personal information.

The submission text must be presented verbatim before staging. Use the repository URL from the verified remote, normalized to the canonical HTTPS URL, and do not invent assignment details. If the submission page requires a field whose value is unknown, stop and ask rather than guessing.

## Blackboard interaction

- Ask the student for explicit permission before opening or controlling any Blackboard tab. A prior general approval does not authorize browser interaction.
- The student must authenticate personally. Never request, read, store, type, transmit, or expose passwords, one-time codes, session tokens, recovery codes, or other credentials. Pause while the student completes authentication themselves.
- After authentication, navigate only to this homework’s Blackboard submission page. Do not browse unrelated courses, pages, accounts, messages, or files.
- Stage only the verified notebook, the verified archive, and the verified repository URL/text required by this assignment. Re-check the selected filenames and URL immediately before staging.
- Do not click the final submit button, press an equivalent key, or invoke an equivalent irreversible action yet. Stop and show the student exactly what Blackboard is about to submit, including filenames, repository URL, text, and any visible assignment target.
- Require a fresh, explicit confirmation at that exact point. “Proceed,” “submit,” or equivalent must refer to the displayed final payload; earlier approval is insufficient.
- Only after that confirmation, perform the final submission. Verify the resulting confirmation page or receipt and report the result without exposing credentials or unnecessary personal information.

If any page, assignment target, selected file, URL, archive contents, or confirmation state is ambiguous, stop immediately and ask the student to resolve it. Do not bypass warnings or continue after an unexpected navigation.
