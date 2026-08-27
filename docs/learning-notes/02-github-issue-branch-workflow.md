# GitHub Issue → Branch → Pull Request Workflow

## 1. Overview

A professional software development workflow separates planning, development, testing, review, and integration.

A common workflow is:

Issue
    ↓
Feature Branch
    ↓
Implementation
    ↓
Testing
    ↓
Commit
    ↓
Push
    ↓
Pull Request
    ↓
CI / Code Review
    ↓
Merge
    ↓
Issue Closed

This project follows this workflow to simulate an industry-style development process.

---

# 2. What is a GitHub Issue?

A GitHub Issue is a work item used to describe a feature, bug, improvement, task, or technical requirement.

Example:

Issue #3

Title:

Implement Incident Management API

The issue describes:

- What needs to be built
- Why it is needed
- Scope of the work
- API requirements
- Acceptance criteria
- Definition of Done
- Future work
- Non-goals

The Issue represents the planned work, not the code itself.

---

# 3. Why Create an Issue Before Coding?

Creating an Issue before implementation helps the development team understand the expected outcome.

Instead of starting with:

"Let's write some code."

The process becomes:

Requirement
    ↓
Issue
    ↓
Technical Design
    ↓
Implementation
    ↓
Testing
    ↓
Review

Benefits:

- Clear scope
- Better planning
- Easier tracking
- Better communication
- Easier code review
- Clear definition of completion
- Historical record of why the change was made

---

# 4. Acceptance Criteria

Acceptance criteria define what must be true for the work to be considered complete.

Example:

- API can create an incident
- Every incident receives a unique ID
- API can retrieve an incident
- API can list incidents
- Request validation is implemented
- Response schemas are defined
- Correct HTTP status codes are returned
- Automated tests are included
- Swagger/OpenAPI documentation is available

Acceptance criteria should be testable.

Example:

Requirement:

"API can create an incident."

Testable behavior:

Given valid incident information

When:

POST /api/v1/incidents

Then:

HTTP 201 Created

And:

The response contains an incident ID.

---

# 5. Definition of Done

Definition of Done describes the conditions that must be satisfied before the work is considered complete.

Example:

- Implementation completed
- Tests added
- Tests passing
- API manually verified
- Documentation updated
- Pull Request created
- CI checks passing
- Code reviewed
- Changes merged

Definition of Done prevents a feature from being considered complete just because the code was written.

---

# 6. Non-Goals

Non-goals define what is intentionally outside the current scope.

For the first Incident Management API implementation, the following are intentionally excluded:

- PostgreSQL persistence
- Authentication
- AI analysis
- Automated remediation
- Evidence collection

These capabilities will be implemented in later milestones.

This helps prevent scope creep.

---

# 7. What is a Git Branch?

A Git branch is an independent line of development.

The main branch represents the stable integration branch.

Example:

main
    |
    +---- feature/incident-api
    |
    +---- feature/evidence-collection
    |
    +---- fix/incident-validation

Instead of changing main directly, developers normally create a branch for their work.

---

# 8. Why Use Feature Branches?

Feature branches isolate changes from the stable main branch.

Benefits:

- Protect main
- Allow independent development
- Make code review easier
- Reduce accidental changes
- Enable multiple developers to work simultaneously
- Provide a clear history of feature development

Example:

main
    |
    A---B---C
             \
              D---E---F
              feature/incident-api

The feature work can be reviewed before being merged into main.

---

# 9. Branch Naming

Branches should use meaningful names.

Examples:

feature/incident-api
feature/evidence-collection
feature/ai-investigation
feature/audit-logging

Bug fixes:

fix/incident-validation
fix/database-connection

Documentation:

docs/github-workflow
docs/api-documentation

Refactoring:

refactor/incident-service

A good branch name communicates the purpose of the change.

---

# 10. Why Update main Before Creating a Branch?

Before creating a new feature branch:

git switch main

Then:

git pull --ff-only

This ensures the local main branch contains the latest changes from the remote repository.

Workflow:

Remote main
    ↓
git pull
    ↓
Updated local main
    ↓
Create feature branch

This reduces the possibility of starting development from an outdated version of the project.

---

# 11. Creating a Feature Branch

Example:

git switch main

git pull --ff-only

git switch -c feature/incident-api

The command:

git switch -c feature/incident-api

does two things:

1. Creates the branch
2. Switches to the new branch

After creating it:

git branch

Example:

* feature/incident-api
  main

The * indicates the current branch.

---

# 12. Issue vs Branch

A GitHub Issue and Git branch are different things.

Issue:

"What needs to be done?"

Branch:

"Where will I develop the change?"

Example:

Issue #3
Implement Incident Management API

↓

feature/incident-api

↓

Code implementation

The issue tracks the work.

The branch contains the development changes.

---

# 13. What is a Commit?

A commit is a recorded snapshot of changes in Git.

Example:

git add backend/

git commit -m "feat: add incident management API"

A good commit message explains what changed.

Examples:

feat: add incident management API

fix: validate incident priority

docs: add API architecture documentation

test: add incident creation tests

refactor: separate incident service layer

---

# 14. Conventional Commit Style

This project uses a conventional commit style.

Common prefixes:

feat:
New functionality

fix:
Bug fix

docs:
Documentation changes

test:
Testing changes

refactor:
Code restructuring without changing behavior

chore:
Maintenance work

Example:

feat: add incident creation endpoint

This makes the Git history easier to understand.

---

# 15. What is a Remote?

A remote repository is a repository hosted somewhere outside the local machine.

