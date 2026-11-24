import os
# One-liner entry (143 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "A subscription that texts your boss 'in a meeting' the moment your code breaks, so you can fix it in peace. Teams pay $9 a month for the alibi."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
