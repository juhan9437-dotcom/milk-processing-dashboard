import re
import os

files = [r"c:\haccp_dashboard\haccp_dashboard\app.py"]
pages_dir = r"c:\haccp_dashboard\haccp_dashboard\pages"
if os.path.exists(pages_dir):
    for f in os.listdir(pages_dir):
        if f.endswith(".py"):
            files.append(os.path.join(pages_dir, f))

# Emoji and Symbol Range
# 2600-27BF: Misc Symbols, Dingbats
# 1F300-1F9FF: Misc Symbols and Pictographs, Emoticons, Transport, etc.
# 2B00-2BFF: Misc Symbols and Arrows
pattern = re.compile(r"[\u2600-\u27BF]|[\U0001F300-\U0001F9FF]|[\u2B00-\u2BFF]")

for file_path in files:
    if not os.path.exists(file_path): continue
    printed_filename = False
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if pattern.search(line):
                if not printed_filename:
                    print(f"\nFile: {file_path}")
                    printed_filename = True
                print(f"{i}: {line.strip()}")
