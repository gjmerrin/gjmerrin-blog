#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Parse the full publication list provided by the user
publications_text = '''
*Bi, K., Chen, M. S., Zhang, C., Li, T., Liu, Y., Chen, J., Chen, H., Xie, Z., Merrin, G. J., & Yip, P. (in press). Day-to-day dynamic coupling of affective symptomatology in Chinese mother-adolescent and father-adolescent dyads. Clinical Psychological Science.

Green, J. G., Ramirez, M., Merrin, G. J., & Holt, M. K. (2024). Bias-based harassment among U.S. adolescents. School Mental Health, 16, 343-353. https://doi.org/10.1007/s12310-024-09648-8

*Li, T., Wang, Z., Merrin, G. J., Wan, S., Bi, K., Quintero, M., & Song, S. (2024). The joint operations of teacher-student and peer relationships on classroom engagement among low-achieving elementary students: A longitudinal multilevel study. Journal of Contemporary Educational Psychology, 77, 1-14. https://doi.org/10.1016/j.cedpsych.2024.102258

*Bi, K., Li, T., Merrin, G. J., Zhang, C., Wang, Y., Xiao, Y., & Chen, M. S. (2024). Are there reciprocal interplays among Chinese adolescents', fathers', and mothers' depression at the within-family level? A family systems perspective. Journal of Psychopathology and Clinical Science, 133(2), 140–154. https://doi.org/10.1037/abn0000883

*Fairclough, J., *Abd-Elmonem, M., Merrin, G. J., Hong, J. S., & Voisin, D. R. (2024). Religiosity and associations with substance use and delinquency among urban African American adolescents. Journal of Religion and Health, 63, 531-550. https://doi.org/10.1007/s10943-023-01916-2

*Liu, Q., Razza, R. A., Zhang, Y., & Merrin, G. J. (2024). Differential growth trajectories of behavioral self-regulation from early childhood to adolescence: Implications for youth domain-general and school-specific outcomes. Applied Developmental Science, 1-21. https://doi.org/10.1080/10888691.2024.2405578

Bailey, J. A., Le, V. T., McMorris, B. J., Merrin, G. J., Heerde, J. A., Batmaz, E. A., & Toumbourou, J. W. (2024). Longitudinal associations between adult-supervised drinking during adolescence and alcohol misuse from ages 25–31 years: A comparison of Australia and the United States. Addictive Behaviors, 153, 1-6. https://doi.org/10.1016/j.addbeh.2024.107984

*Liu, Q., Razza, R. A., Vasilenko, S. A., & Merrin, G. J. (2024). Associations between early material hardship and behavioral self-regulation development across childhood: A person-centered approach. Research in Human Development, 20, 183-207. https://doi.org/10.1080/15427609.2024.2310449

*Liu, Q., Merrin, G. J., Vasilenko, S. A., & Razza, R. A. (2024). Continuity and change in early material hardship domains on the development of children's behavioral self-regulation in middle childhood. Children and Youth Services Review, 167, 1-12. https://doi.org/10.1016/j.childyouth.2024.107995

*Liu, Q., Merrin, G. J., & Razza, R. A. (2024). Reciprocal associations between parenting behaviors and children's self-regulation during the transition from early to middle childhood. Journal of Child and Family Studies, 33, 1602-1617. https://doi.org/10.1007/s10826-023-02703-z

Espelage, D. L., Kuehl, T., Wyman, P. A., Nickodem, K., Mintz, S., Valido, A., Robinson, L. E., Merrin, G. J., Hoagland, K., Schmeelk-Cone, K., LoMurray, S., Woolweaver, A. B., Ingram, K. M., & Rulison, K. (2024). An RCT of Sources of Strength high school primary prevention program on sexual violence perpetration and victimization and dismissiveness of sexual harassment. School Psychology Review, 53(6), 649-667. https://doi.org/10.1080/2372966X.2022.2164460

Wang, X., Liu. Q., Merrin, G. J., Keller, A., Dalhee, Y., & Henderson, A. (2023). Harsh parenting among veterans: parents' military-related PTSD, mentalization, and pre-military trauma. Frontiers in Psychology, 14, 1-14. https://doi.org/10.3389/fpsyg.2023.1283801

Ames, M. E., Robillard, C. L., Ryan, J. E. H., Merrin, G. J., & Turner, B. J. (2023). Reciprocal associations between physical activity, self-concept, somatic symptoms, and depression from adolescence to young adulthood: Disaggregating within- and between-person effects. Mental Health and Physical Activity, 23, 1-9. https://doi.org/10.1016/j.mhpa.2023.100513

Forber-Pratt, A. J., Price, L. R., Merrin, G. J., Hanebutt, R. A., & Fairclough, J. A. (2022). Psychometric properties of the Disability Identity Development Scale: Confirmatory factor and bifactor analyses. Rehabilitation Psychology, 67(2), 120-127. https://doi.org/10.1037/rep0000445

Leadbeater, B. J., Sukhawathanakul, P., Rush, J., Merrin, G. J., & Lewis, N. (2022). Examining the effectiveness of the WITS programs in the context of variability in trajectories of child development. Prevention Science 23, 538-551. https://doi.org/10.1007/s11121-021-01327-3

Espelage, D. L., Ingram, K. M., Hong, J. S., & Merrin, G. J. (2022). Bullying as a developmental precursor to sexual violence throughout adolescence: Decade in review. Trauma, Violence, & Abuse, 23(4), 1358-1370. https://doi.org/10.1177/15248380211043811

Forber-Pratt, A. J., Merrin, G. J., & Espelage, D. L. (2021). Exploring the intersections of disability, race and gender on student outcomes in High School. Remedial and Special Education 42(5), 290-303. https://doi.org/10.1177/0741932520941201

Valido, A., Ingram, K. M., Espelage, D. L., Torgal, C., Merrin, G. J., & Davis, J. P. (2021). Intrafamilial violence and verbal and physical aggression among early adolescents: Moderating role of school sense of belonging. Journal of Family Violence 36, 87-98. https://doi.org/10.1007/s10896-020-00142-8
'''

