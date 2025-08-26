#!/usr/bin/env python3
"""
Complete and accurate publication creation script for Gabriel Merrin
Based on the comprehensive list provided with proper DOIs and formatting
"""

import os
import re
from pathlib import Path
import shutil

# Complete accurate list of all publications
publications_data = """
Merrin, G. J., Nickodem, K., Grant, N., Weerakoon, S., Holt, M., & Espelage, D. (accepted). CATAcode: A principled approach for coding check-all-that-apply demographic items. Advances in Methods and Practices in Psychological Science.

*Bi, K., Merrin, G. J., Li, T., Sun, X., Chai, Y., Lu, Z., Chen, M. S. (2025). Thinking critically about unmeasured confounding in non-experimental psychological research: A practical guide to computing and interpreting E-value. Advances in Methods and Practices in Psychological Science, 8(2), 1-21. https://doi.org/10.1177/25152459251326571

Holt, M. K., Merrin, G. J., Wyatt, O., Green, J. G., Gini, G., & Fogelman, P. (2025). Direct and witnessed bias-based harassment exposures among adolescents: Associations with functioning and the influence of protective factors. Violence and Victims, 1-43. https://doi.org/10.1891/VV-2023-0027

Wang, J. H., Merrin, G. J., Wang, X., Liu, Q., & Kiefer, S. M. (2025). Co-occurring early adolescent ACEs and associations with later peer relationships. Journal of Youth and Adolescence, 54, 1827-1844. https://doi.org/10.1007/s10964-025-02157-0

Lawrence, T. I., Merrin, G. J., & Mcfield, A. A. (2025). Family violence and adolescent aggressive behavior: The direct and indirect effects of depression and substance use. International Journal of Mental Health and Addiction, 23, 1-14. https://doi.org/10.1007/s11469-022-00971-2

*Fusco, N. V., Holt, M. K., Merrin, G. J., & Green, J. G. (2025). Social-emotional functioning among bias-based bullies, victims, and bully-victims. School Psychology, 40(3), 397-403. https://doi.org/10.1037/spq0000620

Heerde, J. A., Bailey, J. A., Merrin, G. J., Raniti, M., Patton, G. C., Toumbourou, J. W., & Sawyer, S. M. (2025). School suspension as a predictor of young adult homelessness: The International Youth Development Study. Journal of Prevention, 46, 467-485. https://doi.org/10.1007/s10935-025-00829-y

Le, V. T., Bailey, J. A., Heerde, J. A., Merrin, G. J., Batmaz, E. A., Kelly, A. B., & Toumbourou, J. W. (2025). The roles of alcohol availability, overserving, and enforcement in recreational and social settings on alcohol misuse and harms: A comparison of Australia and the United States. Journal of Studies on Alcohol and Drugs, 86(3), 340–348. https://doi.org/10.15288/jsad.24-00036

Parodi, K. B., Holt, M. K., Aradhya, P., Green, J. G., & Merrin, G. J. (2025). A longitudinal analysis of risk and protective factors of bias-based bullying victimization among adolescents. Journal of Interpersonal Violence, 1-25. https://doi.org/10.1177/08862605251318276

*Marsico, C., *Wyatt, O., Parodi, K. B., Holt, M. K., Green, J. G., & Merrin, G. J. (2025). Longitudinal associations between witnessing bias-based harassment and mental health functioning. Journal of School Violence, 1-15. https://doi.org/10.1080/15388220.2025.2524335

Razza, R. A., Liu, Q., Feng, R., Hao, X., Kirkman, K. A., & Merrin, G. J. (2025). Cultivating adolescents' self-compassion through mindfulness: The role of self-regulation at both the individual- and classroom-level. Contemporary School Psychology 1-12. https://doi.org/10.1007/s40688-025-00548-5

*Bi, K., Chen, M. S., Zhang, C., Li, T., Liu, Y., Chen, J., Chen, H., Xie, Z., Merrin, G. J., & Yip, P. (in press). Day-to-day dynamic coupling of affective symptomatology in Chinese mother-adolescent and father-adolescent dyads. Clinical Psychological Science.

Merrin, G. J., Bailey, J. A., Kelly, A. B., Le, V. T., Heerde, J. A., Doery, E., Batmaz, E. A., & Toumbourou, J. W. (2024). Continuity and change in substance use patterns during the transition from adolescence to young adulthood: Examining changes in social roles. International Journal of Mental Health and Addiction 1-23. https://doi.org/10.1007/s11469-024-01342-9

Merrin, G. J., Wang, J. H., Kiefer, S. M., Jackson, J. L., Pascarella, L. A., Huckaby, P. L., Blake, C. L., Gomez, M. D., & Smith, N. D. W. (2024). Adverse childhood experiences and bullying during adolescence: A systematic literature review of two decades. Adolescent Research Review, 9, 513-541. https://doi.org/10.1007/s40894-023-00229-5

Wang, J. H., Merrin, G. J., Kiefer, S. M., Jackson, J. L., Huckaby, P. L., Pascarella, L. A., Blake, C. L., Gomez, M. D., & Smith, N. D. W. (2024). Peer relations of adolescents with adverse childhood experiences: A systematic review of two decades. Adolescent Research Review, 9, 477-512. https://doi.org/10.1007/s40894-023-00226-8

Zhang, X., Merrin, G. J., & Slavich, G. M. (2024). Adverse childhood experiences and emotion dysregulation phenotypes: An intersectional analysis of race/ethnicity and gender in a nationally representative U.S. sample. Child Abuse & Neglect, 158, 1-16. https://doi.org/10.1016/j.chiabu.2024.107129

Grant, N., Merrin, G. J., April, K., April-Sandars, A. K., Arora, I., & Gordon, D. (2024). A prospective study of sexual risk patterns associated with delinquency and justice involvement among child welfare system-involved adolescent males. Perspectives on Sexual and Reproductive Health, 56, 30-40. https://doi.org/10.1111/psrh.12255

*Robillard, C. L., Merrin, G. J., Legg, N. K., Ames, M. E., & Turner, B. J. (2024). Different self-damaging behaviors, similar motives? Testing measurement invariance of motives for nonsucidal self-injury, disordered eating, and substance misuse. British Journal of Clinical Psychology, 63, 394-415. https://doi.org/10.1111/bjc.12467

*Liu, Q., Merrin, G. J., Vasilenko, S. A., & Razza, R. A. (2024). Continuity and change in early material hardship domains on the development of children's behavioral self-regulation in middle childhood. Children and Youth Services Review, 167, 1-12. https://doi.org/10.1016/j.childyouth.2024.107995

*Liu, Q., Merrin, G. J., & Razza, R. A. (2024). Reciprocal associations between parenting behaviors and children's self-regulation during the transition from early to middle childhood. Journal of Child and Family Studies, 33, 1602-1617. https://doi.org/10.1007/s10826-023-02703-z

Green, J. G., Ramirez, M., Merrin, G. J., & Holt, M. K. (2024). Bias-based harassment among U.S. adolescents. School Mental Health, 16, 343-353. https://doi.org/10.1007/s12310-024-09648-8

*Li, T., Wang, Z., Merrin, G. J., Wan, S., Bi, K., Quintero, M., & Song, S. (2024). The joint operations of teacher-student and peer relationships on classroom engagement among low-achieving elementary students: A longitudinal multilevel study. Journal of Contemporary Educational Psychology, 77, 1-14. https://doi.org/10.1016/j.cedpsych.2024.102258

*Bi, K., Li, T., Merrin, G. J., Zhang, C., Wang, Y., Xiao, Y., & Chen, M. S. (2024). Are there reciprocal interplays among Chinese adolescents', fathers', and mothers' depression at the within-family level? A family systems perspective. Journal of Psychopathology and Clinical Science, 133(2), 140–154. https://doi.org/10.1037/abn0000883

*Fairclough, J., *Abd-Elmonem, M., Merrin, G. J., Hong, J. S., & Voisin, D. R. (2024). Religiosity and associations with substance use and delinquency among urban African American adolescents. Journal of Religion and Health, 63, 531-550. https://doi.org/10.1007/s10943-023-01916-2

*Liu, Q., Razza, R. A., Zhang, Y., & Merrin, G. J. (2024). Differential growth trajectories of behavioral self-regulation from early childhood to adolescence: Implications for youth domain-general and school-specific outcomes. Applied Developmental Science, 1-21. https://doi.org/10.1080/10888691.2024.2405578

Bailey, J. A., Le, V. T., McMorris, B. J., Merrin, G. J., Heerde, J. A., Batmaz, E. A., & Toumbourou, J. W. (2024). Longitudinal associations between adult-supervised drinking during adolescence and alcohol misuse from ages 25–31 years: A comparison of Australia and the United States. Addictive Behaviors, 153, 1-6. https://doi.org/10.1016/j.addbeh.2024.107984

*Liu, Q., Razza, R. A., Vasilenko, S. A., & Merrin, G. J. (2024). Associations between early material hardship and behavioral self-regulation development across childhood: A person-centered approach. Research in Human Development, 20, 183-207. https://doi.org/10.1080/15427609.2024.2310449

Espelage, D. L., Kuehl, T., Wyman, P. A., Nickodem, K., Mintz, S., Valido, A.,  Robinson, L. E., Merrin, G. J., Hoagland, K., Schmeelk-Cone, K., LoMurray, S., Woolweaver, A. B., Ingram, K. M., & Rulison, K. (2024). An RCT of Sources of Strength high school primary prevention program on sexual violence perpetration and victimization and dismissiveness of sexual harassment. School Psychology Review, 53(6), 649-667. https://doi.org/10.1080/2372966X.2022.2164460

Merrin, G. J. & Lowe, S. (2023). Who benefits from universal SEL programming?: Assessment of Second Step© using a growth mixture modeling approach. Journal of School Mental Health, 15, 177-189. https://doi.org/10.1007/s12310-022-09542-1

*Rivas-Koehl, M. M., Merrin, G. J., & Espelage, D. L. (2023). Assessing the longitudinal measurement invariance of the conflict in adolescent dating relationship inventory (CADRI) across heterosexual and sexual minority adolescents in the United States. Psychology of Violence, 13(1), 84-92. https://doi.org/10.1037/vio0000452

Leadbeater, B. J., Merrin, G. J., Contreras, A., & Ames, M. E. (2023). Trajectories of oppositional defiant disorder severity from adolescence to young adulthood and substance use, mental health, and behavioral problems. Journal of the Canadian Academy of Child and Adolescent Psychiatry, 32(4), 224–235. PMID: 38034412

Wang, X., Liu. Q., Merrin, G. J., Keller, A., Dalhee, Y., & Henderson, A. (2023). Harsh parenting among veterans: parents' military-related PTSD, mentalization, and pre-military trauma. Frontiers in Psychology, 14, 1-14. https://doi.org/10.3389/fpsyg.2023.1283801

Ames, M. E., Robillard, C. L., Ryan, J. E. H., Merrin, G. J., & Turner, B. J. (2023). Reciprocal associations between physical activity, self-concept, somatic symptoms, and depression from adolescence to young adulthood: Disaggregating within- and between-person effects. Mental Health and Physical Activity, 23, 1-9. https://doi.org/10.1016/j.mhpa.2023.100513

Merrin, G. J., Leadbeater, B. J., Sturgess, C. M. B., Ames, M. E., & Thompson, K. (2022). Predictors of early-onset cannabis use in adolescence and risks for substance use disorder symptoms in young adulthood. Journal of Drug Issues, 52(2), 182-206. https://doi.org/10.1177/00220426211049356

Valido, A., Merrin, G. J., Espelage, D. L., Robinson, L. E., Nickodem, K., Ingram, K. M., El Sheikh, A. J., Torgal, C., & Fairclough, J. (2022). Social-ecological predictors of homophobic name-calling perpetration and victimization among early adolescents. Journal of Early Adolescence, 42(9), 1115-1151. https://doi.org/10.1177/02724316211002271

Forber-Pratt, A. J., Price, L. R., Merrin, G. J., Hanebutt, R. A., & Fairclough, J. A.  (2022). Psychometric properties of the Disability Identity Development Scale: Confirmatory factor and bifactor analyses. Rehabilitation Psychology, 67(2), 120-127. https://doi.org/10.1037/rep0000445

Leadbeater, B. J., Sukhawathanakul, P., Rush, J., Merrin, G. J., & Lewis, N. (2022). Examining the effectiveness of the WITS programs in the context of variability in trajectories of child development. Prevention Science 23, 538-551. https://doi.org/10.1007/s11121-021-01327-3

Espelage, D. L., Ingram, K. M., Hong, J. S., & Merrin, G. J. (2022). Bullying as a developmental precursor to sexual violence throughout adolescence: Decade in review. Trauma, Violence, & Abuse, 23(4), 1358-1370. https://doi.org/10.1177/15248380211043811

Forber-Pratt, A. J., Merrin, G. J., & Espelage, D. L. (2021). Exploring the intersections of disability, race and gender on student outcomes in High School. Remedial and Special Education 42(5), 290-303. https://doi.org/10.1177/0741932520941201

Valido, A., Ingram, K. M., Espelage, D. L., Torgal, C., Merrin, G. J., & Davis, J. P. (2021). Intrafamilial violence and verbal and physical aggression among early adolescents: Moderating role of school sense of belonging. Journal of Family Violence 36, 87-98. https://doi.org/10.1007/s10896-020-00142-8

Merrin, G. J., Davis, J. P., Ingram, K. M., & Espelage, D. L. (2020). Examining social-ecological predictors of youth gang entry among serious juvenile offenders: A survival analysis. American Journal of Orthopsychiatry 90(5), 623-632. https://doi.org/10.1037/ort0000491

Merrin, G. J., Ames, M., Sturgess, C. M. B., & Leadbeater, B. J. (2020). Disruption of transitions in high-risk substance use from adolescence to young adulthood: School, employment, and romantic relationship factors. Substance Use and Misuse 55(7), 1129-1137. https://doi.org/10.1080/10826084.2020.1729200

Forber-Pratt, A., Merrin, G. J., Mueller, C. O., Price, L. R., & Kettrey, H. H. (2020). Initial factor exploration of disability identity. Rehabilitation Psychology 65(1), 1-10. https://doi.org/10.1037/rep0000308

Davis, J. P., Ingram, K. M., Merrin, G. J., & Espelage, D. L. (2020). Exposure to parental and community violence and the relationship to bullying perpetration and victimization among early adolescents: A parallel process growth mixture latent transition analysis. Scandinavian Journal of Psychology, 61, 77-89. https://doi.org/10.1111/sjop.12493

Ames, M. E., Leadbeater, B. J., Merrin, G. J., & Thompson, K. (2020). Patterns of marijuana use and physical health indicators among Canadian Youth. International Journal of Psychology, 55(1), 1-12. https://doi.org/10.1002/ijop.12549

Ingram, K. M., Espelage, D. L., Davis, J. P., & Merrin, G. J. (2020). Family violence, sibling, and peer aggression during adolescence: Associations with behavioral health outcomes. Frontiers in Psychiatry 11(26), 1-14. https://doi.org/10.3389/fpsyt.2020.00026

Green, J. G., Holt, M. K., Oblath, R., Robinson, E., Story, K., Merrin, G. J. (2020). Engaging professional sports to reduce bullying: An evaluation of the Boston vs. Bullies program. Journal of School Violence, 19(3), 389-405. https://doi.org/10.1080/15388220.2019.1709849

Merrin, G. J., Davis, J. P., Berry, D., & Espelage, D. L. (2019). Developmental changes in deviant and violent behavior from early to late adolescence: Associations with parental monitoring and peer deviance. Psychology of Violence, 9(2), 196-208. http://dx.doi.org/10.1037/vio0000207

Grant, N. J., Merrin, G. J., King, M. T., & Espelage, D. L. (2019). Examining within-person and between-person associations of family violence and peer deviance on bullying perpetration among middle school students. Psychology of Violence, 9(1), 18 - 27. http://doi.org/10.1037/vio0000210.

Davis, J. P., Merrin, G. J., Ingram, K. M., Espelage, D. L., Valido, A., & El Sheikh, A. J. (2019). Examining pathways between bully victimization, depression, & school belonging among early adolescents. Journal of Child and Family Studies, 28(9), 2365-2378. https://doi.org/10.1007/s10826-019-01340-9

Hatchel, T., Merrin, G. J., & Espelage, D. L. (2019). Peer victimization and suicidality among LGBTQ youth: The protective roles of self-compassion, school belonging, and parental support. Journal of LGBT Youth, 16(2), 134-156. https://doi.org/10.1080/19361653.2018.1543036

Peguero, A. A., Merrin, G. J., Hong, J. S., & Johnson, K. R. (2019). School disorder and dropping out: The intersection of gender, race, and ethnicity. Youth and Society, 51(2), 193–218. https://doi.org/10.1177/0044118X16668059.

Ames, M. E., Leadbeater, B. J., Merrin, G. J., & Sturgess, C. M. B. (2019). Adolescent patterns of peer victimization: Concurrent and longitudinal health correlates. Journal of Applied Biobehavioral Research, 24, 1-21. https://doi.org/10.1111/jabr.12151

Ingram, K. M., Espelage, D. L., Merrin, G. J., Valido, A., Heinhorst, J., & Joyce, M. (2019). Evaluation of a virtual reality enhanced bullying prevention curriculum pilot trial. Journal of Adolescence 71, 72-83. https://doi.org/10.1016/j.adolescence.2018.12.006

Ingram, K. M., Davis, J. P., Espelage, D. L., Hatchel, T., Merrin, G. J., Valido, A., & Torgal, C. (2019). Longitudinal associations between toxic masculinity and bystander willingness to intervene in bullying among middle school boys. Journal of School Psychology, 77, 139-151. https://doi.org/10.1016/j.jsp.2019.10.007

Jones, A. E., Espelage, D. L., Valido, A., Ingram, K. M., & Merrin, G. J. (2019). Examining classes of bully perpetration among Latinx high school students and associations with substance use and mental health. International Journal of Bullying Prevention, 1(3), 170-179. https://doi.org/10.1007/s42380-019-00028-4

Thompson, K., Leadbeater, B. J., Ames, M. E., & Merrin, G. J. (2019). Associations between marijuana use trajectories and educational and occupational success in adulthood. Prevention Science 20(2), 257-269. https://doi.org/10.1007/s11121-018-0904-7

Merrin, G. J., Thompson, K., & Leadbeater, B. J. (2018). Transitions in the use of multiple substances from adolescence to young adulthood. Drug and Alcohol Dependence 189, 147-153. https://doi.org/10.1016/j.drugalcdep.2018.05.015

Merrin, G. J., & Leadbeater, B. J. (2018). Do adolescent patterns of polysubstance use predict differential use of substances in young adulthood? Journal of Substance Use and Misuse 53(13), 2112 - 2124. https://doi.org/10.1080/10826084.2018.1455702

Merrin, G. J., de la Haye, K., Espelage, D. L., Ewing, B., Tucker, J. S., Hoover, M., & Green, H. D. (2018). The co-evolution of bullying perpetration, homophobic teasing, and a school friendship network. Journal of Youth and Adolescence, 47(3), 601-618. https://doi.org/10.1007/s10964-017-0783-4.

Merrin, G. J., Espelage, D. L., & Hong, J. S. (2018). Applying the social-ecological framework to understand the associations of bullying perpetration among high school students: A multilevel analysis. Psychology of Violence, 8(1), 43-56. http://dx.doi.org/10.1037/vio0000084.

Espelage, D. L., Merrin, G. J., Hong, J. S., & Resko, S. M. (2018). Applying social cognitive and social information processing theory to explore relational aggression across early adolescence: A within- and between-person analysis. Journal of Youth and Adolescence 47(11), 2401-2413. https://doi.org/10.1007/s10964-018-0910-x

Espelage, D. L., Merrin, G. J., & Hatchel, T. (2018). Peer victimization and dating violence among LGBTQ youth: The impact of school violence and crime on mental health outcomes. Journal of Youth Violence and Juvenile Justice 16(2), 156-173. https://doi.org/10.1177/1541204016680408.

King, M. T., Merrin, G. J., Espelage, D. L., Grant., N. J., & Bub, K. L. (2018). Victimization, suicidal ideation, and intersectionality among LGBQ youth and students with disabilities. Exceptional Children, 84(2), 141-158. https://doi.org/10.1177/0014402917736261.

Thompson, K., Merrin, G. J, Ames, M. E., & Leadbeater, B. J. (2018). Trajectories of marijuana use in Canadian youth and association with substance use, mental health, and behavioral problems in adolescence and young adulthood. Canadian Journal of Behavioural Sciences 50(1), 17-28. http://dx.doi.org/10.1037/cbs0000090.

Dumas, T. M., Davis, J. P., Merrin, G. J., Puccia, M., & Blustein, D. (2018). If you're high status and you know it: Teasing apart the within- and between-person effects of peer-nominated and self-reported status in the drinking group on alcohol-related outcomes. Psychology of Addictive Behaviors, 32(3), 327-337. https://doi.org/10.1037/adb0000352.

Davis, J. P., Dumas, T. M., Merrin, G. J., Espelage, D. L., Tan, K., Madden, D., & Hong, J. S. (2018). Examining the pathways between bully victimization, depression, academic achievement, and problematic drinking in adolescence. Psychology of Addictive Behaviors, 32(6), 605-616. http://dx.doi.org/10.1037/adb0000394

Espelage, D. L., Hong, J. S., Merrin, G. J., Davis, J. P., Rose, C. A., & Little, T. D. (2018). A longitudinal examination of homophobic name-calling perpetration in middle school: Bullying, traditional masculinity, and sexual harassment as predictors. Psychology of Violence, 8(1), 57-66. http://dx.doi.org/10.1037/vio0000083.

Leadbeater, B. J., Thompson, K., Sukhawathanakul, P., & Merrin, G. J. (2018). How program users enhance fidelity: Implementing the WITS programs in rural Canadian elementary schools. Prevention Science 19(8), 1066-1078. https://doi.org/10.1007/s11121-018-0948-8

Davis, J. P., Dumas, T. M., Berey, B., Merrin, G. J., Tan, K., Madden, D. R. (2018). Poly-victimization and trajectories of binge drinking from adolescence to young adulthood among serious juvenile offenders. Drug and Alcohol Dependence, 186, 29 - 35. https://doi.org/10.1016/j.drugalcdep.2018.01.006.

Davis, J. P., Dumas, T. M., Berey, B. L., Merrin, G. J., Robinson-Cimpian, J., & Roberts, B. W. (2017). Effect of victimization on impulse control and binge drinking among juvenile delinquents from adolescence to young adulthood. Journal of Youth and Adolescence, 46(7), 1515-1532. https://doi.org/10.1007/s10964-017-0676-6.

Merrin, G. J., Davis, J. P., Berry, D., D'Amico, E. J., & Dumas, T. M. (2016). The longitudinal associations between substance use, crime, and social risk among emerging adults: A longitudinal within and between-person latent variables analysis. Drug and Alcohol Dependence, 165, 71-78. https://doi.org/10.1016/j.drugalcdep.2016.05.009.

Hong, J. S., Merrin, G. J., Peguero, A. A., Gonzalez-Prendes, A. A., & Lee, N. Y. (2016). Exploring the social-ecological determinants of physical fighting in U.S. schools: What about youth in immigrant families? Child and Youth Care Forum, 45(2), 279-299. https://doi.org/10.1007/s10566-015-9330-1.

Davis, J. P., Merrin, G. J., Berry, D. J., Dumas, T. M., Hong, J. S., & Smith, D. C. (2016). Examining within-person and between-person effects of victimization and social risk on cannabis use among emerging adults in substance-use treatment. Psychology of Addictive Behaviors, 30(1), 52-63. http://dx.doi.org/10.1037/adb0000121.

Hong, J. S., Merrin, G. J., Crosby, S., Hernandez-Jozefowicz, D. M., Lee, J. M., & Allen-Meares, P. (2016). Individual and contextual factors associated with immigrant youth's feeling unsafe in school: A social-ecological analysis. Journal of Immigrant and Minority Health, 18(5), 996-1006. https://doi.org/10.1007/s10903-015-0242-9.

Davis, J. P., Dumas, T. M., Wagner, E. F., & Merrin, G. J. (2016). Social ecological determinants of substance use treatment entry among serious juvenile offenders from adolescences through emerging adulthood. Journal of Substance Abuse Treatment, 71, 8-15. https://doi.org/10.1016/j.jsat.2016.08.004.

Merrin, G. J., Hong, J. S., & Espelage, D. L. (2015). Are the risk and protective factors similar for gang-involved, pressured-to-join, and non-gang involved youth? A social-ecological analysis. American Journal of Orthopsychiatry, 85(6), 522-535. http://dx.doi.org/10.1037/ort0000094.
"""

