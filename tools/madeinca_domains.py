import re, sys, json, urllib.request, ssl, concurrent.futures
ctx = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/124"}
def get(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=20, context=ctx) as r:
            return r.read().decode("utf-8", "ignore")
    except Exception:
        return ""
SKIP = r"madeinca|gmpg|facebook|instagram|twitter|pinterest|amazon|google|wp\.com|wordpress|gravatar|youtube|linkedin|tiktok|shareasale|etsy|x\.com|jetpack|w\.org|cloudflare|schema\.org|kraftheinz|postfoods|oceanspray|cowbell|perthbrewery|canada\.ca|gc\.ca"
posts = []
cats = sys.argv[1:]
for cat in cats:
    for page in range(1, 6):
        t = get(f"https://madeinca.ca/category/{cat}/" + (f"page/{page}/" if page > 1 else ""))
        posts += re.findall(r'href="(https://madeinca\.ca/[a-z0-9\-]+-[a-z0-9\-]+/)"', t)
posts = sorted({p for p in posts if not re.search(r"/(about-us|advertising|blog|browse|donate|feed|grocery|media-kit|newsletter|privacy|submissions|terms|wp-json)", p)})
def dom(p):
    t = get(p)
    for u in re.findall(r'href="https?://(?:www\.)?([a-z0-9\-\.]+\.[a-z]{2,})', t):
        if not re.search(SKIP, u):
            return u
    return ""
with concurrent.futures.ThreadPoolExecutor(10) as ex:
    ds = sorted({d for d in ex.map(dom, posts) if d})
print(len(posts), "posts", len(ds), "domains", file=sys.stderr)
print(" ".join(ds))
