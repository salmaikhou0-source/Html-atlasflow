import re, sys, json, concurrent.futures, urllib.request, ssl, collections
ctx = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=15, context=ctx) as r:
            return r.read(700000).decode("utf-8", "ignore")
    except Exception:
        return ""
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:ca|com|co|net|org|shop|store)\b")
POSTAL = re.compile(r"\b([ABCEGHJKLMNPRSTVXY])\d[ABCEGHJKLMNPRSTVWXYZ][ -]?\d[ABCEGHJKLMNPRSTVWXYZ]\d\b")
PROV = {"A":"NL","B":"NS","C":"PE","E":"NB","G":"QC","H":"QC","J":"QC","K":"ON","L":"ON","M":"ON","N":"ON","P":"ON","R":"MB","S":"SK","T":"AB","V":"BC","X":"NT","Y":"YT"}
GENERIC = re.compile(r"^(info|hello|hi|contact|support|help|care|customercare|customerservice|service|orders|order|shop|sales|team|mail|office|admin|inquiries|enquiries|questions|ask|wholesale|concierge|bonjour|cs|studio|eat|yes|psteam)\b", re.I)
def check(d):
    home = get(f"https://{d}/")
    pages = home
    for p in ["/pages/contact", "/pages/contact-us", "/contact", "/contact-us", "/pages/about", "/about"]:
        pages += get(f"https://{d}{p}")
    fr = bool(re.search(r'hreflang="fr|href="/fr[/"\-]|href="/fr-ca|lang="fr|>\s*Fran[cç]ais\s*<|>\s*FR\s*<', home, re.I))
    pcs = collections.Counter(PROV[m] for m in POSTAL.findall(re.sub(r"<[^>]+>", " ", pages)))
    quebec_words = len(re.findall(r"Montr[ée]al|Qu[ée]bec, ?QC|, QC\b|Laval, Q|Gatineau|Sherbrooke", pages))
    emails = sorted({e.lower() for e in EMAIL.findall(pages) if d.split(".")[-2] in e.lower() or True})
    emails = [e for e in emails if not re.search(r"(sentry|example|wixpress|shopify|domain\.|email\.com|u00|\.png|\.jpg|@2x|privacy@|legal@|careers@|jobs@|press@|media@)", e)]
    own = [e for e in emails if e.split("@")[1].split(".")[0] in d]
    generic = [e for e in own if GENERIC.match(e.split("@")[0])]
    nosolicit = bool(re.search(r"unsolicited|no solicitation|do not send (us )?(sales|marketing)", pages, re.I))
    return {"domain": d, "up": bool(home), "fr": fr, "prov": pcs.most_common(1)[0][0] if pcs else "", "qc_signals": quebec_words + pcs.get("QC", 0),
            "generic_email": generic[0] if generic else "", "nosolicit": nosolicit}
doms = open(sys.argv[1]).read().split()
with concurrent.futures.ThreadPoolExecutor(16) as ex:
    for r in ex.map(check, doms):
        print(json.dumps(r), flush=True)