def parse_publication(pub_text):
    """Parse a single publication entry"""
    pub_text = pub_text.strip()
    if not pub_text:
        return None
    
    # Check if student-led (starts with *)
    student_led = pub_text.startswith('*')
    if student_led:
        pub_text = pub_text[1:].strip()
    
    # Extract DOI if present
    doi_match = re.search(r'https://doi\.org/(.*?)(?:\s|$)', pub_text)
    doi = doi_match.group(1) if doi_match else ""
    if doi_match:
        pub_text = pub_text.replace(doi_match.group(0), "").strip()
    
    # Extract PMID if present
    pmid_match = re.search(r'PMID:\s*(\d+)', pub_text)
    pmid = pmid_match.group(1) if pmid_match else ""
    if pmid_match:
        pub_text = pub_text.replace(pmid_match.group(0), "").strip()
    
    # Split into parts
    # Pattern: Authors (Year). Title. Journal, Volume(Issue), Pages.
    year_match = re.search(r'\((\d{4}|accepted|in press)\)', pub_text)
    if not year_match:
        return None
    
    year = year_match.group(1)
    year_pos = year_match.end()
    
    authors = pub_text[:year_match.start()].strip()
    if authors.endswith(' '):
        authors = authors.strip()
    
    remainder = pub_text[year_pos:].strip()
    if remainder.startswith('.'):
        remainder = remainder[1:].strip()
    
    # Find the journal (after first period)
    parts = remainder.split('.', 1)
    if len(parts) < 2:
        title = remainder
        journal = ""
        citation = ""
    else:
        title = parts[0].strip()
        journal_and_citation = parts[1].strip()
        
        # Split journal from citation info
        journal_parts = journal_and_citation.split(',', 1)
        journal = journal_parts[0].strip()
        citation = journal_parts[1].strip() if len(journal_parts) > 1 else ""
    
    # Determine if this is a featured publication based on key topics
    featured_keywords = [
        'CATAcode', 'E-value', 'systematic review', 'systematic literature review',
        'Second Step', 'SEL programming', 'substance use patterns', 'ACEs'
    ]
    featured = any(keyword.lower() in title.lower() for keyword in featured_keywords)
    
    # Parse citation details
    volume = ""
    issue = ""
    pages = ""
    
    if citation:
        # Extract volume and issue: "9, 513-541" or "133(2), 140-154"
        volume_match = re.search(r'(\d+)(?:\((\d+)\))?,?\s*([\d\-–]+)', citation)
        if volume_match:
            volume = volume_match.group(1)
            issue = volume_match.group(2) or ""
            pages = volume_match.group(3)
    
    return {
        'authors': authors,
        'title': title,
        'journal': journal,
        'year': year,
        'volume': volume,
        'issue': issue,
        'pages': pages,
        'doi': doi,
        'pmid': pmid,
        'student_led': student_led,
        'featured': featured,
        'citation': citation
    }

