#!/usr/bin/env python3
"""
Fix DOI duplicates by removing manual DOI links when Hugo can auto-generate them
"""

import os
import re
from pathlib import Path

def fix_publication_file(file_path):
    """Remove manual DOI links when there's a doi field in frontmatter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if there's a doi field in the frontmatter
    doi_field_match = re.search(r'doi:\s*"([^"]+)"', content)
    
    if doi_field_match and doi_field_match.group(1):  # Non-empty DOI
        # Remove manual DOI links from the links section
        # Pattern: - name: "DOI"\n  url: "https://doi.org/..."
        doi_link_pattern = r'-\s*name:\s*["\']DOI["\']\s*\n\s*url:\s*["\']https://doi\.org/[^"\']+["\']\s*\n?'
        
        if re.search(doi_link_pattern, content):
            content = re.sub(doi_link_pattern, '', content)
            
            # Clean up any empty links sections
            content = re.sub(r'links:\s*\n\s*\n', 'links:\n\n', content)
            
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
                    print(f"Fixed DOI duplicate: {pub_folder.name}")
                    fixed_count += 1
    
    print(f"\nFixed DOI duplicates in {fixed_count} publications")

if __name__ == "__main__":
    main()