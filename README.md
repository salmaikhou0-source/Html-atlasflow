# Bilingual Support Co. website

The public website for Bilingual Support Co., a Toronto company that answers customer emails and chats in English and French for other businesses.

It's plain HTML and CSS with no build step, so it can be hosted for free.

## Files

| File | What it is |
|---|---|
| `index.html` | English home page |
| `fr/index.html` | French (Canadian) home page |
| `privacy.html` | English privacy policy |
| `fr/confidentialite.html` | French privacy policy |
| `assets/styles.css` | All styles (colours, fonts, layout) |
| `assets/site.js` | Contact form, FR/EN ticket demo, settings |
| `assets/favicon.svg` | Logo icon |

## Put the site online for $0 (GitHub Pages)

1. On GitHub, open this repository, then go to **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Choose the branch that holds these files (`main` once merged) and the `/ (root)` folder, then click **Save**.
4. After a minute or two, the site is live at `https://<your-github-username>.github.io/<repository-name>/`.

The repository can be renamed (for example to `bilingual-support-co`) under **Settings → General**. The web address changes with it.

## Contact form (free)

The form sends messages to the business inbox through FormSubmit (formsubmit.co), which is free and needs no account. The inbox address is `CONTACT_EMAIL` at the top of `assets/site.js`.

The first message ever sent triggers an "Activate Form" email from FormSubmit to that inbox. Click the button in it once; after that, every message arrives normally. If you ever change the address, activate it again the same way.

## Change prices or text

Prices appear on both home pages. Change them in `index.html` (English format: `$1,900`) and in `fr/index.html` (French format: `1 900 $`).

## Before launch

- [x] Create the business email and fill in `CONTACT_EMAIL`
- [ ] Activate the form (click the FormSubmit email once)
- [ ] Add the founder's name, photo and LinkedIn in the About section (both languages)
- [ ] Register the business name "Bilingual Support Co." in Ontario
- [ ] Later: buy `bilingualsupport.ca` and point it at GitHub Pages