def create_slug(authors, title, year):
    """Create URL-friendly slug"""
    # Get first author's last name
    first_author = authors.split(',')[0].strip()
    # Remove asterisks
    first_author = re.sub(r'[*]', '', first_author)
    
    # Extract last name
    if ',' in first_author:
        last_name = first_author.split(',')[0].strip()
    else:
        parts = first_author.split()
        last_name = parts[-1] if parts else first_author
    
    # Create slug with meaningful identifier
    if 'merrin' in authors.lower():
        # Find Merrin's position
        if authors.lower().startswith('merrin'):
            slug = f"merrin-{year}"
        else:
            slug = f"{last_name.lower()}-merrin-{year}"
    else:
        slug = f"{last_name.lower()}-{year}"
    
    # Add distinguishing word for duplicates
    title_words = re.findall(r'\b\w{4,}\b', title.lower())
    if title_words:
        key_word = title_words[0][:8]  # First significant word, max 8 chars
        slug += f"-{key_word}"
    
    # Clean up slug
    slug = re.sub(r'[^\w\-]', '', slug)
    slug = re.sub(r'-+', '-', slug)
    
    return slug

def format_authors_yaml(authors):
    """Format authors for YAML frontmatter"""
    # Clean and split authors
    clean_authors = re.sub(r'[*]', '', authors)
    
    # Handle '&' by replacing with comma
    clean_authors = clean_authors.replace(' & ', ', ')
    clean_authors = clean_authors.replace(' &', ',')
    
    # Split by comma and clean up
    author_list = []
    for author in clean_authors.split(','):
        author = author.strip()
        if author and author not in author_list:  # Avoid duplicates
            author_list.append(author)
    
    # Format for YAML (keep full names together)
    formatted = []
    for author in author_list:
        if author.strip():
            formatted.append(f'  - "{author.strip()}"')
    
    return '\n'.join(formatted)

