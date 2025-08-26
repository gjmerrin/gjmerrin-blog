#!/usr/bin/env python3
"""
Fix duplicate DOI links in publication files
"""

import os
import re
from pathlib import Path

def fix_publication_file(file_path):
    """Fix duplicate DOI links in a publication file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if there's a duplicate DOI section at the end
    # Pattern: **DOI:** https://doi.org/...
    doi_pattern = r'\*\*DOI:\*\* https://doi\.org/[^\s\n]+\s*\n*$'
    
    if re.search(doi_pattern, content):
        # Remove the duplicate DOI at the end
        content = re.sub(doi_pattern, '', content)
        
        # Also remove any trailing empty lines
        content = content.rstrip() + '\n'
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    return False

def main():
    """Process all publication files"""
    pub_dir = Path("/home/user/webapp/content/publication")
    fixed_count = 0
    
    for pub_folder in pub_dir.iterdir():
        if pub_folder.is_dir():
            index_file = pub_folder / "index.md"
            if index_file.exists():
                if fix_publication_file(index_file):
                    print(f"Fixed: {pub_folder.name}")
                    fixed_count += 1
    
    print(f"\nFixed duplicate DOI links in {fixed_count} publications")

if __name__ == "__main__":
    main()