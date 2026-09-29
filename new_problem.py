#!/usr/bin/env python3
import sys
import os

TOPIC_MAP = {
    "arrays-and-hashing": "01-arrays-and-hashing",
    "two-pointers": "02-two-pointers",
    "sliding-window": "03-sliding-window",
    "stack": "04-stack",
    "binary-search": "05-binary-search",
    "linked-list": "06-linked-list",
    "trees": "07-trees",
    "tries": "08-tries",
    "heap-priority-queue": "09-heap-priority-queue",
    "backtracking": "10-backtracking",
    "graphs": "11-graphs",
    "advanced-graphs": "12-advanced-graphs",
    "1d-dynamic-programming": "13-1d-dynamic-programming",
    "2d-dynamic-programming": "14-2d-dynamic-programming",
    "greedy": "15-greedy",
    "intervals": "16-intervals",
    "math-and-geometry": "17-math-and-geometry",
    "bit-manipulation": "18-bit-manipulation",
}

def resolve_topic(topic: str) -> str:
    cleaned = topic.strip().lower()
    # If already prefixed (e.g. 01-arrays-and-hashing)
    if cleaned in TOPIC_MAP.values():
        return cleaned
    return TOPIC_MAP.get(cleaned, cleaned)

def create_problem(order, number, slug, topic, difficulty):
    order_idx = f"{int(str(order).strip()):02d}"
    number = str(number).strip()
    slug = slug.strip().lower()
    difficulty = difficulty.strip().capitalize()
    topic_folder = resolve_topic(topic)
    
    # Title from slug (e.g. concatenation-of-array -> Concatenation of Array)
    title = " ".join(word.capitalize() for word in slug.split("-"))
    
    dir_name = f"{order_idx}-{number}-{slug}"
    folder_path = os.path.join("problems", topic_folder, dir_name)
    os.makedirs(folder_path, exist_ok=True)
    
    readme_path = os.path.join(folder_path, "README.md")
    solution_path = os.path.join(folder_path, "solution.py")
    
    readme_template = f"""- Problem: [{title}](https://leetcode.com/problems/{slug}/)
- Difficulty: {difficulty}
- Pattern: 
- Time complexity: 
- Space complexity: 
- What I learned / my mistake: 
"""

    solution_template = """class Solution:
    pass
"""

    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_template)
            
    if not os.path.exists(solution_path):
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(solution_template)
            
    print(f"Created: {folder_path}/")
    print(f"  ├── README.md")
    print(f"  └── solution.py")

if __name__ == "__main__":
    if len(sys.argv) >= 6:
        order = sys.argv[1]
        num = sys.argv[2]
        slug = sys.argv[3]
        topic = sys.argv[4]
        diff = sys.argv[5]
    else:
        order = input("NeetCode Order Index (e.g. 1): ").strip()
        num = input("LeetCode Problem Number (e.g. 1929): ").strip()
        slug = input("Slug (e.g. concatenation-of-array): ").strip()
        topic = input("Topic (e.g. arrays-and-hashing): ").strip()
        diff = input("Difficulty (e.g. Easy): ").strip()
        
    create_problem(order, num, slug, topic, diff)