def create_publication_file(pub, pub_dir):
    """Create the index.md file for a publication"""
    
    # Create abstract
    abstract = f"This study examines {pub['title'].lower()}."
    
    # Format publication info
    pub_info = f"*{pub['journal']}*"
    if pub['volume']:
        if pub['issue']:
            pub_info += f", {pub['volume']}({pub['issue']})"
        else:
            pub_info += f", {pub['volume']}"
    if pub['pages']:
        pub_info += f", {pub['pages']}"
    
    # Determine tags
    tags = ["Adolescent Development"]
    if pub['student_led']:
        tags.append("Student Research")
    if 'substance' in pub['title'].lower() or 'alcohol' in pub['title'].lower():
        tags.append("Substance Use")
    if 'bullying' in pub['title'].lower() or 'victimization' in pub['title'].lower():
        tags.append("Bullying")
    if 'ACE' in pub['title'] or 'adverse childhood' in pub['title'].lower():
        tags.append("Adverse Childhood Experiences")
    if any(word in pub['title'].lower() for word in ['methodology', 'method', 'measurement', 'psychometric']):
        tags.append("Methodology")
    
    tag_yaml = '\n'.join([f"- {tag}" for tag in tags])
    
    # Create title with student notation if needed
    display_title = pub['title']
    if pub['student_led']:
        display_title += " (Student-led research)"
    
    # Create content
    content = f'''---
title: "{display_title}"
authors:
{format_authors_yaml(pub['authors'])}
date: "{pub['year']}-01-01"
doi: "{pub['doi']}"

# Publication type
publication_types: ["2"]

# Publication name and optional abbreviated publication name
publication: "{pub_info}"
publication_short: "{pub['journal']}"

abstract: "{abstract}"

# Summary
summary: ""

tags:
{tag_yaml}

# Display this page in the Featured widget?
featured: {'true' if pub['featured'] else 'false'}

# Custom links
links:
{('- name: "DOI"' if pub['doi'] else '')}
{(f'  url: "https://doi.org/{pub["doi"]}"' if pub['doi'] else '')}
{('- name: "PubMed"' if pub['pmid'] else '')}
{(f'  url: "https://pubmed.ncbi.nlm.nih.gov/{pub["pmid"]}/"' if pub['pmid'] else '')}

url_pdf: ""
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""

# Featured image
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects
projects: []

# Slides
slides: ""
---

{abstract}

{f"**Student-led research** - This publication was led by a student researcher." if pub['student_led'] else ""}

{f"**DOI:** https://doi.org/{pub['doi']}" if pub['doi'] else ""}
{f"**PubMed ID:** {pub['pmid']}" if pub['pmid'] else ""}
'''
    
    # Write the file
    with open(pub_dir / "index.md", 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """Process all publications"""
    
    # First, backup existing publications
    pub_dir = Path("/home/user/webapp/content/publication")
    backup_dir = Path("/home/user/webapp/publications_backup")
    
    if pub_dir.exists() and not backup_dir.exists():
        print("Creating backup of existing publications...")
        shutil.copytree(pub_dir, backup_dir)
    
    # Remove existing publications (except _index.md)
    if pub_dir.exists():
        for item in pub_dir.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
                print(f"Removed: {item}")
    
    # Parse publications
    publications = []
    pub_entries = [p.strip() for p in publications_data.split('\n\n') if p.strip()]
    
    print(f"Processing {len(pub_entries)} publications...")
    
    for entry in pub_entries:
        pub = parse_publication(entry)
        if pub:
            publications.append(pub)
        else:
            print(f"Failed to parse: {entry[:100]}...")
    
    print(f"Successfully parsed {len(publications)} publications")
    
    # Create publication files
    created = 0
    featured_count = 0
    
    pub_dir.mkdir(exist_ok=True)
    
    for pub in publications:
        slug = create_slug(pub['authors'], pub['title'], pub['year'])
        pub_folder = pub_dir / slug
        
        # Handle duplicate slugs
        counter = 1
        original_slug = slug
        while pub_folder.exists():
            slug = f"{original_slug}-{counter}"
            pub_folder = pub_dir / slug
            counter += 1
        
        pub_folder.mkdir(exist_ok=True)
        create_publication_file(pub, pub_folder)
        
        print(f"Created: {slug} ({'FEATURED' if pub['featured'] else 'regular'})")
        created += 1
        
        if pub['featured']:
            featured_count += 1
    
    print(f"\n✅ Successfully created {created} publications")
    print(f"📌 Featured publications: {featured_count}")
    print(f"👥 Student-led publications: {sum(1 for p in publications if p['student_led'])}")

if __name__ == "__main__":
    main()