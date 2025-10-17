# QuantBot Cloud Trainer (GitHub Actions, every 6 hours)

This package makes GitHub Actions run your QuantBot **Research Lab** automatically every 6 hours.

## What it does
- Pulls fresh Binance 1m kline data
- Runs walk-forward paper trading with RL weight updates
- Writes results to `research_out/`
- Commits back to your repo: `learned_weights.json`, `leaderboard.csv`, and per-epoch CSVs

## How to install in your repo
1. Ensure the **Research Lab** folder exists at `quantbot_research_lab/` from our earlier zip.
2. Download this zip and extract into your repo **root** (it creates `.github/workflows/self_train.yml`).
3. Commit & push.

## Manual run
Go to **Actions** tab → select **QuantBot Cloud Training** → **Run workflow**.

## Schedule
- Cron: `0 */6 * * *` (every 6 hours, minute 0, UTC).

## Optional GitHub Secrets
- None strictly required for public Binance REST klines.
- Later, you can add `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, or custom webhooks for notifications.

## Consuming the weights
Your live bot (Streamlit/API) can read the latest `research_out/learned_weights.json` on startup to adapt signals.
