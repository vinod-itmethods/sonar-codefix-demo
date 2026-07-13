# sonar-demo

A tiny Python project used to demo SonarQube Cloud (Enterprise) for a customer:
automatic onboarding, analysis, PR decoration, AI CodeFix, and the MCP server.

The code in `src/` contains **intentional** issues (a weak hash, a hardcoded
token, a mutable default argument, duplicated blocks, dead code, etc.) so the
scan produces real findings to fix live.

## Files
- `src/account_service.py` — planted bug / hotspot / code-smell / duplication issues
- `src/utils.py` — a few more issues for variety
- `sonar-project.properties` — Sonar project + org keys (edit before first scan)
- `.github/workflows/sonar.yml` — GitHub Actions scan (push = baseline, PR = decoration)

## One-time setup
1. Create the repo in GitHub and push these files (see commands below).
2. In SonarQube Cloud, import the repo into your organization (Enterprise).
3. Add the `SONAR_TOKEN` secret in the GitHub repo (Settings > Secrets and
   variables > Actions). Use a **user or project analysis token** from Sonar Cloud.
4. Update `sonar.projectKey` and `sonar.organization` in
   `sonar-project.properties` to match your org.
5. Enable AI CodeFix for this project in Sonar Cloud
   (Organization > Administration > AI capabilities > AI CodeFix), provider
   Claude Sonnet 4.