In this project:

GitHub repository

is represented locally by:

origin

Check it with:

git remote -v

Example:

origin  https://github.com/YogeshS-Mca/enterprise-ai-support-automation-platform.git (fetch)

origin  https://github.com/YogeshS-Mca/enterprise-ai-support-automation-platform.git (push)

origin is simply the conventional name given to the GitHub repository.

---

# 16. Push

After committing changes locally, the branch can be pushed to GitHub.

Example:

git push -u origin feature/incident-api

The first push uses:

-u

This establishes the upstream relationship between the local branch and remote branch.

After that:

git push

is usually enough.

---

# 17. What is a Pull Request?

A Pull Request is a proposal to merge changes from one branch into another.

Example:

feature/incident-api
        ↓
    Pull Request
        ↓
       main

The Pull Request allows the changes to be:

- Reviewed
- Tested
- Discussed
- Validated by CI
- Approved
- Merged

A Pull Request is not the same thing as a Git commit.

Commit:

Records a change.

Pull Request:

Requests integration of a set of changes.

---

# 18. Connecting an Issue to a Pull Request

A Pull Request can reference the Issue it implements.

Example:

Closes #3

When the Pull Request is successfully merged, GitHub can automatically close the linked Issue.

Workflow:

Issue #3
    ↓
feature/incident-api
    ↓
Pull Request
    ↓
Closes #3
    ↓
Merge
    ↓
Issue closed

This creates traceability between the requirement and implementation.

---

# 19. Code Review

Before merging a Pull Request, the code should be reviewed.

A reviewer may check:

- Correctness
- Architecture
- Readability
- Security
- Error handling
- Tests
- API design
- Performance
- Maintainability

The purpose of review is not only to find bugs.

It also helps maintain engineering standards.

---

# 20. CI

CI means Continuous Integration.

A CI pipeline automatically checks changes when a Pull Request is created or updated.

Typical checks include:

- Install dependencies
- Run linting
- Run unit tests
- Run integration tests
- Check formatting
- Perform security checks
- Build application

Example:

Pull Request
    ↓
GitHub Actions
    ↓
Tests
    ↓
Lint
    ↓
Security checks
    ↓
Build
    ↓
Pass / Fail

CI will be added to this project in a later milestone.

---

# 21. Merge

After review and successful CI checks, the Pull Request can be merged.

Example:

feature/incident-api
        ↓
Pull Request
        ↓
Review
        ↓
CI
        ↓
Merge
        ↓
main

After merging, the feature becomes part of main.

---

# 22. Branch Cleanup

After a feature branch is merged, it normally does not need to remain active.

Local branch:

git branch -d feature/incident-api

Remote branch:

git push origin --delete feature/incident-api

Then:

git fetch --prune

Cleaning merged branches keeps the repository easier to understand.

---

# 23. Project Workflow Used in This Repository

The workflow used for this project is:

1. Create GitHub Issue
2. Update local main
3. Create feature branch
4. Design the feature
5. Implement the feature
6. Add automated tests
7. Verify locally
8. Create meaningful commits
9. Push branch to GitHub
10. Create Pull Request
11. Link Pull Request to Issue
12. Run CI
13. Review code
14. Merge Pull Request
15. Update local main
16. Delete merged branch
17. Continue with the next Issue

---

# 24. Example: Incident Management Feature

Our current feature follows:

GitHub Issue #3

"Implement Incident Management API"

↓

feature/incident-api

↓

API design

↓

FastAPI implementation

↓

Pydantic validation

↓

Automated tests

↓

Swagger verification

↓

Git commit

↓

Push

↓

Pull Request

↓

CI

↓

Code review

↓

Merge into main

↓

Issue #3 closed

---

# 25. Important Interview Questions

## Q1. Why don't you directly commit to main?

Because main should represent a stable integration branch. Feature branches allow isolated development, testing, and code review before changes are integrated.

---

## Q2. What is the difference between an Issue and a Pull Request?

An Issue tracks planned work or a problem.

A Pull Request proposes integrating completed changes into another branch.

---

## Q3. Why create a branch from updated main?

To ensure the feature starts from the latest stable code and reduce unnecessary integration conflicts.

---

## Q4. What is origin?

origin is the local Git alias for the remote repository, usually hosted on GitHub.

---

## Q5. What does git pull --ff-only do?

It updates the current branch only when Git can perform a fast-forward update.

It avoids automatically creating a merge commit during the pull.

---

## Q6. Why use feature branches?

They isolate development work, protect the stable branch, and make code review and collaboration easier.

---

## Q7. What is CI?

Continuous Integration automatically validates changes by running checks such as tests, linting, security checks, and builds.

---

## Q8. What is the purpose of a Pull Request?

A Pull Request provides a controlled process for reviewing, validating, discussing, and merging changes.

---

# 26. Mental Model

Remember this simple model:

Issue
"What should we do?"

Branch
"Where will we work?"

Commit
"What did we change?"

Push
"Send the branch to GitHub."

Pull Request
"Can we merge this?"

CI
"Does it pass automated checks?"

Review
"Is the implementation acceptable?"

Merge
"Integrate it into main."

Cleanup
"Remove the completed branch."

---

# 27. Our Project's Engineering Principle

The project should evolve incrementally.

We should prefer:

Simple
    ↓
Correct
    ↓
Tested
    ↓
Maintainable
    ↓
Scalable
    ↓
Production-oriented

We should avoid adding technologies only to make the architecture appear complex.

Every component should have a reason and should be explainable during an interview.