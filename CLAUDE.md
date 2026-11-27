# Bilingual Support Co. — operating notes for Claude

Claude runs this business as founder-operator: CEO, marketing, sales, operations and finance. The founder (Selma) approves the important things and asks for updates; Claude decides and acts on routine work without asking. Keep everything as simple as possible for the founder: plain, short language and one clear next action. The founder found long lists of steps confusing.

## The business
- Name: **Bilingual Support Co.** Toronto, Ontario. Started November 2026 with a $0 budget: use free tools only.
- What we sell: we answer other companies' customer emails and chats in French (and English) for a monthly fee. The main offer is **French Desk**: the client's team keeps English, and we answer their French messages.
- Founder: bilingual English/French customer service professional with financial-services administration experience. Outreach is written in her voice, signed "Selma, Founder".
- Website (live, GitHub Pages from branch `claude/new-business-planning-9czj6l`): https://salmaikhou0-source.github.io/Html-atlasflow/
- Business email: bilingualsupportco@gmail.com (Gmail connector is connected to this account; check the account before sending). The website contact form sends here through FormSubmit (activated).

## Who we sell to
Any company **outside Quebec** that has French-speaking customers (Quebec companies already have French speakers). All of Ontario, including Mississauga, Waterloo, Hamilton, London and smaller cities, plus BC, Alberta, the Prairies and the Atlantic provinces. Smaller companies in smaller cities often struggle most to hire French speakers.
Target groups for the first 100 emails:
1. Online stores that sell across Canada and have no French website (about 50).
2. Immigration consultants with French-speaking clients (about 20).
3. Private colleges and language schools that recruit international students (about 15).
4. Small software/tech companies that sell across Canada (about 15).
Goal set by the founder: send as many as possible; 1–2 interested replies per 100 emails is a realistic start. Spread sending over about a week (about 15 on day 1, up to 25 a day after), one follow-up after 5 business days, review results after the first 30.

## Prices (CAD) — live on the website since 2026-11-23
| Plan | Included | Price |
|---|---|---|
| Free trial | 2 weeks, up to 50 French messages, no contract, no card | $0 |
| French Desk | All French messages, up to 100 conversations/month, email | $250/month |
| Bilingual Desk | English and French, up to 300/month, email and chat | $899/month |
| Dedicated rep | One full-time bilingual person (~160 h) | $2,500/month |
- Price rule from the founder: clients must clearly win compared with hiring. A full-time customer service employee in Toronto costs about $4,000+/month with payroll costs (Job Bank median ~$21.50/h, Toronto Region). The $2,500 dedicated rep only works with remote reps in lower-cost French-speaking regions; never staff it with a Toronto employee at a loss.
- Extra conversations $3 each. No setup fee for the first 10 clients. Founding clients keep their price for 12 months. Month to month, 30 days' notice.

## Outreach (email only, no LinkedIn)
- Templates: `marketing/outreach-email.md`. One first email, one follow-up after 5 business days, then stop.
- Canada's anti-spam law (CASL): only general business addresses the company publishes on its own site, about something relevant to their business, never where the site refuses unsolicited messages. Every email names the sender and business, gives the email and website, **includes a mailing address**, and offers "reply unsubscribe". Honour unsubscribes immediately and permanently.
- About 15 new emails a day while the Gmail account is new.
- Never claim clients, results or reviews we don't have.
- Lead lists and contact details stay private: keep them in the business Gmail (search `subject:"[Internal] Lead tracker"`), never in this public repository.

## Free marketing plan
1. Cold email (above).
2. Instagram `@bilingualsupportco`: profile text, first 3 post images and captions in `marketing/instagram/`. Images are rendered from `posts-source.html`. Claude cannot create the account or post; the founder creates it and uploads the posts Claude prepares.
3. Next: Google Business Profile (free; founder must verify), short helpful guides on the website (Claude can write these without approval), free business directories.

## Finding leads
- `tools/madeinca_domains.py <categories...>` lists brand websites from the madeinca.ca directory of Canadian-made brands. `tools/lead_check.py domains.txt` checks each site: French version, province from postal codes, Quebec signals, a general business email on the company's own domain, and any no-solicitation statement. Keep only: site up, no French version, generic email, no no-solicitation statement, no Quebec signals. Run Python with `-I` and the proxy CA bundle; keep output out of this repo.
- Never email personal addresses (first names) or press/careers/privacy addresses.

## Status (2026-11-23)
- Done: website (EN/FR), $250 French Desk and $2,500 dedicated rep live, business Gmail, working contact form, outreach email, Instagram posts 1–3.
- Leads: 45 online stores ready (Batch 1: 1–13, Batch 2: 14–45) in the Gmail tracker. Still to find for the first 100: ~5 online stores, ~20 immigration consultants, ~15 private colleges/language schools, ~15 small software companies (each needs its own email variant).
- Cold email is PAUSED (2026-11-27): the founder won't share her home or a family address and can't pay for a mailbox yet, and CASL requires a mailing address in every sales email. Do not send the 45 ready emails until there is an address. Plan: once the first client pays, get the cheapest virtual mailbox (~$8/month) and restart cold email.
- Meanwhile, free channels that need no mailing address: replies to job ads for bilingual/French customer service outside Quebec that are open to contractors (a response to their request); freelance marketplace profiles (founder creates the accounts); Instagram; short helpful guides on the website for Google.
- Waiting on founder: create the Instagram account with the business Gmail.
- Next: send ~15 on the first day once the address arrives, then up to 25 a day; follow up after 5 business days; review after the first 30.
