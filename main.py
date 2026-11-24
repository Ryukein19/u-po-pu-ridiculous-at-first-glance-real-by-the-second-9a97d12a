import os
# One-liner entry: the line below is the whole submission.
LINE = "A subscription that texts your boss 'in a meeting' the moment your code breaks, so you can fix it in peace. Teams pay $9 a month for the alibi."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
