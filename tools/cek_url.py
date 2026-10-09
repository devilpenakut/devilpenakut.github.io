"""Cek bahwa setiap URL di sitemap Hashnode punya halaman atau redirect di build Jekyll.

Pakai:  jekyll build  lalu  python tools/cek_url.py [_site] [https://devilpenakut.com]
Keluar dengan kode 1 kalau ada URL yang tidak tertangani.
"""
import os
import re
import sys
import urllib.request

site = sys.argv[1] if len(sys.argv) > 1 else "_site"
host = (sys.argv[2] if len(sys.argv) > 2 else "https://devilpenakut.com").rstrip("/")


def locs(url):
    req = urllib.request.Request(url, headers={"User-Agent": "cek-url"})
    xml = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def redirect_rules():
    rules = []
    with open(os.path.join(site, "_redirects"), encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                src = line.split()[0]
                pattern = re.escape(src).replace(r"\*", ".*")
                pattern = re.sub(r":\w+", "[^/]+", pattern)
                rules.append(re.compile("^" + pattern + "$"))
    return rules


urls = []
for loc in locs(host + "/sitemap.xml"):
    urls += locs(loc) if "sitemap" in loc else [loc]

rules = redirect_rules()
missing = []
for url in urls:
    path = url[len(host):] or "/"
    rel = path.strip("/")
    if path == "/" or os.path.isfile(os.path.join(site, rel + ".html")) \
            or os.path.isfile(os.path.join(site, rel, "index.html")) \
            or any(r.match(path) for r in rules):
        continue
    missing.append(path)

print(f"{len(urls)} URL di sitemap, {len(missing)} tidak tertangani")
for path in missing:
    print("  ", path)
sys.exit(1 if missing else 0)
