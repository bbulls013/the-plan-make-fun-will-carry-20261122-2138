import os
from pathlib import Path

PLAN = "Day1: Buy 12 expired .coms on ExpiredDomains.net via Cloudflare ($8ea, screened for backlinks/traffic). List on Dan.com $349ea, AI builds landing page + emails 40 SMB buyers/domain via Hunter.io. Drop price day20. Likely sell 2-3 by day30 = $698-$1,047."


def main() -> None:
    """Write the fixed plan text to entry.txt in the output directory."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