def parse_publication(pub_text):
    """Parse a publication string to extract components"""
    # Extract year from DOI or text
    year_match = re.search(r'\((\d{4})\)', pub_text)
    year = year_match.group(1) if year_match else "2024"
    
    # Extract DOI
    doi_match = re.search(r'https://doi\.org/([\w\./\-]+)', pub_text)
    doi = doi_match.group(1) if doi_match else ""
    
    # Extract journal (text between period and volume/page numbers)
    # This is a simplified approach - might need manual refinement
    journal_match = re.search(r'\. ([A-Za-z\s&,]+),?\s*\d', pub_text)
    journal = journal_match.group(1).strip() if journal_match else "Unknown Journal"
    
    # Check if student-led
    student_led = pub_text.strip().startswith('*')
    
    # Create title (everything before the first period)
    title_match = re.search(r'^(\*?[^.]+)', pub_text.strip())
    title = title_match.group(1).replace('*', '').strip() if title_match else "Unknown Title"
    
    # Extract authors (between title and year)
    author_pattern = r'\. ([^.]+) \(\d{4}\)'
    author_match = re.search(author_pattern, pub_text)
    authors_str = author_match.group(1) if author_match else "Gabriel J. Merrin"
    
    # Parse authors
    authors = []
    if '&' in authors_str:
        author_parts = re.split(r',\s*(?=\w)', authors_str.replace(' & ', ', '))
        for author in author_parts:
            authors.append(author.strip())
    else:
        authors = [authors_str.strip()]
    
    # Create folder name (simplified)
    folder = re.sub(r'[^\w\s-]', '', title[:50]).strip().replace(' ', '-').lower()
    folder = re.sub(r'-+', '-', folder)
    
    return {
        'title': title,
        'authors': authors,
        'year': year,
        'journal': journal,
        'doi': doi,
        'student_led': student_led,
        'folder': folder,
        'featured': False
    }

def create_publication_folder(pub):
    """Create a publication folder and index.md file"""
    base_path = Path("/home/user/webapp/content/publication")
    pub_path = base_path / pub["folder"]
    
    # Skip if already exists
    if pub_path.exists():
        print(f"Skipping existing: {pub_path}")
        return False
        
    pub_path.mkdir(exist_ok=True)
    
    # Generate author list
    author_list = "\n".join([f"- {author}" for author in pub["authors"]])
    
    # Determine tags based on content
    tags = ["Adolescent Development", "Prevention Science"]
    title_lower = pub["title"].lower()
    
    if any(word in title_lower for word in ["substance", "drug", "alcohol", "cannabis", "marijuana"]):
        tags.append("Substance Use")
    if any(word in title_lower for word in ["bullying", "harassment", "victimization", "aggression"]):
        tags.append("Bullying")
    if any(word in title_lower for word in ["school", "academic", "classroom", "teacher"]):
        tags.append("School Context")
    if any(word in title_lower for word in ["method", "analytic", "model", "measurement"]):
        tags.append("Research Methods")
    if any(word in title_lower for word in ["longitudinal", "trajectory", "development"]):
        tags.append("Longitudinal Research")
        
    tag_list = "\n".join([f"- {tag}" for tag in tags])
    
    # Student leadership note
    student_note = ""
    if pub.get("student_led", False):
        student_note = "\n\n*Student-led research under Dr. Merrin's mentorship.*"
    
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
---{student_note}'''

    # Write to file
    index_file = pub_path / "index.md"
    with open(index_file, 'w') as f:
        f.write(content)
    
    print(f"Created: {pub_path}")
    return True

# Parse and create publications
publications = []
for line in publications_text.strip().split('\n\n'):
    if line.strip():
        pub = parse_publication(line.strip())
        publications.append(pub)

# Create publication folders
created_count = 0
for pub in publications:
    if create_publication_folder(pub):
        created_count += 1

print(f"Processed {len(publications)} publications, created {created_count} new folders")