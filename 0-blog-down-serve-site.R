# Local preview of the site with blogdown (run from RStudio with gjmerrin-blog.Rproj open)
#
# Most common updates:
#   Bio / interests / awards ...... content/authors/admin/_index.md
#   Experience timeline ........... content/home/experience.md
#   MAP Lab page .................. content/lab/_index.md
#   Contact info .................. config/_default/params.toml
#   Publications .................. content/publication/<slug>/index.md
#   CV download ................... static/files/cv.pdf
#
# See README.md for publishing instructions (push to master -> Netlify deploys).

blogdown::serve_site()
