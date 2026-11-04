# gabrieljmerrin.rbind.io

Personal academic website for **Dr. Gabriel J. Merrin**, Associate Professor & Zeta Psi
Endowed Faculty Fellow, Department of Human Development and Family Science, Syracuse University.

Built with [Hugo](https://gohugo.io/) + the `hugo-academic` theme, and deployed automatically
by **Netlify** whenever `master` changes on GitHub.

---

## Repository layout

| Path | What it is |
|------|------------|
| `config.toml`, `config/_default/` | Site settings, menus, contact info (`params.toml`) |
| `content/authors/admin/_index.md` | **Biography** shown on the home page (role, interests, education, bio text) |
| `content/home/*.md` | Home-page sections (About, Skills, Experience, MAP Lab blurb, Gallery, Featured publications, Contact) |
| `content/lab/_index.md` | The **MAP Lab** page |
| `content/publication/<slug>/index.md` | One folder per publication (86 peer-reviewed articles) |
| `static/files/cv.pdf` | The downloadable CV linked from the nav bar |
| `static/files/*.pdf` | Author-copy PDFs for selected publications |
| `static/img/` | Images (avatar, headers, logos) |
| `assets/scss/custom.scss`, `layouts/partials/` | Custom styling / head & JS overrides |
| `themes/hugo-academic/` | The theme (vendored; do not edit) |
| `netlify.toml` | Netlify build command and pinned Hugo version |

`public/` and `resources/_gen/` are build output and are **git-ignored** -- Netlify regenerates
them on every deploy.

---

## Common updates

| To change... | Edit... |
|--------------|---------|
| Bio, title, research interests, awards | `content/authors/admin/_index.md` |
| Positions / experience timeline | `content/home/experience.md` |
| MAP Lab page (projects, mentorship, funding) | `content/lab/_index.md` |
| Contact info / address | `config/_default/params.toml` |
| Nav menu | `config/_default/menus.toml` |
| CV download | replace `static/files/cv.pdf` |

### Adding a publication

1. Copy an existing folder, e.g. `content/publication/zhang-merrin-2026-state/`, to a new
   slug such as `content/publication/lastname-merrin-YYYY-keyword/`.
2. Edit `index.md`: `title`, `authors`, `date`, `doi`, `publication`, `abstract`, `tags`.
3. Append `(Student-led research)` to the title and add the `Student Research` tag for
   mentored student-led papers.
4. Set `featured: true` to pin it in the "Featured Publications" section on the home page
   (currently 7 are featured).

---

## Preview locally

**Option A - RStudio / blogdown** (what the `.Rproj` is for):

```r
blogdown::serve_site()      # or open 0-blog-down-serve-site.R and run it
```

**Option B - Hugo CLI** (needs Hugo *extended* 0.118.x, matching `netlify.toml`):

```bash
hugo server -D            # http://localhost:1313
```

---

## Publishing changes

Netlify watches the `master` branch. Anything merged to `master` goes live in ~1-2 minutes.

```bash
git checkout master
git pull origin master
# ...edit files...
git add -A
git commit -m "Update bio and add new publication"
git push origin master
```

Then check the deploy at <https://app.netlify.com/> (Site -> Deploys). If a build fails, the
log there shows the Hugo error.

---

## License

Theme and site scaffold: MIT (see `LICENSE`). Site content (c) Gabriel J. Merrin.
