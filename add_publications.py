#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Define the publications data
publications = [
    # 2025 Publications
    {
        "title": "Direct and witnessed bias-based harassment exposures among adolescents: Associations with functioning and the influence of protective factors",
        "authors": ["Melissa K. Holt", "Gabriel J. Merrin", "Owen Wyatt", "Jennifer G. Green", "Gianluca Gini", "Peter Fogelman"],
        "year": "2025",
        "journal": "Violence and Victims",
        "doi": "10.1891/VV-2023-0027",
        "featured": False,
        "folder": "holt-merrin-wyatt-2025"
    },
    {
        "title": "Family violence and adolescent aggressive behavior: The direct and indirect effects of depression and substance use",
        "authors": ["Tiffany I. Lawrence", "Gabriel J. Merrin", "Ashlee A. Mcfield"],
        "year": "2025",
        "journal": "International Journal of Mental Health and Addiction",
        "doi": "10.1007/s11469-022-00971-2",
        "featured": False,
        "folder": "lawrence-merrin-mcfield-2025"
    },
    {
        "title": "Social-emotional functioning among bias-based bullies, victims, and bully-victims",
        "authors": ["Nicole V. Fusco", "Melissa K. Holt", "Gabriel J. Merrin", "Jennifer G. Green"],
        "year": "2025",
        "journal": "School Psychology",
        "doi": "10.1037/spq0000620",
        "featured": False,
        "folder": "fusco-holt-merrin-2025",
        "student_led": True
    },
    {
        "title": "School suspension as a predictor of young adult homelessness: The International Youth Development Study",
        "authors": ["Jessica A. Heerde", "Jennifer A. Bailey", "Gabriel J. Merrin", "Margarita Raniti", "George C. Patton", "John W. Toumbourou", "Susan M. Sawyer"],
        "year": "2025",
        "journal": "Journal of Prevention",
        "doi": "10.1007/s10935-025-00829-y",
        "featured": False,
        "folder": "heerde-bailey-merrin-2025"
    },
    {
        "title": "The roles of alcohol availability, overserving, and enforcement in recreational and social settings on alcohol misuse and harms: A comparison of Australia and the United States",
        "authors": ["Van T. Le", "Jennifer A. Bailey", "Jessica A. Heerde", "Gabriel J. Merrin", "Emine A. Batmaz", "Alexandra B. Kelly", "John W. Toumbourou"],
        "year": "2025",
        "journal": "Journal of Studies on Alcohol and Drugs",
        "doi": "10.15288/jsad.24-00036",
        "featured": False,
        "folder": "le-bailey-heerde-2025"
    },
    {
        "title": "A longitudinal analysis of risk and protective factors of bias-based bullying victimization among adolescents",
        "authors": ["Kaitlin B. Parodi", "Melissa K. Holt", "Prerna Aradhya", "Jennifer G. Green", "Gabriel J. Merrin"],
        "year": "2025",
        "journal": "Journal of Interpersonal Violence",
        "doi": "10.1177/08862605251318276",
        "featured": False,
        "folder": "parodi-holt-aradhya-2025"
    },
    {
        "title": "Longitudinal associations between witnessing bias-based harassment and mental health functioning",
        "authors": ["Christine Marsico", "Owen Wyatt", "Kaitlin B. Parodi", "Melissa K. Holt", "Jennifer G. Green", "Gabriel J. Merrin"],
        "year": "2025",
        "journal": "Journal of School Violence",
        "doi": "10.1080/15388220.2025.2524335",
        "featured": False,
        "folder": "marsico-wyatt-parodi-2025",
        "student_led": True
    },
    {
        "title": "Cultivating adolescents' self-compassion through mindfulness: The role of self-regulation at both the individual- and classroom-level",
        "authors": ["Rachel A. Razza", "Qingyang Liu", "Ruiqing Feng", "Xinyi Hao", "Kelsey A. Kirkman", "Gabriel J. Merrin"],
        "year": "2025",
        "journal": "Contemporary School Psychology",
        "doi": "10.1007/s40688-025-00548-5",
        "featured": False,
        "folder": "razza-liu-feng-2025"
    }
]

# Continue with more publications...
# I'll add a few more key ones and then create the files

def create_publication_folder(pub):
    """Create a publication folder and index.md file"""
    base_path = Path("/home/user/webapp/content/publication")
    pub_path = base_path / pub["folder"]
    pub_path.mkdir(exist_ok=True)
    
    # Generate author list
    author_list = "\n".join([f"- {author}" for author in pub["authors"]])
    
    # Create content
    content = f'''---
title: "{pub["title"]}"
authors:
{author_list}
date: "{pub["year"]}-01-01T00:00:00Z"
doi: "{pub.get("doi", "")}"

# Schedule page publish date (NOT publication's date).
publishDate: "{pub["year"]}-01-01T00:00:00Z"

# Publication type.
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "*{pub["journal"]}*"
publication_short: ""

abstract: ""

summary: ""

tags:
- Adolescent Development
- Prevention Science

featured: {str(pub.get("featured", False)).lower()}

# Links (optional).
url_pdf: 
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
image:
  caption: ''
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
projects: []

# Slides (optional).
slides: ""
---'''

    # Write to file
    index_file = pub_path / "index.md"
    with open(index_file, 'w') as f:
        f.write(content)
    
    print(f"Created: {pub_path}")

# Create publication folders
for pub in publications:
    create_publication_folder(pub)

print(f"Created {len(publications)} publication folders")