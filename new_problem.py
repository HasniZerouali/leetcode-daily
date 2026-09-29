#!/usr/bin/env python3
import sys
import os

def create_problem(number, slug, topic, difficulty):
    number = str(number).strip()
    slug = slug.strip().lower()
    topic = topic.strip().lower()
    difficulty = difficulty.strip().capitalize()
    
    # Title from slug (e.g. concatenation-of-array -> Concatenation of Array)
    title = " ".join(word.capitalize() for word in slug.split("-"))
    
    dir_name = f"{number}-{slug}"
    folder_path = os.path.join("problems", topic, dir_name)
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
    if len(sys.argv) >= 5:
        num = sys.argv[1]
        slug = sys.argv[2]
        topic = sys.argv[3]
        diff = sys.argv[4]
    else:
        num = input("LeetCode Problem Number (e.g. 1929): ").strip()
        slug = input("Slug (e.g. concatenation-of-array): ").strip()
        topic = input("Topic (e.g. arrays-and-hashing): ").strip()
        diff = input("Difficulty (e.g. Easy): ").strip()
        
    create_problem(num, slug, topic, diff)
