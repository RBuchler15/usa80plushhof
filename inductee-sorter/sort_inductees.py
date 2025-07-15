import re

input_file = "inductees.html"
output_file = "sorted_inductees.html"

with open(input_file, 'r', encoding='utf-8') as f:
    html = f.read()

entries = re.findall(r'(<div class="inductee-entry">.*?</div>\s*</div>?)', html, re.DOTALL)

def get_name(entry):
    match = re.search(r'<button class="accordion">(.*?)</button>', entry)
    return match.group(1).strip() if match else ""

sorted_entries = sorted(entries, key=get_name)

sorted_html = "\n\n".join(sorted_entries)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(sorted_html)

print(f"Sorted inductees saved to '{output_file}'")
