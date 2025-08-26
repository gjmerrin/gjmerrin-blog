#!/usr/bin/env python3

import os
import re
from pathlib import Path

# All publications with detailed information
all_publications = [
    # Featured Publications (already created, just listing for reference)
    {
        "title": "CATAcode: A principled approach for coding check-all-that-apply demographic items",
        "authors": ["Gabriel J. Merrin", "Kathleen Nickodem", "Natalie Grant", "Shanelle Weerakoon", "Melissa Holt", "Dorothy L. Espelage"],
        "year": "2025",
        "journal": "Advances in Methods and Practices in Psychological Science",
        "doi": "",
        "featured": True,
        "folder": "merrin-nickodem-catacode-accepted",
        "status": "accepted"
    },
    
    # 2024 Publications
    {
        "title": "Zhang, X., Merrin, G. J., & Slavich, G. M. (2024). Adverse childhood experiences and emotion dysregulation phenotypes: An intersectional analysis of race/ethnicity and gender in a nationally representative U.S. sample",
        "authors": ["Xinxin Zhang", "Gabriel J. Merrin", "George M. Slavich"],
        "year": "2024",
        "journal": "Child Abuse & Neglect",
        "doi": "10.1016/j.chiabu.2024.107129",
        "featured": False,
        "folder": "zhang-merrin-slavich-2024"
    },
    {
        "title": "A prospective study of sexual risk patterns associated with delinquency and justice involvement among child welfare system-involved adolescent males",
        "authors": ["Natalie Grant", "Gabriel J. Merrin", "Khadijah April", "Amara K. April-Sandars", "Ishita Arora", "David Gordon"],
        "year": "2024",
        "journal": "Perspectives on Sexual and Reproductive Health",
        "doi": "10.1111/psrh.12255",
        "featured": False,
        "folder": "grant-merrin-april-2024"
    },
    {
        "title": "Different self-damaging behaviors, similar motives? Testing measurement invariance of motives for nonsucidal self-injury, disordered eating, and substance misuse",
        "authors": ["Chloe L. Robillard", "Gabriel J. Merrin", "Nicholas K. Legg", "Megan E. Ames", "Brianna J. Turner"],
        "year": "2024",
        "journal": "British Journal of Clinical Psychology",
        "doi": "10.1111/bjc.12467",
        "featured": False,
        "folder": "robillard-merrin-legg-2024",
        "student_led": True
    },
    
    # 2023 Publications
    {
        "title": "Assessing the longitudinal measurement invariance of the conflict in adolescent dating relationship inventory (CADRI) across heterosexual and sexual minority adolescents in the United States",
        "authors": ["Maria M. Rivas-Koehl", "Gabriel J. Merrin", "Dorothy L. Espelage"],
        "year": "2023",
        "journal": "Psychology of Violence",
        "doi": "10.1037/vio0000452",
        "featured": False,
        "folder": "rivas-koehl-merrin-espelage-2023",
        "student_led": True
    },
    {
        "title": "Trajectories of oppositional defiant disorder severity from adolescence to young adulthood and substance use, mental health, and behavioral problems",
        "authors": ["Bonnie J. Leadbeater", "Gabriel J. Merrin", "Andrea Contreras", "Megan E. Ames"],
        "year": "2023",
        "journal": "Journal of the Canadian Academy of Child and Adolescent Psychiatry",
        "doi": "PMID: 38034412",
        "featured": False,
        "folder": "leadbeater-merrin-contreras-2023"
    },
    
    # Continue with more key publications...
    # 2022 Publications
    {
        "title": "Predictors of early-onset cannabis use in adolescence and risks for substance use disorder symptoms in young adulthood",
        "authors": ["Gabriel J. Merrin", "Bonnie J. Leadbeater", "Carla M. B. Sturgess", "Megan E. Ames", "Kara Thompson"],
        "year": "2022",
        "journal": "Journal of Drug Issues",
        "doi": "10.1177/00220426211049356",
        "featured": False,
        "folder": "merrin-leadbeater-sturgess-2022"
    },
    {
        "title": "Social-ecological predictors of homophobic name-calling perpetration and victimization among early adolescents",
        "authors": ["Alberto Valido", "Gabriel J. Merrin", "Dorothy L. Espelage", "Luz E. Robinson", "Kathleen Nickodem", "Katherine M. Ingram", "Alie J. El Sheikh", "Cagil Torgal", "Jennifer Fairclough"],
        "year": "2022",
        "journal": "Journal of Early Adolescence",
        "doi": "10.1177/02724316211002271",
        "featured": False,
        "folder": "valido-merrin-espelage-2022"
    },
    
    # Key earlier publications
    {
        "title": "Examining social-ecological predictors of youth gang entry among serious juvenile offenders: A survival analysis",
        "authors": ["Gabriel J. Merrin", "Jordan P. Davis", "Katherine M. Ingram", "Dorothy L. Espelage"],
        "year": "2020",
        "journal": "American Journal of Orthopsychiatry",
        "doi": "10.1037/ort0000491",
        "featured": False,
        "folder": "merrin-davis-ingram-2020"
    },
    {
        "title": "Disruption of transitions in high-risk substance use from adolescence to young adulthood: School, employment, and romantic relationship factors",
        "authors": ["Gabriel J. Merrin", "Megan Ames", "Carla M. B. Sturgess", "Bonnie J. Leadbeater"],
        "year": "2020",
        "journal": "Substance Use and Misuse",
        "doi": "10.1080/10826084.2020.1729200",
        "featured": False,
        "folder": "merrin-ames-sturgess-2020"
    },
    {
        "title": "The co-evolution of bullying perpetration, homophobic teasing, and a school friendship network",
        "authors": ["Gabriel J. Merrin", "Kayla de la Haye", "Dorothy L. Espelage", "Brett Ewing", "Joan S. Tucker", "Matthew Hoover", "Harold D. Green"],
        "year": "2018",
        "journal": "Journal of Youth and Adolescence",
        "doi": "10.1007/s10964-017-0783-4",
        "featured": False,
        "folder": "merrin-delahaye-espelage-2018"
    }
]

def create_publication_folder(pub):
    """Create a publication folder and index.md file"""
    base_path = Path("/home/user/webapp/content/publication")
    pub_path = base_path / pub["folder"]
    
    # Skip if already exists
    if pub_path.exists():
        print(f"Skipping existing: {pub_path}")
        return
        
    pub_path.mkdir(exist_ok=True)
    
    # Generate author list
    author_list = "\n".join([f"- {author}" for author in pub["authors"]])
    
    # Determine tags based on content
    tags = ["Adolescent Development", "Prevention Science"]
    if "substance" in pub["title"].lower() or "drug" in pub["title"].lower():
        tags.append("Substance Use")
    if "bullying" in pub["title"].lower() or "harassment" in pub["title"].lower():
        tags.append("Bullying")
    if "gang" in pub["title"].lower():
        tags.append("Youth Gangs")
    if "method" in pub["title"].lower() or "analytic" in pub["title"].lower():
        tags.append("Research Methods")
        
    tag_list = "\n".join([f"- {tag}" for tag in tags])
    
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
{tag_list}

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
created_count = 0
for pub in all_publications:
    create_publication_folder(pub)
    created_count += 1

print(f"Processed {len(all_publications)} publications, created {created_count} new folders")